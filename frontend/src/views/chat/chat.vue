<template>
    <div class="chat-container">
      <!-- 顶部显示对话信息 -->
      <div class="chat-header">
        <button class="back-button" @click="goBack">⬅ Back</button>
        <h3 style="font-weight: bold;">{{chat_with_name}}</h3>
      </div>

  
      <!-- 消息列表 -->
      <div class="chat-messages" ref="messageBox">
        <div v-for="msg in messages" :key="msg.id" 
             :class="{'my-message': msg.sender ==  loginedUserId , 'other-message' : msg.sender !=  loginedUserId}">
          <!-- <label>{{ msg.sender==loginedUserId ? loginedUser:chat_with_name }}</label> -->
          <p>{{ msg.content }}</p>
          <span class="time">{{ msg.timestamp }}</span>
        </div>
      </div>
  
      <!-- 输入框 -->
      <div class="chat-input">
        <input v-model="newMessage" @keydown.enter="sendMessage" placeholder="type in..." />
        <button @click="sendMessage">send</button>
      </div>
    </div>
</template>
<script setup>
import { post } from '@/net';
import {ref, onMounted,onUnmounted} from 'vue';
import { useRoute,useRouter } from 'vue-router';
import { useUrlStore } from '@/store/urlStore';
const urlStore = useUrlStore()
const BASE_URL=urlStore.baseUrl.slice(7)
const router =useRouter()
const route=useRoute()
const newMessage=ref('') //存储新输入的消息内容
const messageBox = ref(null) //绑定消息列表的 DOM 元素，方便滚动到底部
const messages=ref([]) //聊天内容数组
const chat_with_id=ref(null) // 当前聊天对象的id
const chat_with_name=ref('')
const ws = ref(null) // WebSocket连接对象
const loginedUserId=localStorage.getItem('loginedUserId')
const loginedUser=localStorage.getItem('loginedUser')
const goBack = () => {
  router.back(); // 返回上一页
};
onMounted(()=>{
    chat_with_id.value=route.params.chatWith
    chat_with_name.value=route.params.chatTarget
    const chat_room=`${Math.min(loginedUserId, chat_with_id.value)}_${Math.max(loginedUserId, chat_with_id.value)}`;
    post('api/post/load-chat/',
        {'chatWith':chat_with_id.value},
        (res)=>{
            console.log(res)
            messages.value=res.map(item=>({
                sender: item.sender,
                receiver: item.receiver,
                content: item.content,
                create_at : item.create_at,
                is_read: item.is_read
            }))
        }
    )
    ws.value = new WebSocket(`ws://${BASE_URL}/ws/chat/${chat_room}/`)

    ws.value.onmessage = (event)=>{
        const data=JSON.parse(event.data)
        messages.value.push(data);
        scrollToBottom()
    }
})

// 滚动消息列表到底部
const scrollToBottom = () => {
  setTimeout(() => {
    if (messageBox.value) { // 确保 DOM 元素存在
      messageBox.value.scrollTop = messageBox.value.scrollHeight; // 设置滚动高度为最大
    }
  }, 100); // 设置延迟，确保 DOM 更新后再滚动
};

// 组件卸载时，关闭 WebSocket 连接
onUnmounted(() => {
  if (ws.value) ws.value.close(); // 关闭 WebSocket 连接，防止内存泄漏
});
// 发送消息到 WebSocket 服务器
const sendMessage = () => {
  if (newMessage.value.trim() !== '') { // 确保消息非空
    ws.value.send(JSON.stringify({ // 发送 JSON 格式的消息
      sender: localStorage.getItem('loginedUserId'), // 当前用户 ID
      receiver: chat_with_id.value, // 接收方 ID
      content: newMessage.value, // 消息内容
    }));
    newMessage.value = ''; // 发送后清空输入框
  }
};
</script>
<style scoped>

.chat-container {
    font-family: Verdana, Geneva, Tahoma, sans-serif;
    display: flex; 
    flex-direction: column;
    padding: 10px;
    width: 40vw;;
    height:80vh;
    overflow: hidden;

    border-radius: 30px;
    border: 2px solid #eae8e8;

    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
}
.chat-header {
    width: 100%;
    padding: 10px;
  border-bottom: 1px solid #ddd;
  text-align: center;
}
.chat-header {
    position: relative;
    display: flex;
    align-items: center;
    justify-content: center; /* 让标题居中 */
    padding: 10px;

    position: relative;
}

.back-button {
    position: absolute;
    left: 10px;
    background: none;
    border: none;
    font-size: 16px;
    cursor: pointer;
    color: #555;
}



.chat-messages {
    width: 100%;
  flex: 1;
  overflow-y: auto;
  padding: 10px;
  display: flex;
  flex-direction: column;
}
.my-message {
    margin-bottom: 5px;
    align-self: flex-end;
    max-width: 70%;
    
    
    text-align: right;

    display: inline-block;
    

}
.my-message p{
    background: #dcf8c6;
    border-radius: 10px;
    
    padding: 8px 14px;
}
.other-message {
    margin-bottom: 5px;
    max-width: 70%;
    /* min-width: 20%; */
    align-self: flex-start;
    text-align: left;

    display: inline-block;
     /* 让宽度根据内容自适应 */
}
.other-message p{
    background: #eee;
    border-radius: 10px;
    padding: 8px 18px;
}

.chat-input {
    
    height: 60px;
    width: 100%;
     display: flex;
    justify-content: space-between;
    padding: 10px;
    border-top: 1px solid #ddd;
}
.chat-input input{
    width: 90%;text-align: center;
    border-radius: 10px;
    border:1px #eee solid;
}

.chat-input button{
    margin-left: 10px;
    border-radius: 15px;
    width: 15%;
    border: #eee;
}
button:hover{
    cursor: pointer;

    transform: translateY(-1px); /* 悬停时略微上移 */ 
}

</style>