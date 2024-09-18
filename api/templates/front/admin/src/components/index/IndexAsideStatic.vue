<template>
	<div class="menu-preview">
		<!-- 竖向-2 -->
		<el-scrollbar :wrap-class="isCollapse ? 'scrollbar-wrapper scrollbar-wrapper-close' : 'scrollbar-wrapper scrollbar-wrapper-open'">
		  <el-button :style="verticalStyle2[isCollapse?'close':'open'].btn.default" type="primary" @click="collapse">
		    <span class="icon iconfont"
		      :style="verticalStyle2[isCollapse?'close':'open'].btn.icon.default"
		      :class="verticalStyle2[isCollapse?'close':'open'].btn.icon.text"></span>{{verticalStyle2[isCollapse?'close':'open'].btn.text}}
		  </el-button>
		  <div class="userinfo"
		    :style="verticalStyle2[isCollapse?'close':'open'].userinfo.box.default">
		    <el-image :style="verticalStyle2[isCollapse?'close':'open'].userinfo.img.default" :src="avatar?this.$base.url + avatar:require('@/assets/img/avator.png')" fit="cover"></el-image>
		    <div :style="verticalStyle2[isCollapse?'close':'open'].userinfo.nickname.default">
		      {{this.$storage.get('adminName')}}</div>
		  </div>
		  <el-menu :default-active="activeMenu" :unique-opened="true" :style="verticalStyle2[isCollapse?'close':'open'].menu.box.default"
		    class="el-menu-vertical-2" :collapse-transition="false" :collapse="isCollapse">
		    <el-menu-item class="home" :popper-append-to-body="false" popper-class="home" @click.native="menuHandler('')" :style="verticalStyle2[isCollapse?'close':'open'].home.one.box.default" index="/">
		      <div class="el-tooltip">
		        <i :style="verticalStyle2[isCollapse?'close':'open'].home.one.icon.default"
		          class="icon iconfont icon-shouye-zhihui"></i>
		        <span :style="verticalStyle2[isCollapse?'close':'open'].home.one.title.default"
		          slot="title">{{verticalStyle2.open.home.one.title.text}}</span>
		      </div>
		    </el-menu-item>
		    <el-submenu class="user" popper-class="user" :popper-append-to-body="false"
		      :style="verticalStyle2[isCollapse?'close':'open'].user.one.box.default" index="1">
		      <template slot="title">
		        <i :style="verticalStyle2[isCollapse?'close':'open'].user.one.icon.default"
		          class="icon iconfont icon-kuaijiezhifu"></i>
		        <span :style="verticalStyle2[isCollapse?'close':'open'].user.one.title.default"
		          slot="title">{{verticalStyle2.open.user.one.title.text}}</span>
		      </template>
		      <el-menu-item index="/updatePassword" @click="menuHandler('updatePassword')">修改密码</el-menu-item>
		      <el-menu-item index="/center" @click="menuHandler('center')">个人信息</el-menu-item>
		    </el-submenu>
			<template v-for="(menu,index) in menuList.backMenu">
				<el-submenu v-if="menu.child.length > 1 || !verticalIsMultiple" class="other" popper-class="other" :popper-append-to-body="false" :style="verticalStyle2[isCollapse?'close':'open'].menu.one.box.default" :index="index+2+''">
					<template slot="title">
						<i :style="verticalStyle2[isCollapse?'close':'open'].menu.one.icon.default" class="el-icon-menu" :class="icons[index]"></i>
						<span :style="verticalStyle2[isCollapse?'close':'open'].menu.one.title.default" slot="title">{{menu.menu + (verticalFlag ? '管理' : '')}}</span>
					</template>
					<el-menu-item v-for="(child,sort) in menu.child" :key="sort" :index="'/'+child.tableName" @click="menuHandler(child.tableName)">{{ child.menu }}</el-menu-item>
				</el-submenu>
				<el-menu-item v-if="menu.child.length <= 1 && verticalIsMultiple" class="other" popper-class="other" :style="verticalStyle2[isCollapse?'close':'open'].menu.one.box.default" @click="menuHandler(menu.child[0].tableName)" :index="'/'+menu.child[0].tableName">
				  <div class="el-tooltip">
				    <i :style="verticalStyle2[isCollapse?'close':'open'].menu.one.icon.default" class="el-icon-menu" :class="icons[index]"></i>
				    <span :style="verticalStyle2[isCollapse?'close':'open'].menu.one.title.default" slot="title">{{menu.child[0].menu + (verticalFlag ? '管理' : '')}}</span>
				  </div>
				</el-menu-item>
			</template>
		  </el-menu>
		</el-scrollbar>


	</div>
</template>

