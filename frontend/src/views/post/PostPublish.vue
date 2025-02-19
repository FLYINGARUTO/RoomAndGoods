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
        <el-button class="button" :disabled="processing==true" @click="publishPost" type="success">Publish</el-button>
      </div>
  
      
    </div>
    
  </template>
  
  <script setup>
  import { ref } from "vue";
  import {post,get,internalPost} from "@/net/index"
import router from "@/routers/route";
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
      photos.value[index] = URL.createObjectURL(file); // Show preview
      photoFiles.value[index] = file; // Store file for submission
    }
  };
  
  // 🔹 Send form data & files to backend
  const publishPost = () => {
    if(form.value.title=="" || form.value.type=="" ||form.value.details==""){
      alert("All input items are required, please try again")
    }
    else{
      processing.value=true
      const formData = new FormData();
      formData.append("title", form.value.title);
      formData.append("type", form.value.type);
      formData.append("details", form.value.details);
    
      // Append each file to FormData
      photoFiles.value.forEach((file, index) => {
        if (file) {
          formData.append(`photos`, file); // Backend should expect 'photos' as an array
        }
      });
    
      internalPost("http://127.0.0.1:8000/api/post/publish/", formData, {
          headers: {
            "Content-Type": "multipart/form-data",
          },
        },(response)=>{
          console.log("Upload Successful:", response);
          alert("Post Published Successfully!");
          processing.value=false
          //成功后清空页面
          form.value=[]
          photos.value=Array(6).fill(null)
          photoFiles.value=Array(6).fill(null)
          router.push('/')
        },(error)=>{
          console.error("Upload Failed:", error);
        alert("Failed to publish post.");
        });
      
    }
    

  };
  </script>
  
  
  <style scoped>
  .post-form {
    display: flex;
    flex-direction: column;
    width: 700px;
    max-width: 100%;
    margin: 30px auto;
    gap: 10px;
    background: white;
    padding: 50px;
    border-radius: 10px;
    border: 1px solid #ddd;
  }
  
  .radio-group {
    display: flex;
    gap: 45px;
  }
  
  .photo-grid {
    display: grid;
    /* grid-template-columns: repeat(3, 1fr); */
    grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
    align-items: center;
    justify-content: center;
    gap: 10px;
    width: 100%;
  }
  
  .photo-box {
    width: 100%;
    aspect-ratio: 1/1;
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
    opacity: 0.5;
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
  