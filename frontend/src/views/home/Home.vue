<script setup>
    import { onMounted } from 'vue'
    import { ref,computed} from 'vue';
    import {get,post} from '@/net/index'
    import router from "@/routers/route"
    onMounted(() => {
        get("/api/get_post_list",(res)=>{
            console.log(res)
            posts.value=res.map(item=>({
              id: item.id,
              title: item.title,
              user: item.publisher_id,
              details: item.details,
              views: item.views,
              date: item.create_time
            }))
          })

    })

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

</script>
<template>
      
    <div class="main-content">
      
      <div class="banner">
        <text style="font-weight: bold;">Advertising Space for Rent</text>
      </div>

     
      <div class="sort-bar">
        <div>
          <el-button @click="sortBy = 'views'" :type="sortBy === 'views' ? 'primary' : ''">Sort by views</el-button>
          <el-button @click="sortBy = 'time'" :type="sortBy === 'time' ? 'primary' : ''">Sort by time</el-button>
        </div>
        
        <el-button type="success" class="post-btn">Post</el-button>
      </div>

      
      <div class="post-list">
        <el-card v-for="post in sortedPosts" :key="post.title" shadow="hover" class="post-card"
              @click="goToDetail(post.id)">

          <h3 style="font-weight: bold;">{{ post.title }}</h3>
          <p>{{ post.details }}</p>
          <p>{{ post.views }} views, {{ post.date }}</p>
        </el-card>
      </div>
    </div>
  </template>
  



  <style scoped>

  /* 🌟 让 main-content 占满剩余空间 */
  .main-content {
    flex: 1;  /* 让它自动填充剩余空间 */
    display: flex;
    flex-direction: column;
    padding: 10px;
    width: 500px;
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
  .post-list {
    margin-top: 10px;
    flex: 1;
  }
  
  .post-card {
    margin-bottom: 10px;
  }

  </style>
  