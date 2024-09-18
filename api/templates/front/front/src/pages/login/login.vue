<template>
<div>
	<div class="container" :style='{"minHeight":"100vh","alignItems":"center","background":"url(http://codegen.caihongy.cn/20231024/9954e3ae0f95421ea6eeee9f2a2cf1b0.png)","display":"flex","width":"100%","backgroundSize":"cover","backgroundPosition":"center center","backgroundRepeat":"no-repeat","justifyContent":"center"}'>
		<el-form ref="loginForm" :model="loginForm" :style='{"border":"1px solid #AD8936","padding":"60px 60px 80px","boxShadow":"0 0px 0px rgba(64, 158, 255, .8)","margin":"0","alignItems":"flex-start","flexDirection":"row","display":"flex","borderRadius":"0","flexWrap":"wrap","background":"url(http://codegen.caihongy.cn/20231024/00a0bca7cd9443f0b539bbefa61e51a4.png)","borderWidth":"0 0 15px","width":"80%","backgroundSize":"cover","backgroundPosition":"center center","backgroundRepeat":"no-repeat","height":"auto"}' :rules="rules">
			<div v-if="false" :style='{"margin":"0 0 10px 0","color":"rgba(64, 158, 255, 1)","textAlign":"center","width":"100%","lineHeight":"44px","fontSize":"20px","textShadow":"4px 4px 2px rgba(64, 158, 255, .5)"}'>USER / LOGIN</div>
			<div v-if="true" :style='{"margin":"0 0 50px 80px","color":"#000","textAlign":"left","width":"80%","lineHeight":"44px","fontSize":"36px","textShadow":"none","fontWeight":"bold"}'>BS23-287基于Python的期货程序化交易系统的设计与实现登录</div>
			<el-form-item v-if="loginType==1" class="list-item" :style='{"width":"80%","margin":"0 0 20px"}' prop="username">
				<div v-if="true" :style='{"width":"80px","lineHeight":"44px","fontSize":"14px","color":"#000","textAlign":"center"}'>账号：</div>
				<input :style='{"border":"2px solid #C7C7C7","padding":"0 10px","boxShadow":"0 0 0px rgba(64, 158, 255, .5)","outline":"0px solid #efefef","color":"#000","outlineOffset":"0","borderRadius":"10px","width":"400px","fontSize":"14px","height":"44px"}' v-model="loginForm.username" placeholder="请输入账户">
			</el-form-item>
			<el-form-item v-if="loginType==1" class="list-item" :style='{"width":"80%","margin":"0 0 20px"}' prop="password">
				<div v-if="true" :style='{"width":"80px","lineHeight":"44px","fontSize":"14px","color":"#000","textAlign":"center"}'>密码：</div>
				<input :style='{"border":"2px solid #C7C7C7","padding":"0 10px","boxShadow":"0 0 0px rgba(64, 158, 255, .5)","outline":"0px solid #efefef","color":"#000","outlineOffset":"0","borderRadius":"10px","width":"400px","fontSize":"14px","height":"44px"}' v-model="loginForm.password" placeholder="请输入密码" type="password">
			</el-form-item>

			<el-form-item class="list-type select" :style='{"width":"80%","margin":"0 0 20px"}' v-if="roles.length>1">
			  <el-select v-model="loginForm.tableName" placeholder="请选择角色" @change="selectChange">
				<el-option v-for="item,index in roles" :key="index" :label="item.roleName" :value="item.tableName" />
			  </el-select>
			</el-form-item>

			
			<el-form-item :style='{"width":"autoC","margin":"0px 0 0 80px","alignItems":"center","display":"flex"}'>
				<el-button v-if="loginType==1" :style='{"border":"0","cursor":"pointer","padding":"0 24px","margin":"0 5px","outline":"none","color":"#fff","borderRadius":"4px","background":"#AD8936","width":"200px","fontSize":"30px","height":"70px"}' @click="submitForm('loginForm')">登录</el-button>
				<el-button v-if="loginType==1" :style='{"border":"0","cursor":"pointer","padding":"0 10px","margin":"0 5px","outline":"none","color":"#000","borderRadius":"0","background":"transparent","width":"auto","fontSize":"14px","lineHeight":"1","height":"44px"}' @click="resetForm('loginForm')">重置</el-button>
			</el-form-item>
			<div :style='{"margin":"0 0","alignItems":"center","flexWrap":"wrap","display":"flex","width":"200px","justifyContent":"center","height":"70px"}'>
			<router-link :style='{"cursor":"pointer","margin":"0 5px","color":"#000","background":"transparent","fontSize":"14px","textDecoration":"none","lineHeight":"1"}' :to="{path: '/register', query: {role: item.tableName,pageFlag:'register'}}" v-if="item.hasFrontRegister=='是'" v-for="(item, index) in roles" :key="index">注册{{item.roleName.replace('注册','')}}</router-link>
			</div>
			<div class="idea1" :style='{"width":"100%","background":"#AD8936","display":"none","height":"15px"}'></div>
			<div class="idea2" :style='{"width":"100%","background":"blue","display":"none","height":"40px"}'></div>
		</el-form>
    </div>
</div>
</template>

