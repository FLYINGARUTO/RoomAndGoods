import {createRouter , createWebHistory} from "vue-router";
import {isUnauthorized} from "../net/index.js"

const router =createRouter({

    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [
        {
            path:"/",
            name:"welcome",
            component: ()=>import('../views/WelcomeView.vue'),
            children:[
                {
                    path:'',
                    name:"welcome-login",
                    component: ()=>import('../views/welcome/LoginPage.vue')
                },
                {
                    path:'register',
                    name:'welcome-register',
                    component:()=>import('../views/welcome/RegisterPageReplicate.vue')
                },
                {
                    path:'reset',
                    name:"welcome-reset",
                    component:()=>import('../views/welcome/ResetPage.vue')
                }
            ]
        },
        {
            path:"/welcome",
            redirect:"/"
        }
        ,{
            path:'/index',
            name:"index",
            component:()=>import('../views/IndexView.vue')
        }
    ]
}
)
router.beforeEach((to, from, next)=>{
    //如果已登陆，但是访问登录页，则自动跳至indexView
    if(to.name.startsWith('welcome') && !isUnauthorized()){
        next('/index')
    }
    //未登录且试图访问indexView，则跳转回登录页
    else if(to.path==='/index'&& isUnauthorized()){
        next('/')
    }else
        next()
})
export default router