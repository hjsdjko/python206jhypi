<template>
<div class="center-preview" :style='{"width":"68%","margin":"10px auto","position":"relative","flexWrap":"wrap","background":"transparent","display":"flex"}'>
	<div class="title" :style='{"margin":"10px 0 0","color":"#fff","textAlign":"center","background":"#000","width":"100%","fontSize":"20px","lineHeight":"2"}'>{{ title }}</div>
	
	<div class="info" :style='{"padding":"20px 40px 60px","boxShadow":"none","margin":"0 0 20px","borderRadius":"0","flexWrap":"wrap","background":"#ffffff","flexDirection":"column","display":"flex","width":"100%","position":"relative","height":"180px"}'>
		<div :style='{"borderColor":"#efefef","color":"#333","borderWidth":"0 0 1px 0","display":"none","width":"100%","lineHeight":"44px","fontSize":"15px","borderStyle":"solid","height":"44px"}'>个人信息</div>
		<div :style='{"width":"auto","borderColor":"#efefef","fontSize":0,"borderStyle":"solid","borderWidth":"0","height":"100%"}' v-if="userTableName=='yonghu'">
			<el-image :style='{"margin":"0 auto","borderColor":"#efefef","objectFit":"cover","borderRadius":"5px","borderWidth":"0 0 1px 0","display":"block","width":"100px","borderStyle":"solid","height":"100px"}' :src="sessionForm.touxiang?baseUrl + sessionForm.touxiang:require('@/assets/avator.png')" fit="cover"></el-image>
		</div>
		<div :style='{"width":"auto","borderColor":"#efefef","fontSize":0,"borderStyle":"solid","borderWidth":"0","height":"100%"}' v-if="userTableName=='qihuogongsi'">
			<el-image :style='{"margin":"0 auto","borderColor":"#efefef","objectFit":"cover","borderRadius":"5px","borderWidth":"0 0 1px 0","display":"block","width":"100px","borderStyle":"solid","height":"100px"}' :src="sessionForm.touxiang?baseUrl + sessionForm.touxiang:require('@/assets/avator.png')" fit="cover"></el-image>
		</div>
		<div :style='{"padding":"0 20px","borderColor":"#efefef","alignItems":"flex-start","borderWidth":"0","display":"flex","width":"auto","lineHeight":"1","borderStyle":"solid","height":"50%"}' v-if="userTableName=='yonghu'">
			<span class="icon iconfont icon-shouye-zhihui" :style='{"padding":"0 5px","fontSize":"14px","color":"#333","display":"none"}'></span>
			<div :style='{"color":"#333","fontSize":"14px","display":"none"}'>用户名</div>
			<div :style='{"fontSize":"18px","color":"#000","textAlign":"left","flex":1,"fontWeight":"bold"}'>{{sessionForm.yonghuming}}</div>
		</div>
		<div :style='{"padding":"0 20px","borderColor":"#efefef","alignItems":"flex-start","borderWidth":"0","display":"flex","width":"100%","lineHeight":"1","borderStyle":"solid","height":"50%"}' v-if="userTableName=='yonghu'">
			<span class="icon iconfont icon-shouye-zhihui" :style='{"padding":"0 5px","fontSize":"14px","color":"#333","display":"none"}'></span>
			<div :style='{"color":"#9e9e9e","padding":"0 6px 0 0","fontSize":"14px"}'>姓名</div>
			<div :style='{"fontSize":"14px","color":"#000","textAlign":"left","flex":1}'>{{sessionForm.xingming}}</div>
		</div>
		<div :style='{"padding":"0 0","borderColor":"#efefef","alignItems":"center","bottom":"6px","display":"flex","justifyContent":"center","left":"0","borderWidth":"0","width":"calc(100% / 3)","lineHeight":"40px","position":"absolute","borderStyle":"solid","height":"auto"}' v-if="userTableName=='yonghu'">
			<span class="icon iconfont icon-baohuhaoma" :style='{"padding":"0 5px","margin":"0 16px 0 0","color":"#fff","borderRadius":"50%","textAlign":"center","background":"#000","width":"30px","fontSize":"14px","lineHeight":"30px","height":"30px"}'></span>
			<div :style='{"color":"#333","fontSize":"14px","display":"none"}'>性别</div>
			<div :style='{"color":"#333","width":"auto","fontSize":"14px"}'>{{sessionForm.xingbie}}</div>
		</div>
		<div :style='{"padding":"0 0","borderColor":"#efefef","alignItems":"center","bottom":"6px","display":"flex","justifyContent":"center","left":"calc(100% / 3)","borderWidth":"0","width":"calc(100% / 3)","lineHeight":"40px","position":"absolute","borderStyle":"solid","height":"auto"}' v-if="userTableName=='yonghu'">
			<span class="icon iconfont icon-baohuhaoma" :style='{"padding":"0 5px","margin":"0 16px 0 0","color":"#fff","borderRadius":"50%","textAlign":"center","background":"#000","width":"30px","fontSize":"14px","lineHeight":"30px","height":"30px"}'></span>
			<div :style='{"color":"#333","fontSize":"14px","display":"none"}'>年龄</div>
			<div :style='{"color":"#333","textAlign":"left","fontSize":"14px"}'>{{sessionForm.nianling}}</div>
		</div>
		<div :style='{"padding":"0 0","borderColor":"#efefef","alignItems":"center","bottom":"6px","display":"flex","justifyContent":"center","left":"calc(200% / 3)","borderWidth":"0","width":"calc(100% / 3)","lineHeight":"40px","position":"absolute","borderStyle":"solid","height":"auto"}' v-if="userTableName=='yonghu'">
			<span class="icon iconfont icon-baohuhaoma" :style='{"padding":"0 5px","margin":"0 16px 0 0","color":"#fff","borderRadius":"50%","textAlign":"center","background":"#000","width":"30px","fontSize":"14px","lineHeight":"30px","height":"30px"}'></span>
			<div :style='{"color":"#333","fontSize":"14px","display":"none"}'>邮箱</div>
			<div :style='{"color":"#333","textAlign":"left","fontSize":"14px"}'>{{sessionForm.youxiang}}</div>
		</div>
		<div :style='{"padding":"0 20px","borderColor":"#efefef","borderWidth":"0 0 1px 0","display":"none","width":"100%","lineHeight":"40px","borderStyle":"solid","height":"auto"}' v-if="userTableName=='yonghu'">
			<span class="icon iconfont icon-shouye-zhihui" :style='{"color":"#333","padding":"0 5px","fontSize":"14px"}'></span>
			<div :style='{"color":"#333","fontSize":"14px"}'>手机</div>
			<div :style='{"fontSize":"14px","color":"#333","textAlign":"right","flex":1}'>{{sessionForm.shouji}}</div>
		</div>
		<div :style='{"padding":"0 20px","borderColor":"#efefef","alignItems":"flex-start","borderWidth":"0","display":"flex","width":"auto","lineHeight":"1","borderStyle":"solid","height":"50%"}' v-if="userTableName=='qihuogongsi'">
			<span class="icon iconfont icon-shouye-zhihui" :style='{"padding":"0 5px","fontSize":"14px","color":"#333","display":"none"}'></span>
			<div :style='{"color":"#333","fontSize":"14px","display":"none"}'>账号</div>
			<div :style='{"fontSize":"18px","color":"#000","textAlign":"left","flex":1,"fontWeight":"bold"}'>{{sessionForm.zhanghao}}</div>
		</div>
		<div :style='{"padding":"0 20px","borderColor":"#efefef","alignItems":"flex-start","borderWidth":"0","display":"flex","width":"100%","lineHeight":"1","borderStyle":"solid","height":"50%"}' v-if="userTableName=='qihuogongsi'">
			<span class="icon iconfont icon-shouye-zhihui" :style='{"padding":"0 5px","fontSize":"14px","color":"#333","display":"none"}'></span>
			<div :style='{"color":"#9e9e9e","padding":"0 6px 0 0","fontSize":"14px"}'>负责人姓名</div>
			<div :style='{"fontSize":"14px","color":"#000","textAlign":"left","flex":1}'>{{sessionForm.fuzerenxingming}}</div>
		</div>
		<div :style='{"padding":"0 0","borderColor":"#efefef","alignItems":"center","bottom":"6px","display":"flex","justifyContent":"center","left":"0","borderWidth":"0","width":"calc(100% / 3)","lineHeight":"40px","position":"absolute","borderStyle":"solid","height":"auto"}' v-if="userTableName=='qihuogongsi'">
			<span class="icon iconfont icon-baohuhaoma" :style='{"padding":"0 5px","margin":"0 16px 0 0","color":"#fff","borderRadius":"50%","textAlign":"center","background":"#000","width":"30px","fontSize":"14px","lineHeight":"30px","height":"30px"}'></span>
			<div :style='{"color":"#333","fontSize":"14px","display":"none"}'>性别</div>
			<div :style='{"color":"#333","width":"auto","fontSize":"14px"}'>{{sessionForm.xingbie}}</div>
		</div>
		<div :style='{"padding":"0 0","borderColor":"#efefef","alignItems":"center","bottom":"6px","display":"flex","justifyContent":"center","left":"calc(100% / 3)","borderWidth":"0","width":"calc(100% / 3)","lineHeight":"40px","position":"absolute","borderStyle":"solid","height":"auto"}' v-if="userTableName=='qihuogongsi'">
			<span class="icon iconfont icon-baohuhaoma" :style='{"padding":"0 5px","margin":"0 16px 0 0","color":"#fff","borderRadius":"50%","textAlign":"center","background":"#000","width":"30px","fontSize":"14px","lineHeight":"30px","height":"30px"}'></span>
			<div :style='{"color":"#333","fontSize":"14px","display":"none"}'>公司名称</div>
			<div :style='{"color":"#333","textAlign":"left","fontSize":"14px"}'>{{sessionForm.gongsimingcheng}}</div>
		</div>
		<div :style='{"padding":"0 0","borderColor":"#efefef","alignItems":"center","bottom":"6px","display":"flex","justifyContent":"center","left":"calc(200% / 3)","borderWidth":"0","width":"calc(100% / 3)","lineHeight":"40px","position":"absolute","borderStyle":"solid","height":"auto"}' v-if="userTableName=='qihuogongsi'">
			<span class="icon iconfont icon-baohuhaoma" :style='{"padding":"0 5px","margin":"0 16px 0 0","color":"#fff","borderRadius":"50%","textAlign":"center","background":"#000","width":"30px","fontSize":"14px","lineHeight":"30px","height":"30px"}'></span>
			<div :style='{"color":"#333","fontSize":"14px","display":"none"}'>邮箱</div>
			<div :style='{"color":"#333","textAlign":"left","fontSize":"14px"}'>{{sessionForm.youxiang}}</div>
		</div>
		<div :style='{"padding":"0 20px","borderColor":"#efefef","borderWidth":"0 0 1px 0","display":"none","width":"100%","lineHeight":"40px","borderStyle":"solid","height":"auto"}' v-if="userTableName=='qihuogongsi'">
			<span class="icon iconfont icon-shouye-zhihui" :style='{"color":"#333","padding":"0 5px","fontSize":"14px"}'></span>
			<div :style='{"color":"#333","fontSize":"14px"}'>手机</div>
			<div :style='{"fontSize":"14px","color":"#333","textAlign":"right","flex":1}'>{{sessionForm.lianxidianhua}}</div>
		</div>
		
	</div>
	
    <el-tabs tab-position="left" :style='{"border":"1px solid #ddd","width":"100%","flexWrap":"wrap","background":"transparent","display":"flex","height":"auto"}' @tab-click="handleClick">
      <el-tab-pane label="个人中心">
        <el-form class="center-preview-pv" ref="sessionForm" :model="sessionForm" :rules="rules" label-width="80px">
          <el-form-item :style='{"width":"auto","padding":"10px","margin":"0 0 10px","background":"transparent","display":"inline-block"}' v-if="userTableName=='yonghu'" label="用户名" prop="yonghuming">
            <el-input v-model="sessionForm.yonghuming" placeholder="用户名" readonly></el-input>
          </el-form-item>
          <el-form-item :style='{"width":"auto","padding":"10px","margin":"0 0 10px","background":"transparent","display":"inline-block"}' v-if="userTableName=='yonghu'" label="密码" prop="mima">
            <el-input type="password" v-model="sessionForm.mima" placeholder="密码"></el-input>
          </el-form-item>
          <el-form-item :style='{"width":"auto","padding":"10px","margin":"0 0 10px","background":"transparent","display":"inline-block"}' v-if="userTableName=='yonghu'" label="姓名" prop="xingming">
            <el-input v-model="sessionForm.xingming" placeholder="姓名" ></el-input>
          </el-form-item>
          <el-form-item :style='{"width":"auto","padding":"10px","margin":"0 0 10px","background":"transparent","display":"inline-block"}' v-if="userTableName=='yonghu'" label="性别">
            <el-select v-model="sessionForm.xingbie" placeholder="请选择性别" >
              <el-option v-for="(item, index) in dynamicProp.xingbie" :key="index" :label="item" :value="item"></el-option>
            </el-select>
          </el-form-item>
          <el-form-item :style='{"width":"auto","padding":"10px","margin":"0 0 10px","background":"transparent","display":"inline-block"}' v-if="userTableName=='yonghu'" label="头像">
			<file-upload
			tip="点击上传头像"
			action="file/upload"
			:limit="1"
			:multiple="true"
			:fileUrls="sessionForm.touxiang?sessionForm.touxiang:''"
			@change="yonghutouxiangHandleAvatarSuccess"
			></file-upload>
          </el-form-item>
          <el-form-item :style='{"width":"auto","padding":"10px","margin":"0 0 10px","background":"transparent","display":"inline-block"}' v-if="userTableName=='yonghu'" label="年龄" prop="nianling">
            <el-input v-model="sessionForm.nianling" placeholder="年龄" ></el-input>
          </el-form-item>
          <el-form-item :style='{"width":"auto","padding":"10px","margin":"0 0 10px","background":"transparent","display":"inline-block"}' v-if="userTableName=='yonghu'" label="邮箱" prop="youxiang">
            <el-input v-model="sessionForm.youxiang" placeholder="邮箱" ></el-input>
          </el-form-item>
          <el-form-item :style='{"width":"auto","padding":"10px","margin":"0 0 10px","background":"transparent","display":"inline-block"}' v-if="userTableName=='yonghu'" label="手机" prop="shouji">
            <el-input v-model="sessionForm.shouji" placeholder="手机" ></el-input>
          </el-form-item>
          <el-form-item :style='{"width":"auto","padding":"10px","margin":"0 0 10px","background":"transparent","display":"inline-block"}' v-if="userTableName=='yonghu'" label="账户卡号">
            <el-select v-model="sessionForm.kahao" placeholder="请选择账户卡号" disabled>
              <el-option v-for="(item, index) in dynamicProp.kahao" :key="index" :label="item" :value="item"></el-option>
            </el-select>
          </el-form-item>
          <el-form-item :style='{"width":"auto","padding":"10px","margin":"0 0 10px","background":"transparent","display":"inline-block"}' v-if="userTableName=='yonghu'" label="金额" prop="jine">
            <el-input v-model="sessionForm.jine" placeholder="金额" readonly></el-input>
          </el-form-item>
          <el-form-item :style='{"width":"auto","padding":"10px","margin":"0 0 10px","background":"transparent","display":"inline-block"}' v-if="userTableName=='qihuogongsi'" label="账号" prop="zhanghao">
            <el-input v-model="sessionForm.zhanghao" placeholder="账号" readonly></el-input>
          </el-form-item>
          <el-form-item :style='{"width":"auto","padding":"10px","margin":"0 0 10px","background":"transparent","display":"inline-block"}' v-if="userTableName=='qihuogongsi'" label="密码" prop="mima">
            <el-input type="password" v-model="sessionForm.mima" placeholder="密码"></el-input>
          </el-form-item>
          <el-form-item :style='{"width":"auto","padding":"10px","margin":"0 0 10px","background":"transparent","display":"inline-block"}' v-if="userTableName=='qihuogongsi'" label="负责人姓名" prop="fuzerenxingming">
            <el-input v-model="sessionForm.fuzerenxingming" placeholder="负责人姓名" ></el-input>
          </el-form-item>
          <el-form-item :style='{"width":"auto","padding":"10px","margin":"0 0 10px","background":"transparent","display":"inline-block"}' v-if="userTableName=='qihuogongsi'" label="性别">
            <el-select v-model="sessionForm.xingbie" placeholder="请选择性别" >
              <el-option v-for="(item, index) in dynamicProp.xingbie" :key="index" :label="item" :value="item"></el-option>
            </el-select>
          </el-form-item>
          <el-form-item :style='{"width":"auto","padding":"10px","margin":"0 0 10px","background":"transparent","display":"inline-block"}' v-if="userTableName=='qihuogongsi'" label="头像">
			<file-upload
			tip="点击上传头像"
			action="file/upload"
			:limit="1"
			:multiple="true"
			:fileUrls="sessionForm.touxiang?sessionForm.touxiang:''"
			@change="qihuogongsitouxiangHandleAvatarSuccess"
			></file-upload>
          </el-form-item>
          <el-form-item :style='{"width":"auto","padding":"10px","margin":"0 0 10px","background":"transparent","display":"inline-block"}' v-if="userTableName=='qihuogongsi'" label="公司名称" prop="gongsimingcheng">
            <el-input v-model="sessionForm.gongsimingcheng" placeholder="公司名称" ></el-input>
          </el-form-item>
          <el-form-item :style='{"width":"auto","padding":"10px","margin":"0 0 10px","background":"transparent","display":"inline-block"}' v-if="userTableName=='qihuogongsi'" label="邮箱" prop="youxiang">
            <el-input v-model="sessionForm.youxiang" placeholder="邮箱" ></el-input>
          </el-form-item>
          <el-form-item :style='{"width":"auto","padding":"10px","margin":"0 0 10px","background":"transparent","display":"inline-block"}' v-if="userTableName=='qihuogongsi'" label="手机" prop="lianxidianhua">
            <el-input v-model="sessionForm.lianxidianhua" placeholder="手机" ></el-input>
          </el-form-item>
          <el-form-item :style='{"width":"auto","padding":"10px","margin":"0 0 10px","background":"transparent","display":"inline-block"}' v-if="userTableName=='qihuogongsi'" label="公司简介" prop="gongsijianjie">
            <el-input v-model="sessionForm.gongsijianjie" placeholder="公司简介" ></el-input>
          </el-form-item>
          <el-form-item :style='{"padding":"0","margin":"0"}'>
            <el-button :style='{"border":"0","cursor":"pointer","padding":"6px 10px","margin":"0 20px 0 0","outline":"none","color":"rgba(255, 255, 255, 1)","borderRadius":"4px","background":"#000","width":"auto","fontSize":"16px","height":"auto"}' type="primary" @click="onSubmit('sessionForm')">更新信息</el-button>
            <el-button :style='{"border":"0px solid rgba(64, 158, 255, 1)","cursor":"pointer","padding":"6px 16px","margin":"0","outline":"none","color":"#fff","borderRadius":"4px","background":"#9E9E9E","width":"auto","fontSize":"16px","height":"auto"}' type="danger" @click="logout">退出登录</el-button>
          </el-form-item>
        </el-form>
      </el-tab-pane>
		<el-tab-pane v-for="(item,index) in menuList" :key="index" v-if="hasBack(item.menu)" :label="item.child[0].menu" :name="item.child[0].tableName"></el-tab-pane>
	  
      <el-tab-pane label="我的收藏"></el-tab-pane>
    </el-tabs>
