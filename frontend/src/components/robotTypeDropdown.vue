<template>
    <div id='robot_type_dropdown'> 
        <dropdown :options="arrayOfObjects" :selected="object" v-on:updateOption="setType"></dropdown>
    </div>
</template>

<script >

import ros from './ros.js'
import ROSLIB from 'roslib'
import dropdown from 'vue-dropdowns';

var robot = new ROSLIB.Topic({
   ros : ros,
   name : '/robot_type',
   messageType : 'std_msgs/String'
 });

export default {
  name: 'robotTypeDropdown',
  components: {
    dropdown,
  },
  data: () => ({
            arrayOfObjects: {
                object: {
                    name: 'Mecanum Wheeled Robot',
                },
                object2: {
                    name: 'Differential Wheeled Robot',
                },
            },
            object: {
              name: 'Select Robot!',
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
    #robot_type_dropdown{
        width: 300px;
        position: relative;
        left: 10%;
        top: 6%;
    }
</style>
