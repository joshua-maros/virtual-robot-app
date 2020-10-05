
# Setup backend
echo 'Setting up backend...'
python3 -m venv ./backend/env
source ./backend/env/bin/activate
pip3 install -r backend/requirements.txt

# Setup frontend
echo 'Setting up frontend...'
cd frontend
sudo apt install nodejs
sudo npm install -g @vue/cli
npm install
cd ..

# Setup nginx
echo 'Installing nginx'
sudo apt-get update
sudo apt-get install nginx

deactivate

# Done
echo 'Done, see README.md for more details'


