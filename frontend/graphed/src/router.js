import Vue from 'vue'
import Router from 'vue-router'
import Loading from '@/views/Loading.vue'
import Home from './views/Home.vue'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'loading',
      component: Loading
    },
    {
      path: '/home',
      name: 'home',
      component: Home
    }
  ]
})
