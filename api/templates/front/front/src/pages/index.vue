<template>
	<div class="main-containers">
		<div class="body-containers" :style='{"minHeight":"100vh","padding":"138px 0 0","margin":"0","position":"relative","background":"#F6F6F6"}'>
		<div class="top-container" :style='{"border":"1px solid #EBEBEB","boxShadow":"0 1px 6px rgba(64, 158, 255, .3)","padding":"0 220px","display":"flex","justifyContent":"flex-end","top":"0","left":"0","background":"url(http://codegen.caihongy.cn/20231031/0639c7b64edc43b499588d0e9c56f57e.png) repeat-x center top,#ffffff","borderWidth":"0px 0 0","width":"100%","position":"fixed","height":"138px","zIndex":"1002"}'>
			<!-- info -->
			<div :style='{"position":"absolute","alignItems":"center","top":"68px","float":"left","left":"340px","display":"flex"}'>
			  <el-image :style='{"width":"86px","objectFit":"cover","float":"left","height":"50px"}' src="http://codegen.caihongy.cn/20231024/1c63146363984330b0195c5279f34e83.png" fit="cover" />
			  <span :style='{"padding":"0 0 0 12px","lineHeight":"44px","fontSize":"32px","color":"#000","float":"left","fontWeight":"bold"}'>BS23-287基于Python的期货程序化交易系统的设计与实现</span>
			</div>
			<!-- weather -->
			<div class="weather" :style='{"padding":"0 20px","alignItems":"center","top":"-48px","left":"120px","display":"flex","position":"absolute","justifyContent":"center"}'>
				<div :style='{"padding":"0 4px","fontSize":"15px","lineHeight":"44px","color":"#767676"}'>{{weather.city}}</div>
				<div :style='{"padding":"0 4px","fontSize":"15px","lineHeight":"44px","color":"#767676"}'>{{weather.tem}}°</div>
				<div :style='{"padding":"0 4px","fontSize":"15px","lineHeight":"44px","color":"#767676"}'>{{weather.wea}}</div>
				<div :style='{"padding":"0 4px","fontSize":"15px","lineHeight":"44px","color":"#767676"}'>{{weather.win}}</div>
				<div :style='{"padding":"0 4px","fontSize":"15px","lineHeight":"44px","color":"#767676"}'>{{weather.win_speed}}</div>
			</div>
			
			<div v-if="false" :style='{"color":"#666","margin":"0 10px","fontSize":"14px"}'>0753-1234567</div>
			
			
			<div v-if="Token" :style='{"padding":"0 12px","fontSize":"16px","lineHeight":"50px","color":"#9E9E9E","height":"50px"}'>{{username}}</div>
			<div v-if="Token && notAdmin" :style='{"cursor":"pointer","padding":"0 12px","fontSize":"16px","lineHeight":"50px","color":"#9E9E9E","height":"50px"}' @click="goMenu('/index/center')">个人中心</div>
			<el-button v-if="!Token" @click="toLogin()" :style='{"border":"0","padding":"0","margin":"0px 10px 0","color":"#000","borderRadius":"2px","background":"transparent","display":"inline-block","fontSize":"16px","lineHeight":"50px","fontWeight":"bold","height":"50px"}'>登录/注册</el-button>
			<el-button v-if="Token" @click="logout" :style='{"border":"none","padding":"0 0","margin":"0px 10px 0","color":"#000","borderRadius":"0","background":"transparent","display":"inline-block","fontSize":"16px","lineHeight":"50px","float":"right","fontWeight":"bold","height":"50px"}'>退出</el-button>
		</div>


			<div class="menu-preview" :style='{"padding":"0 20px","borderColor":"#efefef","top":"570px","left":"16%","background":"#313131","borderWidth":"0 0 1px 0","width":"68%","position":"absolute","borderStyle":"solid","height":"auto","zIndex":"998"}'>
			<el-scrollbar wrap-class="scrollbar-wrapper-horizontal">
				<el-menu class="el-menu-horizontal-demo" :style='{"border":0,"padding":"0","listStyle":"none","margin":"0","background":"transparent","display":"flex","position":"relative"}' :default-active="activeMenu" :unique-opened="true" mode="horizontal" :router="true" @select="handleSelect">
					<div class="userinfo" :style='{"width":"84px","padding":"6px 10px 0","display":"none","height":"auto"}'>
					  <el-image :style='{"width":"100%","objectFit":"cover","borderRadius":"20px","display":"block","height":"32px"}' src="http://codegen.caihongy.cn/20201114/7856ba26477849ea828f481fa2773a95.jpg" fit="cover"></el-image>
					  <div :style='{"fontSize":"12px","lineHeight":"1.5","color":"#333","textAlign":"center"}'>nickname</div>
					</div>
					<el-menu-item class="home" index="/index/home" @click.native="goMenu('/index/home')">
						<span :style='{"padding":"0 10px","margin":"0","color":"inherit","width":"14px","lineHeight":"56px","fontSize":"inherit","height":"56px"}' class="icon iconfont icon-shouye-zhihui"></span>
						<span :style='{"padding":"0 10px","lineHeight":"56px","fontSize":"inherit","color":"inherit","height":"56px"}'>系统首页</span>
					</el-menu-item>
					<el-menu-item class="item" v-for="(menu, index) in menuList" :index="menu.url" :key="index" @click.native="goMenu(menu.url)">
						<i :style='{"padding":"0 10px","margin":"0","color":"inherit","width":"14px","lineHeight":"56px","fontSize":"inherit","height":"56px"}' :class="iconArr[index]"></i>
						<span :style='{"padding":"0 10px","lineHeight":"56px","fontSize":"inherit","color":"inherit","height":"56px"}'>{{menu.name}}</span>
					</el-menu-item>
					<el-menu-item class="user" index="/index/center" v-if="Token && notAdmin" @click.native="goMenu('/index/center')">
						<span :style='{"padding":"0 10px","margin":"0","color":"inherit","width":"14px","lineHeight":"56px","fontSize":"inherit","height":"56px"}' class="icon iconfont icon-shouye-zhihui"></span>
						<span :style='{"padding":"0 10px","lineHeight":"56px","fontSize":"inherit","color":"inherit","height":"56px"}'>个人中心</span>
					</el-menu-item>
				</el-menu>
			</el-scrollbar>
			</div>


			<div class="banner-preview" :style='{"width":"100%","height":"auto"}'>
				<el-carousel :style='{"width":"100%","margin":"0 auto"}' trigger="click" indicator-position="inside" arrow="always" type="default" direction="vertical" height="500px" :autoplay="true" :interval="3000" :loop="false">
					<el-carousel-item :style='{"borderRadius":"0","width":"100%","height":"100%"}' v-for="item in carouselList" :key="item.id">
						<el-image @click="carouselClick(item.url)" :style='{"objectFit":"cover","width":"100%","height":"100%"}' :src="baseUrl + item.value" fit="cover"></el-image>
					</el-carousel-item>
				</el-carousel>
			</div>


			<router-view></router-view>
			
			<div class="bottom-preview" :style='{"width":"100%","height":"auto"}'>
				<div :style='{"width":"100%","padding":"20px","overflow":"hidden","background":"#000","height":"auto"}'><div v-html="bottomContent"></div></div>
			</div>
		</div>
		
	</div>