<script>
import menu from '@/config/menu'
export default {
	//数据集合
	data() {
		return {
            baseUrl: this.$config.baseUrl,
            loginType: 1,
			roleMenus: [],
			loginForm: {
				username: '',
				password: '',
				tableName: '',
				code: '',
			},
			role: '',
            roles: [],
			rules: {
				username: [
					{ required: true, message: '请输入账户', trigger: 'blur' }
				],
				password: [
					{ required: true, message: '请输入密码', trigger: 'blur' }
				]
			},
			codes: [{
				num: 1,
				color: '#000',
				rotate: '10deg',
				size: '16px'
			}, {
				num: 2,
				color: '#000',
				rotate: '10deg',
				size: '16px'
			}, {
				num: 3,
				color: '#000',
				rotate: '10deg',
				size: '16px'
			}, {
				num: 4,
				color: '#000',
				rotate: '10deg',
				size: '16px'
			}],
			flag: false,
			verifyCheck2: false,
		}
	},
  components: {
  },
	created() {
		this.roleMenus = menu.list()
		for(let item in this.roleMenus) {
		    if(this.roleMenus[item].hasFrontLogin=='是') {
		        this.roles.push(this.roleMenus[item]);
		    }
		}
		
	},
	mounted() {
	},
    //方法集合
    methods: {
		randomString() {
			var len = 4;
			var chars = [
			  'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
			  'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
			  'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G',
			  'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
			  'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2',
			  '3', '4', '5', '6', '7', '8', '9'
			]
			var colors = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
			var sizes = ['14', '15', '16', '17', '18']
			
			var output = []
			for (var i = 0; i < len; i++) {
			  // 随机验证码
			  var key = Math.floor(Math.random() * chars.length)
			  this.codes[i].num = chars[key]
			  // 随机验证码颜色
			  var code = '#'
			  for (var j = 0; j < 6; j++) {
			    var key = Math.floor(Math.random() * colors.length)
			    code += colors[key]
			  }
			  this.codes[i].color = code
			  // 随机验证码方向
			  var rotate = Math.floor(Math.random() * 45)
			  var plus = Math.floor(Math.random() * 2)
			  if (plus == 1) rotate = '-' + rotate
			  this.codes[i].rotate = 'rotate(' + rotate + 'deg)'
			  // 随机验证码字体大小
			  var size = Math.floor(Math.random() * sizes.length)
			  this.codes[i].size = sizes[size] + 'px'
			}
		},
	  selectChange(e){
		  this.role = e
	  },
      submitForm(formName) {
        if (this.roles.length!=1) {
            if (!this.role) {
                this.$message.error("请选择登录用户类型");
                return false;
            }
        } else {
            this.role = this.roles[0].roleName;
            this.loginForm.tableName = this.roles[0].tableName;
        }

		this.loginPost(formName)
      },
      resetForm(formName) {
        this.$refs[formName].resetFields();
      },
	  loginPost(formName) {
		this.$refs[formName].validate((valid) => {
		  if (valid) {
		    this.$http.get(`${this.loginForm.tableName}/login`, {params: this.loginForm}).then(res => {
		      if (res.data.code === 0) {
		        localStorage.setItem('Token', res.data.token);
		        localStorage.setItem('UserTableName', this.loginForm.tableName);
		        localStorage.setItem('username', this.loginForm.username);
		        localStorage.setItem('adminName', this.loginForm.username);
		        localStorage.setItem('sessionTable', this.loginForm.tableName);
		        localStorage.setItem('role', this.role);
		        localStorage.setItem('keyPath', 0);
		        this.$router.push('/');
		        this.$message({
		          message: '登录成功',
		          type: 'success',
		          duration: 1500,
		        });
		      } else {
		        this.$message.error(res.data.msg);
		      }
		    });
		  } else {
		    return false;
		  }
		});
	  },
    }
  }
</script>

<style rel="stylesheet/scss" lang="scss" scoped>
	.container {
		position: relative;
		background: url(http://codegen.caihongy.cn/20231024/9954e3ae0f95421ea6eeee9f2a2cf1b0.png);
		
		.el-form-item {
		  & /deep/ .el-form-item__content {
		    width: 100%;
		  }
		}
		
		.list-item /deep/ .el-form-item__content {
			display: flex;
		}

		.list-code /deep/ .el-form-item__content {
			display: flex;
		}

		.list-type /deep/ .el-form-item__content {
			display: flex;
		}

		.list-btn /deep/ .el-form-item__content {
			display: flex;
			justify-content: center;
			align-items: center;
		}
		
		.list-item /deep/ .el-input .el-input__inner {
			border: 2px solid #C7C7C7;
			border-radius: 10px;
			padding: 0 10px;
			box-shadow: 0 0 0px rgba(64, 158, 255, .5);
			outline: 0px solid #efefef;
			color: #000;
			width: 400px;
			font-size: 14px;
			outline-offset: 0;
			height: 44px;
		}
		
		.list-code /deep/ .el-input .el-input__inner {
			border: 2px solid #C7C7C7;
			border-radius: 10px 0 0 10px;
			padding: 0 10px;
			outline: none;
			color: #000;
			display: inline-block;
			vertical-align: middle;
			width: 300px;
			font-size: 14px;
			border-width: 2px 0 2px 2px;
			height: 44px;
		}

		// select
		.list-type.select .el-select /deep/ .el-input__inner {
			border: 2px solid #C7C7C7;
			border-radius: 10px;
			padding: 0 10px;
			box-shadow: 0 0 0px rgba(64, 158, 255, .5);
			margin: 0 0 0 80px;
			color: #000;
			width: 400px;
			font-size: 14px;
			height: 44px;
		}
	}

</style>
