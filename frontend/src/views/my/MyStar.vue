<script setup>
    import { onMounted } from 'vue'
    import { ref,computed} from 'vue';
    import {get,post} from '@/net/index'
    import router from "@/routers/route"
    // import { usePostStore } from '@/store/postStore';
    // const postStore =usePostStore()
    import { useUrlStore } from '@/store/urlStore';
    const urlStore =useUrlStore()
    onMounted(() => {
        post("/api/post/get-starred-posts/",{"username":localStorage.getItem('loginedUser')},(res)=>{
            console.log(res)
            posts.value=res.map(item=>({
              id: item.id,
              title: item.title,
              user: item.publisher,
              details: item.details,
              views: item.views,
              date: item.create_time,
              category: item.category,
              image: item.image
            }))
          })

    })
    //根据分类过滤
    
    // const filteredPosts = computed(() =>
    //         postStore.selectedCategory === "All"
    //             ? posts.value
    //             : posts.value.filter(post => post.category === postStore.selectedCategory)
    //     );
      
    // Sample post data
    const posts = ref([]);

    const sortBy = ref('views'); // Default sorting method

    // Sorting logic
    const sortedPosts = computed(() => {
      return [...posts.value].sort((a, b) => (sortBy.value === 'views' ? b.views - a.views : new Date(b.date) - new Date(a.date)));
    });

    const goToDetail=(postId)=>{
        router.push(`/post/${postId}`)
    }

    const BASE_URL = urlStore.baseUrl

    const getImageUrl = (imagePath) => {
      return imagePath ? `${BASE_URL}${imagePath}` : `${BASE_URL}/media/uploads/white.png`; // 处理 null 或 undefined
    };
</script>
<template>
      
    <div class="main-content">
      
      <el-divider></el-divider>
     <h1 style="margin:0px auto">My Stars</h1>
     <el-divider></el-divider>
      <div class="sort-bar">
        <div>
          <label style="margin: 15px;font-weight: 600;">Sort by</label>
          <el-button @click="sortBy = 'views'"
                     :type="sortBy === 'views' ? 'primary' : ''"
                     class="btn">views</el-button>
          <el-button @click="sortBy = 'time'" 
                      :type="sortBy === 'time' ? 'primary' : ''"
                      class="btn">time</el-button>
        </div>
        
      </div>

      
      <div class="post-list">
        <el-card v-for="post in sortedPosts" :key="post.title" shadow="hover" class="post-card"
              @click="goToDetail(post.id)">
          <img :src="getImageUrl(post.image)">
    
          <h3 style="font-weight: bold;">{{ post.title }}</h3>
            
   
          
          <div style="justify-content: space-between; display: flex; color: darkgray;">
            <p>{{ post.user }}</p><p>{{ post.views }} views</p>
            <p>{{ post.date }}</p>
             
            
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
    overflow-y: auto;
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

  .btn{
    font-family: Verdana, Geneva, Tahoma, sans-serif;
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
  