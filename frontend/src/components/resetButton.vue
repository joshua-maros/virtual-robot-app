<template>
    <div id='reset_button'> 
        <vue-confirmation-button
          ref="confirmationButton"
          :messages="customMessages"
          v-on:confirmation-success="resetField()">
        </vue-confirmation-button>
    </div>
</template>

<script >

import ros from './ros.js'
import ROSLIB from 'roslib'
import vueConfirmationButton from './vueConfirmationButton'

var reset = new ROSLIB.Topic({
   ros : ros,
   name : '/field_reset',
   messageType : 'std_msgs/Bool'
 });

export default {
  name: 'resetButton',
  components: {
    vueConfirmationButton,
  },
  data: () => ({
    customMessages: [
      'Reset Field',
      'Are you sure?',
      '✔'
    ],
  }),
  methods: {
    resetField()
    {
        //Reset the robot
        var resetField = new ROSLIB.Message({
                data: true
        });
        reset.publish(resetField);

        //Stop reseting the robot
        setTimeout(function(){ 
            var resetStop = new ROSLIB.Message({
                data: false
            });
            reset.publish(resetStop);
        }, 3000);
        setTimeout(() => {  this.resetButton() }, 3000);
    },
    resetButton() {
      this.$refs.confirmationButton.reset()
      // Your Logic Here
    },
  }
}


</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

#reset_button{
  position: relative;
  bottom: -40%;
  left: 39%;
}
</style>
