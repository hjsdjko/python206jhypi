<template>
	<div>

	<div class="container" :style='{"minHeight":"100vh","alignItems":"center","background":"url(http://codegen.caihongy.cn/20231024/6a72ed211ce4490abbbb49e6c6f05331.png)","display":"flex","width":"100%","backgroundSize":"cover","backgroundPosition":"center center","backgroundRepeat":"no-repeat","justifyContent":"center"}'>
		<el-form class='rgs-form' v-if="pageFlag=='register'" :style='{"padding":"60px","boxShadow":"0 0px 0px rgba(64, 158, 255, .8)","margin":"0","alignItems":"flex-start","flexDirection":"row","display":"flex","borderRadius":"10px","flexWrap":"wrap","background":"url(http://codegen.caihongy.cn/20231024/7cc60785ed50483986e084eddbdc0137.png)","width":"80%","backgroundSize":"cover","backgroundPosition":"center center","backgroundRepeat":"no-repeat","height":"auto"}' ref="registerForm" :model="registerForm" :rules="rules">
			<div v-if="false" :style='{"margin":"0 0 10px 0","color":"rgba(64, 158, 255, 1)","textAlign":"center","width":"100%","lineHeight":"44px","fontSize":"20px","textShadow":"4px 4px 2px rgba(64, 158, 255, .5)"}'>USER / REGISTER</div>
			<div v-if="true" :style='{"margin":"0 0 0 80px","color":"#000","textAlign":"left","width":"100%","lineHeight":"44px","fontSize":"36px","textShadow":"none"}'>BS23-287基于Python的期货程序化交易系统的设计与实现注册</p></div>
			<el-form-item :style='{"width":"100%","padding":"0","margin":"15px 0 0","height":"auto"}' v-if="tableName=='yonghu'" prop="yonghuming">
				<div v-if="true" :style='{"width":"80px","lineHeight":"44px","fontSize":"14px","color":"#000","textAlign":"center"}' :class="changeRules('yonghuming')?'required':''">用户名：</div>
				<el-input v-model="registerForm.yonghuming"  placeholder="请输入用户名" />
			</el-form-item>
			<el-form-item :style='{"width":"100%","padding":"0","margin":"15px 0 0","height":"auto"}' v-if="tableName=='yonghu'" prop="mima">
				<div v-if="true" :style='{"width":"80px","lineHeight":"44px","fontSize":"14px","color":"#000","textAlign":"center"}' :class="changeRules('mima')?'required':''">密码：</div>
				<el-input v-model="registerForm.mima" type="password" placeholder="请输入密码" />
			</el-form-item>
			<el-form-item :style='{"width":"100%","padding":"0","margin":"15px 0 0","height":"auto"}' v-if="tableName=='yonghu'" prop="mima">
				<div v-if="true" :style='{"width":"80px","lineHeight":"44px","fontSize":"14px","color":"#000","textAlign":"center"}' :class="changeRules('mima')?'required':''">确认密码：</div>
				<el-input v-model="registerForm.mima2" type="password" placeholder="请再次输入密码" />
			</el-form-item>
			<el-form-item :style='{"width":"100%","padding":"0","margin":"15px 0 0","height":"auto"}' v-if="tableName=='yonghu'" prop="xingming">
				<div v-if="true" :style='{"width":"80px","lineHeight":"44px","fontSize":"14px","color":"#000","textAlign":"center"}' :class="changeRules('xingming')?'required':''">姓名：</div>
				<el-input v-model="registerForm.xingming"  placeholder="请输入姓名" />
			</el-form-item>
			<el-form-item :style='{"width":"100%","padding":"0","margin":"15px 0 0","height":"auto"}' v-if="tableName=='yonghu'" prop="xingbie">
				<div v-if="true" :style='{"width":"80px","lineHeight":"44px","fontSize":"14px","color":"#000","textAlign":"center"}' :class="changeRules('xingbie')?'required':''">性别：</div>
                <el-select v-model="registerForm.xingbie" placeholder="请选择性别" >
                  <el-option
                      v-for="(item,index) in yonghuxingbieOptions"
                      :key="index"
                      :label="item"
                      :value="item">
                  </el-option>
                </el-select>
			</el-form-item>
			<el-form-item :style='{"width":"100%","padding":"0","margin":"15px 0 0","height":"auto"}' v-if="tableName=='yonghu'" prop="touxiang">
				<div v-if="true" :style='{"width":"80px","lineHeight":"44px","fontSize":"14px","color":"#000","textAlign":"center"}' :class="changeRules('touxiang')?'required':''">头像：</div>
                <file-upload
					tip="点击上传头像"
					action="file/upload"
					:limit="1"
					:multiple="true"
					:fileUrls="registerForm.touxiang?registerForm.touxiang:''"
					@change="yonghutouxiangUploadChange"
				></file-upload>
			</el-form-item>
			<el-form-item :style='{"width":"100%","padding":"0","margin":"15px 0 0","height":"auto"}' v-if="tableName=='yonghu'" prop="nianling">
				<div v-if="true" :style='{"width":"80px","lineHeight":"44px","fontSize":"14px","color":"#000","textAlign":"center"}' :class="changeRules('nianling')?'required':''">年龄：</div>
				<el-input v-model="registerForm.nianling"  placeholder="请输入年龄" />
			</el-form-item>
			<el-form-item :style='{"width":"100%","padding":"0","margin":"15px 0 0","height":"auto"}' v-if="tableName=='yonghu'" prop="youxiang">
				<div v-if="true" :style='{"width":"80px","lineHeight":"44px","fontSize":"14px","color":"#000","textAlign":"center"}' :class="changeRules('youxiang')?'required':''">邮箱：</div>
				<el-input v-model="registerForm.youxiang"  placeholder="请输入邮箱" />
			</el-form-item>
			<el-form-item :style='{"width":"100%","padding":"0","margin":"15px 0 0","height":"auto"}' v-if="tableName=='yonghu'" prop="shouji">
				<div v-if="true" :style='{"width":"80px","lineHeight":"44px","fontSize":"14px","color":"#000","textAlign":"center"}' :class="changeRules('shouji')?'required':''">手机：</div>
				<el-input v-model="registerForm.shouji"  placeholder="请输入手机" />
			</el-form-item>
			<el-form-item :style='{"width":"100%","padding":"0","margin":"15px 0 0","height":"auto"}' v-if="tableName=='yonghu'" prop="kahao">
				<div v-if="true" :style='{"width":"80px","lineHeight":"44px","fontSize":"14px","color":"#000","textAlign":"center"}' :class="changeRules('kahao')?'required':''">账户卡号：</div>
                <el-select v-model="registerForm.kahao" placeholder="请选择账户卡号" disabled>
                  <el-option
                      v-for="(item,index) in yonghukahaoOptions"
                      :key="index"
                      :label="item"
                      :value="item">
                  </el-option>
                </el-select>
			</el-form-item>
			<el-form-item :style='{"width":"100%","padding":"0","margin":"15px 0 0","height":"auto"}' v-if="tableName=='qihuogongsi'" prop="zhanghao">
				<div v-if="true" :style='{"width":"80px","lineHeight":"44px","fontSize":"14px","color":"#000","textAlign":"center"}' :class="changeRules('zhanghao')?'required':''">账号：</div>
				<el-input v-model="registerForm.zhanghao"  placeholder="请输入账号" />
			</el-form-item>
			<el-form-item :style='{"width":"100%","padding":"0","margin":"15px 0 0","height":"auto"}' v-if="tableName=='qihuogongsi'" prop="mima">
				<div v-if="true" :style='{"width":"80px","lineHeight":"44px","fontSize":"14px","color":"#000","textAlign":"center"}' :class="changeRules('mima')?'required':''">密码：</div>
				<el-input v-model="registerForm.mima" type="password" placeholder="请输入密码" />
			</el-form-item>
			<el-form-item :style='{"width":"100%","padding":"0","margin":"15px 0 0","height":"auto"}' v-if="tableName=='qihuogongsi'" prop="mima">
				<div v-if="true" :style='{"width":"80px","lineHeight":"44px","fontSize":"14px","color":"#000","textAlign":"center"}' :class="changeRules('mima')?'required':''">确认密码：</div>
				<el-input v-model="registerForm.mima2" type="password" placeholder="请再次输入密码" />
			</el-form-item>
			<el-form-item :style='{"width":"100%","padding":"0","margin":"15px 0 0","height":"auto"}' v-if="tableName=='qihuogongsi'" prop="fuzerenxingming">
				<div v-if="true" :style='{"width":"80px","lineHeight":"44px","fontSize":"14px","color":"#000","textAlign":"center"}' :class="changeRules('fuzerenxingming')?'required':''">负责人姓名：</div>
				<el-input v-model="registerForm.fuzerenxingming"  placeholder="请输入负责人姓名" />
			</el-form-item>
			<el-form-item :style='{"width":"100%","padding":"0","margin":"15px 0 0","height":"auto"}' v-if="tableName=='qihuogongsi'" prop="xingbie">
				<div v-if="true" :style='{"width":"80px","lineHeight":"44px","fontSize":"14px","color":"#000","textAlign":"center"}' :class="changeRules('xingbie')?'required':''">性别：</div>
                <el-select v-model="registerForm.xingbie" placeholder="请选择性别" >
                  <el-option
                      v-for="(item,index) in qihuogongsixingbieOptions"
                      :key="index"
                      :label="item"
                      :value="item">
                  </el-option>
                </el-select>
			</el-form-item>
			<el-form-item :style='{"width":"100%","padding":"0","margin":"15px 0 0","height":"auto"}' v-if="tableName=='qihuogongsi'" prop="touxiang">
				<div v-if="true" :style='{"width":"80px","lineHeight":"44px","fontSize":"14px","color":"#000","textAlign":"center"}' :class="changeRules('touxiang')?'required':''">头像：</div>
                <file-upload
					tip="点击上传头像"
					action="file/upload"
					:limit="1"
					:multiple="true"
					:fileUrls="registerForm.touxiang?registerForm.touxiang:''"
					@change="qihuogongsitouxiangUploadChange"
				></file-upload>
			</el-form-item>
			<el-form-item :style='{"width":"100%","padding":"0","margin":"15px 0 0","height":"auto"}' v-if="tableName=='qihuogongsi'" prop="gongsimingcheng">
				<div v-if="true" :style='{"width":"80px","lineHeight":"44px","fontSize":"14px","color":"#000","textAlign":"center"}' :class="changeRules('gongsimingcheng')?'required':''">公司名称：</div>
				<el-input v-model="registerForm.gongsimingcheng"  placeholder="请输入公司名称" />
			</el-form-item>
			<el-form-item :style='{"width":"100%","padding":"0","margin":"15px 0 0","height":"auto"}' v-if="tableName=='qihuogongsi'" prop="youxiang">
				<div v-if="true" :style='{"width":"80px","lineHeight":"44px","fontSize":"14px","color":"#000","textAlign":"center"}' :class="changeRules('youxiang')?'required':''">邮箱：</div>
				<el-input v-model="registerForm.youxiang"  placeholder="请输入邮箱" />
			</el-form-item>
			<el-form-item :style='{"width":"100%","padding":"0","margin":"15px 0 0","height":"auto"}' v-if="tableName=='qihuogongsi'" prop="lianxidianhua">
				<div v-if="true" :style='{"width":"80px","lineHeight":"44px","fontSize":"14px","color":"#000","textAlign":"center"}' :class="changeRules('lianxidianhua')?'required':''">手机：</div>
				<el-input v-model="registerForm.lianxidianhua"  placeholder="请输入手机" />
			</el-form-item>
			<el-button :style='{"border":"0","cursor":"pointer","padding":"0 10px","boxShadow":"0 0 0px rgba(64, 158, 255, .5)","margin":"20px 0 5px","color":"#fff","display":"block","outline":"none","borderRadius":"8px","background":"#AD8936","width":"200px","fontSize":"24px","height":"60px"}' type="primary" @click="submitForm('registerForm')">注册</el-button>
			<el-button :style='{"border":"0","cursor":"pointer","padding":"0 10px","boxShadow":"0 0 0px rgba(64, 158, 255, .5)","margin":"20px 40px 5px","color":"#AD8936","textAlign":"left","display":"block","outline":"none","borderRadius":"0","background":"transparent","width":"80%","fontSize":"15px","height":"60px"}' @click="resetForm('registerForm')">重置</el-button>
			<router-link :style='{"cursor":"pointer","padding":"0 10%","color":"#AD8936","display":"inline-block","lineHeight":"1","fontSize":"14px","textDecoration":"none"}' to="/login">已有账户登录</router-link>
			<div class="idea1" :style='{"width":"100%","background":"red","display":"none","height":"40px"}'></div>
			<div class="idea2" :style='{"width":"100%","background":"blue","display":"none","height":"40px"}'></div>
		</el-form>
    </div>
  </div>
