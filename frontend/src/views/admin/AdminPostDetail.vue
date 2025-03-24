<script setup>
import { reactive, ref } from 'vue';
import axios from "axios";
import { ElAlert, ElAvatar, ElButton, ElDivider, ElIcon } from 'element-plus';
import { onMounted } from 'vue';
import {get,post,internalPost} from '@/net/index'

import router from '@/routers/route'
import { useRoute } from 'vue-router';
import likeImg from '@/assets/like.png'
import likedImg from '@/assets/liked.png'
import starImg from '@/assets/star.png'
import starredImg from '@/assets/starred.png'
import commentImg from '@/assets/comment.png'
import { useUrlStore } from '@/store/urlStore';
const urlStore =useUrlStore()
const BASE_URL=urlStore.baseUrl;
const postData = ref({ });
const route = useRoute()
const photoUrls=ref([])
const comments=ref([])
const inputValue=ref('')
const commentValue=ref('')
const showInput=ref(false)
const iconURL=reactive({
  like: likeImg,
  liked: likedImg,
  star: starImg,
  starred: starredImg,
  comment: commentImg
})
const showDeleteDialog = ref(false); // 控制删除确认框的显示
const postId = route.params.id; // 获取当前帖子 ID
const likeIconUrl=ref(iconURL.like)
const starIconUrl=ref(iconURL.star)
const loginedUser=ref('')
const status=reactive({
  like:0,
  star:0
})
const commentInput=ref(null)
const focusCommentInput=()=>{
  commentInput.value?.focus()
}
onMounted(()=>{
    loginedUser.value=localStorage.getItem('loginedUser')
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
        //判断是否登录， 没有登录就不需要查看点赞收藏状态（访客模式
        if(loginedUser.value){
          post('/api/post/like-or-not/',{
          'from-user':loginedUser.value,
          'post-id':postData.value.id
          },(res)=>{
            console.log("like-or-not:",res)
            if(res.code==1){
              status.like=1
              likeIconUrl.value=iconURL.liked
            }
          })
          post('/api/post/star-or-not/',{
            'from-user':loginedUser.value,
            'post-id':postData.value.id
          },(res)=>{
            console.log("star-or-not:",res)
            if(res.code==1){
              status.star=1
              starIconUrl.value=iconURL.starred
            }
          })
        }


    })



})
const showPicModal=ref(false)
//点击放大的照片url
const bigPicUrl=ref("")
const openBigPicture=(url)=>{
  bigPicUrl.value=`${BASE_URL}${url}`
  showPicModal.value=true
}


const deletePost = () => {
  if (!postId) {
    console.error("Post ID not found");
    return;
  }
  post(`/api/post/admin-delete-post/`, { post_id: postId }, (res) => {
      console.log("🚀 Delete Post Response:", res);
      console.log("📌 Attempting to navigate to /admin/dashboard");
      router.push("/admin/dashboard");  
  });
};

//confirm to send messgae
const sendMessage=()=>{
  if(localStorage.getItem("accessToken")!=null)
    post('api/post/send-msg/',{
      "from-user":loginedUser.value, //之后这里要动态的获取当前登录用户的id
      "to-user":postData.value.publisher,
      "msg":inputValue.value
    },()=>{
      showInput.value=false
      alert("Message Sent");
    })
 else{
  alert('please login first')
 }
}

// ✅ 删除评论
const deleteComment = (commentId) => {
  ElMessageBox.confirm(
    "Are you sure you want to delete this comment?",
    "Warning",
    {
      confirmButtonText: "Yes",
      cancelButtonText: "No",
      type: "warning",
    }
  ).then(() => {
    post('/api/post/delete-comment/', { comment_id: commentId }, (res) => {
      // if (res && res.success) {
      //   ElMessage.success("Comment deleted successfully!");
      //   fetchComments(); // 重新获取评论列表
      // } else {
      //   ElMessage.error("Failed to delete comment.");
      // }
      ElMessage.success("Comment deleted successfully!");
      router.go(0)
    });
  }).catch(() => {
    console.log("Comment deletion canceled.");
  });
};