</template>

<script>
import Vue from 'vue'
import Swiper from "swiper";
import axios from 'axios'

export default {
    data() {
		return {
            activeIndex: '0',
			roleMenus: [{"backMenu":[{"child":[{"appFrontIcon":"cuIcon-skin","buttons":["新增","查看","修改","删除","首页总数","首页统计","开户"],"menu":"用户","menuJump":"列表","tableName":"yonghu"}],"menu":"用户管理"},{"child":[{"appFrontIcon":"cuIcon-flashlightopen","buttons":["新增","查看","修改","删除"],"menu":"期货公司","menuJump":"列表","tableName":"qihuogongsi"}],"menu":"期货公司管理"},{"child":[{"appFrontIcon":"cuIcon-vipcard","buttons":["查看","修改","删除"],"menu":"开户信息","menuJump":"列表","tableName":"kaihuxinxi"}],"menu":"开户信息管理"},{"child":[{"appFrontIcon":"cuIcon-vipcard","buttons":["查看","修改","删除"],"menu":"充值信息","menuJump":"列表","tableName":"chongzhixinxi"}],"menu":"充值信息管理"},{"child":[{"appFrontIcon":"cuIcon-camera","buttons":["新增","查看","修改","删除"],"menu":"期货类型","menuJump":"列表","tableName":"qihuoleixing"}],"menu":"期货类型管理"},{"child":[{"appFrontIcon":"cuIcon-qrcode","buttons":["查看","修改","删除","查看评论","首页总数","首页统计"],"menu":"期货信息","menuJump":"列表","tableName":"qihuoxinxi"}],"menu":"期货信息管理"},{"child":[{"appFrontIcon":"cuIcon-newshot","buttons":["查看","修改","删除"],"menu":"期货投资","menuJump":"列表","tableName":"qihuotouzi"}],"menu":"期货投资管理"},{"child":[{"appFrontIcon":"cuIcon-cardboard","buttons":["查看","修改","删除","首页统计","首页总数"],"menu":"取消投资","menuJump":"列表","tableName":"quxiaotouzi"}],"menu":"取消投资管理"},{"child":[{"appFrontIcon":"cuIcon-explore","buttons":["新增","查看","修改","删除","查看评论"],"menu":"投资风险","menuJump":"列表","tableName":"touzifengxian"}],"menu":"投资风险管理"},{"child":[{"appFrontIcon":"cuIcon-qrcode","buttons":["查看","修改","删除"],"menu":"期货卖出","menuJump":"列表","tableName":"qihuomaichu"}],"menu":"期货卖出管理"},{"child":[{"appFrontIcon":"cuIcon-message","buttons":["查看","修改","回复","删除"],"menu":"意见反馈","tableName":"messages"}],"menu":"意见反馈"},{"child":[{"appFrontIcon":"cuIcon-news","buttons":["新增","查看","修改","删除"],"menu":"资讯信息分类","tableName":"newstype"},{"appFrontIcon":"cuIcon-pic","buttons":["查看","修改"],"menu":"关于我们","tableName":"aboutus"},{"appFrontIcon":"cuIcon-shop","buttons":["查看","修改"],"menu":"轮播图管理","tableName":"config"},{"appFrontIcon":"cuIcon-vipcard","buttons":["查看","修改"],"menu":"系统简介","tableName":"systemintro"},{"appFrontIcon":"cuIcon-cardboard","buttons":["新增","查看","修改","删除"],"menu":"新闻资讯","tableName":"news"}],"menu":"系统管理"}],"frontMenu":[{"child":[{"appFrontIcon":"cuIcon-newshot","buttons":["查看","投资","买入"],"menu":"期货信息列表","menuJump":"列表","tableName":"qihuoxinxi"}],"menu":"期货信息模块"},{"child":[{"appFrontIcon":"cuIcon-newshot","buttons":["查看"],"menu":"投资风险列表","menuJump":"列表","tableName":"touzifengxian"}],"menu":"投资风险模块"}],"hasBackLogin":"是","hasBackRegister":"否","hasFrontLogin":"否","hasFrontRegister":"否","roleName":"管理员","tableName":"users"},{"backMenu":[{"child":[{"appFrontIcon":"cuIcon-vipcard","buttons":["新增","查看","支付"],"menu":"充值信息","menuJump":"列表","tableName":"chongzhixinxi"}],"menu":"充值信息管理"},{"child":[{"appFrontIcon":"cuIcon-newshot","buttons":["查看","取消","交易","卖出"],"menu":"期货投资","menuJump":"列表","tableName":"qihuotouzi"}],"menu":"期货投资管理"},{"child":[{"appFrontIcon":"cuIcon-cardboard","buttons":["查看"],"menu":"取消投资","menuJump":"列表","tableName":"quxiaotouzi"}],"menu":"取消投资管理"},{"child":[{"appFrontIcon":"cuIcon-qrcode","buttons":["查看"],"menu":"期货卖出","menuJump":"列表","tableName":"qihuomaichu"}],"menu":"期货卖出管理"}],"frontMenu":[{"child":[{"appFrontIcon":"cuIcon-newshot","buttons":["查看","投资","买入"],"menu":"期货信息列表","menuJump":"列表","tableName":"qihuoxinxi"}],"menu":"期货信息模块"},{"child":[{"appFrontIcon":"cuIcon-newshot","buttons":["查看"],"menu":"投资风险列表","menuJump":"列表","tableName":"touzifengxian"}],"menu":"投资风险模块"}],"hasBackLogin":"否","hasBackRegister":"否","hasFrontLogin":"是","hasFrontRegister":"是","roleName":"用户","tableName":"yonghu"},{"backMenu":[{"child":[{"appFrontIcon":"cuIcon-qrcode","buttons":["新增","查看","修改","删除","查看评论","首页总数","首页统计"],"menu":"期货信息","menuJump":"列表","tableName":"qihuoxinxi"}],"menu":"期货信息管理"},{"child":[{"appFrontIcon":"cuIcon-newshot","buttons":["查看"],"menu":"期货投资","menuJump":"列表","tableName":"qihuotouzi"}],"menu":"期货投资管理"},{"child":[{"appFrontIcon":"cuIcon-cardboard","buttons":["查看","首页总数","首页统计"],"menu":"取消投资","menuJump":"列表","tableName":"quxiaotouzi"}],"menu":"取消投资管理"},{"child":[{"appFrontIcon":"cuIcon-qrcode","buttons":["查看"],"menu":"期货卖出","menuJump":"列表","tableName":"qihuomaichu"}],"menu":"期货卖出管理"}],"frontMenu":[{"child":[{"appFrontIcon":"cuIcon-newshot","buttons":["查看","投资","买入"],"menu":"期货信息列表","menuJump":"列表","tableName":"qihuoxinxi"}],"menu":"期货信息模块"},{"child":[{"appFrontIcon":"cuIcon-newshot","buttons":["查看"],"menu":"投资风险列表","menuJump":"列表","tableName":"touzifengxian"}],"menu":"投资风险模块"}],"hasBackLogin":"是","hasBackRegister":"是","hasFrontLogin":"否","hasFrontRegister":"否","roleName":"期货公司","tableName":"qihuogongsi"}],
			baseUrl: '',
			carouselList: [],
			menuList: [],
			form: {
				ask: '',
				userid: localStorage.getItem('userid')
			},
			Token: localStorage.getItem('Token'),
            username: localStorage.getItem('username'),
            notAdmin: localStorage.getItem('sessionTable')!='"users"',
			timer: '',
			// 天气
			weather: {},
			iconArr: [
				'el-icon-star-off',
				'el-icon-goods',
				'el-icon-warning',
				'el-icon-question',
				'el-icon-info',
				'el-icon-help',
				'el-icon-picture-outline-round',
				'el-icon-camera-solid',
				'el-icon-video-camera-solid',
				'el-icon-video-camera',
				'el-icon-bell',
				'el-icon-s-cooperation',
				'el-icon-s-order',
				'el-icon-s-platform',
				'el-icon-s-operation',
				'el-icon-s-promotion',
				'el-icon-s-release',
				'el-icon-s-ticket',
				'el-icon-s-management',
				'el-icon-s-open',
				'el-icon-s-shop',
				'el-icon-s-marketing',
				'el-icon-s-flag',
				'el-icon-s-comment',
				'el-icon-s-finance',
				'el-icon-s-claim',
				'el-icon-s-opportunity',
				'el-icon-s-data',
				'el-icon-s-check'
			],
			headportrait: localStorage.getItem('headportrait')?localStorage.getItem('headportrait'):'',
			bottomContent: 'Copyright © 2023 Sohu All Rights Reserved. 基于Python的期货程序化交易系统的设计与实现 版权所有',
		}
    },
    created() {
		// 获取天气
		this.getWeather()
		this.baseUrl = this.$config.baseUrl;
		this.menuList = this.$config.indexNav;
		this.getCarousel();
        if(localStorage.getItem('Token') && localStorage.getItem('Token')!=null) {
			this.getSession()
        }
    },
    mounted() {
        this.activeIndex = localStorage.getItem('keyPath') || '0';



    },
    computed: {
		activeMenu() {
			const route = this.$route
			const {
				meta,
				path
			} = route
			// if st path, the sidebar will highlight the path you sete
			if (meta.activeMenu) {
				return meta.activeMenu
			}
			return path
		},
    },
    watch: {
        $route(newValue) {
            let that = this
            let url = window.location.href
            let arr = url.split('#')
            for (let x in this.menuList) {
                if (newValue.path == this.menuList[x].url) {
                    this.activeIndex = x
                }
            }
            this.Token = localStorage.getItem('Token')
            // window.scrollTo( 0, 100 )
        },
    },
    methods: {
		// 获取当前城市天气
		getWeather(){
			axios({
				method: 'get',
				url: 'https://v0.yiketianqi.com/free/day?appid=69475998&appsecret=rldbX1Zl'
			}).then(res => {
				this.weather = res.data
			})
		},

		getSession() {
			this.$http.get(`${localStorage.getItem('UserTableName')}/session`, {emulateJSON: true}).then(res => {
				if (res.data.code == 0) {
					localStorage.setItem('sessionForm',JSON.stringify(res.data.data))
					localStorage.setItem('userid', res.data.data.id);
					if(res.data.data.vip) {
						localStorage.setItem('vip', res.data.data.vip);
					}
					if(res.data.data.touxiang) {
						localStorage.setItem('headportrait', res.data.data.touxiang);
					} else if(res.data.data.headportrait) {
						localStorage.setItem('headportrait', res.data.data.headportrait);
					}
				}
			});
		},
        handleSelect(keyPath) {
            if (keyPath) {
                localStorage.setItem('keyPath', keyPath)
            }
        },
		toLogin() {
		  this.$router.push('/login');
		},
        logout() {
            localStorage.clear();
            Vue.http.headers.common['Token'] = "";
            this.$router.push('/index/home');
            this.activeIndex = '0'
            localStorage.setItem('keyPath', this.activeIndex)
            this.Token = ''
            this.$forceUpdate()
            this.$message({
                message: '登出成功',
                type: 'success',
                duration: 1000,
            });
        },
		getCarousel() {
			this.$http.get('config/list', {params: { page: 1, limit: 3 }}).then(res => {
				if (res.data.code == 0) {
					this.carouselList = res.data.data.list;
				}
			});
		},
		// 轮播图跳转
		carouselClick(url) {
			if (url) {
				if (url.indexOf('https') != -1) {
					window.open(url)
				} else {
					this.$router.push(url)
				}
			}
		},
		goBackend() {
			window.open(`http://localhost:8080/admin/dist/index.html`, "_blank");
		},
		goMenu(path) {
            this.$router.push(path);
		},
    }
}
</script>

