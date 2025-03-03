<script setup>
    import { onMounted } from 'vue'
    import { ref,computed} from 'vue';
    import {get,post} from '@/net/index'
    import router from "@/routers/route"

    onMounted(() => {
        post("/api/post/msg-list/",{"username":localStorage.getItem('loginedUser')},(res)=>{
            console.log(res)
            messages.value=res.map(item=>({
              id: item.id,
              from_user: item.from_user,
              to_user: item.to_user,
              details: item.text,
              read: item.read,
              date: item.created_time,
              reply: item.reply
            }))
          })

    })
  
    // Sample post data
    const messages = ref([]);

    const sortBy = ref('desc'); // Default sorting method

    // Sorting logic
    const sortedMsgs = computed(() => {
      return [...messages.value].sort((a, b) => (sortBy.value === 'desc' ?  new Date(b.date) - new Date(a.date) : new Date(a.date) - new Date(b.date)));
    });
    const showMsgBox=ref(false)
    const chosenMsg=ref({})
    const openMsgBox=(msg)=>{
        showMsgBox.value=true
        chosenMsg.value.details=msg.details
        chosenMsg.value.from_user=msg.from_user
        chosenMsg.value.id=msg.id
        
    }

    const mark_read=()=>{
      post('api/post/read-all/',{
        "username":localStorage.getItem('loginedUser')
      },(res)=>{
        console.log(res)

        router.go(0)
      })
    }
    const replyMsg=ref('')
    const sendMessage=()=>{
      if(replyMsg.value!==""){
        post('api/post/reply/',{
          'id':chosenMsg.value.id,
          'from-user':localStorage.getItem("loginedUser"),
          "to-user":chosenMsg.value.from_user,
          "msg":replyMsg.value
        },(res)=>{
          alert(res)
          router.go(0)
        })
      }else{
        alert('Reply message cannot be blank')
      }
    }

</script>
<template>
      
    <div class="main-content">
      
      <el-divider></el-divider>
     <h1 style="margin:0px auto">Message Box</h1>
     <el-divider></el-divider>
      <div class="sort-bar">
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
        
      </div>

      
      <div class="msg-list">
        <el-card v-for="msg in sortedMsgs" :key="msg.id" shadow="hover" class="msg-card" @click="openMsgBox(msg)">

          <h3 style="font-weight: bold;">{{ msg.from_user }}</h3>
          <p style="margin-top: 5px;">{{ msg.details }}</p>
          <div style="margin-top: 5px;justify-content: space-between; display: flex; color: darkgray;">

            <p>{{ msg.date }}</p>
            <div>
              <label v-if="msg.read==0" style="margin-right: 15px; color: coral;">Un-read</label> 
              <label v-if="msg.reply==0" style="color:red;">Un-replied</label>
               
            </div>
            
          </div>
        </el-card>
      </div>
      <div>
            <!-- <input-box :caption="caption" :show="showInput" :value="inputValue" @close="showInput=false" @confirm="inputBoxYes" @cancel="showInput=false">
          </input-box> -->
            <el-dialog v-model="showMsgBox" title="Reply">
              <label>{{chosenMsg.from_user}}:"{{ chosenMsg.details }}"</label>
              <el-input v-model="replyMsg"></el-input>
              <template #footer>
                <span>

                  <el-button @click="sendMessage" style="width: 100px;border-radius: 10px;">send</el-button>
                </span>
              </template>
            </el-dialog>
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
    width: 100%;
    display: flex;
    justify-content: center;
    overflow-y: auto;
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
    overflow:auto;
    margin-top: 10px;
    flex: 1;
  }
  .btn{
    font-family: Verdana, Geneva, Tahoma, sans-serif;
  }
  .msg-card {
    margin-bottom: 10px;
  }

  </style>
  