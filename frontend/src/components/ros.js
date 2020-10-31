//Javascript file for initalizing ROS and a websocket on port 9090
import ROSLIB from 'roslib'

var current_url = window.location.href;
var ros_ip = current_url.split(":")
var ros = new ROSLIB.Ros({
    url : 'ws:' + ros_ip[1] + ':9091'
  });

  ros.on('connection', function() {
    console.log('Connected to websocket server.');
  });

  ros.on('error', function(error) {
    console.log('Error connecting to websocket server: ', error);
  });

  ros.on('close', function() {
    console.log('Connection to websocket server closed.');
  });

export default ros;