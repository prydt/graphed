import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import './registerServiceWorker'

// for css loaders
import 'vue-loaders/dist/vue-loaders.css'
import { BallTrianglePathLoader } from 'vue-loaders'

Vue.config.productionTip = false

Vue.component(BallTrianglePathLoader.name, BallTrianglePathLoader)

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
