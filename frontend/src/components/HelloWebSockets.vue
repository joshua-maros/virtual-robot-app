<template>
  <div class="hello">
    <h1>{{msg}}</h1>
    <md-button class="md-primary" v-on:click="onClick">Action</md-button>
  </div>
</template>

<script>
export default {
  name: 'TestWebSockets',
  data: () => ({
    msg: 'idle'
  }),
  sockets: {
    connect: function () {
      this.msg = 'connected'
    },
    disconnect: function () {
      this.msg = 'disconnected'
    },
    counter: function (data) {
      this.msg = 'Got: ' + data['counter']
    },
    testPong: function (data) {
      this.msg = 'Pong: ' + data['msg']
    }
  },
  methods: {
    onClick: function () {
      this.msg = 'clicked'
      this.$socket.emit('testPing', {'msg': 'PING'})
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
