import './assets/main.css'
import axios from "axios";

import 'element-plus/theme-chalk/dark/css-vars.css'
axios.defaults.baseURL="http://10.223.74.229:8000"
import { createApp } from 'vue'
import { createPinia } from 'pinia';
import App from './App.vue'
import router from './routers/route'
const pinia=createPinia()
const app=createApp(App)
app.use(pinia)
app.use(router)
app.mount('#app')
