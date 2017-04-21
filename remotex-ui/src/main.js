import Vue from 'vue'
import App from './App.vue'
import MuseUI from 'muse-ui'
import 'muse-ui/dist/muse-ui.css'
// import 'muse-ui/dist/theme-dark.css'
import 'muse-ui/dist/theme-carbon.css'
// import 'muse-ui/dist/theme-default.css'

Vue.use(MuseUI)

new Vue({
  el: '#app',
  render: h => h(App)
})
