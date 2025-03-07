import './assets/main.css'
import axios from "axios";
import 'element-plus/theme-chalk/el-message-box.css';

import 'element-plus/theme-chalk/dark/css-vars.css'

// 动态获取当前页面的主机名（可能是 localhost, 127.0.0.1, 局域网IP 或域名）
axios.defaults.baseURL = `${window.location.protocol}//${window.location.hostname}:8000`;

import { createApp } from 'vue'
import { createPinia } from 'pinia';
import App from './App.vue'
import router from './routers/route'
const pinia=createPinia()
const app=createApp(App)
app.use(pinia)
app.use(router)
app.mount('#app')
