<template>
    <div id='robot_position_dropdown'> 
        <dropdown :options="arrayOfObjects" :selected="object" v-on:updateOption="setType"></dropdown>
    </div>
</template>

<script >

import ros from './ros.js'
import ROSLIB from 'roslib'
import dropdown from 'vue-dropdowns';

var robot = new ROSLIB.Topic({
   ros : ros,
   name : '/robot_position',
   messageType : 'std_msgs/String'
 });

export default {
  name: 'robotPositionDropdown',
  components: {
    dropdown,
  },
  data: () => ({
            arrayOfObjects: {
                object1: {
                    name: 'Red Left',
                },
                object2: {
                    name: 'Red Right',
                },
                object3: {
                    name: 'Blue Left',
                },
                object4: {
                    name: 'Blue Right',
                },
            },
            object: {
              name: 'Select Starting Position!',
            }
  }),
  methods: {
    setType(x)
    {
        //Select the robot type
        var robotType = new ROSLIB.Message({
                data: x.name
        });
        robot.publish(robotType);
    },
  }
}


</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
    #robot_position_dropdown{
        position: absolute;
        width: 300px;
        left: 20%;
        top: 6%;
    }
</style>
