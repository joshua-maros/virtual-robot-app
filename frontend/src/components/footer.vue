<template>
    <div id="footer">
        <div class="open-close-footer" v-on:click="onClick"></div>
        <div class="footer">
            <enable-button/>
            <resetButton/>
            <upload-button/> 
        </div>
    </div>
</template>

<script >
import resetButton from './resetButton.vue'
import enableButton from './enableButton.vue'
import uploadButton from './upload.vue'

export default {
  name: 'footerComp',
  components: {
    resetButton,
    enableButton,
    uploadButton
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
  left: 50%;
  transition: 0.5s;
  border-bottom: 50px solid #555;
  border-left: 15px solid transparent;
  border-right: 15px solid transparent;
  height: 0;
  width: 125px;
}


</style>
