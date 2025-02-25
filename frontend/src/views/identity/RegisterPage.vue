<script setup>
import {reactive,ref} from "vue";
import {User,Lock} from '@element-plus/icons-vue'
// import {login} from "../../net/index.js";
import router from "@/routers/route";
import {get,post} from "@/net/index"

const form =reactive({
    username:'',
    password:'',
    rePassword:''
})
const formRef=ref()

const rule={
    username:[
        {required: true,message:"username cannot left blank"}
    ],
    password:[
        {required: true,message:"password cannot left blank"}
    ],
    rePassword:[
        {required: true,message:"please confirm the password"}
    ]}

function registerForm(){
  formRef.value.validate((valid)=>{
    if(valid){
      post('api/post/register/',{username:form.username,password:form.password},(res)=>{
        console.log("api/post/register/ : ",res)
        
        
        router.push('/login')
        alert('signed up successfully')

      })
    }
  })
}
</script>

<template>
  <div style="text-align: center; font-family: Verdana, Geneva, Tahoma, sans-serif;" class="container">
    <div style="margin-top:60px">

      <div style="font-size: 30px;font-weight: bold">Create Your Account</div>
      <div style="font-size: 13px;color: grey">you are almost there!</div>
    </div>
    <div style="margin-top: 50px">
      <el-form :rules="rule" :model="form" ref="formRef">
          <el-form-item prop="username">
            <el-input v-model="form.username" maxlength="30" type="text" placeholder="username">
              <template #prefix>
                <el-icon><User/></el-icon>
              </template>
            </el-input>
          </el-form-item>
          <el-form-item prop="password">
            <el-input v-model="form.password" maxlength="20" type="password" placeholder="password">
              <template #prefix>
                <el-icon><Lock /></el-icon>
              </template>
            </el-input>
          </el-form-item>
          <el-form-item prop="rePassword">
            <el-input v-model="form.rePassword" maxlength="20" type="password" placeholder="confirm password">
              <template #prefix>
                <el-icon><Lock /></el-icon>
              </template>
            </el-input>
          </el-form-item>

          <div style="margin-top: 40px">
              <el-button @click="registerForm" style="width: 200px" type="success" plain>register</el-button>
          </div>
          <el-divider style="font-size: 13px;color: grey">I have account</el-divider>
          <div>
            <el-button @click='router.push("/login")' style="width: 200px;" type="warning" plain>login</el-button>
          </div>
      </el-form>
    </div>
  </div>
</template>

<style scoped>
.container {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    width: 400px;  /* 适当设定宽度 */
    padding: 20px;
    background: white;
    border-radius: 10px;
    border: 1px solid #ddd;
    box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
}
</style>