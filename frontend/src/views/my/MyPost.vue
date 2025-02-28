<script setup>
    import { onMounted } from 'vue'
    import { ref,computed} from 'vue';
    import {get,post} from '@/net/index'
    import router from "@/routers/route"
    import { usePostStore } from '@/store/postStore';
    const postStore =usePostStore()
    onMounted(() => {
        post("/api/post/get-my-posts/",{"username":localStorage.getItem('loginedUser')},(res)=>{
            console.log(res)
            posts.value=res.map(item=>({
              id: item.id,
              title: item.title,
              user: item.publisher_id,
              details: item.details,
              views: item.views,
              date: item.create_time,
              category: item.category
            }))
          })

    })
    //根据分类过滤
    const filteredPosts = computed(() =>
            postStore.selectedCategory === "All"
                ? posts.value
                : posts.value.filter(post => post.category === postStore.selectedCategory)
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


</script>
<template>
      
    <div class="main-content">
      
      <el-divider></el-divider>
     <h1 style="margin:0px auto">My Posts</h1>
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

          <h3 style="font-weight: bold;">{{ post.title }}</h3>
          <p style="margin-top: 5px;">{{ post.details }}</p>
          <div style="margin-top: 5px;justify-content: space-between; display: flex; color: darkgray;">
            <p>{{ post.views }} views</p> 
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
  .post-list {
    overflow:auto;
    margin-top: 10px;
    flex: 1;
  }
  .btn{
    font-family: Verdana, Geneva, Tahoma, sans-serif;
  }
  .post-card {
    margin-bottom: 10px;
  }

  </style>
  