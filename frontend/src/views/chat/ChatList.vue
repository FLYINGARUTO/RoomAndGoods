<script setup>
    import { onMounted } from 'vue'
    import { ref,computed} from 'vue';
    import {get,post} from '@/net/index'
    import router from "@/routers/route"

    onMounted(() => {
        post("/api/post/chat-list/",{"user_id":localStorage.getItem('loginedUserId')},(res)=>{
            console.log(res)
            chat_targets.value=res.map(item=>({
              id: item.id,
              username: item.username,

            }))
          })

    })
  
    // Sample post data
    const chat_targets = ref([]);

    const sortBy = ref('desc');

    const openChatBox=(id,name)=>{
        router.push(`chat/${id}/${name}`)
    }


</script>
<template>
      
    <div class="main-content">
      
     <h1 style="margin:0px auto">💬</h1>
     <el-divider></el-divider>
      <!-- <div class="sort-bar">
        <div>
          <label style="margin: 15px;font-weight: 600;">Sort by Date</label>
          <el-button @click="sortBy = 'desc'"
                     :type="sortBy === 'desc' ? 'primary' : ''"
                     class="btn">recent to past</el-button>
          <el-button @click="sortBy = 'asc'" 
                      :type="sortBy === 'asc' ? 'primary' : ''"
                      class="btn">past to recent</el-button>
        </div>
        <el-button type="success" class="btn" @click="mark_read">mark as read</el-button>
        
      </div> -->

      
      <div class="msg-list">
        <el-card v-for="user in chat_targets" :key="user.id" shadow="hover" class="msg-card" @click="openChatBox(user.id,user.username)" >

          <h3 style="font-weight: bold;">{{ user.username }}</h3>
          <!-- <p style="margin-top: 5px;">{{ msg.details }}</p> -->
          <!-- <div style="margin-top: 5px;justify-content: space-between; display: flex; color: darkgray;">

            <p>{{ msg.date }}</p>
            <div>
              <label v-if="msg.read==0" style="margin-right: 15px; color: coral;">Un-read</label> 
              <label v-if="msg.reply==0" style="color:red;">Un-replied</label>
               
            </div>
            
          </div> -->
        </el-card>
      </div>

    </div>
  </template>
  



  <style scoped>

  /* 🌟 让 main-content 占满剩余空间 */
  .main-content {
    flex: 1;  /* 让它自动填充剩余空间 */
    flex-direction: column;
    padding: 10px;
    max-width: 100%;
    height: 100vh;
    width: 100vw;
    display: flex;
    justify-content: center;
    overflow-y: auto;
    margin: 0 auto;
font-family: Verdana, Geneva, Tahoma, sans-serif;
  }
  
  /* Banner */
  .banner {
    width: 100%;
    height: 100px;
    background: white;
    border-radius: 15px;
    border:1px solid #eeeeee;
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 20px;
    overflow: hidden;
  }
  
  /* Sorting Bar */
.sort-bar {
  display: flex;
  justify-content: space-between; /* ✅ 让第一个和最后一个元素分开 */
  align-items: center;
  width: 100%;
  margin-top: 10px;
  
}

  
  .sort-bar .el-button {
    margin-right: 10px;
  }
  
  /* Post List */
  .msg-list {
    margin: 0 auto;
    width: 40vw;
    overflow:auto;
    margin-top: 10px;
    flex: 1;
  }
  .btn{
    font-family: Verdana, Geneva, Tahoma, sans-serif;
  }
  .msg-card {
    margin-bottom: 10px;
    border-radius: 15px;
    text-align: center;
    
  }
  .msg-card:hover {
    cursor: pointer;
    
  }

  </style>
  