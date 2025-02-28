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
 
  .homepage {
    display: flex;
    flex-direction: column;
    height: 100vh;
    width: 100vh;  /* 确保撑满整个屏幕 */
    
    margin-bottom: 100px;
    font-family: Verdana, Geneva, Tahoma, sans-serif;
    
    justify-content: center; 

  }
  

  .sidebar {
    padding: 10px;
    margin:100px 10px 0px 10px;
    /* left: 0px; */
    height: 200px;
    max-width: 1200px; /* ✅ 限制最大宽度 */
    min-width: 1000px;
  
    display: flex;
    flex-direction: row;
    border-radius: 10px;
    /* flex:1; */

}

.sidebar-btn {
  text-align: center;
  background-color:white;
  margin-left: 20px;
  width: 100%; /* ✅ 统一按钮宽度 */
  max-width: 100px; /* ✅ 确保不会太宽 */
  font-size: 20px;
  font-family:'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
  font-weight: 500;
  border:1px solid darkgray;
  border-radius: 5px;


}

.logout {
    background: #d9534f;
    color: white;


   
}
.side-bottom{
  margin-left: auto;
  display: flex;
  flex-direction: row;
  width: 100%;
  margin-right: 40px;
  justify-content: flex-end;

}
.active{
  background-color: #007bff;
    color: white;
}

.post-container {
    
    max-width: 1200px; /* ✅ 限制最大宽度 */
    min-width: 1000px;
    width: 100%;

    
    flex-grow: 1; 

    align-items: center;  /* 水平居中 */
    height: 100vh;
 
}
.post-container1 {
    display: flex;
    flex-direction: column;
    align-items: center;  /* ✅ 让子元素居中 */
    justify-content: center; /* ✅ 从顶部开始排列 */
    
    max-width: 1000px; /* ✅ 限制最大宽度 */
    min-width: 800px;

    
    flex-grow: 1;
    height: 100vh; /* ✅ 让内容填充整个视口高度 */

    overflow-y: auto; /* ✅ 允许滚动 */
}
  </style>
  