<script setup>
import { useRouter } from 'vue-router';
const route =useRouter()
const goBack = () => {
  route.back(); // 返回上一页
};
</script>

<template>
  <div>






    <!-- 这里才是核心 -->
    <router-view v-slot="{Component}">
          <transition name="el-zoom-in-center" mode="out-in" >
            <component :is="Component"/>
          </transition>
    </router-view>






              <!-- 悬浮回退按钮 -->
    <button class="floating-button" @click="goBack">
        ⬅ Back
    </button>
  </div>
  

</template>










<style scoped>
/* 悬浮按钮样式 */
.floating-button {
  position: fixed;  /* ✅ 让按钮固定在页面上 */
  bottom: 20px;     /* ✅ 距离底部 20px */
  right: 30px;      /* ✅ 距离右侧 20px */
  background-color: #007bff;  /* 按钮颜色 */
  color: white; 
  border: none;
  padding: 12px 20px;
  font-size: 16px;
  border-radius: 30px;
  cursor: pointer;
  box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);font-family: Verdana, Geneva, Tahoma, sans-serif;
  /* transition: background 0.3s ease; */
}

.floating-button:hover {
  background-color: #0056b3;
}
</style>
