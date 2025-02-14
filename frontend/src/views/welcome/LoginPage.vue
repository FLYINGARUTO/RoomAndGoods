<script setup>
import {reactive,ref} from "vue";
import {User,Lock} from '@element-plus/icons-vue'
// import {login} from "../../net/index.js";
// import router from "../../router/router.js";

const form =reactive({
  username:'',
  password:'',
  remember: false
})
const formRef=ref()

const rule={
  username:[
    {required: true,message:"请输入用户名"}
  ],
  password:[
    {required: true,message:"请输入密码"}
  ]}

// function loginForm(username,){
//   formRef.value.validate((valid)=>{
//     if(valid)
//       login(form.username,form.password,form.remember,()=>{
//         router.push('/index')
//       })
//   })
// }
</script>

<template>
  <div style="text-align: center;margin: 0 20px">
    <div style="margin-top: 180px">

      <div style="font-size: 30px;font-weight: bold">登录</div>
      <div style="font-size: 13px;color: grey">输入用户名和密码登录，访问更多功能</div>
    </div>
    <div style="margin-top: 50px">
      <el-form :rules="rule" :model="form" ref="formRef">
          <el-form-item prop="username">
            <el-input v-model="form.username" maxlength="30" type="text" placeholder="用户名/邮箱">
              <template #prefix>
                <el-icon><User/></el-icon>
              </template>
            </el-input>
          </el-form-item>
          <el-form-item prop="password">
            <el-input v-model="form.password" maxlength="20" type="password" placeholder="密码">
              <template #prefix>
                <el-icon><Lock /></el-icon>
              </template>
            </el-input>
          </el-form-item>
          <el-row>
            <el-col :span="12" style="text-align: left">
                <el-checkbox v-model="form.remember" label="记住我"/>
            </el-col>
            <el-col :span="12" style="text-align: right">
                <el-link @click="router.push('/reset')">忘记密码？</el-link>
            </el-col>
          </el-row>
          <div style="margin-top: 40px">
              <el-button @click="loginForm" style="width: 200px" type="success" plain>立即登录</el-button>
          </div>
          <el-divider style="font-size: 13px;color: grey">没有账号？</el-divider>
          <div>
            <el-button @click='router.push("/register")' style="width: 200px;" type="warning" plain>立即注册</el-button>
          </div>
      </el-form>
    </div>
  </div>
</template>

<style scoped>

</style>