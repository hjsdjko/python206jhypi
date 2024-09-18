import VueRouter from 'vue-router'

//引入组件
import Index from '../pages'
import Home from '../pages/home/home'
import Login from '../pages/login/login'
import Register from '../pages/register/register'
import Center from '../pages/center/center'
import Messages from '../pages/messages/list'
import Storeup from '../pages/storeup/list'
import News from '../pages/news/news-list'
import NewsDetail from '../pages/news/news-detail'
import payList from '../pages/pay'

import yonghuList from '../pages/yonghu/list'
import yonghuDetail from '../pages/yonghu/detail'
import yonghuAdd from '../pages/yonghu/add'
import qihuogongsiList from '../pages/qihuogongsi/list'
import qihuogongsiDetail from '../pages/qihuogongsi/detail'
import qihuogongsiAdd from '../pages/qihuogongsi/add'
import kaihuxinxiList from '../pages/kaihuxinxi/list'
import kaihuxinxiDetail from '../pages/kaihuxinxi/detail'
import kaihuxinxiAdd from '../pages/kaihuxinxi/add'
import chongzhixinxiList from '../pages/chongzhixinxi/list'
import chongzhixinxiDetail from '../pages/chongzhixinxi/detail'
import chongzhixinxiAdd from '../pages/chongzhixinxi/add'
import qihuoleixingList from '../pages/qihuoleixing/list'
import qihuoleixingDetail from '../pages/qihuoleixing/detail'
import qihuoleixingAdd from '../pages/qihuoleixing/add'
import qihuoxinxiList from '../pages/qihuoxinxi/list'
import qihuoxinxiDetail from '../pages/qihuoxinxi/detail'
import qihuoxinxiAdd from '../pages/qihuoxinxi/add'
import qihuotouziList from '../pages/qihuotouzi/list'
import qihuotouziDetail from '../pages/qihuotouzi/detail'
import qihuotouziAdd from '../pages/qihuotouzi/add'
import quxiaotouziList from '../pages/quxiaotouzi/list'
import quxiaotouziDetail from '../pages/quxiaotouzi/detail'
import quxiaotouziAdd from '../pages/quxiaotouzi/add'
import touzifengxianList from '../pages/touzifengxian/list'
import touzifengxianDetail from '../pages/touzifengxian/detail'
import touzifengxianAdd from '../pages/touzifengxian/add'
import qihuomaichuList from '../pages/qihuomaichu/list'
import qihuomaichuDetail from '../pages/qihuomaichu/detail'
import qihuomaichuAdd from '../pages/qihuomaichu/add'
import newstypeList from '../pages/newstype/list'
import newstypeDetail from '../pages/newstype/detail'
import newstypeAdd from '../pages/newstype/add'
import aboutusList from '../pages/aboutus/list'
import aboutusDetail from '../pages/aboutus/detail'
import aboutusAdd from '../pages/aboutus/add'
import systemintroList from '../pages/systemintro/list'
import systemintroDetail from '../pages/systemintro/detail'
import systemintroAdd from '../pages/systemintro/add'
import discussqihuoxinxiList from '../pages/discussqihuoxinxi/list'
import discussqihuoxinxiDetail from '../pages/discussqihuoxinxi/detail'
import discussqihuoxinxiAdd from '../pages/discussqihuoxinxi/add'
import discusstouzifengxianList from '../pages/discusstouzifengxian/list'
import discusstouzifengxianDetail from '../pages/discusstouzifengxian/detail'
import discusstouzifengxianAdd from '../pages/discusstouzifengxian/add'

const originalPush = VueRouter.prototype.push
VueRouter.prototype.push = function push(location) {
	return originalPush.call(this, location).catch(err => err)
}

