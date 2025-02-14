import './assets/main.css'
import axios from "axios";
import 'element-plus/theme-chalk/dark/css-vars.css'
axios.defaults.baseURL="http://localhost:8000"
import { createApp } from 'vue'
import App from './App.vue'
import router from './routers/route'
const app=createApp(App)
app.use(router)
app.mount('#app')