</div>
</template>

<script>
  import config from '@/config/config'
  import menu from '@/config/menu'
  import Vue from 'vue'
  export default {
    //数据集合
    data() {
      return {
        title: '个人中心',
        baseUrl: config.baseUrl,
        sessionForm: {},
        rules: {},
		menuList: [],
        disabled: false,
        uploadUrl: config.baseUrl + 'file/upload',
        imageUrl: '',
        headers: {Token: localStorage.getItem('Token')},
        userTableName: localStorage.getItem('UserTableName'),
        dynamicProp: {}
      }
    },
    created() {
		let menus = menu.list()
		for(let x in menus){
			if(menus[x].tableName == this.userTableName){
				this.menuList = menus[x].backMenu
			}
		}
		if ('yonghu' == this.userTableName) {
			this.$set(this.sessionForm, 'yonghuming', null);
		}
		if ('yonghu' == this.userTableName) {
			this.$set(this.sessionForm, 'mima', null);
		}
		if ('yonghu' == this.userTableName) {
			this.$set(this.sessionForm, 'xingming', null);
		}
		if ('yonghu' == this.userTableName) {
			this.$set(this.sessionForm, 'xingbie', null);
		}
		if ('yonghu' == this.userTableName) {
			this.$set(this.sessionForm, 'touxiang', null);
		}
		if ('yonghu' == this.userTableName) {
			this.$set(this.sessionForm, 'nianling', null);
		}
		if ('yonghu' == this.userTableName) {
			this.$set(this.sessionForm, 'youxiang', null);
		}
		if ('yonghu' == this.userTableName) {
			this.$set(this.sessionForm, 'shouji', null);
		}
		if ('yonghu' == this.userTableName) {
			this.$set(this.sessionForm, 'kahao', null);
		}
		if ('yonghu' == this.userTableName) {
			this.$set(this.sessionForm, 'jine', null);
		}
		if ('qihuogongsi' == this.userTableName) {
			this.$set(this.sessionForm, 'zhanghao', null);
		}
		if ('qihuogongsi' == this.userTableName) {
			this.$set(this.sessionForm, 'mima', null);
		}
		if ('qihuogongsi' == this.userTableName) {
			this.$set(this.sessionForm, 'fuzerenxingming', null);
		}
		if ('qihuogongsi' == this.userTableName) {
			this.$set(this.sessionForm, 'xingbie', null);
		}
		if ('qihuogongsi' == this.userTableName) {
			this.$set(this.sessionForm, 'touxiang', null);
		}
		if ('qihuogongsi' == this.userTableName) {
			this.$set(this.sessionForm, 'gongsimingcheng', null);
		}
		if ('qihuogongsi' == this.userTableName) {
			this.$set(this.sessionForm, 'youxiang', null);
		}
		if ('qihuogongsi' == this.userTableName) {
			this.$set(this.sessionForm, 'lianxidianhua', null);
		}
		if ('qihuogongsi' == this.userTableName) {
			this.$set(this.sessionForm, 'gongsijianjie', null);
		}

      if ('yonghu' == this.userTableName) {
        this.$set(this.rules, 'yonghuming', [{ required: true, message: '请输入用户名', trigger: 'blur' }]);
      }
      if ('yonghu' == this.userTableName) {
        this.$set(this.rules, 'mima', [{ required: true, message: '请输入密码', trigger: 'blur' }]);
      }
			if ('yonghu' == this.userTableName) {
        this.$set(this.rules, 'nianling', [{ required: false, validator: this.$validate.isIntNumer, trigger: 'blur' }]);
      }
			if ('yonghu' == this.userTableName) {
        this.$set(this.rules, 'youxiang', [{ required: false, validator: this.$validate.isEmail, trigger: 'blur' }]);
      }
			if ('yonghu' == this.userTableName) {
        this.$set(this.rules, 'shouji', [{ required: false, validator: this.$validate.isMobile, trigger: 'blur' }]);
      }
      if ('yonghu' == this.userTableName) {
        this.$set(this.rules, 'jine', [{ required: true, message: '请输入金额', trigger: 'blur' }]);
      }
			if ('yonghu' == this.userTableName) {
        this.$set(this.rules, 'jine', [{ required: false, validator: this.$validate.isNumber, trigger: 'blur' }]);
      }
      if ('qihuogongsi' == this.userTableName) {
        this.$set(this.rules, 'zhanghao', [{ required: true, message: '请输入账号', trigger: 'blur' }]);
      }
      if ('qihuogongsi' == this.userTableName) {
        this.$set(this.rules, 'mima', [{ required: true, message: '请输入密码', trigger: 'blur' }]);
      }
      if ('qihuogongsi' == this.userTableName) {
        this.$set(this.rules, 'fuzerenxingming', [{ required: true, message: '请输入负责人姓名', trigger: 'blur' }]);
      }
			if ('qihuogongsi' == this.userTableName) {
        this.$set(this.rules, 'youxiang', [{ required: false, validator: this.$validate.isEmail, trigger: 'blur' }]);
      }
			if ('qihuogongsi' == this.userTableName) {
        this.$set(this.rules, 'lianxidianhua', [{ required: false, validator: this.$validate.isMobile, trigger: 'blur' }]);
      }

      this.init();
      this.sessionForm = JSON.parse(localStorage.getItem('sessionForm'))
    },
    //方法集合
    methods: {
      init() {
        if ('yonghu' == this.userTableName) {
          this.dynamicProp.xingbie = '男,女'.split(',');
        }
        if ('yonghu' == this.userTableName) {
          this.$http.get('option/kaihuxinxi/zhanghukahao', {emulateJSON: true}).then(res => {
            if (res.data.code == 0) {
              this.dynamicProp.kahao = res.data.data;
			  this.$forceUpdate()
            }
          });
        }
        if ('qihuogongsi' == this.userTableName) {
          this.dynamicProp.xingbie = '男,女'.split(',');
        }
      },
	  setSession(){
		  localStorage.setItem('sessionForm',JSON.stringify(this.sessionForm))
	  },
      onSubmit(formName) {
		if(`yonghu` == this.userTableName && this.sessionForm.touxiang!=null){
			this.sessionForm.touxiang = this.sessionForm.touxiang.replace(new RegExp(this.$config.baseUrl,"g"),"");
		}
		if(`qihuogongsi` == this.userTableName && this.sessionForm.touxiang!=null){
			this.sessionForm.touxiang = this.sessionForm.touxiang.replace(new RegExp(this.$config.baseUrl,"g"),"");
		}
        this.$refs[formName].validate((valid) => {
			if (valid) {
				this.$http.post(this.userTableName + '/update', this.sessionForm).then(res => {
					if (res.data.code == 0) {
						this.setSession()
						this.$message({
							message: '更新成功',
							type: 'success',
							duration: 1500
						});
					}
				});
			} else {
				return false;
			}
        });
      },
      yonghutouxiangHandleAvatarSuccess(fileUrls) {
        this.sessionForm.touxiang = fileUrls;
      },
      qihuogongsitouxiangHandleAvatarSuccess(fileUrls) {
        this.sessionForm.touxiang = fileUrls;
      },
      handleClick(tab, event) {
        switch(event.target.outerText) {
          case '个人中心':
            tab.$router.push('/index/center');
            break;
          case '我的收藏':
            localStorage.setItem('storeupType', 1);
            tab.$router.push('/index/storeup');
            break;
		  default:
		  	tab.$router.push(`/index/${tab.name}?centerType=1`);
        }

        this.title = event.target.outerText;
      },
      logout() {
        localStorage.clear();
        Vue.http.headers.common['Token'] = "";
        this.$router.push('/index/home');
        this.activeIndex = '0'
        localStorage.setItem('keyPath', this.activeIndex)
        this.$forceUpdate()
        this.$message({
            message: '登出成功',
            type: 'success',
            duration: 1500,
        });
      },
	  hasBack(name){
		  switch(name){
			case '我的收藏管理':
				return false
				break;
			default:
				return true
		  }
	  }
    }
  }
