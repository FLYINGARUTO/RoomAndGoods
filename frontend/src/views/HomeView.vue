<script setup>
import router from '@/routers/route';

</script>
<template>
    <div class="homepage">
      <!-- Sidebar -->
      <div class="sidebar" > 
        <el-button class="sidebar-btn" @click="router.push('/')">All</el-button>
        <el-button class="sidebar-btn" @click="router.push('/')">Used</el-button>
        <el-button class="sidebar-btn" @click="router.push('/')">Sublet</el-button>
        <el-button class="sidebar-btn">My</el-button>
        <el-button class="sidebar-btn logout">Logout</el-button>
      </div>
  
      <router-view v-slot="{Component}">
        <transition name="el-zoom-in-center" mode="out-in" >
          <component :is="Component"/>
        </transition>
      </router-view>

    </div>
  </template>
  
  <style scoped>
  /* 🌟 让 homepage 使用 flex 贴紧左侧，并让右侧填充 */
  .homepage {
    display: flex;
    height: 100vh;
    width: 100%;  /* 确保撑满整个屏幕 */
    overflow: hidden;
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
    padding: 10px;
}

.sidebar-btn {
    width: 90%; /* ✅ 统一按钮宽度 */
    max-width: 180px; /* ✅ 确保不会太宽 */
    margin-bottom: 10px; /* ✅ 让按钮间隔一致 */
}

.logout {
    background: #d9534f;
    color: white;
    position: relative;
    margin-top: auto;
    width: 90%; /* ✅ 让 Logout 按钮和其他按钮宽度一致 */
}

  

  </style>
  