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
    const username=localStorage.getItem('loginedUser')
    onMounted(() => {
        get("/api/get/post-list",(res)=>{
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

</script>
<template>
      
    <div class="main-content">
      <el-divider v-if="username!=null">{{ "Welcome,"+ username}}</el-divider>
      <div class="banner">
        <text style="font-weight: bold;">投放广告联系abc@abc.com</text>
      </div>

       
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
    overflow: auto;
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
  .post-list {
    overflow:auto;
    margin-top: 10px;
    flex: 1;
  }
  .btn{
    margin-left: 30px;
    font-family:'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
  }
  .post-card {
    margin-bottom: 10px;
  }
  .el-dropdown-link {
  
  margin-top: 8px;
  display: flex;
  align-items: center;
  color:#007bff;
  font-weight: bold;

}
  </style>
  