<script>
import menu from '@/utils/menu'
export default {
	data() {
		return {
			menuList: [],
			dynamicMenuRoutes: [],
			role: '',
			user: null,
			avatar:'',
			icons: [
				'el-icon-s-cooperation',
				'el-icon-s-order',
				'el-icon-s-platform',
				'el-icon-s-fold',
				'el-icon-s-unfold',
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
				'el-icon-s-custom',
				'el-icon-s-opportunity',
				'el-icon-s-data',
				'el-icon-s-check',
				'el-icon-s-grid',
				'el-icon-menu',
				'el-icon-chat-dot-square',
				'el-icon-message',
				'el-icon-postcard',
				'el-icon-position',
				'el-icon-microphone',
				'el-icon-close-notification',
				'el-icon-bangzhu',
				'el-icon-time',
				'el-icon-odometer',
				'el-icon-crop',
				'el-icon-aim',
				'el-icon-switch-button',
				'el-icon-full-screen',
				'el-icon-copy-document',
				'el-icon-mic',
				'el-icon-stopwatch',
			],
			menulistBorderBottom: {},
			verticalFlag: false,
			isCollapse: false,
			verticalStyle2: {"isCollapse":false,"close":{"contentBox":{"hover":{},"active":{"margin":"0 0 0 54px"},"default":{"minHeight":"100%","padding":"0px 0 0 56px","margin":"0","position":"relative","background":"url(http://codegen.caihongy.cn/20230807/bc751527d2454c82a345e91b17a44608.jpg) no-repeat center top / cover","display":"block"}},"box":{"hover":{},"active":{"width":"54px"},"default":{"boxShadow":"0px 0 0px rgba(255,205,155,1)","padding":"40px 0 0","borderColor":"#f6dce0","bottom":"0","transition":"width 0.3s","overflow":"hidden","top":"0","left":"0","background":"rgba(0, 0, 0, 0.1)","borderWidth":"0 0px 0 0","width":"56px","fontSize":"0px","position":"fixed","borderStyle":"solid","height":"100%","zIndex":"1003"}},"menu":{"two":{"title":{"hover":{"padding":"0 0px","borderColor":"#fbafbf","color":"#fff","textAlign":"center","background":"#222!important","borderWidth":"0px 0","lineHeight":"auto","borderStyle":"solid","height":"auto"},"active":{"padding":"0 0px","borderColor":"#fbafbf","color":"#fff","textAlign":"center","background":"#222!important","borderWidth":"0px 0","lineHeight":"auto","borderStyle":"solid","height":"auto"},"default":{"padding":"0 0px","borderColor":"#ffd0da","color":"#fff","textAlign":"center","background":"#000","borderWidth":"0px 0","lineHeight":"auto","fontSize":"14px","borderStyle":"solid","height":"auto"}},"box":{"hover":{},"default":{"border":"none","padding":"0","fontSize":"inherit","borderRadius":"0px","left":"-5px","background":"none"}}},"box":{"hover":{},"default":{"border":0,"padding":"10px 0px","listStyle":"none","margin":"10px 0 0","flexWrap":"wrap","background":"none","display":"flex","width":"100%","position":"relative"}},"one":{"box1":{"hover":{"color":"#fff","background":"rgba(0, 0, 0, 0.2)"},"active":{"color":"#fff","background":"rgba(0, 0, 0, 0.2)"},"default":{"cursor":"pointer","padding":"0","borderColor":"rgba(255, 255, 255, 0.23)","whiteSpace":"nowrap","color":"#fff","textAlign":"center","background":"rgba(0, 0, 0, 0.1)","borderWidth":"0 0 0px","width":"100%","fontSize":"inherit","position":"relative","borderStyle":"solid","height":"auto"}},"icon":{"hover":{},"default":{"verticalAlign":"middle","margin":"0 auto","color":"inherit","textAlign":"center","display":"inline-block","width":"24px","fontSize":"24px"},"flag":true},"box":{"hover":{},"default":{"width":"100%","padding":"0px","listStyle":"none","margin":"0 0 5px","fontSize":"inherit"}},"title":{"hover":{},"default":{"width":"0","verticalAlign":"middle","fontSize":"inherit","color":"inherit","height":"0"}},"arrow":{"hover":{},"default":{"verticalAlign":"middle","margin":"-7px 0 0 0","top":"50%","color":"inherit","display":"none","fontSize":"12px","position":"absolute","right":"20px"}}}},"btn":{"icon":{"hover":{},"default":{"color":"inherit","margin":"0 2px 0 0","fontSize":"18px"},"text":"icon-menu17"},"hover":{"opacity":"0.8"},"default":{"border":"0","cursor":"pointer","padding":"0 0px","margin":"18px 0px 0px","color":"#fff","outline":"none","borderRadius":"4px","top":"0","left":"12px","background":"rgba(0,0,0,.3)","width":"30px","fontSize":"14px","position":"fixed","height":"30px","zIndex":"1003"},"text":""},"user":{"two":{"title":{"hover":{"padding":"0 0px","backgroundColor":"#222!important","lineHeight":"auto","color":"#fff","height":"auto"},"active":{"padding":"0 0px","backgroundColor":"#222!important","lineHeight":"auto","color":"#fff","height":"auto"},"default":{"padding":"0 0px","backgroundColor":"#000","lineHeight":"auto","color":"#fff","textAlign":"center","height":"auto"}},"box":{"hover":{},"default":{"border":"none","left":"-5px"}}},"one":{"box1":{"hover":{"color":"#fff","background":"#36a2f5"},"active":{"color":"#fff","background":"#36a2f5"},"default":{"cursor":"pointer","padding":"0 0px","borderColor":"rgba(255, 255, 255, 0.23)","whiteSpace":"nowrap","color":"#fff","textAlign":"center","background":"none","borderWidth":"0 0 1px","position":"relative","borderStyle":"solid"}},"icon":{"hover":{},"default":{"verticalAlign":"middle","margin":"0","color":"inherit","textAlign":"center","display":"inline-block","width":"24px","fontSize":"24px"},"flag":true,"text":"icon-kuaijiezhifu"},"box":{"hover":{},"default":{"width":"100%","padding":"0","listStyle":"none","margin":"0 0 0px","background":"none","order":"0"}},"title":{"hover":{},"default":{"width":"0","verticalAlign":"middle","fontSize":"14px","color":"inherit","height":"0"}},"arrow":{"hover":{},"default":{"verticalAlign":"middle","margin":"-7px 0 0 0","top":"50%","color":"inherit","display":"none","fontSize":"12px","position":"absolute","right":"20px"}}}},"userinfo":{"nickname":{"hover":{},"default":{"fontSize":"24px","lineHeight":"1.5","color":"#fff","textAlign":"center"}},"img":{"hover":{},"default":{"width":"100%","objectFit":"cover","borderRadius":"20px","display":"block","height":"170px"}},"box":{"hover":{},"default":{"width":"100%","padding":"20px","display":"none","height":"auto"}}},"home":{"two":{"title":{"hover":{"padding":"0 20px","backgroundColor":"#222 !important","lineHeight":"56px","color":"#fff","height":"56px"},"active":{"padding":"0 20px","backgroundColor":"#222 !important","lineHeight":"56px","color":"#fff","height":"56px"},"default":{"padding":"0 20px","backgroundColor":"#fff","lineHeight":"56px","color":"#646","height":"56px"}},"box":{"hover":{},"default":{"border":"none"}}},"one":{"box1":{"hover":{"color":"#fff","background":"rgba(0, 0, 0, 0.2)"},"active":{"color":"#fff","background":"rgba(0, 0, 0, 0.2)"},"default":{"cursor":"pointer","padding":"0","borderColor":"rgba(255, 255, 255, 0.23)","whiteSpace":"nowrap","color":"#fff","textAlign":"center","background":"rgba(0, 0, 0, 0.1)","borderWidth":"0 0 0px","position":"relative","borderStyle":"solid"}},"icon":{"hover":{},"default":{"verticalAlign":"middle","margin":"0","color":"inherit","textAlign":"center","display":"inline-block","width":"24px","fontSize":"24px"},"flag":true,"text":"icon-home19"},"box":{"hover":{},"default":{"width":"100%","padding":"0","listStyle":"none","margin":"0 0 5px","background":"none"}},"title":{"hover":{},"default":{"width":"0","verticalAlign":"middle","fontSize":"14px","color":"inherit","height":"0"}},"arrow":{"hover":{},"default":{"verticalAlign":"middle","margin":"-7px 0 0 0","top":"50%","color":"inherit","display":"none","fontSize":"12px","position":"absolute","right":"20px"}}}}},"open":{"contentBox":{"hover":{},"default":{"minHeight":"100%","padding":"0px 0 0 260px","margin":"0","position":"relative","background":"url(http://codegen.caihongy.cn/20230807/bc751527d2454c82a345e91b17a44608.jpg) no-repeat center top / cover","display":"block"}},"box":{"hover":{},"default":{"boxShadow":"0px 0 0px rgba(255,205,155,1)","padding":"70px 0px 0px","borderColor":"#f0cad3","bottom":"0px","transition":"width 0.3s","overflow":"hidden","top":"0px","left":"10px","background":"rgba(0, 0, 0, 0.0)","borderWidth":"0 0px 0 0","width":"260px","fontSize":"16px","position":"fixed","borderStyle":"solid","height":"100%","zIndex":"1003"}},"menu":{"two":{"title":{"hover":{"padding":"0px 25px","borderColor":"rgba(126, 96, 16, .1)","color":"#fff","background":"url(http://codegen.caihongy.cn/20230808/750a77dd2ad148b6a2dff6a4f8103bd5.png) no-repeat left center,rgba(0, 0, 0, 0.3)","width":"auto","lineHeight":"45px","borderStyle":"solid","height":"45px"},"active":{"padding":"0px 25px","borderColor":"rgba(126, 96, 16, .1)","color":"#fff","background":"url(http://codegen.caihongy.cn/20230808/750a77dd2ad148b6a2dff6a4f8103bd5.png) no-repeat left center,rgba(0, 0, 0, 0.3)","width":"auto","lineHeight":"45px","borderStyle":"solid","height":"45px"},"default":{"padding":"0px 25px","margin":"0px 0 6px","borderColor":"rgba(126, 96, 16, .2)","color":"#fff","textAlign":"left","clipPath":"polygon(0% 0%, 95% 0, 100% 50%, 95% 100%, 0% 100%)","borderRadius":"0px","background":"url(http://codegen.caihongy.cn/20230808/750a77dd2ad148b6a2dff6a4f8103bd5.png) no-repeat left center,rgba(0, 0, 0, 0.1)","borderWidth":"0 0 0px","width":"auto","lineHeight":"45px","fontSize":"inherit","borderStyle":"dashed","height":"45px"}},"box":{"hover":{},"default":{"border":"0px solid rgba(252, 234, 238, .9)","padding":"0px 0 0","margin":"10px auto 0","borderRadius":"4px","background":"rgba(0, 0, 0, 0.0)","width":"auto","fontSize":"inherit"}}},"box":{"hover":{},"default":{"border":0,"padding":"0px","listStyle":"none","margin":"0","alignItems":"flex-start","flexWrap":"wrap","background":"none","display":"flex","position":"relative"}},"one":{"box1":{"hover":{"color":"#fff","background":"linear-gradient(323deg, rgba(40,55,72,1) 0%, rgba(122,133,147,.5) 70%, rgba(40,55,72,.5) 100%)","height":"auto"},"active":{"color":"#fff","background":"linear-gradient(323deg, rgba(40,55,72,1) 0%, rgba(122,133,147,.5) 70%, rgba(40,55,72,.5) 100%)","height":"auto"},"default":{"cursor":"pointer","border":"0px solid rgba(3, 152, 15, .2)","padding":"0px 15px","borderColor":"rgba(255, 255, 255, 0.23)","whiteSpace":"nowrap","color":"#fff","clipPath":"polygon(0% 0%, 100% 0, 95% 51%, 100% 100%, 0% 100%)","borderRadius":"4px","background":"linear-gradient(323deg, rgba(40,55,72,1) 0%, rgba(122,133,147,1) 70%, rgba(40,55,72,1) 100%)","borderWidth":"0 0 0px","fontSize":"inherit","lineHeight":"58px","position":"relative","borderStyle":"solid","height":"auto"}},"icon":{"hover":{},"default":{"width":"auto","verticalAlign":"middle","margin":"0 3px","fontSize":"24px","color":"inherit","textAlign":"center"},"flag":true},"box":{"hover":{},"default":{"width":"100%","padding":"0 0 10px","listStyle":"none","margin":"0","lineHeight":"auto","height":"auto"}},"title":{"hover":{},"default":{"verticalAlign":"middle","color":"inherit","textAlign":"center","display":"inline-block","width":"auto","fontSize":"16px","lineHeight":"32px"}},"arrow":{"hover":{},"default":{"verticalAlign":"middle","margin":"-7px 0 0 0","top":"50%","color":"inherit","fontSize":"inherit","position":"absolute","right":"20px"}}}},"btn":{"icon":{"hover":{},"default":{"color":"inherit","margin":"0px 2px","fontSize":"18px"},"text":"icon-menu17"},"hover":{"opacity":"0.8"},"default":{"border":"0px solid #ddd","cursor":"pointer","padding":"0 0px","margin":"22px 4px 0px","color":"#fff","outline":"none","borderRadius":"4px","top":"0","left":"234px","background":"rgba(0,0,0,.3)","width":"30px","fontSize":"inherit","position":"fixed","height":"30px","zIndex":"1003"},"text":""},"user":{"two":{"title":{"hover":{"padding":"0px 25px","borderColor":"rgba(126, 96, 16, .1)","color":"#fff","background":"url(http://codegen.caihongy.cn/20230808/750a77dd2ad148b6a2dff6a4f8103bd5.png) no-repeat left center,rgba(0, 0, 0, 0.3)","width":"auto","lineHeight":"45px","borderStyle":"solid","height":"45px"},"active":{"width":"auto","padding":"0px 25px","lineHeight":"45px","color":"#fff","background":"url(http://codegen.caihongy.cn/20230808/750a77dd2ad148b6a2dff6a4f8103bd5.png) no-repeat left center,rgba(0, 0, 0, 0.3)","height":"45px"},"default":{"padding":"0px 25px","borderColor":"#eee","margin":"0 0 6px","color":"#fff","textAlign":"left","clipPath":"polygon(0% 0%, 95% 0, 100% 50%, 95% 100%, 0% 100%)","background":"url(http://codegen.caihongy.cn/20230808/750a77dd2ad148b6a2dff6a4f8103bd5.png) no-repeat left center,rgba(0, 0, 0, 0.1)","borderWidth":"0 0 0px","width":"auto","lineHeight":"45px","fontSize":"inherit","borderStyle":"solid","height":"45px"}},"box":{"hover":{},"default":{"border":"0px solid rgba(3, 152, 15, .2)","margin":"10px 0 0","fontSize":"inherit","borderRadius":"0px","background":"none"}}},"one":{"box1":{"hover":{"color":"#fff","background":"linear-gradient(323deg, rgba(40,55,72,1) 0%, rgba(122,133,147,.5) 70%, rgba(40,55,72,.5) 100%)","height":"auto"},"active":{"color":"#fff","background":"linear-gradient(323deg, rgba(40,55,72,1) 0%, rgba(122,133,147,.5) 70%, rgba(40,55,72,.5) 100%)","height":"auto"},"default":{"cursor":"pointer","padding":"0px 15px","borderColor":"rgba(255, 255, 255, 0.23)","whiteSpace":"nowrap","color":"#fff","clipPath":"polygon(0% 0%, 100% 0, 95% 51%, 100% 100%, 0% 100%)","borderRadius":"0px","background":"linear-gradient(323deg, rgba(40,55,72,1) 0%, rgba(122,133,147,1) 70%, rgba(40,55,72,1) 100%)","borderWidth":"0 0 1px","fontSize":"inherit","lineHeight":"58px","position":"relative","borderStyle":"solid","height":"auto"}},"icon":{"hover":{},"default":{"width":"auto","verticalAlign":"middle","margin":"0 3px","fontSize":"24px","color":"inherit","textAlign":"center"},"flag":true,"text":"icon-kuaijiezhifu"},"box":{"hover":{},"default":{"padding":"0 0 0px","listStyle":"none","margin":"0","width":"100%","lineHeight":"auto","order":"0","height":"auto"}},"title":{"hover":{},"default":{"verticalAlign":"middle","color":"inherit","textAlign":"center","display":"inline-block","width":"auto","fontSize":"inherit","lineHeight":"32px"},"text":"我的信息"},"arrow":{"hover":{},"default":{"verticalAlign":"middle","margin":"-7px 0 0 0","top":"50%","color":"inherit","fontSize":"inherit","position":"absolute","right":"20px"}}}},"userinfo":{"nickname":{"hover":{},"default":{"fontSize":"18px","lineHeight":"1.5","color":"#fff","textAlign":"center"}},"img":{"hover":{},"default":{"border":"0px solid #fff","margin":"0 auto 6px","objectFit":"cover","borderRadius":"4px","display":"block","width":"100%","height":"180px"}},"box":{"hover":{},"default":{"width":"100%","padding":"0","margin":"0 0 20px","display":"block","height":"auto","order":"2"}}},"home":{"two":{"title":{"hover":{"padding":"0px 25px","lineHeight":"44px","color":"#fff","background":"rgba(0, 0, 0, 0.2)","height":"44px"},"active":{"padding":"0px 25px","lineHeight":"44px","color":"#fff","background":"rgba(0, 0, 0, 0.2)","height":"44px"},"default":{"padding":"0px 25px","lineHeight":"44px","color":"#664","background":"none","height":"44px"}},"box":{"hover":{},"default":{"border":"none","display":"none"}}},"one":{"box1":{"hover":{"color":"#fff","background":"linear-gradient(323deg, rgba(40,55,72,1) 0%, rgba(122,133,147,.5) 70%, rgba(40,55,72,.5) 100%)"},"active":{"color":"#fff","background":"linear-gradient(323deg, rgba(40,55,72,1) 0%, rgba(122,133,147,.5) 70%, rgba(40,55,72,.5) 100%)"},"default":{"cursor":"pointer","padding":"0px 15px","borderColor":"rgba(255, 255, 255, 0.23)","whiteSpace":"nowrap","color":"#fff","clipPath":"polygon(0% 0%, 100% 0, 95% 51%, 100% 100%, 0% 100%)","borderRadius":"4px","background":"linear-gradient(323deg, rgba(40,55,72,1) 0%, rgba(122,133,147,1) 70%, rgba(40,55,72,1) 100%)","borderWidth":"0 0 0px","fontSize":"inherit","lineHeight":"58px","position":"relative","borderStyle":"solid","height":"auto"}},"icon":{"hover":{},"default":{"verticalAlign":"middle","margin":"0 3px","color":"inherit","textAlign":"center","display":"inline-block","width":"auto","fontSize":"24px"},"flag":true,"text":"icon-home19"},"box":{"hover":{},"default":{"padding":"0 0 10px","listStyle":"none","margin":"0","width":"100%","fontSize":"inherit","lineHeight":"auto","height":"auto"}},"title":{"hover":{},"default":{"color":"inherit","verticalAlign":"middle","fontSize":"inherit"},"text":"Home"},"arrow":{"hover":{},"default":{"verticalAlign":"middle","margin":"-7px 0 0 0","top":"50%","color":"inherit","fontSize":"12px","position":"absolute","right":"20px"}}}}}},
			verticalIsMultiple: false,
		}
	},
	computed: {
		activeMenu() {
			const route = this.$route
			console.log(route)
			const {
				meta,
				path
			} = route
			// if st path, the sidebar will highlight the path you sete
			if (meta.activeMenu) {
				return meta.activeMenu
			}
			return path
		}
	},
	mounted() {
		const menus = menu.list()
		if(menus) {
			this.menuList = menus
		} else {
			let params = {
				page: 1,
				limit: 1,
				sort: 'id',
			}
			
			this.$http({
				url: "menu/list",
				method: "get",
				params: params
			}).then(({
				data
			}) => {
				if (data && data.code === 0) {
					this.menuList = JSON.parse(data.data.list[0].menujson);
					this.$storage.set("menus", this.menuList);
				}
			})
		}
		this.role = this.$storage.get('role')
		
		for(let i=0;i<this.menuList.length;i++) {
			if(this.menuList[i].roleName == this.role) {
				this.menuList = this.menuList[i];
				break;
			}
		}
		this.styleChange()
		
		let sessionTable = this.$storage.get("sessionTable")
		this.$http({
			url: sessionTable + '/session',
			method: "get"
		}).then(({
			data
		}) => {
			if (data && data.code === 0) {
				if(sessionTable == 'yonghu') {
					this.avatar = data.data.touxiang
				}
				if(sessionTable == 'qihuogongsi') {
					this.avatar = data.data.touxiang
				}
				this.user = data.data;
			} else {
				let message = this.$message
				message.error(data.msg);
			}
		});
	},
	created(){
		this.icons.sort(()=>{
			return (0.5-Math.random())
		})
	},
	methods: {
		collapse() {
		  this.isCollapse = !this.isCollapse
		  this.$emit('oncollapsechange', this.isCollapse)
		},
		styleChange() {
			this.$nextTick(() => {
								document.querySelectorAll('.el-menu-vertical-demo .el-submenu .el-menu').forEach(el => {
				  el.removeAttribute('style')
				  const icon = {"border":"none","display":"none"}
				  Object.keys(icon).forEach((key) => {
					el.style[key] = icon[key]
				  })
				})
											})
		},
		menuHandler(name) {
			let router = this.$router
			name = '/'+name
			router.push(name)
		},
	}
}
</script>
<style lang="scss" scoped>
	.menu-preview {
	  .el-scrollbar {
	    height: 100%;
	
	    & /deep/ .scrollbar-wrapper {
	      overflow-x: hidden;
	    }
		
				// 竖向
		.el-menu-vertical-demo {
		  .el-submenu:first-of-type /deep/ .el-submenu__title .el-submenu__icon-arrow {
		    display: none;
		  }
		}
		
		.el-menu-vertical-demo>.el-menu-item {
				  				  cursor: pointer;
				  				  padding: 0 20px;
				  				  color: #333;
				  				  white-space: nowrap;
				  				  background: #fff;
				  				  position: relative;
				  		}
		
		.el-menu-vertical-demo>.el-menu-item:hover {
						color: #fff;
						background: blue;
					}
		
		.el-menu-vertical-demo .el-submenu /deep/ .el-submenu__title {
						cursor: pointer;
						padding: 0 20px;
						color: #333;
						white-space: nowrap;
						background: #fff;
						position: relative;
					}
		
		.el-menu-vertical-demo .el-submenu /deep/ .el-submenu__title:hover {
						color: #fff;
						background: blue;
					}
		
		.el-menu-vertical-demo .el-submenu /deep/ .el-submenu__title .el-submenu__icon-arrow {
						margin: -7px 0 0 0;
						top: 50%;
						color: inherit;
						vertical-align: middle;
						font-size: 12px;
						position: absolute;
						right: 20px;
					}
		
		.el-menu-vertical-demo .el-submenu {
						padding: 0;
						margin: 0;
						list-style: none;
					}
		
		// .el-menu-vertical-demo .el-submenu /deep/ .el-menu {
		// 				// 		border: none;
		// 				// 		display: none;
		// 				// }
		
		.el-menu-vertical-demo .el-submenu /deep/ .el-menu .el-menu-item {
						padding: 0 40px;
						color: #666;
						background: #fff;
						line-height: 50px;
						height: 50px;
					}
		
		.el-menu-vertical-demo .el-submenu /deep/ .el-menu .el-menu-item:hover {
						padding: 0 40px;
						color: #fff;
						background: red;
						line-height: 50px;
						height: 50px;
					}
		
		.el-menu-vertical-demo .el-submenu /deep/ .el-menu .el-menu-item.is-active {
						padding: 0 40px;
						color: #fff;
						background: blue;
						line-height: 50px;
						height: 50px;
					}
		// 竖向
			  }
	  	}
	// 竖向 样式二-open
	.scrollbar-wrapper-open .el-menu-vertical-2>.el-menu-item.other {
		font-size: inherit;
		background: none;
	}
	.scrollbar-wrapper-open .el-menu-vertical-2>.el-menu-item.home {
		font-size: inherit;
		background: none;
	}
	.scrollbar-wrapper-open .el-menu-vertical-2>.el-menu-item.other>.el-tooltip {
				cursor: pointer;
				border: 0px solid rgba(3, 152, 15, .2);
				padding: 0px 15px;
				color: #fff;
				white-space: nowrap;
				font-size: inherit;
				border-color: rgba(255, 255, 255, 0.23);
				line-height: 58px;
				border-radius: 4px;
				clip-path: polygon(0% 0%, 100% 0, 95% 51%, 100% 100%, 0% 100%);
				background: linear-gradient(323deg, rgba(40,55,72,1) 0%, rgba(122,133,147,1) 70%, rgba(40,55,72,1) 100%);
				border-width: 0 0 0px;
				position: relative;
				border-style: solid;
				height: auto;
			}
	
	.scrollbar-wrapper-open .el-menu-vertical-2>.el-menu-item.other>.el-tooltip:hover {
				color: #fff;
				background: linear-gradient(323deg, rgba(40,55,72,1) 0%, rgba(122,133,147,.5) 70%, rgba(40,55,72,.5) 100%);
				height: auto;
			}
	
	.scrollbar-wrapper-open .el-menu-vertical-2>.el-menu-item.other.is-active>.el-tooltip {
				color: #fff;
				background: linear-gradient(323deg, rgba(40,55,72,1) 0%, rgba(122,133,147,.5) 70%, rgba(40,55,72,.5) 100%);
				height: auto;
			}
	
	.scrollbar-wrapper-open .el-menu-vertical-2 .el-submenu.other /deep/ .el-submenu__title {
				cursor: pointer !important;
				border: 0px solid rgba(3, 152, 15, .2) !important;
				padding: 0px 15px !important;
				color: #fff !important;
				white-space: nowrap !important;
				font-size: inherit !important;
				border-color: rgba(255, 255, 255, 0.23) !important;
				line-height: 58px !important;
				border-radius: 4px !important;
				clip-path: polygon(0% 0%, 100% 0, 95% 51%, 100% 100%, 0% 100%) !important;
				background: linear-gradient(323deg, rgba(40,55,72,1) 0%, rgba(122,133,147,1) 70%, rgba(40,55,72,1) 100%) !important;
				border-width: 0 0 0px !important;
				position: relative !important;
				border-style: solid !important;
				height: auto !important;
			}
	
	.scrollbar-wrapper-open .el-menu-vertical-2 .el-submenu.other /deep/ .el-submenu__title:hover {
				color: #fff !important;
				background: linear-gradient(323deg, rgba(40,55,72,1) 0%, rgba(122,133,147,.5) 70%, rgba(40,55,72,.5) 100%) !important;
				height: auto !important;
			}
	
	.scrollbar-wrapper-open .el-menu-vertical-2 .el-submenu.other /deep/ .el-submenu__title .iconfont {
				margin: 0 3px;
				color: inherit;
				width: auto;
				vertical-align: middle;
				font-size: 24px;
				text-align: center;
			}
	
	.scrollbar-wrapper-open .el-menu-vertical-2 .el-submenu.other /deep/ .el-submenu__title .el-submenu__icon-arrow {
				margin: -7px 0 0 0;
				top: 50%;
				color: inherit;
				vertical-align: middle;
				font-size: inherit;
				position: absolute;
				right: 20px;
			}
	
	.scrollbar-wrapper-open .el-menu-vertical-2 /deep/ .el-submenu.other .el-menu {
				border: 0px solid rgba(252, 234, 238, .9);
				border-radius: 4px;
				padding: 0px 0 0;
				margin: 10px auto 0;
				background: rgba(0, 0, 0, 0.0);
				width: auto;
				font-size: inherit;
			}
	
	.scrollbar-wrapper-open .el-menu-vertical-2 .el-submenu.other .el-menu .el-menu-item {
				padding: 0px 25px !important;
				margin: 0px 0 6px !important;
				color: #fff !important;
				font-size: inherit !important;
				border-color: rgba(126, 96, 16, .2) !important;
				line-height: 45px !important;
				border-radius: 0px !important;
				clip-path: polygon(0% 0%, 95% 0, 100% 50%, 95% 100%, 0% 100%) !important;
				background: url(http://codegen.caihongy.cn/20230808/750a77dd2ad148b6a2dff6a4f8103bd5.png) no-repeat left center,rgba(0, 0, 0, 0.1) !important;
				width: auto !important;
				border-width: 0 0 0px !important;
				border-style: dashed !important;
				text-align: left !important;
				height: 45px !important;
			}
	
	.scrollbar-wrapper-open .el-menu-vertical-2 .el-submenu.other .el-menu .el-menu-item:hover {
				padding: 0px 25px !important;
				color: #fff !important;
				background: url(http://codegen.caihongy.cn/20230808/750a77dd2ad148b6a2dff6a4f8103bd5.png) no-repeat left center,rgba(0, 0, 0, 0.3) !important;
				width: auto !important;
				border-color: rgba(126, 96, 16, .1) !important;
				line-height: 45px !important;
				border-style: solid !important;
				height: 45px !important;
			}
	
	.scrollbar-wrapper-open .el-menu-vertical-2 .el-submenu.other .el-menu .el-menu-item.is-active {
				padding: 0px 25px;
				color: #fff;
				background: url(http://codegen.caihongy.cn/20230808/750a77dd2ad148b6a2dff6a4f8103bd5.png) no-repeat left center,rgba(0, 0, 0, 0.3);
				width: auto;
				border-color: rgba(126, 96, 16, .1);
				line-height: 45px;
				border-style: solid;
				height: 45px;
			}

	// 竖向 样式二-close
	.scrollbar-wrapper-close .el-menu-vertical-2>.el-menu-item.other>.el-tooltip {
				cursor: pointer;
				padding: 0;
				color: #fff;
				white-space: nowrap;
				font-size: inherit;
				border-color: rgba(255, 255, 255, 0.23);
				background: rgba(0, 0, 0, 0.1);
				width: 100%;
				border-width: 0 0 0px;
				position: relative;
				border-style: solid;
				text-align: center;
				height: auto;
			}
	
	.scrollbar-wrapper-close .el-menu-vertical-2>.el-menu-item.other>.el-tooltip:hover {
				color: #fff;
				background: rgba(0, 0, 0, 0.2);
			}
	
	.scrollbar-wrapper-close .el-menu-vertical-2>.el-menu-item.other.is-active>.el-tooltip {
				color: #fff;
				background: rgba(0, 0, 0, 0.2);
			}
	
	.scrollbar-wrapper-close .el-menu-vertical-2 .el-submenu.other /deep/ .el-submenu__title {
				cursor: pointer !important;
				padding: 0 !important;
				color: #fff !important;
				white-space: nowrap !important;
				font-size: inherit !important;
				border-color: rgba(255, 255, 255, 0.23) !important;
				background: rgba(0, 0, 0, 0.1) !important;
				width: 100% !important;
				border-width: 0 0 0px !important;
				position: relative !important;
				border-style: solid !important;
				text-align: center !important;
				height: auto !important;
			}
	
	.scrollbar-wrapper-close .el-menu-vertical-2 .el-submenu.other /deep/ .el-submenu__title:hover {
				color: #fff !important;
				background: rgba(0, 0, 0, 0.2) !important;
			}
	
	.scrollbar-wrapper-close .el-menu-vertical-2 .el-submenu.other /deep/ .el-submenu__title .iconfont {
				margin: 0 auto;
				color: inherit;
				display: inline-block;
				vertical-align: middle;
				width: 24px;
				font-size: 24px;
				text-align: center;
			}
	
	.scrollbar-wrapper-close .el-menu-vertical-2 .el-submenu.other /deep/ .el-submenu__title .el-submenu__icon-arrow {
				margin: -7px 0 0 0;
				top: 50%;
				color: inherit;
				display: none;
				vertical-align: middle;
				font-size: 12px;
				position: absolute;
				right: 20px;
			}
	
	.scrollbar-wrapper-close .el-menu-vertical-2 .el-submenu.other .el-menu {
				border: none;
				border-radius: 0px;
				padding: 0;
				left: -5px;
				background: none;
				font-size: inherit;
			}
	
	.scrollbar-wrapper-close .el-menu-vertical-2 .el-submenu.other .el-menu--vertical.other .el-menu-item {
				padding: 0 0px;
				color: #fff;
				background: #000;
				font-size: 14px;
				border-color: #ffd0da;
				border-width: 0px 0;
				line-height: auto;
				border-style: solid;
				text-align: center;
				height: auto;
			}
	
	.scrollbar-wrapper-close .el-menu-vertical-2 .el-submenu.other .el-menu--vertical.other .el-menu-item:hover {
				padding: 0 0px;
				color: #fff;
				background: #222!important;
				border-color: #fbafbf;
				border-width: 0px 0;
				line-height: auto;
				border-style: solid;
				text-align: center;
				height: auto;
			}
	
	.scrollbar-wrapper-close .el-menu-vertical-2 .el-submenu.other .el-menu--vertical.other .el-menu-item.is-active {
				padding: 0 0px;
				color: #fff;
				background: #222!important;
				border-color: #fbafbf;
				border-width: 0px 0;
				line-height: auto;
				border-style: solid;
				text-align: center;
				height: auto;
			}
	
	// 竖向 样式二-open-首页
	.scrollbar-wrapper-open .el-menu-vertical-2>.el-menu-item.home>.el-tooltip {
				cursor: pointer;
				border: 0px solid rgba(3, 152, 15, .2);
				padding: 0px 15px;
				color: #fff;
				white-space: nowrap;
				font-size: inherit;
				border-color: rgba(255, 255, 255, 0.23);
				line-height: 58px;
				border-radius: 4px;
				clip-path: polygon(0% 0%, 100% 0, 95% 51%, 100% 100%, 0% 100%);
				background: linear-gradient(323deg, rgba(40,55,72,1) 0%, rgba(122,133,147,1) 70%, rgba(40,55,72,1) 100%);
				border-width: 0 0 0px;
				position: relative;
				border-style: solid;
				height: auto;
			}
	
	.scrollbar-wrapper-open .el-menu-vertical-2>.el-menu-item.home>.el-tooltip:hover {
				color: #fff;
				background: linear-gradient(323deg, rgba(40,55,72,1) 0%, rgba(122,133,147,.5) 70%, rgba(40,55,72,.5) 100%);
				height: auto;
			}
	
	.scrollbar-wrapper-open .el-menu-vertical-2>.el-menu-item.home.is-active>.el-tooltip {
				color: #fff;
				background: linear-gradient(323deg, rgba(40,55,72,1) 0%, rgba(122,133,147,.5) 70%, rgba(40,55,72,.5) 100%);
				height: auto;
			}
	
	.scrollbar-wrapper-open .el-menu-vertical-2 .el-submenu.home /deep/ .el-submenu__title {
				cursor: pointer !important;
				border: 0px solid rgba(3, 152, 15, .2) !important;
				padding: 0px 15px !important;
				color: #fff !important;
				white-space: nowrap !important;
				font-size: inherit !important;
				border-color: rgba(255, 255, 255, 0.23) !important;
				line-height: 58px !important;
				border-radius: 4px !important;
				clip-path: polygon(0% 0%, 100% 0, 95% 51%, 100% 100%, 0% 100%) !important;
				background: linear-gradient(323deg, rgba(40,55,72,1) 0%, rgba(122,133,147,1) 70%, rgba(40,55,72,1) 100%) !important;
				border-width: 0 0 0px !important;
				position: relative !important;
				border-style: solid !important;
				height: auto !important;
			}
	
	.scrollbar-wrapper-open .el-menu-vertical-2 .el-submenu.home /deep/ .el-submenu__title:hover {
				color: #fff !important;
				background: linear-gradient(323deg, rgba(40,55,72,1) 0%, rgba(122,133,147,.5) 70%, rgba(40,55,72,.5) 100%) !important;
				height: auto !important;
			}
	
	.scrollbar-wrapper-open .el-menu-vertical-2 .el-submenu.home /deep/ .el-submenu__title .iconfont {
				margin: 0 3px;
				color: inherit;
				width: auto;
				vertical-align: middle;
				font-size: 24px;
				text-align: center;
			}
	
	.scrollbar-wrapper-open .el-menu-vertical-2 .el-submenu.home /deep/ .el-submenu__title .el-submenu__icon-arrow {
				margin: -7px 0 0 0;
				top: 50%;
				color: inherit;
				vertical-align: middle;
				font-size: inherit;
				position: absolute;
				right: 20px;
			}
	
	.scrollbar-wrapper-open .el-menu-vertical-2 .el-submenu.home .el-menu {
				border: 0px solid rgba(252, 234, 238, .9);
				border-radius: 4px;
				padding: 0px 0 0;
				margin: 10px auto 0;
				background: rgba(0, 0, 0, 0.0);
				width: auto;
				font-size: inherit;
			}
	
	.scrollbar-wrapper-open .el-menu-vertical-2 .el-submenu.home .el-menu .el-menu-item {
				padding: 0px 25px;
				margin: 0px 0 6px;
				color: #fff;
				font-size: inherit;
				border-color: rgba(126, 96, 16, .2);
				line-height: 45px;
				border-radius: 0px;
				clip-path: polygon(0% 0%, 95% 0, 100% 50%, 95% 100%, 0% 100%);
				background: url(http://codegen.caihongy.cn/20230808/750a77dd2ad148b6a2dff6a4f8103bd5.png) no-repeat left center,rgba(0, 0, 0, 0.1);
				width: auto;
				border-width: 0 0 0px;
				border-style: dashed;
				text-align: left;
				height: 45px;
			}
	
	.scrollbar-wrapper-open .el-menu-vertical-2 .el-submenu.home .el-menu .el-menu-item:hover {
				padding: 0px 25px;
				color: #fff;
				background: url(http://codegen.caihongy.cn/20230808/750a77dd2ad148b6a2dff6a4f8103bd5.png) no-repeat left center,rgba(0, 0, 0, 0.3);
				width: auto;
				border-color: rgba(126, 96, 16, .1);
				line-height: 45px;
				border-style: solid;
				height: 45px;
			}
	
	.scrollbar-wrapper-open .el-menu-vertical-2 .el-submenu.home .el-menu .el-menu-item.is-active {
				padding: 0px 25px;
				color: #fff;
				background: url(http://codegen.caihongy.cn/20230808/750a77dd2ad148b6a2dff6a4f8103bd5.png) no-repeat left center,rgba(0, 0, 0, 0.3);
				width: auto;
				border-color: rgba(126, 96, 16, .1);
				line-height: 45px;
				border-style: solid;
				height: 45px;
			}
	
	// 竖向 样式二-close-首页
	.scrollbar-wrapper-close .el-menu-vertical-2>.el-menu-item.home>.el-tooltip {
				cursor: pointer;
				padding: 0;
				color: #fff;
				white-space: nowrap;
				font-size: inherit;
				border-color: rgba(255, 255, 255, 0.23);
				background: rgba(0, 0, 0, 0.1);
				width: 100%;
				border-width: 0 0 0px;
				position: relative;
				border-style: solid;
				text-align: center;
				height: auto;
			}
	
	.scrollbar-wrapper-close .el-menu-vertical-2>.el-menu-item.home>.el-tooltip:hover {
				color: #fff;
				background: rgba(0, 0, 0, 0.2);
			}
	
	.scrollbar-wrapper-close .el-menu-vertical-2>.el-menu-item.home.is-active>.el-tooltip {
				color: #fff;
				background: rgba(0, 0, 0, 0.2);
			}
	
	.scrollbar-wrapper-close .el-menu-vertical-2 .el-submenu.home /deep/ .el-submenu__title {
				cursor: pointer;
				padding: 0;
				color: #fff;
				white-space: nowrap;
				font-size: inherit;
				border-color: rgba(255, 255, 255, 0.23);
				background: rgba(0, 0, 0, 0.1);
				width: 100%;
				border-width: 0 0 0px;
				position: relative;
				border-style: solid;
				text-align: center;
				height: auto;
			}
	
	.scrollbar-wrapper-close .el-menu-vertical-2 .el-submenu.home /deep/ .el-submenu__title:hover {
				color: #fff;
				background: rgba(0, 0, 0, 0.2);
			}
	
	.scrollbar-wrapper-close .el-menu-vertical-2 .el-submenu.home /deep/ .el-submenu__title .iconfont {
				margin: 0 auto;
				color: inherit;
				display: inline-block;
				vertical-align: middle;
				width: 24px;
				font-size: 24px;
				text-align: center;
			}
	
	.scrollbar-wrapper-close .el-menu-vertical-2 .el-submenu.home /deep/ .el-submenu__title .el-submenu__icon-arrow {
				margin: -7px 0 0 0;
				top: 50%;
				color: inherit;
				display: none;
				vertical-align: middle;
				font-size: 12px;
				position: absolute;
				right: 20px;
			}
	
	.scrollbar-wrapper-close .el-menu-vertical-2 .el-submenu.home .el-menu {
				border: none;
				border-radius: 0px;
				padding: 0;
				left: -5px;
				background: none;
				font-size: inherit;
			}
	
	.scrollbar-wrapper-close .el-menu-vertical-2 .el-submenu.home .el-menu--vertical.home .el-menu-item {
				padding: 0 0px;
				color: #fff;
				background: #000;
				font-size: 14px;
				border-color: #ffd0da;
				border-width: 0px 0;
				line-height: auto;
				border-style: solid;
				text-align: center;
				height: auto;
			}
	
	.scrollbar-wrapper-close .el-menu-vertical-2 .el-submenu.home .el-menu--vertical.home .el-menu-item:hover {
				padding: 0 0px;
				color: #fff;
				background: #222!important;
				border-color: #fbafbf;
				border-width: 0px 0;
				line-height: auto;
				border-style: solid;
				text-align: center;
				height: auto;
			}
	
	.scrollbar-wrapper-close .el-menu-vertical-2 .el-submenu.home .el-menu--vertical.home .el-menu-item.is-active {
				padding: 0 0px;
				color: #fff;
				background: #222!important;
				border-color: #fbafbf;
				border-width: 0px 0;
				line-height: auto;
				border-style: solid;
				text-align: center;
				height: auto;
			}
	
	// 竖向 样式二-open-个人中心
	.scrollbar-wrapper-open .el-menu-vertical-2>.el-menu-item.user>.el-tooltip {
				cursor: pointer;
				border: 0px solid rgba(3, 152, 15, .2);
				padding: 0px 15px;
				color: #fff;
				white-space: nowrap;
				font-size: inherit;
				border-color: rgba(255, 255, 255, 0.23);
				line-height: 58px;
				border-radius: 4px;
				clip-path: polygon(0% 0%, 100% 0, 95% 51%, 100% 100%, 0% 100%);
				background: linear-gradient(323deg, rgba(40,55,72,1) 0%, rgba(122,133,147,1) 70%, rgba(40,55,72,1) 100%);
				border-width: 0 0 0px;
				position: relative;
				border-style: solid;
				height: auto;
			}
	
	.scrollbar-wrapper-open .el-menu-vertical-2>.el-menu-item.user>.el-tooltip:hover {
				color: #fff;
				background: linear-gradient(323deg, rgba(40,55,72,1) 0%, rgba(122,133,147,.5) 70%, rgba(40,55,72,.5) 100%);
				height: auto;
			}
	
	.scrollbar-wrapper-open .el-menu-vertical-2>.el-menu-item.user.is-active>.el-tooltip {
				color: #fff;
				background: linear-gradient(323deg, rgba(40,55,72,1) 0%, rgba(122,133,147,.5) 70%, rgba(40,55,72,.5) 100%);
				height: auto;
			}
	
	.scrollbar-wrapper-open .el-menu-vertical-2 .el-submenu.user /deep/ .el-submenu__title {
				cursor: pointer !important;
				border: 0px solid rgba(3, 152, 15, .2) !important;
				padding: 0px 15px !important;
				color: #fff !important;
				white-space: nowrap !important;
				font-size: inherit !important;
				border-color: rgba(255, 255, 255, 0.23) !important;
				line-height: 58px !important;
				border-radius: 4px !important;
				clip-path: polygon(0% 0%, 100% 0, 95% 51%, 100% 100%, 0% 100%) !important;
				background: linear-gradient(323deg, rgba(40,55,72,1) 0%, rgba(122,133,147,1) 70%, rgba(40,55,72,1) 100%) !important;
				border-width: 0 0 0px !important;
				position: relative !important;
				border-style: solid !important;
				height: auto !important;
			}
	
	.scrollbar-wrapper-open .el-menu-vertical-2 .el-submenu.user /deep/ .el-submenu__title:hover {
				color: #fff !important;
				background: linear-gradient(323deg, rgba(40,55,72,1) 0%, rgba(122,133,147,.5) 70%, rgba(40,55,72,.5) 100%) !important;
				height: auto !important;
			}
	
	.scrollbar-wrapper-open .el-menu-vertical-2 .el-submenu.user /deep/ .el-submenu__title .iconfont {
				margin: 0 3px;
				color: inherit;
				width: auto;
				vertical-align: middle;
				font-size: 24px;
				text-align: center;
			}
	
	.scrollbar-wrapper-open .el-menu-vertical-2 .el-submenu.user /deep/ .el-submenu__title .el-submenu__icon-arrow {
				margin: -7px 0 0 0;
				top: 50%;
				color: inherit;
				vertical-align: middle;
				font-size: inherit;
				position: absolute;
				right: 20px;
			}
	
	.scrollbar-wrapper-open .el-menu-vertical-2 /deep/ .el-submenu.user .el-menu {
				border: 0px solid rgba(252, 234, 238, .9);
				border-radius: 4px;
				padding: 0px 0 0;
				margin: 10px auto 0;
				background: rgba(0, 0, 0, 0.0);
				width: auto;
				font-size: inherit;
			}
	
	.scrollbar-wrapper-open .el-menu-vertical-2 .el-submenu.user .el-menu .el-menu-item {
				padding: 0px 25px !important;
				margin: 0px 0 6px !important;
				color: #fff !important;
				font-size: inherit !important;
				border-color: rgba(126, 96, 16, .2) !important;
				line-height: 45px !important;
				border-radius: 0px !important;
				clip-path: polygon(0% 0%, 95% 0, 100% 50%, 95% 100%, 0% 100%) !important;
				background: url(http://codegen.caihongy.cn/20230808/750a77dd2ad148b6a2dff6a4f8103bd5.png) no-repeat left center,rgba(0, 0, 0, 0.1) !important;
				width: auto !important;
				border-width: 0 0 0px !important;
				border-style: dashed !important;
				text-align: left !important;
				height: 45px !important;
			}
	
	.scrollbar-wrapper-open .el-menu-vertical-2 .el-submenu.user .el-menu .el-menu-item:hover {
				padding: 0px 25px !important;
				color: #fff !important;
				background: url(http://codegen.caihongy.cn/20230808/750a77dd2ad148b6a2dff6a4f8103bd5.png) no-repeat left center,rgba(0, 0, 0, 0.3) !important;
				width: auto !important;
				border-color: rgba(126, 96, 16, .1) !important;
				line-height: 45px !important;
				border-style: solid !important;
				height: 45px !important;
			}
	
	.scrollbar-wrapper-open .el-menu-vertical-2 .el-submenu.user .el-menu .el-menu-item.is-active {
				padding: 0px 25px;
				color: #fff;
				background: url(http://codegen.caihongy.cn/20230808/750a77dd2ad148b6a2dff6a4f8103bd5.png) no-repeat left center,rgba(0, 0, 0, 0.3);
				width: auto;
				border-color: rgba(126, 96, 16, .1);
				line-height: 45px;
				border-style: solid;
				height: 45px;
			}
	
	// 竖向 样式二-close-个人中心
	.scrollbar-wrapper-close .el-menu-vertical-2>.el-menu-item.user>.el-tooltip {
				cursor: pointer;
				padding: 0;
				color: #fff;
				white-space: nowrap;
				font-size: inherit;
				border-color: rgba(255, 255, 255, 0.23);
				background: rgba(0, 0, 0, 0.1);
				width: 100%;
				border-width: 0 0 0px;
				position: relative;
				border-style: solid;
				text-align: center;
				height: auto;
			}
	
	.scrollbar-wrapper-close .el-menu-vertical-2>.el-menu-item.user>.el-tooltip:hover {
				color: #fff;
				background: rgba(0, 0, 0, 0.2);
			}
	
	.scrollbar-wrapper-close .el-menu-vertical-2>.el-menu-item.user.is-active>.el-tooltip {
				color: #fff;
				background: rgba(0, 0, 0, 0.2);
			}
	
	.scrollbar-wrapper-close .el-menu-vertical-2 .el-submenu.user /deep/ .el-submenu__title {
				cursor: pointer !important;
				padding: 0 !important;
				color: #fff !important;
				white-space: nowrap !important;
				font-size: inherit !important;
				border-color: rgba(255, 255, 255, 0.23) !important;
				background: rgba(0, 0, 0, 0.1) !important;
				width: 100% !important;
				border-width: 0 0 0px !important;
				position: relative !important;
				border-style: solid !important;
				text-align: center !important;
				height: auto !important;
			}
	
	.scrollbar-wrapper-close .el-menu-vertical-2 .el-submenu.user /deep/ .el-submenu__title:hover {
				color: #fff !important;
				background: rgba(0, 0, 0, 0.2) !important;
			}
	
	.scrollbar-wrapper-close .el-menu-vertical-2 .el-submenu.user /deep/ .el-submenu__title .iconfont {
				margin: 0 auto;
				color: inherit;
				display: inline-block;
				vertical-align: middle;
				width: 24px;
				font-size: 24px;
				text-align: center;
			}
	
	.scrollbar-wrapper-close .el-menu-vertical-2 .el-submenu.user /deep/ .el-submenu__title .el-submenu__icon-arrow {
				margin: -7px 0 0 0;
				top: 50%;
				color: inherit;
				display: none;
				vertical-align: middle;
				font-size: 12px;
				position: absolute;
				right: 20px;
			}
	
	.scrollbar-wrapper-close .el-menu-vertical-2 .el-submenu.user .el-menu {
				border: none;
				border-radius: 0px;
				padding: 0;
				left: -5px;
				background: none;
				font-size: inherit;
			}
	
	.scrollbar-wrapper-close .el-menu-vertical-2 .el-submenu.user .el-menu--vertical.user .el-menu-item {
				padding: 0 0px;
				color: #fff;
				background: #000;
				font-size: 14px;
				border-color: #ffd0da;
				border-width: 0px 0;
				line-height: auto;
				border-style: solid;
				text-align: center;
				height: auto;
			}
	
	.scrollbar-wrapper-close .el-menu-vertical-2 .el-submenu.user .el-menu--vertical.user .el-menu-item:hover {
				padding: 0 0px;
				color: #fff;
				background: #222!important;
				border-color: #fbafbf;
				border-width: 0px 0;
				line-height: auto;
				border-style: solid;
				text-align: center;
				height: auto;
			}
	
	.scrollbar-wrapper-close .el-menu-vertical-2 .el-submenu.user .el-menu--vertical.user .el-menu-item.is-active {
				padding: 0 0px;
				color: #fff;
				background: #222!important;
				border-color: #fbafbf;
				border-width: 0px 0;
				line-height: auto;
				border-style: solid;
				text-align: center;
				height: auto;
			}
</style>
