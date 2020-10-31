<template>
  <div id="app">
    <link rel="text/javascript" src="http://static.robotwebtools.org/EventEmitter2/current/eventemitter2.min.js">
    <link rel="stylesheet" href="//fonts.googleapis.com/css?family=Roboto:400,500,700,400italic|Material+Icons">
    <iframe id="stream"
    title="ROS Stream"

    :src="streamIp">
    </iframe>

    <footer-comp @updateIp="updateIp($event)"/>
    
  </div>
</template>

<script>
// import HelloWebSockets from './components/HelloWebSockets.vue'
import footerComp from './components/footer.vue'

export default {
  name: 'App',
  components: {
    footerComp,
  },
  data: () => ({
    streamIp: "",
  }),
  methods: {
    updateIp (ip){
      alert(ip)
      this.streamIp = "https://" + ip;
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #ffffff;
}

#stream{
  height: 100vh;
  width: 100%;
}

</style>