</div>
</template>

<script>

export default {
    //数据集合
    data() {
		return {
            pageFlag : '',
			tableName: '',
			registerForm: {},
			rules: {},
			requiredRules: {},
            yonghuxingbieOptions: [],
            yonghukahaoOptions: [],
            qihuogongsixingbieOptions: [],
		}
    },
	mounted() {
		this.tableName = this.$route.query.role;
		if(this.tableName=='yonghu'){
			this.registerForm = {
                yonghuming: '',
                mima: '',
                xingming: '',
                xingbie: '',
                touxiang: '',
                nianling: '',
                youxiang: '',
                shouji: '',
                kahao: '未开户',
                jine: '0',
			}
		}
		if(this.tableName=='qihuogongsi'){
			this.registerForm = {
                zhanghao: '',
                mima: '',
                fuzerenxingming: '',
                xingbie: '',
                touxiang: '',
                gongsimingcheng: '',
                youxiang: '',
                lianxidianhua: '',
                gongsijianjie: '',
			}
		}
		if ('yonghu' == this.tableName) {
			this.requiredRules.yonghuming = [{ required: true, message: '请输入用户名', trigger: 'blur' }]
		}
		if ('yonghu' == this.tableName) {
			this.requiredRules.mima = [{ required: true, message: '请输入密码', trigger: 'blur' }]
		}
		if ('yonghu' == this.tableName) {
			this.requiredRules.jine = [{ required: true, message: '请输入金额', trigger: 'blur' }]
		}
		if ('qihuogongsi' == this.tableName) {
			this.requiredRules.zhanghao = [{ required: true, message: '请输入账号', trigger: 'blur' }]
		}
		if ('qihuogongsi' == this.tableName) {
			this.requiredRules.mima = [{ required: true, message: '请输入密码', trigger: 'blur' }]
		}
		if ('qihuogongsi' == this.tableName) {
			this.requiredRules.fuzerenxingming = [{ required: true, message: '请输入负责人姓名', trigger: 'blur' }]
		}
	},
    created() {
      this.pageFlag = this.$route.query.pageFlag;
      if ('yonghu' == this.tableName) {
        this.rules.yonghuming = [{ required: true, message: '请输入用户名', trigger: 'blur' }];
      }
      if ('yonghu' == this.tableName) {
        this.rules.mima = [{ required: true, message: '请输入密码', trigger: 'blur' }];
      }
        this.yonghuxingbieOptions = "男,女".split(',');
      if ('yonghu' == this.tableName) {
        this.rules.nianling = [{ required: true, validator: this.$validate.isIntNumer, trigger: 'blur' }];
      }
      if ('yonghu' == this.tableName) {
        this.rules.youxiang = [{ required: true, validator: this.$validate.isEmail, trigger: 'blur' }];
      }
      if ('yonghu' == this.tableName) {
        this.rules.shouji = [{ required: true, validator: this.$validate.isMobile, trigger: 'blur' }];
      }
        this.$http({
          url: `option/kaihuxinxi/zhanghukahao`,
          method: "get",
          params: {}
        }).then(({ data }) => {
          if (data && data.code === 0) {
              this.yonghukahaoOptions = data.data;
          }
        });
      if ('qihuogongsi' == this.tableName) {
        this.rules.zhanghao = [{ required: true, message: '请输入账号', trigger: 'blur' }];
      }
      if ('qihuogongsi' == this.tableName) {
        this.rules.mima = [{ required: true, message: '请输入密码', trigger: 'blur' }];
      }
      if ('qihuogongsi' == this.tableName) {
        this.rules.fuzerenxingming = [{ required: true, message: '请输入负责人姓名', trigger: 'blur' }];
      }
        this.qihuogongsixingbieOptions = "男,女".split(',');
      if ('qihuogongsi' == this.tableName) {
        this.rules.youxiang = [{ required: true, validator: this.$validate.isEmail, trigger: 'blur' }];
      }
      if ('qihuogongsi' == this.tableName) {
        this.rules.lianxidianhua = [{ required: true, validator: this.$validate.isMobile, trigger: 'blur' }];
      }
    },
    //方法集合
    methods: {
		changeRules(name){
			if(this.requiredRules[name]){
				return true
			}
			return false
		},
      // 获取uuid
      getUUID () {
        return new Date().getTime();
      },
        // 下二随
      yonghutouxiangUploadChange(fileUrls) {
          this.registerForm.touxiang = fileUrls.replace(new RegExp(this.$config.baseUrl,"g"),"");
      },
      qihuogongsitouxiangUploadChange(fileUrls) {
          this.registerForm.touxiang = fileUrls.replace(new RegExp(this.$config.baseUrl,"g"),"");
      },

        // 多级联动参数


      submitForm(formName) {
        this.$refs[formName].validate((valid) => {
          if (valid) {
            var url=this.tableName+"/register";
				if((!this.registerForm.yonghuming) && `yonghu` == this.tableName){
					this.$message.error(`用户名不能为空`);
					return
				}
               if(`yonghu` == this.tableName && this.registerForm.mima!=this.registerForm.mima2) {
                this.$message.error(`两次密码输入不一致`);
                return
               }
				if((!this.registerForm.mima) && `yonghu` == this.tableName){
					this.$message.error(`密码不能为空`);
					return
				}
				if(`yonghu` == this.tableName && this.registerForm.nianling &&(!this.$validate.isIntNumer2(this.registerForm.nianling))){
					this.$message.error(`年龄应输入整数`);
					return
				}
					if(`yonghu` == this.tableName && this.registerForm.youxiang &&(!this.$validate.isEmail2(this.registerForm.youxiang))){
						this.$message.error(`邮箱应输入邮件格式`);
						return
					}
					if(`yonghu` == this.tableName && this.registerForm.shouji &&(!this.$validate.isMobile2(this.registerForm.shouji))){
						this.$message.error(`手机应输入手机格式`);
						return
					}
				if((!this.registerForm.zhanghao) && `qihuogongsi` == this.tableName){
					this.$message.error(`账号不能为空`);
					return
				}
               if(`qihuogongsi` == this.tableName && this.registerForm.mima!=this.registerForm.mima2) {
                this.$message.error(`两次密码输入不一致`);
                return
               }
				if((!this.registerForm.mima) && `qihuogongsi` == this.tableName){
					this.$message.error(`密码不能为空`);
					return
				}
				if((!this.registerForm.fuzerenxingming) && `qihuogongsi` == this.tableName){
					this.$message.error(`负责人姓名不能为空`);
					return
				}
					if(`qihuogongsi` == this.tableName && this.registerForm.youxiang &&(!this.$validate.isEmail2(this.registerForm.youxiang))){
						this.$message.error(`邮箱应输入邮件格式`);
						return
					}
					if(`qihuogongsi` == this.tableName && this.registerForm.lianxidianhua &&(!this.$validate.isMobile2(this.registerForm.lianxidianhua))){
						this.$message.error(`手机应输入手机格式`);
						return
					}
            this.$http.post(url, this.registerForm).then(res => {
              if (res.data.code === 0) {
                this.$message({
                  message: '注册成功',
                  type: 'success',
                  duration: 1500,
                  onClose: () => {
                    this.$router.push('/login');
                  }
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
      resetForm(formName) {
        this.$refs[formName].resetFields();
      }
    }
  }
</script>

<style rel="stylesheet/scss" lang="scss" scoped>
	.container {
		position: relative;
		background: url(http://codegen.caihongy.cn/20231024/6a72ed211ce4490abbbb49e6c6f05331.png);
		
		.el-input {
		  width: auto;
		}
		
		.el-date-editor.el-input {
			width: auto;
		}
		
		.el-form-item /deep/ .el-form-item__content {
						display: flex;
					}
		
		.rgs-form .el-input /deep/ .el-input__inner {
						border: 2px solid #C7C7C7;
						border-radius: 10px;
						padding: 0 10px;
						box-shadow: 0 0 0px rgba(64, 158, 255, .5);
						outline: none;
						color: #000;
						background: #fff;
						width: 300px;
						font-size: 14px;
						height: 44px;
					}
		
		.rgs-form .el-select /deep/ .el-input__inner {
						border: 2px solid #C7C7C7;
						border-radius: 10px;
						padding: 0 10px;
						box-shadow: 0 0 0px rgba(64, 158, 255, .5);
						outline: none;
						color: #000;
						width: 300px;
						font-size: 14px;
						height: 44px;
					}
		
		.rgs-form .el-date-editor /deep/ .el-input__inner {
						border: 2px solid #C7C7C7;
						border-radius: 10px;
						padding: 0 10px 0 30px;
						box-shadow: 0 0 0px rgba(64, 158, 255, .5);
						outline: none;
						color: #000;
						width: 300px;
						font-size: 14px;
						height: 44px;
					}
		
		.rgs-form .el-date-editor /deep/ .el-input__inner {
						border: 2px solid #C7C7C7;
						border-radius: 10px;
						padding: 0 10px 0 30px;
						box-shadow: 0 0 0px rgba(64, 158, 255, .5);
						outline: none;
						color: #000;
						width: 300px;
						font-size: 14px;
						height: 44px;
					}
		
		.rgs-form /deep/ .el-upload--picture-card {
			background: transparent;
			border: 0;
			border-radius: 0;
			width: auto;
			height: auto;
			line-height: initial;
			vertical-align: middle;
		}
		
		.rgs-form /deep/ .upload .upload-img {
		  		  border: 2px solid #C7C7C7;
		  		  cursor: pointer;
		  		  border-radius: 10px;
		  		  color: #C7C7C7;
		  		  background: #fff;
		  		  width: 100px;
		  		  font-size: 24px;
		  		  line-height: 50px;
		  		  text-align: center;
		  		  height: 50px;
		  		}
		
		.rgs-form /deep/ .el-upload-list .el-upload-list__item {
		  		  border: 2px solid #C7C7C7;
		  		  cursor: pointer;
		  		  border-radius: 10px;
		  		  color: #C7C7C7;
		  		  background: #fff;
		  		  width: 100px;
		  		  font-size: 24px;
		  		  line-height: 50px;
		  		  text-align: center;
		  		  height: 50px;
		  		}
		
		.rgs-form /deep/ .el-upload .el-icon-plus {
		  		  border: 2px solid #C7C7C7;
		  		  cursor: pointer;
		  		  border-radius: 10px;
		  		  color: #C7C7C7;
		  		  background: #fff;
		  		  width: 100px;
		  		  font-size: 24px;
		  		  line-height: 50px;
		  		  text-align: center;
		  		  height: 50px;
		  		}
	}
	.required {
		position: relative;
	}
	.required::after{
				color: red;
				left: -10px;
				position: absolute;
				content: "*";
			}
</style>
