<template>
    <div id='reset_button'> 
        <button v-on:click="reset" class="reset-button">{{state}}</button>
    </div>
</template>

<script >

import ros from './ros.js'
import ROSLIB from 'roslib'

var reset = new ROSLIB.Topic({
   ros : ros,
   name : '/robot_reset',
   messageType : 'std_msgs/Bool'
 });

export default {
  name: 'resetButton',
  data: () => ({
    state: 'reset'
  }),
  methods: {
    reset()
    {
        //Reset the robot
        var resetRobot = new ROSLIB.Message({
                data: true
        });
        reset.publish(resetRobot);

        //Stop reseting the robot
        setTimeout(function(){ 
            var resetStop = new ROSLIB.Message({
                data: false
            });
            reset.publish(resetStop);
        }, 1000);
    }
  }
}


</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

#reset_button {
  padding: 10px;
  border-radius: 25px;
  border-color: transparent;
  margin-bottom: 5%;
}

#reset_button button {
  height: 100px;
  width: 300px;
  font-size: xx-large;
  border-radius: 25px;
}

button.reset-button {
  padding: 1em 2em;
  margin: 50px 30%;
  border: 2px solid rgb(163, 106, 106);
  border-radius: 1em;
  background: rgb(255, 205, 205);
  transform-style: preserve-3d;
  transition: all 175ms cubic-bezier(0, 0, 1, 1);
}
button.reset-button::before {
  position: absolute;
  content: "";
  width: 100%;
  height: 100%;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgb(232, 150, 150);
  border-radius: inherit;
  box-shadow: 0 0 0 2px rgb(186, 121, 121);
  transform: translate3d(0, 0.75em, -1em);
  transition: all 175ms cubic-bezier(0, 0, 1, 1);
}

button.reset-button:active {
  transform: translate(0em, 0.75em);
}

button.reset-button:focus {
  outline: none;
}

button.reset-button:active::before {
  transform: translate3d(0, 0, -1em);
  box-shadow: 0 0 0 2px rgb(186, 121, 121), 0 0.25em 0 0  rgb(186, 121, 121);
}


</style>
