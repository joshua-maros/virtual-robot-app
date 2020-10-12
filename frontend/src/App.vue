<template>
  <div id="app">
    <link rel="text/javascript" src="http://static.robotwebtools.org/EventEmitter2/current/eventemitter2.min.js">
    <link rel="stylesheet" href="//fonts.googleapis.com/css?family=Roboto:400,500,700,400italic|Material+Icons">
    <img alt="Vue logo" src="./assets/logo.png">
    <footer-comp/>
  </div>
</template>

<script>
// import HelloWebSockets from './components/HelloWebSockets.vue'
import footerComp from './components/footer.vue'

export default {
  name: 'App',
  components: {
    footerComp,
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
