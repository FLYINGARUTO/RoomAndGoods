<script setup>
    import { onMounted } from 'vue'
    import { ref,computed} from 'vue';
    import {get,post} from '@/net/index'
    import router from "@/routers/route"
    import { usePostStore } from '@/store/postStore';
    import {
      ArrowDown,
      Check,
      CircleCheck,
      CirclePlus,
      CirclePlusFilled,
      Plus,
    } from '@element-plus/icons-vue'
    // const postStore =usePostStore()
    import { useUrlStore } from '@/store/urlStore';
    const urlStore =useUrlStore()
    const username=localStorage.getItem('loginedUser')
    onMounted(() => {
        get("/api/get/post-list",(res)=>{
            console.log(res)
            posts.value=res.map(item=>({
              id: item.id,
              title: item.title,
              user: item.publisher,
              details: item.details,
              views: item.views,
              date: item.create_time,
              category: item.category,
              image: item.image,
              likes: item.likes

            }))
          })

    })
    const selectedCategory= ref("all")
    //根据分类过滤
    const filteredPosts = computed(() =>
            selectedCategory.value === "all"
                ? posts.value
                : posts.value.filter(post => post.category === selectedCategory.value)
        );
    // Sample post data
    const posts = ref([]);

    const sortBy = ref('views'); // Default sorting method

    // Sorting logic
    const sortedPosts = computed(() => {
      return [...filteredPosts.value].sort((a, b) => (sortBy.value === 'views' ? b.views - a.views : new Date(b.date) - new Date(a.date)));
    });

    const goToDetail=(postId)=>{
        router.push(`/post/${postId}`)
    }
    const toPost=()=>{
      if(!localStorage.getItem('accessToken')){
        alert('please login first')
      }else{
        router.push('/post/new')
      }
    }
    const BASE_URL = urlStore.baseUrl

    const getImageUrl = (imagePath) => {
      return imagePath ? `${BASE_URL}${imagePath}` : `${BASE_URL}/media/uploads/white.png`; // 处理 null 或 undefined
    };

</script>
<template>
      
    <div class="main-content">
      <el-divider v-if="username!=null">{{ "Welcome, "+ username}}</el-divider>

      <!-- <div class="banner">
        <text style="font-weight: bold;">投放广告联系abc@abc.com</text>
      </div> -->

      <div class="sort-bar">
        <div style="width: 30%;">
          <el-button @click="selectedCategory='all'" class="sidebar-btn" :class="{active: selectedCategory=='all'}">All</el-button>
          <el-button @click="selectedCategory='Used'" class="sidebar-btn" :class="{active: selectedCategory=='Used'}" >Used Goods</el-button>
          <el-button @click="selectedCategory='Sublet'" class="sidebar-btn" :class="{active: selectedCategory=='Sublet'}">Sublet</el-button>
          
        </div>
        <div> 
          <el-dropdown trigger="click">
            <span class="el-dropdown-link" >
              Sort by<el-icon ><arrow-down /></el-icon>
            </span>
            <template #dropdown>
              <el-dropdown-menu>
                <el-dropdown-item @click="sortBy='views'">Views</el-dropdown-item>
                <el-dropdown-item @click="sortBy='times'">Time</el-dropdown-item>
              </el-dropdown-menu>
            </template>
          </el-dropdown>
          <el-button type="success" class="btn" @click="toPost">Post</el-button>
        </div>
        
      </div>

      
      <div class="post-list">
        <el-card v-for="post in sortedPosts" :key="post.title" shadow="hover" class="post-card"
              @click="goToDetail(post.id)">
          <img :src="getImageUrl(post.image)">
    
          <h3 style="font-weight: bold;">{{ post.title }}</h3>
            
   
          
          <div style="justify-content: space-between; display: flex; color: darkgray;">
            <p>{{ post.user }}</p>
            <p>{{ post.likes }} 🩶</p>
            
             
            
          </div>
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
    width: 100%;
    display: flex;

  
  }
  
  /* Banner */
  .banner {
    width: 100%;
    height: 100%;
    max-height: 100px;
    background: white;
    border-radius: 15px;
    border:1px solid #eeeeee;
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 20px;
    
  }
  
  /* Sorting Bar */
.sort-bar {
  display: flex;
  justify-content:space-between; /* ✅ 让第一个和最后一个元素分开 */
  align-items: center;
  width: 100%;
  margin-top: 10px;
  padding: 10px 20px;
  
}

  
  .sort-bar .el-button {
    margin-right: 10px;
  }
  .sidebar-btn {
  text-align: center;
  background-color:white;
  margin-left: 0px;
  width: 100%; /* ✅ 统一按钮宽度 */
  max-width:80px; /* ✅ 确保不会太宽 */
  font-size: 14px;
  font-family:'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
  font-weight: 500;
  border:1px solid darkgray;
  border-radius: 5px;


}
.active{
  background-color: #007bff;
    color: white;
}
  /* Post List */
  .post-list1 {
    overflow:auto;
    margin-top: 10px;
    flex: 1;
  }
  .btn{
    margin-left: 30px;
    font-family:'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
  }
  .post-card1 {
    margin-bottom: 10px;
  }
  .el-dropdown-link {
  
  margin-top: 8px;
  display: flex;
  align-items: center;
  color:#007bff;
  font-weight: bold;

}

.post-list2 {
    display: grid;
    grid-template-columns: repeat(3, 1fr); 
    gap: 20px; /* 控制卡片间距 */
    margin-top: 10px;
    overflow-y: auto;
}
.post-list {
    column-count: 3;  /* ✅ 让它变成 3 列 */
    column-gap: 20px; /* ✅ 控制列间距 */
    margin-top: 10px;
}


.post-card {
  
    width: 100%; /* 让卡片充满父容器 */
    max-width: 400px; /* 设置最大宽度，防止太大 */
    height: fit-content;
    display: flex;
    flex-direction: column;
    align-items:center;
    justify-content: flex-start; /* 让内容均匀分布 */

    border-radius: 10px;
    margin-bottom: 10px;
    display: inline-block;
    position: relative; /* ✅ 让 `hover` 效果只影响自己 */

}

.post-card:hover {
    border: 1px solid rgba(0, 0, 0, 0.5); /* ✅ 确保 border 不会让高度变化 */
}

img{
  width: 100%;
  height: auto;
  
  object-fit: contain;
  border-radius: 15px;
  border: 1px solid #eeeeee;
}
  </style>
  