import Vue from 'vue'
import App from './App.vue'
import { MdButton } from 'vue-material/dist/components'
import 'vue-material/dist/vue-material.min.css'
import 'vue-material/dist/theme/default.css'
import VueSocketIO from 'vue-socket.io'

Vue.config.productionTip = false

Vue.use(MdButton)

Vue.use(new VueSocketIO({
  debug: true,
  //connection: location.hostname + ":8081" // use this when testing without nginx
  connection: location.hostname + ':' + location.port.toString() // use this when running with nginx
}))

new Vue({
  render: h => h(App),
}).$mount('#app')
