<template>
    <div class="post-form">
      <label>Title</label>
      <input v-model="form.title" type="text" placeholder="Enter title" />
  
      <label>Type</label>
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
  
      <label>Details</label>
      <input v-model="form.details" type="text" placeholder="Enter details" />
  
      <label>Photos</label>
      <div class="photo-grid">
        <div v-for="(photo, index) in photos" :key="index" class="photo-box">
          <img v-if="photo" :src="photo" alt="Uploaded Image" />
          <input type="file" @change="handleFileUpload($event, index)" />
        </div>
      </div>
  
      <button @click="publishPost">Publish</button>
    </div>
  </template>
  
  <script setup>
  import { ref } from "vue";
  import {post,get} from "@/net/index"
  
  // 🔹 Define reactive form data
  const form = ref({
    title: "",
    type: "",
    details: "",
  });
  
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
  const publishPost = async () => {
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
  
    try {
      const response = await axios.post("http://127.0.0.1:8000/upload/", formData, {
        headers: {
          "Content-Type": "multipart/form-data",
        },
      });
  
      console.log("Upload Successful:", response.data);
      alert("Post Published Successfully!");
    } catch (error) {
      console.error("Upload Failed:", error);
      alert("Failed to publish post.");
    }
  };
  </script>
  
  
  <style scoped>
  .post-form {
    display: flex;
    flex-direction: column;
    max-width: 400px;
    margin: auto;
    gap: 10px;
  }
  
  .radio-group {
    display: flex;
    gap: 15px;
  }
  
  .photo-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 10px;
  }
  
  .photo-box {
    width: 80px;
    height: 80px;
    border: 1px solid black;
    border-radius: 8px;
    display: flex;
    align-items: center;
    justify-content: center;
    overflow: hidden;
  }
  
  .photo-box img {
    width: 100%;
    height: 100%;
    object-fit: cover;
  }
  
  button {
    background-color: black;
    color: white;
    padding: 8px;
    border-radius: 5px;
    cursor: pointer;
  }
  </style>
  