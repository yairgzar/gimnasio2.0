import { createRouter, createWebHistory } from 'vue-router'
import LoginView from '../components/icons/login.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: LoginView
    }
    
  ]
})

export default router
