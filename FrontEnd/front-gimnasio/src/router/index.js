import { createRouter, createWebHistory } from 'vue-router'
import LoginView from '../components/login.vue'
import RegisterUserView from '../components/RegisterUser.vue'
 
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: LoginView
    },
    {
      path: '/register',
      name: 'register',
      component: RegisterUserView
    }
    
  ]
})

export default router