</script>

<style rel="stylesheet/scss" lang="scss" scoped>
  .center-preview {
  
    .el-tabs {
      & /deep/ .el-tabs__header {
        .el-tabs__nav-wrap {
          margin: 0;
  
          &::after {
            content: none;
          }
        }
  
        .el-tabs__active-bar {
          display: none !important;
        }
      }
  
      .center-preview-pv {
        .el-date-editor.el-input {
          width: auto;
        }
  
        .balance {
          .el-input {
            width: auto;
          }
        }
      }
    }
  }
  
  .center-preview .el-tabs /deep/ .el-tabs__header {
	padding: 10px 0;
	margin: 0;
	background: transparent;
	width: auto;
	border-color: #eee;
	border-width: 0;
	position: relative;
	border-style: solid;
	height: auto;
  }
  
  .center-preview .el-tabs /deep/ .el-tabs__header .el-tabs__item {
  	border: 1px solid transparent;
  	padding: 0 10px;
  	margin: 0 10px;
  	color: #9E9E9E;
  	font-weight: 500;
  	display: inline-block;
  	font-size: 14px;
  	line-height: 40px;
  	border-radius: 30px;
  	background: transparent;
  	position: relative;
  	text-align: center;
  	height: 40px;
  }
  
  .center-preview .el-tabs /deep/ .el-tabs__header .el-tabs__item:hover {
  	border: 1px solid #AD8936;
  	padding: 0 10px;
  	margin: 0 10px;
  	color: #AD8936;
  	font-weight: 500;
  	display: inline-block;
  	font-size: 14px;
  	line-height: 40px;
  	border-radius: 30px;
  	background: transparent;
  	position: relative;
  	text-align: center;
  	height: 40px;
  }
  
  .center-preview .el-tabs /deep/ .el-tabs__header .el-tabs__item.is-active {
  	border: 1px solid #AD8936;
  	padding: 0 10px;
  	margin: 0 10px;
  	color: #AD8936;
  	font-weight: 500;
  	display: inline-block;
  	font-size: 14px;
  	line-height: 40px;
  	border-radius: 30px;
  	background: transparent;
  	position: relative;
  	text-align: center;
  	height: 40px;
  }
  
  .center-preview .el-tabs /deep/ .el-tabs__content .el-tab-pane {
  	padding: 10px;
  	background: transparent;
  	width: 100%;
  }
  
  .center-preview-pv .el-form-item /deep/ .el-form-item__label {
  	padding: 0 10px 0 0;
  	color: #000;
  	font-weight: 500;
  	width: 80px;
  	font-size: 14px;
  	line-height: 40px;
  	text-align: right;
  }
  
  .center-preview-pv .el-form-item .el-form-item__content {
    margin-left: 80px;
  }
  
  .center-preview-pv .el-input /deep/ .el-input__inner {
  	border: 0;
  	border-radius: 0;
  	padding: 0 12px;
  	box-shadow: none;
  	outline: none;
  	color: #000;
  	background: #fff;
  	width: 300px;
  	font-size: 14px;
  	height: 40px;
  }
  
  .center-preview-pv .el-select /deep/ .el-input__inner {
  	border: 0;
  	border-radius: 0;
  	padding: 0 12px;
  	box-shadow: none;
  	outline: none;
  	color: #000;
  	background: #fff;
  	width: 300px;
  	font-size: 14px;
  	height: 40px;
  }
  
  .center-preview-pv .el-date-editor /deep/ .el-input__inner {
  	border: 0;
  	border-radius: 0;
  	padding: 0 10px 0 30px;
  	box-shadow: none;
  	outline: none;
  	color: #000;
  	background: #fff;
  	width: 300px;
  	font-size: 14px;
  	height: 40px;
  }
  
  .center-preview-pv /deep/ .avatar-uploader-icon {
  	border: 1px dashed #000;
  	cursor: pointer;
  	border-radius: 6px;
  	color: #000;
  	background: #fff;
  	width: 120px;
  	font-size: 32px;
  	line-height: 40px;
  	text-align: center;
  	height: 40px;
  }
  
  .center-preview-pv .el-form-item.balance /deep/ .el-input__inner {
  	border: 0;
  	border-radius: 0;
  	padding: 0 12px;
  	box-shadow: none;
  	outline: none;
  	color: #000;
  	background: #fff;
  	display: inline-block;
  	width: 200px;
  	font-size: 14px;
  	height: 40px;
  }
</style>
