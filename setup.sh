# Install Basics
sudo apt-get update
sudo apt-get install python3-venv

# Setup backend
echo 'Setting up backend...'
python3 -m venv ./backend/env
source ./backend/env/bin/activate
pip3 install -r backend/requirements.txt
deactivate

# Setup frontend
echo 'Setting up frontend...'
cd frontend
sudo apt-get update
sudo apt install curl
nvm install 12.18.4
curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.33.11/install.sh | bash
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"

sudo npm install -g @vue/cli
npm install
cd ..

# Setup nginx
echo 'Installing nginx'
sudo apt-get install nginx

# Done
echo 'Done, see README.md for more details'
