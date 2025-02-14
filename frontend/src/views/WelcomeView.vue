<script setup>

</script>

<template>
<!-- <div style="width: 100vw;height: 100vh;overflow: hidden;display: flex">
  <div style="flex: 1;background-color: black">
    <el-image style="width: 100%;height: 100%;"
        src="https://ts1.cn.mm.bing.net/th/id/R-C.3fc00701efb6127f9dc46e2db22e3c2f?rik=EnVuEm00EySCVA&riu=http%3a%2f%2fimg.netbian.com%2ffile%2f2023%2f1210%2f184925MxhjO.jpg&ehk=8EXBAVcGCWEXgTkrhT3l7MoiY%2bbGhefv6nD9gPyLGE0%3d&risl=&pid=ImgRaw&r=0" fit="cover"/>
  </div>

  <div class="welcome-title">
    <div style="font-size: 30px;font-weight: bold;">欢迎访问本站点</div>
    <div style="margin-top: 10px">更多功能，敬请等待～</div>
    <div style="margin-top: 5px">祝你拥有美好的一天，My friend</div>

  </div>
  <div class="right-card">
    <router-view v-slot="{Component}">
      <transition name="el-zoom-in-center" mode="out-in" >
        <component :is="Component"/>
      </transition>
    </router-view>
  </div>

</div> -->
<div style="width: 100vw; height: 100vh; overflow: hidden; display: flex; flex-direction: row;">
  <div style="flex: 1; background-color: black; display: flex; justify-content: center; align-items: center;">
    <el-image 
  style="width: 100%; height: 100%; object-fit: contain;"
  src="https://ts1.cn.mm.bing.net/th/id/R-C.3fc00701efb6127f9dc46e2db22e3c2f?rik=EnVuEm00EySCVA&riu=http%3a%2f%2fimg.netbian.com%2ffile%2f2023%2f1210%2f184925MxhjO.jpg&ehk=8EXBAVcGCWEXgTkrhT3l7MoiY%2bbGhefv6nD9gPyLGE0%3d&risl=&pid=ImgRaw&r=0"
  fit="contain"
/>

  </div>

  <div class="right-card">
    <router-view v-slot="{Component}">
      <transition name="el-zoom-in-center" mode="out-in">
        <component :is="Component"/>
      </transition>
    </router-view>
  </div>
</div>


</template>

<style scoped>
    .welcome-title{
      position: absolute;
      left: 30px ;
      bottom: 30px;
      color: white;
      text-shadow: 0 0 10px black;
    }
    .right-card{
      width: 400px;
      z-index: 1;
      background-color: white;
      display: flex;
      flex-direction: column;
      justify-content: center;
    }
</style>