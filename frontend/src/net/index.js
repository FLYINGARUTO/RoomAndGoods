import axios from "axios";
import {ElMessage} from "element-plus";
import router from "../routers/route.js";

const authItemName="access_token"

const defaultFailure=(message,code,url)=>{
    console.log(`请求地址：${url} ，状态码：${code} ，错误信息：${message}`)
    ElMessage.warning(message)
}
const defaultError = (error) =>{
    console.log(error)
    ElMessage.warning("发生了错误，请联系管理员")
}

/**
 * 封装axios post
 * @param url
 * @param data
 * @param header
 * @param success
 * @param failure
 * @param error
 */
function internalPost(url,data,header,success,failure=defaultFailure,error=defaultError){
    axios.post(url,data,{
        headers: header
    }).then(  ({data})  =>  {
        console.log(data)
            if(data.code===200){
                success(data.data)
            }else {
                failure(data.message,data.code,url)
            }
        }).catch(err =>
            error(err)
        )
}
function internalGet(url,header,success,failure=defaultFailure,error=defaultError){
    axios.get(url,{
        headers: header
    }).then(  ({data})  =>  {
            if(data.code===200){
                // console.log('internal get:',data)
                success(data.data)
            }else {
                failure(data.message,data.code,url)
            }
        }).catch(err =>
            error(err)
        )
}
function post(url,data,success,failure=defaultFailure){
    internalPost(url,data,getTokenHeader(),success)
}
function get(url, success, failure = defaultFailure){
    internalGet(url,getTokenHeader(),success)
}
// function login(username,password,remember,success){
//     internalPost('/api/auth/login',
//         {
//             username: username,
//             password: password
//         },{
//             'Content-Type': "application/x-www-form-urlencoded"
//         },
//         (data1)=>{
//             ElMessage.success(`登录成功，欢迎${data1.username}`)
//             storeAccessToken(data1.token,data1.expire,remember)
//             success(data1)
//         })
// }


// function storeAccessToken(token,expire,remember){
//     const authObj = {token: token ,expire: expire}
//     if(remember){
//         localStorage.setItem(authItemName,JSON.stringify(authObj))
//     }else{
//         sessionStorage.setItem(authItemName,JSON.stringify(authObj))
//     }
// }

/**
 * 从localStorage或者sessionStorage中获取token（如存在）
 */
function getAccessToken(){
    const token=localStorage.getItem(authItemName) || sessionStorage.getItem(authItemName)
    if(!token) return null
    const authObj=JSON.parse(token)
    if(authObj.expire<=new Date()){
        deleteToken()
        ElMessage.warning("登录状态已过期，请重新登录")
        return null
    }
    return authObj.token

}

function getTokenHeader(){
    const token=getAccessToken()
    return token ? {
        "Authorization":`Bearer ${token}`
    }:{}
}

// function deleteToken(){
//     localStorage.removeItem(authItemName)
//     sessionStorage.removeItem(authItemName)
// }

// function isUnauthorized(){
//     return getAccessToken()==null
// }
// function logout(success,failure=defaultFailure){
//     get("/api/auth/logout",()=>{
//         deleteToken()
//         ElMessage.success("退出登录成功")
//         success()
//     },failure)

// }
export {get,post,internalPost }