<template>
    <div class="post-form">
      <label style="font-weight: bold;">Title</label>
      <input v-model="form.title" type="text"  class="input"/>
  
      <label style="font-weight: bold;margin-top: 20px;">Type</label>
      <div class="radio-group">
        <label>
          <input type="radio" value="Used" v-model="form.type" /> Used
        </label>
        <label>
          <input type="radio" value="Sublet" v-model="form.type" /> Sublet
        </label>
        <label>
          <input type="radio" value="Other" v-model="form.type" /> Other
        </label>
      </div>
  
      <label style="font-weight: bold;margin-top: 20px;">Details</label>
      <input v-model="form.details" type="text" class="input"/>
  
      <label style="font-weight: bold;margin-top: 20px;">Photos</label>
      <div class="photo-grid">
        <div v-for="(photo, index) in photos" :key="index" class="photo-box">
          <img v-if="photo" :src="photo" alt="Uploaded Image" />
          <input type="file" @change="handleFileUpload($event, index)" />
        </div>
      </div>
      <div style="text-align: center;">
        <el-button 
        class="button" 
        :loading="processing" 
        :disabled="processing" 
        @click="publishPost" 
        type="success">
        {{ processing ? "Publishing..." : "Publish" }}
      </el-button>

      </div>
  
      
    </div>
    
  </template>
  
  <script setup>
  import { ref } from "vue";
  import {post,get,internalPost} from "@/net/index"
  import { ElLoading, ElMessage } from "element-plus"; // ✅ 引入加载 & 消息组件

  import router from "@/routers/route";
  import { useUrlStore } from "@/store/urlStore";
  import Compresser from "compressorjs"
  const urlStore = useUrlStore()
  const BASE_URL=urlStore.baseUrl

  const processing=ref(false)
  // 🔹 Define reactive form data
  const form = ref({
    title: "",
    type: "",
    details: "",
  });
  const formRef=ref()
  // const rules=
  // 🔹 Define a reactive array for photos (6 slots)
  const photos = ref(Array(6).fill(null));
  const photoFiles = ref(Array(6).fill(null)); // Store actual file objects
  
  // 🔹 Handle file upload and store the actual file object
  const handleFileUpload = (event, index) => {
    const file = event.target.files[0];
    if (file) {
      new Compresser(file,{
        quality: 0.7,
        maxWidth: 1600,
        success(result){
          photos.value[index] = URL.createObjectURL(result); // Show preview
          photoFiles.value[index] = new File([result], file.name, { type: file.type }); // 确保是 File
        },
        error(err){e
          console.log("Compression Error:",err)
        },
      })
      
    }
  };
  
  // 🔹 Send form data & files to backend
  const publishPost = () => {
    if(form.value.title=="" || form.value.type=="" ||form.value.details==""){
      alert("All input fields are required!");
    }
    else{
      alert('The server is located in Shanghai, so it may take some time to upload. We appreciate your patience')
            // 显示加载框
      // const loadingInstance = ElLoading.service({
      //   lock: true,
      //   text: "Publishing your post...",
      //   background: "rgba((238, 238, 238, 1)",
      //   fullscreen: true,  // ✅ 确保加载框完全覆盖屏幕
      // });
      processing.value=true
      const formData = new FormData();
      formData.append("title", form.value.title);
      formData.append("type", form.value.type);
      formData.append("details", form.value.details);
      formData.append("username",localStorage.getItem('loginedUser'))
      formData.append("user-id",localStorage.getItem('loginedUserId'))
    
      // Append each file to FormData
      photoFiles.value.forEach((file, index) => {
        if (file) {
          formData.append(`photos`, file); // Backend should expect 'photos' as an array
        }
      });
      const token=localStorage.getItem('accessToken')
      const headers={
            "Content-Type": "multipart/form-data",
            "Authorization": `Bearer ${token}`,
          } 
      console.log("🚀 Final Request Headers:", JSON.stringify(headers, null, 2)); // ✅ 确保 headers 正确

      internalPost(`${BASE_URL}/api/post/publish/`, formData,
          headers
        ,(response)=>{
          console.log("Upload Successful:", response);
          alert("Post published successfully!");
              // 关闭加载框
          // loadingInstance.close();
          console.log('published')
          processing.value=false
          //成功后清空页面
          form.value=[]
          photos.value=Array(6).fill(null)
          photoFiles.value=Array(6).fill(null)
          router.push('/')
        },(error)=>{
          console.error("Upload Failed:", error);
          alert("Failed to publish post.");
          // loadingInstance.close();
          processing.value=false
          form.value=[]
          photos.value=Array(6).fill(null)
          photoFiles.value=Array(6).fill(null)
          
        });

    
    }
    

  };
  </script>
  
  
  <style scoped>
  .post-form {
    align-content: center;
    display: flex;
    flex-direction: column;
    width: 1200px;
    height:100vh;
    max-width: 100%;
    margin-top: 20px;
    gap: 10px;
    background: white;
    padding: 60px 100px;
    border-radius: 10px;
    border: 1px solid #ddd;
    overflow: auto;
  }
  
  .radio-group {
    display: flex;
    gap: 45px;
  }
  
  .photo-grid {
    display: grid;
    /* grid-template-columns: repeat(3, 1fr); */
    grid-template-columns: repeat(3,1fr);
    align-items: center;
    justify-content: center;
    gap: 10px;
    width: 100%;
  }
  
  .photo-box {
    width: 100%;
    aspect-ratio: 1;
    border: 1px solid black;
    border-radius: 10px;
    display:flex;
    flex-direction: column;
    align-items: center;
    justify-content:center;
    text-align: center;
    overflow: hidden;
    position: relative;
  }
  /* Hide default input file button */
.photo-box input[type="file"] {

    width: 100%;
    height: 100%;
    opacity: 0;
    cursor: pointer;
}

/* If image is uploaded, make sure it fits */
.photo-box img {
    max-width: 100%;
    max-height: 100%;
    object-fit: cover;

}
  
  .button {
    margin: 30px auto;
    width:100px;
    padding: 8px;
    border-radius: 5px;
    cursor: pointer;
  } 
  .input{
    border-radius: 4px;
    height: 30px;
    border: 1px solid #333333;
  }
  </style>
  @/net/index(localstorage)