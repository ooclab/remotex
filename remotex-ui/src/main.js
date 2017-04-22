import Vue from 'vue'
import App from './App.vue'
import MuseUI from 'muse-ui'
import 'muse-ui/dist/muse-ui.css'
// import 'muse-ui/dist/theme-dark.css'
import 'muse-ui/dist/theme-carbon.css'
// import 'muse-ui/dist/theme-default.css'
import VueResource from 'vue-resource'

Vue.use(MuseUI)
Vue.use(VueResource)

new Vue({
  el: '#app',
  http: {
  },
  render: h => h(App)
})
