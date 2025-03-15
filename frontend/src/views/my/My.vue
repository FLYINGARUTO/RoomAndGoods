<template>
  <div class="main-content">
    
   <div class="user-info">
          <div style="display: flex;align-items: center;gap: 20px;"> 
            <el-avatar >
              <img class="avatar" src="../../assets/qqlogo.png">
            </el-avatar>
            <text>{{ username }}</text>
            
          </div>
          
          
          <label>Edit</label>
    </div>
    <el-divider></el-divider>
    <!-- <el-divider></el-divider> -->
    
    <div class="buttons"> 
        <!-- <button @click="router.push('/my/msg')">Message Box(已弃用)
          <span v-if="unread_amount > 0" class="badge">{{ unread_amount }}</span>
        </button> -->
        <button @click="router.push('/my/notification')">Notifications</button> 
        <button @click="router.push('/my/post')">My Posts</button>
        <button @click="router.push('/my/like')">My Likes</button>
        <button @click="router.push('/my/star')">My Stars</button>
    </div>
    
  </div>
</template>

<script setup>
import { post } from "@/net";
import router from "@/routers/route"
import { onMounted } from "vue";
import { ref } from "vue";
const username=localStorage.getItem('loginedUser')


// onMounted(()=>{
//   post('api/post/unread-num/',{
//     "username":username
//   },(res)=>{
//       unread_amount.value=res
//   })
// })
</script>

<style scoped>
  .main-content {
    flex: 1;  /* 让它自动填充剩余空间 */
    flex-direction: column;
    padding: 10px;
    max-width: 100%;
    height: 100vh;
    width: 100%;
    display: flex;  

    margin-top: 20px;
    overflow-y: auto;
    border-radius: 10px;
    border: 1px solid #ddd;
  }
  .avatar {
  height: 60px;
  width: 60px;
  background: #eeeeee;
  color: black;
  border: 1px solid black;
  padding: 10px;
  border-radius: 50%;

}
.user-info {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-top: 20px;
  width: 100%;
  padding: 0px 200px;
}
.buttons{
    margin-top: 20px;
    display: flex;
    flex-direction: column;

    align-items: center;
    gap:90px
    

}
button{
    position: relative;
    text-align: center;
    background-color:white;
    
    width: 90%; 
    max-width: 300px; 
    font-size: 36px;
    font-family:'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
    font-weight: 400;
    border:1px solid darkgray;
    border-radius: 12px;

}


button:hover{
    cursor: pointer;
    box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2); /* 添加阴影 */
    transform: translateY(-1px); /* 悬停时略微上移 */ 
}

label {
    text-decoration: underline; /* 默认有下划线 */
    cursor: pointer;
    font-family:'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;
    color: blue
}

label:hover {
    font-weight: bold; /* 鼠标悬停时加粗 */
}
.badge {
  position: absolute;
  top: 0px;
  right: 0px;
  background: red;
  color: white;
  font-size: 12px;
  font-weight: bold;
  padding: 3px 7px;
  border-radius: 50%;
  transform: translate(50%, -50%);
}
</style>