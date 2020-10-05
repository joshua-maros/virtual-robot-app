# Introduction
This is a project that can be used as a template for creating Vue.js based UIs. It includes a backend implementing a Socket.io server and a nginx reverse proxy used to serve both static content and route requests to the backend.

Communication between the frontend and backend is done through a single Websocket implementing the Socket.io protocol. Both events and requests can be sent in both directions without additional APIs.

See the example code for more details.

# Clone repo and update names

* Clone repo in project, change name with desired name
```
git clone https://github.com/Virtual-FTC/virtual-robot-app.git
```

* Update name field of frontend/package.json and package-lock.json with desired name

# Setting up after clone

Run `. setup.sh` to install dependencies.

# Running for dev

Start backend
```
cd backend
source env/bin/activate
python demo_backend.py
```

Start frontend
```
cd frontend
npm run serve
```

Start nginx proxy (edit nginx.conf to proxy to npm server)
```
cd nginx
sudo nginx -c nginx.conf -p .
```

# Running for prod

Start backend
```
cd backend
source env/bin/activate
python demo_backend.py
```

Build frontend
```
cd frontend
npm run build
```

Start nginx proxy (remember edit nginx config to redirect to static files)
```
cd nginx
nginx -c nginx.conf -p .
```

# Setting up a from scratch

```
sudo apt install nodejs
sudo npm install -g @vue/cli
vue create js8dash-ui
cd js8dash-ui
npm install vue-material vuex vue-socket.io --save
```

Update as per https://vuematerial.io/getting-started/

Add following in first div of App.vue
```
<link rel="stylesheet" href="//fonts.googleapis.com/css?family=Roboto:400,500,700,400italic|Material+Icons">
```


