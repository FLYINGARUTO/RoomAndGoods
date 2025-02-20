<template>
    <div class="post-container">
      <div class="post-card">
                <!-- User Info Section -->
        <div class="user-info">
          <el-avatar >
            <img class="avatar" src="../../assets/qqlogo.png">
          </el-avatar>
          <div>
            <p>{{ postData.create_time }}</p>
          </div>
          <el-button type="info" class="message-btn" @click="openInputBox">Message</el-button>
        </div>
        
        <el-divider></el-divider>
    
        <!-- Post Content -->
        <div class="post-content">
        
              
          <h3  style="font-weight: bold;">{{postData.title}}</h3>
          <p class="post-details">{{postData.details }}</p>

          <!-- Photo Box -->
          <div class="photo-box">
            <div v-for="(photo,index) in photoUrls" :key="index" class="image-wrapper">
              <img :src="photo.photo_url" alt="post image"/> 
            </div>
              
          </div>
          <div class="reaction-icons">
              <text class="reaction-icon">👍{{postData.likes}}</text>

              <text class="reaction-icon">⭐{{postData.stars}}</text>

              <text class="reaction-icon">💬{{postData.comments}}</text>
          </div>
          
            
         
          <div class="comment-list">

            <el-card shadow="hover" style="margin-bottom: 10px;">

              <el-input v-model="commentValue" placeholder="Leave your comment here" style="width: 90%;"></el-input>
              <button style="position: relative;left: 10px;height: 30px;" @click="sendComment">Send</button>
            </el-card>

            <el-card v-for="comment in comments" :key="comment.id" shadow="hover" class="comment-card">

              <h3>评论者id:{{  comment.from_id }}</h3>
              <p style="margin-top: 5px;">{{ comment.comment }}</p>
              <div style="margin-top: 5px;justify-content: space-between; display: flex; color: darkgray;">
                
                <p>{{ comment.create_time }}</p>
              </div>
            </el-card>
          </div>
          <div>
            <!-- <input-box :caption="caption" :show="showInput" :value="inputValue" @close="showInput=false" @confirm="inputBoxYes" @cancel="showInput=false">
          </input-box> -->
            <el-dialog v-model="showInput" title="Send Message">
              <el-input v-model="inputValue"></el-input>
              <template #footer>
                <span>

                  <el-button @click="inputBoxYes" style="width: 100px;border-radius: 10px;">send</el-button>
                </span>
              </template>
            </el-dialog>
          </div>
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
    const photoUrls=ref([])
    const comments=ref([])
    const inputValue=ref('')
    const commentValue=ref('')
    const showInput=ref(false)
    onMounted(()=>{
        console.log(route.params)
        const id=route.params.id;
        get(`/api/get/post/${id}`,(res)=>{
            console.log(`response to /api/get-post/${id} : `,res)
            postData.value=res
            get(`/api/get/pic-urls/${id}`,(res)=>{
              photoUrls.value=res
            })
            get(`/api/get/comments/${id}`,(res)=>{
              comments.value=res
              // console.log(res)
            })
        })
     
    })

    const openInputBox=()=>{

      showInput.value=true

    }
    const inputBoxYes=()=>{

      post('api/post/send-msg/',{
        "from-id":1, //之后这里要动态的获取当前登录用户的id
        "to-id":postData.value.publisher_id,
        "msg":inputValue.value
      },()=>{
        showInput.value=false 
        alert("Message Sent");
      })
      
    }
    const sendComment=()=>{
      post('api/post/comment/',{
        "from-id":1, //之后这里要动态的获取当前登录用户的id
        "to-id":postData.value.publisher_id,
        "comment":commentValue.value,
        "post-id":postData.value.id
      },()=>{
        commentValue.value=""
        alert("Commented successfully")
        router.go(0) //刷新网页
      })
    }
  </script>
  
  <style scoped>
.post-container {
    overflow-y: auto;
    flex-direction: column;
    padding: 10px;
    width: 700px;
    max-width: 100%;  /* Increase this value */
    margin: 30px auto;  /*Center the content */

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
  height: 60px;
  width: 60px;
  background: #eeeeee;
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
  padding: 5px;
  flex-wrap: wrap;  
  width: 100%;
  height: 500px;
  
  border: 1px solid black;
  border-radius: 5px;
  display: flex;
  
  font-weight: bold;
}

/* 每张图片的容器 */
.image-wrapper {
  width: 150px;   /* 固定盒子宽度 */
  height: 150px;  /* 固定盒子高度 */
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: #f8f8f8; /* 背景色 */
  margin: 3px;
  overflow: hidden;
  border: 1px solid #ccc;
  border-radius: 5px;
}

/* 让图片保持原始比例 */
.image-wrapper img {
  max-width: 100%;
  max-height: 100%;
  object-fit: contain; /* 保持比例 */
}
/* 让 reaction-icons 右对齐 */
.reaction-icons {

  font-size: 16px;
  display: flex;
  justify-content: space-between;

  width: 60%;
  /* gap: 30px; */
  align-self:flex-end;
}
.reaction-icon{

  border-radius: 15px;

}
.comment-list {
    flex: 1;
    width: 100%; /* Ensure it takes full width */
    max-width: 100%;
  }
  
  .comment-card {
    margin-bottom: 10px;
    width: 100%;
    height: 80%;
  }
  </style>
  