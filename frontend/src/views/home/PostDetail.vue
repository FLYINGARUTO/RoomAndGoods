<template>
    <div class="post-container">
      <!-- User Info Section -->
      <div class="user-info">
        <el-avatar class="avatar">Avatar</el-avatar>
        <div>
          <p>{{ postData.views }} views     {{ postData.create_time }}</p>
        </div>
        <el-button type="info" class="message-btn">Message</el-button>
      </div>
  
      <el-divider></el-divider>
  
      <!-- Post Content -->
      <div class="post-content">
       
            
        <h3  style="font-weight: bold;">{{postData.title}}</h3>
        <p class="post-details">{{postData.details }}</p>
 
        <!-- Photo Box -->
        <div class="photo-box">
          Photos
        </div>
        <div class="reaction-icons">
            <text>24👍</text>
            <text>-</text>
            <text>13⭐</text>
            <text>-</text>
            <text>2💬</text>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
    import { ref } from 'vue';
    import { ElAvatar, ElButton, ElDivider, ElIcon } from 'element-plus';
    import { onMounted } from 'vue';
    import {get,post} from '@/net/index'
    import router from '@/routers/route'
    import { useRoute } from 'vue-router';
    const postData = ref({ });
    const route = useRoute()
    onMounted(()=>{
        console.log(route.params)
        const id=route.params.id;
        get(`/api/get-post/${id}`,(res)=>{
            console.log(`response to /api/get-post/${id} : `,res)
            postData.value=res
        })
    })
  </script>
  
  <style scoped>
.post-container {
  width: 60vw;
  max-width: 800px;
  margin: 20px auto;
  background: white;
  padding: 15px;
  border-radius: 10px;
  border: 1px solid #ddd;
}

/* 用户信息栏 */
.user-info {
  display: flex;
  align-items: center;
  justify-content: space-between;
  width: 100%;
}

/* 头像 */
.avatar {
  font-size: 14px;
  background: white;
  color: black;
  border: 1px solid black;
  padding: 10px;
  border-radius: 50%;
}

/* 让 post-content 占满 */
.post-content {
    margin: 20px 0;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    width: 100%;
}
.post-details{
    color: #333333;
    margin: 20px 0
}
/* 让照片区域撑满 */
.photo-box {
  width: 100%;
  height: 150px;
  margin: 10px 0;
  border: 1px solid black;
  border-radius: 20px;
  display: flex;
  justify-content: center;
  align-items: center;
  font-weight: bold;
}

/* 让 reaction-icons 右对齐 */
.reaction-icons {
  display: flex;
  gap: 8px;
  align-self: flex-end;
}

  </style>
  