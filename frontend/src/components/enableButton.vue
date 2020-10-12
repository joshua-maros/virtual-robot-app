<template>
    <div id='enable_button' class="enable-button">
        <input v-on:click="change_state" v-model="checked" type="checkbox" name="enable-button" class="enable-button-checkbox" id="my-enable-button" tabindex="0">
        <label class="enable-button-label" for="my-enable-button">
            <span class="enable-button-inner"></span>
            <span class="enable-button-switch"></span>
        </label>
    </div>
</template>

<script >

import ros from './ros.js'
import ROSLIB from 'roslib'

var enabled = new ROSLIB.Topic({
  ros: ros,
  name: "/robot_bool",
  messageType: "std_msgs/Bool",
});

export default {
  name: 'enableButton',
  data: () => ({
    state: "Disabled",
    checked: false,
  }),
  created() {
    this.$watch("checked", () => {
      this.publish();
    });
  },
  methods: {
    change_state() {
      this.state = this.state == "Enabled" ? "Disabled" : "Enabled";
    },
    publish() {
      var robotState = new ROSLIB.Message({
        data: this.state == "Enabled" ? true : false,
      });
      enabled.publish(robotState);
    },
  }
}


</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

#enable_button{
  margin: 100px 30%;
}
  

.enable-button {
  position: relative;
  width: 200px;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
}
.enable-button-checkbox {
  position: absolute;
  opacity: 0;
  pointer-events: none;
}
.enable-button-label {
  display: block;
  overflow: hidden;
  cursor: pointer;
  border: 2px solid #999999;
  border-radius: 0px;
}
.enable-button-inner {
  display: block;
  width: 200%;
  margin-left: -100%;
  transition: margin 0.3s ease-in 0s;
}
.enable-button-inner:before,
.enable-button-inner:after {
  display: block;
  float: left;
  width: 50%;
  height: 69px;
  padding: 0;
  line-height: 65px;
  font-size: 17px;
  color: white;
  font-family: Trebuchet, Arial, sans-serif;
  font-weight: bold;
  box-sizing: border-box;
  border: 2px solid transparent;
  background-clip: padding-box;
}
.enable-button-inner:before {
  content: "ENABLED";
  padding-left: 10px;
  background-color: #6bf02d;
  color: #ffffff;
}
.enable-button-inner:after {
  content: "DISABLED";
  padding-right: 10px;
  background-color: #ff0000;
  color: #333333;
  text-align: right;
}
.enable-button-switch {
  display: block;
  width: 75px;
  max-height: 73px;
  margin: 0px;
  background: #8a8080;
  position: absolute;
  top: 0;
  bottom: 0;
  right: 125px;
  transition: all 0.3s ease-in 0s;
}
.enable-button-checkbox:checked + .enable-button-label .enable-button-inner {
  margin-left: 0;
}
.enable-button-checkbox:checked + .enable-button-label .enable-button-switch {
  right: 0px;
}


</style>