<style rel="stylesheet/scss" lang="scss" scoped>
	.menu-preview {
	  .el-scrollbar {
	    height: 100%;
	  
	    & /deep/ .scrollbar-wrapper-vertical {
	      overflow-x: hidden;
	    }
	  
	    & /deep/ .scrollbar-wrapper-horizontal {
	      overflow-y: hidden;
	  
	      .el-scrollbar__view {
	        white-space: nowrap;
	      }
	    }
	  }
	}
	
	
	.menu-preview .el-menu-horizontal-demo .el-menu-item.home {
				cursor: pointer;
				border: 0;
				padding: 0 20px;
				color: #fff;
				white-space: nowrap;
				display: flex;
				font-size: 16px;
				line-height: 130px;
				background: transparent;
				align-items: center;
				position: relative;
				list-style: none;
				height: 130px;
			}
	
	.menu-preview .el-menu-horizontal-demo .el-menu-item.home:hover {
				color: #AD8936;
				background: transparent;
			}
	
	.menu-preview .el-menu-horizontal-demo .el-menu-item.home.is-active {
				color: #AD8936;
				background: transparent;
			}
	
	.menu-preview .el-menu-horizontal-demo .el-menu-item.user {
				cursor: pointer;
				border: 0;
				padding: 0 20px;
				color: #fff;
				white-space: nowrap;
				display: flex;
				font-size: 16px;
				line-height: 130px;
				background: transparent;
				align-items: center;
				position: relative;
				list-style: none;
				height: 130px;
			}
	
	.menu-preview .el-menu-horizontal-demo .el-menu-item.user:hover {
				color: #AD8936;
				background: transparent;
			}
	
	.menu-preview .el-menu-horizontal-demo .el-menu-item.user.is-active {
				color: #AD8936;
				background: transparent;
			}
	
	.menu-preview .el-menu-horizontal-demo .el-menu-item.service {
				cursor: pointer;
				border: 0;
				padding: 0 20px;
				color: #fff;
				white-space: nowrap;
				display: flex;
				font-size: 16px;
				line-height: 130px;
				background: transparent;
				align-items: center;
				position: relative;
				list-style: none;
				height: 130px;
			}
	
	.menu-preview .el-menu-horizontal-demo .el-menu-item.service:hover {
				color: #AD8936;
				background: transparent;
			}
	
	.menu-preview .el-menu-horizontal-demo .el-menu-item.service.is-active {
				color: #AD8936;
				background: transparent;
			}
	
	.menu-preview .el-menu-horizontal-demo .el-menu-item.shop {
				cursor: pointer;
				border: 0;
				padding: 0 20px;
				color: #fff;
				white-space: nowrap;
				display: flex;
				font-size: 16px;
				line-height: 130px;
				background: transparent;
				align-items: center;
				position: relative;
				list-style: none;
				height: 130px;
			}
	
	.menu-preview .el-menu-horizontal-demo .el-menu-item.shop:hover {
				color: #AD8936;
				background: transparent;
			}
	
	.menu-preview .el-menu-horizontal-demo .el-menu-item.shop.is-active {
				color: #AD8936;
				background: transparent;
			}
	
	.menu-preview .el-menu-horizontal-demo .el-menu-item.back {
				cursor: pointer;
				border: 0;
				padding: 0 20px;
				color: #fff;
				white-space: nowrap;
				display: flex;
				font-size: 16px;
				line-height: 130px;
				background: transparent;
				align-items: center;
				position: relative;
				list-style: none;
				height: 130px;
			}
	
	.menu-preview .el-menu-horizontal-demo .el-menu-item.back:hover {
				color: #AD8936;
				background: transparent;
			}
	
	.menu-preview .el-menu-horizontal-demo .el-menu-item.back.is-active {
				color: #AD8936;
				background: transparent;
			}
	
	.menu-preview .el-menu-horizontal-demo .el-menu-item.item {
				cursor: pointer;
				border: 0;
				padding: 0 20px;
				color: #fff;
				white-space: nowrap;
				display: flex;
				font-size: 16px;
				line-height: 130px;
				background: transparent;
				align-items: center;
				position: relative;
				list-style: none;
				height: 130px;
			}
	
	.menu-preview .el-menu-horizontal-demo .el-menu-item.item:hover {
				color: #AD8936;
				background: transparent;
			}
	
	.menu-preview .el-menu-horizontal-demo .el-menu-item.item.is-active {
				color: #AD8936;
				background: transparent;
			}
	
	.banner-preview {
	  .el-carousel /deep/ .el-carousel__indicator button {
	    width: 0;
	    height: 0;
	    display: none;
	  }
	}
	
	.banner-preview .el-carousel /deep/ .el-carousel__container .el-carousel__arrow--left {
		width: 60px;
		font-size: 20px;
		height: 60px;
	}
	
	.banner-preview .el-carousel /deep/ .el-carousel__container .el-carousel__arrow--left:hover {
		background: #AD8936;
	}
	
	.banner-preview .el-carousel /deep/ .el-carousel__container .el-carousel__arrow--right {
		width: 60px;
		font-size: 20px;
		height: 60px;
	}
	
	.banner-preview .el-carousel /deep/ .el-carousel__container .el-carousel__arrow--right:hover {
		background: #AD8936;
	}

	.banner-preview .el-carousel /deep/ .el-carousel__indicators {
		padding: 0;
		margin: 0;
		z-index: 2;
		position: absolute;
		list-style: none;
	}
	
	.banner-preview .el-carousel /deep/ .el-carousel__indicators li {
		padding: 0;
		margin: 0 4px;
		background: #fff;
		display: block;
		width: 12px;
		opacity: 0.4;
		transition: 0.3s;
		height: 12px;
	}
	
	.banner-preview .el-carousel /deep/ .el-carousel__indicators li:hover {
		padding: 0;
		margin: 0 4px;
		background: #AD8936;
		display: inline-block;
		width: 12px;
		opacity: 0.7;
		height: 24px;
	}
	
	.banner-preview .el-carousel /deep/ .el-carousel__indicators li.is-active {
		padding: 0;
		margin: 0 4px;
		background: #AD8936;
		display: inline-block;
		width: 12px;
		opacity: 1;
		height: 24px;
	}

    .chat-content {
        padding-bottom: 20px;
        width: 100%;
        margin-bottom: 10px;
        max-height: 300px;
        height: 300px;
        overflow-y: scroll;
        border: 1px solid #eeeeee;
        background: #fff;

        .left-content {
            float: left;
            margin-bottom: 10px;
            padding: 10px;
            max-width: 80%;
        }

        .right-content {
            float: right;
            margin-bottom: 10px;
            padding: 10px;
            max-width: 80%;
        }
    }

    .clear-float {
        clear: both;
    }


	
	// -------- search --------
	.main-containers .search .select /deep/ .el-input__inner {
				border: 0;
				border-radius: 4px;
				padding: 0 30px 0 10px;
				box-shadow: 0 0 6px rgba(64, 158, 255, .3);
				outline: none;
				color: rgba(64, 158, 255, 1);
				width: 180px;
				font-size: 14px;
				height: 44px;
			}
	
	.main-containers .search .input /deep/ .el-input__inner {
				border: 0;
				border-radius: 4px;
				padding: 0 10px;
				box-shadow: 0 0 6px rgba(64, 158, 255, .3);
				outline: none;
				color: rgba(64, 158, 255, 1);
				width: 180px;
				font-size: 14px;
				height: 44px;
			}
	// -------- search --------
	
	.main-containers .btn-service {
				border: 0;
				padding: 0 8px;
				margin: 0 10px;
				color: #9E9E9E;
				background: transparent;
				width: auto;
				font-size: 16px;
				line-height: 50px;
				height: 50px;
			}
	
	.main-containers .btn-service:hover {
				opacity: 0.5;
			}
	
	.main-containers .btn-shop {
				border: 0;
				padding: 0 8px;
				margin: 0 10px;
				color: #9E9E9E;
				background: transparent;
				width: auto;
				font-size: 16px;
				line-height: 50px;
				height: 50px;
			}
	
	.main-containers .btn-shop:hover {
				opacity: 0.5;
			}
</style>
