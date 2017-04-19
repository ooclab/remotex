import Vue from 'vue'
import MintUI from 'mint-ui'
import 'mint-ui/lib/style.css'
import App from './App.vue'
import { Header } from 'mint-ui'
import { Button } from 'mint-ui'
import { Picker } from 'mint-ui'
import { InfiniteScroll } from 'mint-ui'
import { Spinner } from 'mint-ui'

Vue.use(MintUI)
Vue.component(Header.name, Header)
Vue.component(Button.name, Button)
Vue.component(Picker.name, Picker)
Vue.use(InfiniteScroll)
Vue.component(Spinner.name, Spinner)

new Vue({
  el: '#app',
  render: h => h(App)
})
