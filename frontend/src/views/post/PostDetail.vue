<template>
    <div class="post-container">
      <div class="post-card">
                <!-- User Info Section -->
        <div class="user-info">
          <div style="display: flex;align-items: center;gap: 20px;"> 
            <el-avatar >
              <img class="avatar" src="../../assets/qqlogo.png">
            </el-avatar>
            <text style="font-weight: bold;font-size: 16px;">  {{postData.publisher }}</text>
          </div>
          
          
          <el-button type="info"  @click="openMsgBox">Message</el-button>
        </div>
        
        <el-divider></el-divider>
    
        <!-- Post Content -->
        <div class="post-content">
        
              
          <h3  style="font-weight: bold;">{{postData.title}}</h3>
          <p class="post-details">{{postData.details }}</p>

          <!-- Photo Box -->
          <div class="photo-box" v-if="photoUrls && photoUrls.length > 0">
            <div v-for="(photo,index) in photoUrls" :key="index" class="image-wrapper">
              <img :src="'http://10.223.74.229:8000' +photo.photo_url" alt="post image"/> 
            </div>
              
          </div>
          <div class="bottom-bar">
              <div>
                <p>{{ postData.create_time }}</p>
              </div>
              <div class="reaction-icons">
                <div> 
                  <img :src="likeIconUrl" class="reaction-icon" @click="like">
                  <text >{{postData.likes}}</text>
                </div>
                <div> 
                  <img :src="starIconUrl" class="reaction-icon" @click="star">
                  <text >{{postData.stars}}</text>
                </div>
                <div> 
                  <img :src="iconURL.comment" class="reaction-icon">
                  <text >{{postData.comments}}</text>
                </div>

              </div>
          </div>
          
          
            
         
          <div class="comment-list">

            <el-card shadow="hover" style="margin-bottom: 10px;">

              <el-input v-model="commentValue" placeholder="Leave your comment here" style="width: 90%;"></el-input>
              <button style="position: relative;left: 10px;height: 30px;" @click="sendComment">Send</button>
            </el-card>

            <el-card v-for="comment in comments" :key="comment.id" shadow="hover" class="comment-card">

              <h3>{{  comment.from_user }}</h3>
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

                  <el-button @click="sendMessage" style="width: 100px;border-radius: 10px;">send</el-button>
                </span>
              </template>
            </el-dialog>
          </div>
        </div>
      </div>

    </div>
  </template>
  
  <script setup>
    import { reactive, ref } from 'vue';
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
    const likeIconUrl=ref(iconURL.like)
    const starIconUrl=ref(iconURL.star)
    const loginedUser=ref('')
    const status=reactive({
      like:0,
      star:0
    })
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

        })

        
     
    })

    const openMsgBox=()=>{

      showInput.value=true

    }

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
    const sendComment=()=>{
      if(localStorage.getItem("accessToken")!=null)
        post('api/post/comment/',{
          "from-user":loginedUser.value, //之后这里要动态的获取当前登录用户的id
          "to-user":postData.value.publisher,
          "comment":commentValue.value,
          "post-id":postData.value.id
        },
        ()=>{
          commentValue.value=""
          alert("Commented successfully")
          router.go(0) //刷新网页
        },)
      else{
        alert('please login first')
      }
    }
    const like=()=>{
      if(status.like==0){
        post('api/post/like/',{
          'from-user':loginedUser.value,
          'to-user' : postData.value.publisher,
          'post-id': postData.value.id
        },(res)=>{
          console.log(res)
          status.like=1
          likeIconUrl.value=iconURL.liked
          postData.value.likes+=1
        })
      }else{
        post('api/post/cancel-like/',{
          'from-user':loginedUser.value,
          'post-id': postData.value.id
        },(res)=>{
          console.log(res)
          status.like=0
          likeIconUrl.value=iconURL.like
          postData.value.likes-=1
        })
      }
    }
    const star=()=>{
      if(status.star==0){
        post('api/post/star/',{
          'from-user':loginedUser.value,
          'to-user' : postData.value.publisher,
          'post-id': postData.value.id
        },(res)=>{
          console.log(res)
          status.star=1
          starIconUrl.value=iconURL.starred
          postData.value.stars+=1
        })
      }else{
        post('api/post/cancel-star/',{
          'from-user':loginedUser.value,
          'post-id': postData.value.id
        },(res)=>{
          console.log(res)
          status.star=0
          starIconUrl.value=iconURL.star
          postData.value.stars-=1
        })
      }
    }
</script>
  
  <style scoped>
.post-container {
    overflow-y: auto;
    flex-direction: column;
    padding: 5px;
    width: 100%;
    max-width: 1200px;  /* Increase this value */
    min-width: 1000px;
    margin:10px;

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
  padding: 5px;
  flex-wrap: nowrap;  
  width: 100%;
  height: 500px;
  overflow-x: auto;   /* ✅ 允许横向滚动 */
  overflow-y: hidden; /* ✅ 防止垂直滚动 */
  border: 1px solid black;
  border-radius: 5px;
  display: flex;
  
  font-weight: bold;
}

/* 每张图片的容器 */
.image-wrapper {
  width: 450px;   /* 固定盒子宽度 */
  height: 450px;  /* 固定盒子高度 */
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: #f8f8f8; /* 背景色 */
  margin: 3px;
  overflow: hidden;
  border: 1px solid #ccc;
  border-radius: 5px;
  flex-shrink: 0; /* ✅ 防止图片被压缩 */
}

/* 让图片保持原始比例 */
.image-wrapper img {
  max-width: 100%;
  max-height: 100%;
  object-fit: contain; /* 保持比例 */
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
  </style>
  