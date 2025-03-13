<script setup>
import {onMounted, reactive,ref} from "vue";
import {User,Lock} from '@element-plus/icons-vue'
// import {login} from "../../net/index.js";
import router from "@/routers/route";
import {get,post} from "@/net/index"

const form =reactive({
  username:'',
  password:'',
  remember: false
})
const formRef=ref()

const rule={
  username:[
    {required: true,message:"username cannot left blank"}
  ],
  password:[
    {required: true,message:"password cannot left blank"}
  ]}
onMounted(()=>{
    localStorage.removeItem('accessToken')
    localStorage.removeItem('refreshToken')
    localStorage.removeItem('loginedUser')
})
function loginForm(){
  formRef.value.validate((valid)=>{
    if(valid){
      post('api/post/login/',{username:form.username,password:form.password},(res)=>{
        console.log("?",res)
        localStorage.setItem('loginedUser',res.loginedUser)
        localStorage.setItem('loginedUserId',res.userId) 
        if(res.token){
          localStorage.setItem('accessToken',res.token.access)
          localStorage.setItem('refreshToken',res.token.refresh)
        }
        
        router.push('/')
        alert('Logged in')

      })
    }
  })
}
</script>

<template>
  <div style="text-align: center; font-family: Verdana, Geneva, Tahoma, sans-serif;" class="container">
    <div style="margin-top:60px">

      <div style="font-size: 30px;font-weight: bold">Goods and Rooms</div>
      <div style="font-size: 13px;color: grey">ready to explore?</div>
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
          <el-row>
            <el-col :span="12" style="text-align: left">
                <el-checkbox v-model="form.remember" label="remember"/>
            </el-col>
            <el-col :span="12" style="text-align: right">
                <el-link @click="router.push('/reset')">forgot password</el-link>
            </el-col>
          </el-row>
          <div style="margin-top: 40px">
              <el-button @click="loginForm" style="width: 200px" type="success" plain>login</el-button>
          </div>
          <el-divider style="font-size: 13px;color: grey">no account?</el-divider>
          <div>
            <el-button @click='router.push("/register")' style="width: 200px;" type="warning" plain>register</el-button>
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