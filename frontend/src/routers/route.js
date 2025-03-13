import {createRouter , createWebHistory} from "vue-router";
// import {isUnauthorized} from "../net/index.js"

const router =createRouter({

    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [
        {
            path:"/",
            name:"home",
            component: ()=>import('../views/HomeView.vue'),
            children:[
                {
                    path:'',
                    name:"home-post-list",
                    component:()=>import('@/views/home/Home.vue')

                },{
                    path:'/post/:id',
                    name:"home-post-detail",
                    props:true,
                    component:()=>import('@/views/post/PostDetail.vue')
                },{
                    path:'/post/new',
                    name:"home-post-new",
                    component:()=>import('@/views/post/PostPublish.vue')
                },{
                    path:'/my',
                    name:'my-page',
                    component:()=>import('@/views/my/My.vue')
                },
                {
                    path:'/my/like',
                    name:"my-liked-post",
                    component:()=>import('@/views/my/MyLike.vue')
                },{
                    path:'/my/star',
                    name:"my-starred-post",
                    component:()=>import('@/views/my/MyStar.vue')
                },{
                    path:'/my/post',
                    name:'my-own-post',
                    component:()=>import('@/views/my/MyPost.vue')
                },{
                    path:'/chat',
                    name:'chat-list',
                    component:()=>import('@/views/chat/ChatList.vue')
                },{
                    path:'/user/:username',
                    name:"other-user-page",
                    component:()=>import('@/views/otherUser/OtherUserPage.vue')
                }
                
            ]
        },{
            path:'/login',
            name:'login-page',
            component:()=>import('@/views/identity/LoginPage.vue')
        },{
            path:'/register',
            name:'register-page',
            component:()=>import('@/views/identity/RegisterPage.vue')
        },{
            path:'/chat/:chatWith/:chatTarget',//chatwith id; chatTagert name
            name:'chatbox',
            component:()=>import('@/views/chat/chat.vue')
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