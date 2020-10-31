#!/bin/bash
source /home/leonidas/virtual-robot-app/backend/env/bin/activate
python /home/leonidas/virtual-robot-app/backend/demo_backend.py &
deactivate
cd /home/leonidas/virtual-robot-app/frontend
npm run serve &
cd /home/leonidas/virtual-robot-app/nginx
sudo nginx -c nginx.conf -p .