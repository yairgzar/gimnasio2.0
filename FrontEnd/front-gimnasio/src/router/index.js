import { createRouter, createWebHistory } from 'vue-router'
import LoginView from '../components/login.vue'
import RegisterUserView from '../components/RegisterUser.vue'
import menuView from '../components/menu.vue'
 
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
    },
    {
      path: '/menu',
      name: 'menu',
      component: menuView,
      children:[
        {path: '/personas', name: 'personas', component:RegisterUserView},
      ]
    }
    
  ]
})

export default router
