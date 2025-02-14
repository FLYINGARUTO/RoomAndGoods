import {createRouter , createWebHistory} from "vue-router";
// import {isUnauthorized} from "../net/index.js"

const router =createRouter({

    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [
        {
            path:"/",
            name:"home",
            component: ()=>import('../views/Homepage.vue'),
        }
        
    ]
}
)
// router.beforeEach((to, from, next)=>{
//     //如果已登陆，但是访问登录页，则自动跳至indexView
//     if(to.name.startsWith('welcome') && !isUnauthorized()){
//         next('/index')
//     }
//     //未登录且试图访问indexView，则跳转回登录页
//     else if(to.path==='/index'&& isUnauthorized()){
//         next('/')
//     }else
//         next()
// })
export default router