<template>
    <div id="footer">
        <div class="open-close-footer" v-on:click="onClick"></div>
        <div class="footer">
            <robot-type-dropdown/>
            <robot-position-dropdown/>
            <resetButton/>
            <upload-button/> 
            <stream-selector @updateIp="updateIp($event)"/>
        </div>
    </div>
</template>

<script >
import resetButton from './resetButton.vue'
import uploadButton from './upload.vue'
import streamSelector from './streamSelector.vue'
import robotTypeDropdown from './robotTypeDropdown.vue'
import robotPositionDropdown from './robotPositionDropdown.vue'
import ros from './ros.js'
import ROSLIB from 'roslib'

var keepAlive = new ROSLIB.Topic({
   ros : ros,
   name : '/keep_alive',
   messageType : 'std_msgs/Bool'
 });

function stillAlive(){
     var alive = new ROSLIB.Message({
                data: true
            });
     keepAlive.publish(alive);
     setTimeout(() => {  stillAlive() }, 20000);
}

setTimeout(stillAlive(),20000);

export default {
  name: 'footerComp',
  components: {
    resetButton,
    uploadButton,
    streamSelector,
    robotTypeDropdown,
    robotPositionDropdown,
  },
  methods: {
      onClick: function(){
        var height = document.getElementsByClassName("footer")[0].style.height;
        if (height == "250px") {
        document.getElementsByClassName("footer")[0].style.height = "0px";
        document.getElementsByClassName("open-close-footer")[0].style.bottom =
        "0px";
        }   else {
        document.getElementsByClassName("footer")[0].style.height = "250px";
        document.getElementsByClassName("open-close-footer")[0].style.bottom =
        "250px";
        }
      },
      updateIp: function(ip){
        this.$emit('updateIp', ip);
      }
  }
}

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

.footer {
  position: fixed;
  left: 0;
  bottom: 0px;
  width: 100%;
  height: 0px;
  display: grid;
  grid-template-columns: 33% 33% 33%;
  background-color: #444444;
  z-index: 1;
  overflow-y: hidden;
  transition: 0.5s;
}



.open-close-footer {
  font-size: 50px;
  color: white;
  text-align: center;
  position: fixed;
  bottom: 0px;
  left: 48%;
  transition: 0.5s;
  border-bottom: 50px solid #444444;
  border-left: 15px solid transparent;
  border-right: 15px solid transparent;
  height: 0;
  width: 125px;
}

.open-close-footer:hover{
  border-bottom: 50px solid rgb(133, 126, 126);
  border-left: 20px solid transparent;
  border-right: 20px solid transparent;
}

</style>
