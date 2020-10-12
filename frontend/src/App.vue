<template>
  <div id="app">
    <link rel="text/javascript" src="http://static.robotwebtools.org/EventEmitter2/current/eventemitter2.min.js">
    <link rel="stylesheet" href="//fonts.googleapis.com/css?family=Roboto:400,500,700,400italic|Material+Icons">
    <img alt="Vue logo" src="./assets/logo.png">
    <resetButton/>
    <enable-button/> 
  </div>
</template>

<script>
// import HelloWebSockets from './components/HelloWebSockets.vue'
import resetButton from './components/resetButton.vue'
import enableButton from './components/enableButton.vue'

export default {
  name: 'App',
  components: {
    resetButton,
    enableButton
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
  margin-top: 60px;
}

</style>
