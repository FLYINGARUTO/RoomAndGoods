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
        <button @click="router.push('/my/post')">My Posts</button>
        <button @click="router.push('/my/like')">My Likes</button>
        <button @click="router.push('/my/star')">My Stars</button>
    </div>
    
  </div>
</template>

<script setup>
import router from "@/routers/route"
const username=localStorage.getItem('loginedUser')

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
    margin-top: 180px;
    display: flex;
    flex-direction: row;

    justify-content: center;
    gap:150px
    

}
button{
        text-align: center;
    background-color:white;
    margin-left: 20px;
    width: 100%; /* ✅ 统一按钮宽度 */
    max-width: 100px; /* ✅ 确保不会太宽 */
    font-size: 30px;
    font-family:'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
    font-weight: 500;
    border:1px solid darkgray;
    border-radius: 5px;

}
button:hover{
    cursor: pointer; 
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

</style>