// ✅ 获取评论
const fetchComments = () => {
  get(`/api/get/comments/${postId}`, (res) => {
    if (res && Array.isArray(res)) {
      comments.value = res; // 更新评论
    } else {
      console.error("Failed to fetch comments or incorrect response format.");
    }
  });
};
</script>
<template>
    <div class="post-container">
      <div class="post-card">
                <!-- User Info Section -->
        <div class="user-info">
          <div style="display: flex;align-items: center;gap: 20px;">
            <el-avatar >
              <img class="avatar" src="../../assets/qqlogo.png">
            </el-avatar>
            <div>
              <text style="font-weight: bold;font-size: 16px;">  {{postData.publisher }}</text>

            </div>
          </div>

          <el-button type="danger" @click="showDeleteDialog = true">Delete</el-button>

        </div>

        <el-divider></el-divider>

        <!-- Post Content -->
        <div class="post-content">


          <h3  style="font-weight: bold;">{{postData.title}}</h3>
          <p class="post-details">{{postData.details }}</p>

          <!-- Photo Box -->
          <div class="photo-box" v-if="photoUrls && photoUrls.length > 0">
            <div v-for="(photo,index) in photoUrls" :key="index" class="image-wrapper">
              <!-- 缩略图 -->
              <img :src="BASE_URL +photo.photo_url"  @click="openBigPicture(photo.photo_url)"/>


            </div>

          </div>
          <div class="bottom-bar">
              <div>
                <p>{{ postData.create_time }}</p>
              </div>
              <div class="reaction-icons">
                <div>
                  <img :src="likeIconUrl" class="reaction-icon" >
                  <text >{{postData.likes}}</text>
                </div>
                <div>
                  <img :src="starIconUrl" class="reaction-icon" >
                  <text >{{postData.stars}}</text>
                </div>
                <div>
                  <img :src="iconURL.comment" class="reaction-icon" >
                  <text >{{postData.comments}}</text>
                </div>

              </div>
          </div>




          <div class="comment-list">

            <el-card v-for="comment in comments" :key="comment.id" shadow="hover" class="comment-card">

              <h3>{{  comment.from_user }}</h3>
              <p style="margin-top: 5px;">{{ comment.comment }}</p>
              <div style="margin-top: 5px;justify-content: space-between; display: flex; color: darkgray;">
                <p>{{ comment.create_time }}</p>
                <el-button type="danger" size="small" @click="deleteComment(comment.id)">Delete</el-button>
              </div>
            </el-card>
          </div>
        </div>
      </div>

      <el-dialog v-model="showDeleteDialog" title="Confirm Delete" width="400px">
        <span>Are you sure you want to delete this post?</span>
        <template #footer>
          <span>
            <el-button @click="showDeleteDialog = false">Cancel</el-button>
            <el-button type="danger" @click="deletePost">Confirm Delete</el-button>
          </span>
        </template>
      </el-dialog>

    </div>
  </template>



  <style scoped>
.post-container {
    overflow-y: auto;
    flex-direction: column;

    width: 100%;
    max-width: 1200px;  /* Increase this value */
    min-width: 1000px;
    margin:10px;

    background: white;
    padding: 50px 100px;
    border-radius: 10px;
    border: 1px solid #ddd;
}

/* 用户信息栏 */
.user-info {
  display: flex;
  align-items: center;
  justify-content: space-between;
  width: 100%;
  padding: 0 5px;
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
    margin: 10px 0;
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

  /* flex-wrap: wrap;   */
  width: 100%;
  height: 320px;
  overflow-x: auto;
  overflow-y: hidden;

  /* border-radius: 5px;
  display: flex;

  font-weight: bold;  */
  display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 30px; /* 控制卡片间距 */
    margin-top: 10px;
    overflow-y: auto;
}

/* 每张图片的容器 */
.image-wrapper {
  width: 300px;   /* 固定盒子宽度 */
  height: 300px;  /* 固定盒子高度 */
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: #f8f8f8; /* 背景色 */

  overflow: hidden;
  border: 1px solid #ccc;
  border-radius: 15px;

}

/* 让图片保持原始比例 */
.image-wrapper img {
  width: 100%;
  height: 100%;
  object-fit: cover; /* 保持比例 */
}
.image-wrapper :hover {
  cursor: pointer;
  transform: translateY(-1px); /* 悬停时略微上移 */
}
/* 让 reaction-icons 右对齐 */
.reaction-icons {

  margin-right: 20px;

  display: flex;
  justify-content: space-between;
  font-size: 18px;
  width: 20%;
  /* gap: 30px; */
  align-items: center;
  align-self:flex-end;
}
.reaction-icons div{
  display: flex;              /* 让每个图标+数字内部横向排列 */
  align-items: center;        /* 确保图标和数字垂直对齐 */
  gap: 5px;
}
.reaction-icon{

  width: 20px;
  height: 20px;
  cursor: pointer;
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

  .bottom-bar{
    display: flex;
    justify-content: space-between;
    align-items: center;
    width: 100%;
    margin:10px 0px;

  }
  .full-image {
  width: 100%;
  border-radius: 8px;
}
  </style>
