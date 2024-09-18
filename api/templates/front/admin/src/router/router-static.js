import Vue from 'vue';
//配置路由
import VueRouter from 'vue-router'
Vue.use(VueRouter);
//1.创建组件
import Index from '@/views/index'
import Home from '@/views/home'
import Login from '@/views/login'
import NotFound from '@/views/404'
import UpdatePassword from '@/views/update-password'
import pay from '@/views/pay'
import register from '@/views/register'
import center from '@/views/center'
    import qihuoleixing from '@/views/modules/qihuoleixing/list'
    import news from '@/views/modules/news/list'
    import qihuomaichu from '@/views/modules/qihuomaichu/list'
    import aboutus from '@/views/modules/aboutus/list'
    import qihuoxinxi from '@/views/modules/qihuoxinxi/list'
    import discusstouzifengxian from '@/views/modules/discusstouzifengxian/list'
    import qihuogongsi from '@/views/modules/qihuogongsi/list'
    import qihuotouzi from '@/views/modules/qihuotouzi/list'
    import discussqihuoxinxi from '@/views/modules/discussqihuoxinxi/list'
    import systemintro from '@/views/modules/systemintro/list'
    import yonghu from '@/views/modules/yonghu/list'
    import quxiaotouzi from '@/views/modules/quxiaotouzi/list'
    import kaihuxinxi from '@/views/modules/kaihuxinxi/list'
    import messages from '@/views/modules/messages/list'
    import touzifengxian from '@/views/modules/touzifengxian/list'
    import config from '@/views/modules/config/list'
    import chongzhixinxi from '@/views/modules/chongzhixinxi/list'
    import newstype from '@/views/modules/newstype/list'


//2.配置路由   注意：名字
export const routes = [{
    path: '/',
    name: '系统首页',
    component: Index,
    children: [{
      // 这里不设置值，是把main作为默认页面
      path: '/',
      name: '系统首页',
      component: Home,
      meta: {icon:'', title:'center', affix: true}
    }, {
      path: '/updatePassword',
      name: '修改密码',
      component: UpdatePassword,
      meta: {icon:'', title:'updatePassword'}
    }, {
      path: '/pay',
      name: '支付',
      component: pay,
      meta: {icon:'', title:'pay'}
    }, {
      path: '/center',
      name: '个人信息',
      component: center,
      meta: {icon:'', title:'center'}
    }
      ,{
	path: '/qihuoleixing',
        name: '期货类型',
        component: qihuoleixing
      }
      ,{
	path: '/news',
        name: '新闻资讯',
        component: news
      }
      ,{
	path: '/qihuomaichu',
        name: '期货卖出',
        component: qihuomaichu
      }
      ,{
	path: '/aboutus',
        name: '关于我们',
        component: aboutus
      }
      ,{
	path: '/qihuoxinxi',
        name: '期货信息',
        component: qihuoxinxi
      }
      ,{
	path: '/discusstouzifengxian',
        name: '投资风险评论',
        component: discusstouzifengxian
      }
      ,{
	path: '/qihuogongsi',
        name: '期货公司',
        component: qihuogongsi
      }
      ,{
	path: '/qihuotouzi',
        name: '期货投资',
        component: qihuotouzi
      }
      ,{
	path: '/discussqihuoxinxi',
        name: '期货信息评论',
        component: discussqihuoxinxi
      }
      ,{
	path: '/systemintro',
        name: '系统简介',
        component: systemintro
      }
      ,{
	path: '/yonghu',
        name: '用户',
        component: yonghu
      }
      ,{
	path: '/quxiaotouzi',
        name: '取消投资',
        component: quxiaotouzi
      }
      ,{
	path: '/kaihuxinxi',
        name: '开户信息',
        component: kaihuxinxi
      }
      ,{
	path: '/messages',
        name: '意见反馈',
        component: messages
      }
      ,{
	path: '/touzifengxian',
        name: '投资风险',
        component: touzifengxian
      }
      ,{
	path: '/config',
        name: '轮播图管理',
        component: config
      }
      ,{
	path: '/chongzhixinxi',
        name: '充值信息',
        component: chongzhixinxi
      }
      ,{
	path: '/newstype',
        name: '资讯信息分类',
        component: newstype
      }
    ]
  },
  {
    path: '/login',
    name: 'login',
    component: Login,
    meta: {icon:'', title:'login'}
  },
  {
    path: '/register',
    name: 'register',
    component: register,
    meta: {icon:'', title:'register'}
  },
  {
    path: '*',
    component: NotFound
  }
]
//3.实例化VueRouter  注意：名字
const router = new VueRouter({
  mode: 'hash',
  /*hash模式改为history*/
  routes // （缩写）相当于 routes: routes
})
const originalPush = VueRouter.prototype.push
//修改原型对象中的push方法
VueRouter.prototype.push = function push(location) {
   return originalPush.call(this, location).catch(err => err)
}
export default router;
