<script setup>
import { onMounted } from 'vue'
import { ref,computed} from 'vue';
import {get,post} from '@/net/index'
onMounted(() => {
    get("/api/get_post_list",(res)=>{
        console.log(res)
        posts.value=res.map(item=>({
          title: item.title,
          user: item.publisher_id,
          details: item.details,
          views: item.views,
          date: item.create_time
        }))
      })

})


// Sample post data
const posts = ref([]);

const sortBy = ref('views'); // Default sorting method

// Sorting logic
const sortedPosts = computed(() => {
  return [...posts.value].sort((a, b) => (sortBy.value === 'views' ? b.views - a.views : new Date(b.date) - new Date(a.date)));
});
</script>
<template>
    <div class="homepage">
      <!-- Sidebar -->
      <div class="sidebar" > 
        <el-button class="sidebar-btn">All</el-button>
        <el-button class="sidebar-btn">Used</el-button>
        <el-button class="sidebar-btn">Sublet</el-button>
        <el-button class="sidebar-btn">My</el-button>
        <el-button class="sidebar-btn logout">Logout</el-button>
      </div>
  
      <!-- Main Content -->
      <div class="main-content">
        <!-- Banner -->
        <div class="banner">
          <!-- <img src="../assets/banner.png" class="banner-img"> -->
          <text style="font-weight: bold;">Advertising Space for Rent</text>
        </div>
  
        <!-- Sorting & Post Button -->
        <div class="sort-bar">
          <el-button @click="sortBy = 'views'" :type="sortBy === 'views' ? 'primary' : ''">Sort by views</el-button>
          <el-button @click="sortBy = 'time'" :type="sortBy === 'time' ? 'primary' : ''">Sort by time</el-button>
          <el-button type="success" class="post-btn">Post</el-button>
        </div>
  
        <!-- Post List -->
        <div class="post-list">
          <el-card v-for="post in sortedPosts" :key="post.title" shadow="hover" class="post-card">
            <h3 style="font-weight: bold;">{{ post.title }}</h3>
            <p>{{ post.details }}</p>
            <p>{{ post.views }} views, {{ post.date }}</p>
          </el-card>
        </div>
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

  
  /* 🌟 让 main-content 占满剩余空间 */
  .main-content {
    flex: 1;  /* 让它自动填充剩余空间 */
    display: flex;
    flex-direction: column;
    padding: 0px;
    width: 60vh;
  }
  
  /* Banner */
  .banner {
    width: 100%;
    height: 100px;
    background: white;
    border-radius: 15px;
    border: 3px solid #eeeeee;    
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 20px;
    overflow: hidden; 
  }
  .banner-img {
  max-width: 100%;  /* ✅ 确保图片不会超出 */
  max-height: 100%; /* ✅ 确保图片不会超出 */
  object-fit: contain; /* ✅ 保持比例 */
}
  /* Sorting Bar */
  .sort-bar {
    display: flex;
    align-items: center;
    margin-top: 10px;
  }
  
  .sort-bar .el-button {
    margin-right: 10px;
  }
  
  /* Post List */
  .post-list {
    margin-top: 10px;
    flex: 1;
  }
  
  .post-card {
    margin-bottom: 10px;
  }
  </style>
  