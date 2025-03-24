import axios from "axios";
import {ElMessage} from "element-plus";
import router from "../routers/route.js";
const refreshItemName="refreshToken"
const authItemName="accessToken"
// const API_BASE_URL="http://127.0.0.1:8000"
// const API_BASE_URL="http://10.223.74.229:8000"
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
        }).catch(async(err) =>
                {
                    if (err.response && err.response.status === 401) {
                    console.warn("🔄 Access token expired, trying to refresh...");
                    ElMessage.error("身份验证失败，请重新登录！");
                    router.push("/login"); // 重新跳转到登录页 
                    // const newToken = await refreshToken();
                    // if (newToken) {
                    //     return internalPost(url, data, getTokenHeader(), success, failure, error);
                    // } else {
                    //     ElMessage.error("身份验证失败，请重新登录！");
                    //     router.push("/login"); // 重新跳转到登录页
                    // }
                    } else {
                        error(err);
                    }
                }
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
        }).catch(async(err) =>
            {
                if (err.response && err.response.status === 401) {
                console.warn("🔄 Access token expired, trying to refresh...");
                ElMessage.error("身份验证失败，请重新登录！");
                router.push("/login"); // 重新跳转到登录页
                // const newToken = await refreshToken();
                // if (newToken) {
                //     return internalGet(url,getTokenHeader(), success, failure, error);
                // } else {
                //     ElMessage.error("身份验证失败，请重新登录！");
                //     router.push("/login"); // 重新跳转到登录页
                // }
                } else {
                    error(err);
                }
            } 
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
    // const authObj=JSON.parse(token)
    // if(authObj.expire<=new Date()){
    //     deleteToken()
    //     ElMessage.warning("登录状态已过期，请重新登录")
    //     return null
    // }
    // return authObj.token
    return token

}

function getTokenHeader(){
    const token=getAccessToken()
    console.log('getTokenHeader:' ,token)
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
// async function refreshToken() {
//     try {
//         const refresh = localStorage.getItem("refreshToken");
//         if (!refresh) {
//             console.error("❌ No refresh token available.");
//             return null;
//         }

//         const response = await axios.post(`${API_BASE_URL}/api/post/token/refresh/`, { refresh });
//         if (response.data.access) {
//             localStorage.setItem("accessToken", response.data.access);
//             console.log("✅ Token refreshed");
//             return response.data.access;
//         }
//     } catch (error) {
//         console.error("❌ Refresh token failed:", error);
//         return null;
//     }
// }
// }
export {get,post,internalPost }