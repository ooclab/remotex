import Vue from 'vue'
import App from './App.vue'
import MuseUI from 'muse-ui'
import 'muse-ui/dist/muse-ui.css'
// import 'muse-ui/dist/theme-dark.css'
import 'muse-ui/dist/theme-carbon.css'
// import 'muse-ui/dist/theme-default.css'
import VueResource from 'vue-resource'
import VueRouter from 'vue-router'

Vue.use(MuseUI)
Vue.use(VueResource)
Vue.use(VueRouter)

import Detail from './Detail.vue'

const routes = [
	{
	    path:'/',
	    component:App
	},
	{
	    path:'/detail/:id',
	    name:'detail',
	    component:Detail
	}
]

const router = new VueRouter({
    routes
});

new Vue({
	el: '#app',
	data: {
	},
	http: {
	},
	router,
	render: h => h(App)
})
