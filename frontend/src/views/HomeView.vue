<script setup>
import router from '@/routers/route';
import {get} from '@/net/index'
import {usePostStore} from '../store/postStore'
import { storeToRefs } from "pinia";
const postStore = usePostStore()
const { selectedCategory } = storeToRefs(postStore); 
const logout=()=>{
  get('api/get/logout',()=>{
    localStorage.removeItem('accessToken')
    localStorage.removeItem('refreshToken')
    localStorage.removeItem('loginedUser')
    router.push('/login')
  })

}
const changeCategory=(category)=>{
  postStore.setCategory(category)
  router.push('/')
}
</script>
<template>
    <div class="homepage">
      <!-- Sidebar -->
      <div class="sidebar" > 
        <label class="sidebar-btn" :class="{ active: selectedCategory === 'All'}" @click="changeCategory('All')">All</label>
        <label class="sidebar-btn" :class="{ active: selectedCategory === 'Used'}" @click="changeCategory('Used')">Used</label>
        <label class="sidebar-btn" :class="{ active: selectedCategory === 'Sublet'}" @click="changeCategory('Sublet')">Sublet</label>
        <div class="side-bottom"> 
          <label class="sidebar-btn">My</label>
          <label class="sidebar-btn logout" @click="logout">Logout</label>
        </div>

       
        
      </div>
      <div class="post-container"> 
        <router-view v-slot="{Component}">
          <transition name="el-zoom-in-center" mode="out-in" >
            <component :is="Component"/>
          </transition>
        </router-view>
      </div> 
      

    </div>
  </template>
  
  <style scoped>
  /* 🌟 让 homepage 使用 flex 贴紧左侧，并让右侧填充 */
  .homepage {
    display: flex;
    height: 100vh;
    width: 100%;  /* 确保撑满整个屏幕 */
    
   
    overflow: hidden;
    font-family: Verdana, Geneva, Tahoma, sans-serif;
    
    justify-content: center;  /* ✅ 确保 sidebar 靠左 */
  }
  
  /* 🌟 让 sidebar 贴紧左边 */
  .sidebar {
    position: fixed;
    left: 0px;
    height: 100vh;
    width: 200px; /* 侧边栏固定宽度 */
    background: #eeeeee;
    display: flex;
    flex-direction: column;
    align-items: center; /* ✅ 让所有按钮居中对齐 */
    padding: 50px;
}

.sidebar-btn {
  text-align: center;
  background-color:white;
  margin-bottom: 30px;
    width: 100%; /* ✅ 统一按钮宽度 */
    max-width: 180px; /* ✅ 确保不会太宽 */
    font-size: 20px;
  font-family:Verdana, Geneva, Tahoma, sans-serif;
  font-weight: 700;
  border:1px solid darkgray;
  border-radius: 5px;


}

.logout {
    background: #d9534f;
    color: white;


   
}
.side-bottom{
  margin-top: auto;
  display: flex;
  flex-direction: column;
  width: 100%;
  align-content: center;
  align-items: center;
  justify-content: center;

}
.active{
  background-color: #007bff;
    color: white;
}

.post-container {
    
    max-width: 800px; /* ✅ 限制最大宽度 */
    min-width: 600px;
    width: 100%;
    
    flex-grow: 1;  /* 让内容区域填充剩余空间 */
    overflow-y: auto;
    align-items: center;  /* 水平居中 */
 
}
.post-container1 {
    display: flex;
    flex-direction: column;
    align-items: center;  /* ✅ 让子元素居中 */
    justify-content: flex-start; /* ✅ 从顶部开始排列 */
    
    max-width: 800px; /* ✅ 限制最大宽度 */
    min-width: 600px;
    width: calc(100% - 200px); /* ✅ 让内容填充 sidebar 之外的所有空间 */
    
    flex-grow: 1;
    height: 100vh; /* ✅ 让内容填充整个视口高度 */
    margin-left: 200px; /* ✅ 避免 sidebar 遮挡 */
    overflow-y: auto; /* ✅ 允许滚动 */
}
  </style>
  