//配置路由
export default new VueRouter({
	routes:[
		{
      path: '/',
      redirect: '/index/home'
    },
		{
			path: '/index',
			component: Index,
			children:[
				{
					path: 'home',
					component: Home
				},
				{
					path: 'center',
					component: Center,
				},
				{
					path: 'pay',
					component: payList,
				},
				{
					path: 'messages',
					component: Messages
				},
				{
					path: 'storeup',
					component: Storeup
				},
				{
					path: 'news',
					component: News
				},
				{
					path: 'newsDetail',
					component: NewsDetail
				},
				{
					path: 'yonghu',
					component: yonghuList
				},
				{
					path: 'yonghuDetail',
					component: yonghuDetail
				},
				{
					path: 'yonghuAdd',
					component: yonghuAdd
				},
				{
					path: 'qihuogongsi',
					component: qihuogongsiList
				},
				{
					path: 'qihuogongsiDetail',
					component: qihuogongsiDetail
				},
				{
					path: 'qihuogongsiAdd',
					component: qihuogongsiAdd
				},
				{
					path: 'kaihuxinxi',
					component: kaihuxinxiList
				},
				{
					path: 'kaihuxinxiDetail',
					component: kaihuxinxiDetail
				},
				{
					path: 'kaihuxinxiAdd',
					component: kaihuxinxiAdd
				},
				{
					path: 'chongzhixinxi',
					component: chongzhixinxiList
				},
				{
					path: 'chongzhixinxiDetail',
					component: chongzhixinxiDetail
				},
				{
					path: 'chongzhixinxiAdd',
					component: chongzhixinxiAdd
				},
				{
					path: 'qihuoleixing',
					component: qihuoleixingList
				},
				{
					path: 'qihuoleixingDetail',
					component: qihuoleixingDetail
				},
				{
					path: 'qihuoleixingAdd',
					component: qihuoleixingAdd
				},
				{
					path: 'qihuoxinxi',
					component: qihuoxinxiList
				},
				{
					path: 'qihuoxinxiDetail',
					component: qihuoxinxiDetail
				},
				{
					path: 'qihuoxinxiAdd',
					component: qihuoxinxiAdd
				},
				{
					path: 'qihuotouzi',
					component: qihuotouziList
				},
				{
					path: 'qihuotouziDetail',
					component: qihuotouziDetail
				},
				{
					path: 'qihuotouziAdd',
					component: qihuotouziAdd
				},
				{
					path: 'quxiaotouzi',
					component: quxiaotouziList
				},
				{
					path: 'quxiaotouziDetail',
					component: quxiaotouziDetail
				},
				{
					path: 'quxiaotouziAdd',
					component: quxiaotouziAdd
				},
				{
					path: 'touzifengxian',
					component: touzifengxianList
				},
				{
					path: 'touzifengxianDetail',
					component: touzifengxianDetail
				},
				{
					path: 'touzifengxianAdd',
					component: touzifengxianAdd
				},
				{
					path: 'qihuomaichu',
					component: qihuomaichuList
				},
				{
					path: 'qihuomaichuDetail',
					component: qihuomaichuDetail
				},
				{
					path: 'qihuomaichuAdd',
					component: qihuomaichuAdd
				},
				{
					path: 'newstype',
					component: newstypeList
				},
				{
					path: 'newstypeDetail',
					component: newstypeDetail
				},
				{
					path: 'newstypeAdd',
					component: newstypeAdd
				},
				{
					path: 'aboutus',
					component: aboutusList
				},
				{
					path: 'aboutusDetail',
					component: aboutusDetail
				},
				{
					path: 'aboutusAdd',
					component: aboutusAdd
				},
				{
					path: 'systemintro',
					component: systemintroList
				},
				{
					path: 'systemintroDetail',
					component: systemintroDetail
				},
				{
					path: 'systemintroAdd',
					component: systemintroAdd
				},
				{
					path: 'discussqihuoxinxi',
					component: discussqihuoxinxiList
				},
				{
					path: 'discussqihuoxinxiDetail',
					component: discussqihuoxinxiDetail
				},
				{
					path: 'discussqihuoxinxiAdd',
					component: discussqihuoxinxiAdd
				},
				{
					path: 'discusstouzifengxian',
					component: discusstouzifengxianList
				},
				{
					path: 'discusstouzifengxianDetail',
					component: discusstouzifengxianDetail
				},
				{
					path: 'discusstouzifengxianAdd',
					component: discusstouzifengxianAdd
				},
			]
		},
		{
			path: '/login',
			component: Login
		},
		{
			path: '/register',
			component: Register
		},
	]
})
