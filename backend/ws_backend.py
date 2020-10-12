from flask import Flask, flash, request, redirect, url_for, render_template
from flask_socketio import SocketIO, emit, send
from flask_cors import CORS
from threading import Thread
from werkzeug.utils import secure_filename
import asyncio
import concurrent.futures
import logging
import os

# Setup logging 
logging.basicConfig(level=logging.DEBUG,format='[%(asctime)s][%(levelname)s] - [%(name)s]: %(message)s')
logging.getLogger('werkzeug').setLevel(logging.ERROR)
logging.getLogger('socketio.server').setLevel(logging.ERROR)
logging.getLogger('engineio.server').setLevel(logging.ERROR)

#Upload Folder Location 
UPLOAD_FOLDER = 'uploads'

#Extension Checker
ALLOWED_EXTENSIONS = {'xml', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
def allowed_file_types(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Setup flask
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SECRET_KEY'] = '\xfd{H\xe5<\x95\xf9\xe3\x96.5\xd1\x01O<!\xd5\xa2\xa0\x9fR"\xa1\xa8'
CORS(app, resources={r"/*": {"origins": "*"}})
socketio = SocketIO(app, cors_allowed_origins = '*')


   



# Backend class (asyncio based)
class WSBackend:

    """ Base class for backends, interfaces with websockets and handles asyncio setup """
    def __init__(self):
        """ Constructor """
        # Setup asyncio objects
        self.event_loop = asyncio.new_event_loop()
        self.executor_pool = concurrent.futures.ThreadPoolExecutor()  

    def run(self):
        """ Start event loops, will not return """
        # Start asyncio event loop in new thread
        self.event_loop_thread = Thread(target=self._run_event_loop, daemon=True)
        self.event_loop_thread.start()

        @app.route('/upload', methods=['GET', 'POST'])
        def upload_page():
            if request.method == 'GET':
                return redirect('http://127.0.0.1:9080/')
                    
            if request.method == 'POST':
                if 'file' not in request.files:
                    flash('No file part')
                    return redirect('http://127.0.0.1:9080/')

                file = request.files['file']

                if file.filename == '':
                    flash('No selected file')
                    return redirect('http://127.0.0.1:9080/')

                if file and allowed_file_types(file.filename):
                    filename = secure_filename(file.filename)
                    path = os.getcwd()
                    file.save(os.path.join(path, app.config['UPLOAD_FOLDER'], filename))
                    return redirect('http://127.0.0.1:9080/')


        # Start flask/socketio loop, will not return
        socketio.run(app, host='0.0.0.0', port=8081, debug=False)

    def _run_event_loop(self):
        """ Creates a new event loop and runs the main coroutine """
        asyncio.set_event_loop(self.event_loop)
        self.event_loop.run_until_complete(self.main())

    def _generate_event_cb(self, ev_name, async_cb):
        """ Generate a callback that passes ws events to an asyncio callback """
        def on_ws_event(ev_data):
            future = asyncio.run_coroutine_threadsafe(async_cb(ev_name, ev_data), self.event_loop)
            ret = future.result(timeout=1.0)
            if ret is not None:
                ret_name, ret_data = ret
                emit(ret_name, ret_data)
        return on_ws_event

    async def main(self):
        """ Main coroutine, starts tasks and waits till all are done, to be implemented by subclass """
        pass

    async def ws_listen(self, ev_name, async_cb):
        """ Listen for a ws event """
        socketio.on_event(ev_name, self._generate_event_cb(ev_name, async_cb))

    async def ws_broadcast(self, ev_name, ev_data):
        """ Emit new ws event """
        await self.event_loop.run_in_executor(self.executor_pool, socketio.emit, ev_name, ev_data)   




