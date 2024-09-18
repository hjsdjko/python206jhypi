<template>
  <div :style='{"minHeight":"calc(100vh - 200px)","padding":"20px","margin":"0 auto","color":"#666","background":"#f5f5f5","width":"calc(100% - 60px)","fontSize":"14px","height":"100%"}'>
    <el-form
	  :style='{"border":"1px solid rgba(255,255,255,1)","padding":"30px 0","boxShadow":"0 2px 3px 0px rgba(100,100,100,.05)","borderColor":"#fceaee","alignItems":"flex-start","borderRadius":"4px","flexWrap":"wrap","background":"rgba(255,255,255,1)","borderWidth":"0px","display":"flex","fontSize":"inherit","borderStyle":"double"}'
      class="add-update-preview"
      ref="ruleForm"
      :model="ruleForm"
      label-width="200px"
    >  
     <el-row>
        <el-form-item :style='{"padding":"2px 0","margin":"0 auto 4px","color":"inherit","borderRadius":"4px","background":"#f6f6f6","width":"60%","fontSize":"inherit"}'   v-if="flag=='yonghu'"  label="用户名" prop="yonghuming">
          <el-input v-model="ruleForm.yonghuming" readonly              placeholder="用户名" clearable></el-input>
        </el-form-item>
        <el-form-item :style='{"padding":"2px 0","margin":"0 auto 4px","color":"inherit","borderRadius":"4px","background":"#f6f6f6","width":"60%","fontSize":"inherit"}'   v-if="flag=='yonghu'"  label="姓名" prop="xingming">
          <el-input v-model="ruleForm.xingming"               placeholder="姓名" clearable></el-input>
        </el-form-item>
        <el-form-item :style='{"padding":"2px 0","margin":"0 auto 4px","color":"inherit","borderRadius":"4px","background":"#f6f6f6","width":"60%","fontSize":"inherit"}' v-if="flag=='yonghu'"  label="性别" prop="xingbie">
          <el-select v-model="ruleForm.xingbie"  placeholder="请选择性别">
            <el-option
                v-for="(item,index) in yonghuxingbieOptions"
                v-bind:key="index"
                :label="item"
                :value="item">
            </el-option>
          </el-select>
        </el-form-item>
        <el-form-item :style='{"padding":"2px 0","margin":"0 auto 4px","color":"inherit","borderRadius":"4px","background":"#f6f6f6","width":"60%","fontSize":"inherit"}' v-if="flag=='yonghu'" label="头像" prop="touxiang">
          <file-upload
          tip="点击上传头像"
          action="file/upload"
          :limit="3"
          :multiple="true"
          :fileUrls="ruleForm.touxiang?ruleForm.touxiang:''"
          @change="yonghutouxiangUploadChange"
          ></file-upload>
        </el-form-item>
        <el-form-item :style='{"padding":"2px 0","margin":"0 auto 4px","color":"inherit","borderRadius":"4px","background":"#f6f6f6","width":"60%","fontSize":"inherit"}'   v-if="flag=='yonghu'"  label="年龄" prop="nianling">
          <el-input v-model="ruleForm.nianling"               placeholder="年龄" clearable></el-input>
        </el-form-item>
        <el-form-item :style='{"padding":"2px 0","margin":"0 auto 4px","color":"inherit","borderRadius":"4px","background":"#f6f6f6","width":"60%","fontSize":"inherit"}'   v-if="flag=='yonghu'"  label="邮箱" prop="youxiang">
          <el-input v-model="ruleForm.youxiang"               placeholder="邮箱" clearable></el-input>
        </el-form-item>
        <el-form-item :style='{"padding":"2px 0","margin":"0 auto 4px","color":"inherit","borderRadius":"4px","background":"#f6f6f6","width":"60%","fontSize":"inherit"}'   v-if="flag=='yonghu'"  label="手机" prop="shouji">
          <el-input v-model="ruleForm.shouji"               placeholder="手机" clearable></el-input>
        </el-form-item>
        <el-form-item :style='{"padding":"2px 0","margin":"0 auto 4px","color":"inherit","borderRadius":"4px","background":"#f6f6f6","width":"60%","fontSize":"inherit"}' v-if="flag=='yonghu'"  label="账户卡号" prop="kahao">
          <el-select v-model="ruleForm.kahao" :disabled="true" placeholder="请选择账户卡号">
            <el-option
                v-for="(item,index) in yonghukahaoOptions"
                v-bind:key="index"
                :label="item"
                :value="item">
            </el-option>
          </el-select>
        </el-form-item>
        <el-form-item :style='{"padding":"2px 0","margin":"0 auto 4px","color":"inherit","borderRadius":"4px","background":"#f6f6f6","width":"60%","fontSize":"inherit"}'   v-if="flag=='yonghu'"  label="金额" prop="jine">
          <el-input v-model="ruleForm.jine" readonly              placeholder="金额" clearable></el-input>
        </el-form-item>
        <el-form-item :style='{"padding":"2px 0","margin":"0 auto 4px","color":"inherit","borderRadius":"4px","background":"#f6f6f6","width":"60%","fontSize":"inherit"}'   v-if="flag=='qihuogongsi'"  label="账号" prop="zhanghao">
          <el-input v-model="ruleForm.zhanghao" readonly              placeholder="账号" clearable></el-input>
        </el-form-item>
        <el-form-item :style='{"padding":"2px 0","margin":"0 auto 4px","color":"inherit","borderRadius":"4px","background":"#f6f6f6","width":"60%","fontSize":"inherit"}'   v-if="flag=='qihuogongsi'"  label="负责人姓名" prop="fuzerenxingming">
          <el-input v-model="ruleForm.fuzerenxingming"               placeholder="负责人姓名" clearable></el-input>
        </el-form-item>
        <el-form-item :style='{"padding":"2px 0","margin":"0 auto 4px","color":"inherit","borderRadius":"4px","background":"#f6f6f6","width":"60%","fontSize":"inherit"}' v-if="flag=='qihuogongsi'"  label="性别" prop="xingbie">
          <el-select v-model="ruleForm.xingbie"  placeholder="请选择性别">
            <el-option
                v-for="(item,index) in qihuogongsixingbieOptions"
                v-bind:key="index"
                :label="item"
                :value="item">
            </el-option>
          </el-select>
        </el-form-item>
        <el-form-item :style='{"padding":"2px 0","margin":"0 auto 4px","color":"inherit","borderRadius":"4px","background":"#f6f6f6","width":"60%","fontSize":"inherit"}' v-if="flag=='qihuogongsi'" label="头像" prop="touxiang">
          <file-upload
          tip="点击上传头像"
          action="file/upload"
          :limit="3"
          :multiple="true"
          :fileUrls="ruleForm.touxiang?ruleForm.touxiang:''"
          @change="qihuogongsitouxiangUploadChange"
          ></file-upload>
        </el-form-item>
        <el-form-item :style='{"padding":"2px 0","margin":"0 auto 4px","color":"inherit","borderRadius":"4px","background":"#f6f6f6","width":"60%","fontSize":"inherit"}'   v-if="flag=='qihuogongsi'"  label="公司名称" prop="gongsimingcheng">
          <el-input v-model="ruleForm.gongsimingcheng"               placeholder="公司名称" clearable></el-input>
        </el-form-item>
        <el-form-item :style='{"padding":"2px 0","margin":"0 auto 4px","color":"inherit","borderRadius":"4px","background":"#f6f6f6","width":"60%","fontSize":"inherit"}'   v-if="flag=='qihuogongsi'"  label="邮箱" prop="youxiang">
          <el-input v-model="ruleForm.youxiang"               placeholder="邮箱" clearable></el-input>
        </el-form-item>
        <el-form-item :style='{"padding":"2px 0","margin":"0 auto 4px","color":"inherit","borderRadius":"4px","background":"#f6f6f6","width":"60%","fontSize":"inherit"}'   v-if="flag=='qihuogongsi'"  label="手机" prop="lianxidianhua">
          <el-input v-model="ruleForm.lianxidianhua"               placeholder="手机" clearable></el-input>
        </el-form-item>
        <el-form-item :style='{"padding":"2px 0","margin":"0 auto 4px","color":"inherit","borderRadius":"4px","background":"#f6f6f6","width":"60%","fontSize":"inherit"}'   v-if="flag=='qihuogongsi'"  label="公司简介" prop="gongsijianjie">
          <el-input v-model="ruleForm.gongsijianjie"               placeholder="公司简介" clearable></el-input>
        </el-form-item>
		<el-form-item :style='{"padding":"2px 0","margin":"0 auto 4px","color":"inherit","borderRadius":"4px","background":"#f6f6f6","width":"60%","fontSize":"inherit"}' v-if="flag=='users'" label="用户名" prop="username">
			<el-input v-model="ruleForm.username" placeholder="用户名"></el-input>
		</el-form-item>
		<el-form-item :style='{"padding":"0","margin":"30px auto","alignItems":"center","textAlign":"center","background":"none","display":"flex","width":"60%","fontSize":"48px"}'>
			<el-button class="btn3" :style='{"border":"0px solid rgba(126, 96, 16, .2)","cursor":"pointer","padding":"0 20px","margin":"0px 4px","outline":"none","color":"#fff","borderRadius":"4px","background":"#45B6B0","width":"auto","fontSize":"16px","lineHeight":"24px","height":"40px"}' type="primary" @click="onUpdateHandler">
				<span class="icon iconfont icon-tijiao16" :style='{"color":"inherit","margin":"0 2px","fontSize":"18px"}'></span>
				保存
			</el-button>
		</el-form-item>
      </el-row>
    </el-form>
  </div>
</template>
<script>
// 数字，邮件，手机，url，身份证校验
import { isNumber,isIntNumer,isEmail,isMobile,isPhone,isURL,checkIdCard } from "@/utils/validate";

export default {
  data() {
    return {
      ruleForm: {},
      flag: '',
      usersFlag: false,
      yonghuxingbieOptions: [],
      yonghukahaoOptions: [],
      qihuogongsixingbieOptions: [],
    };
  },
  mounted() {
    var table = this.$storage.get("sessionTable");
    this.flag = table;
    this.$http({
      url: `${this.$storage.get("sessionTable")}/session`,
      method: "get"
    }).then(({ data }) => {
      if (data && data.code === 0) {
        this.ruleForm = data.data;
      } else {
        this.$message.error(data.msg);
      }
    });
    this.yonghuxingbieOptions = "男,女".split(',')
    this.$http({
      url: `option/kaihuxinxi/zhanghukahao`,
      method: "get"
    }).then(({ data }) => {
      if (data && data.code === 0) {
        this.yonghukahaoOptions = data.data;
      } else {
        this.$message.error(data.msg);
      }
    });
    this.qihuogongsixingbieOptions = "男,女".split(',')
  },
  methods: {
    yonghutouxiangUploadChange(fileUrls) {
        this.ruleForm.touxiang = fileUrls;
    },
    qihuogongsitouxiangUploadChange(fileUrls) {
        this.ruleForm.touxiang = fileUrls;
    },
    onUpdateHandler() {
      if((!this.ruleForm.yonghuming)&& 'yonghu'==this.flag){
        this.$message.error('用户名不能为空');
        return
      }


      if((!this.ruleForm.mima)&& 'yonghu'==this.flag){
        this.$message.error('密码不能为空');
        return
      }








        if(this.ruleForm.touxiang!=null) {
                this.ruleForm.touxiang = this.ruleForm.touxiang.replace(new RegExp(this.$base.url,"g"),"");
        }


      if( 'yonghu' ==this.flag && this.ruleForm.nianling&&(!isIntNumer(this.ruleForm.nianling))){
       this.$message.error(`年龄应输入整数`);
        return
      }


      if( 'yonghu' ==this.flag && this.ruleForm.youxiang&&(!isEmail(this.ruleForm.youxiang))){
        this.$message.error(`邮箱应输入邮箱格式`);
        return
      }


      if( 'yonghu' ==this.flag && this.ruleForm.shouji&&(!isMobile(this.ruleForm.shouji))){
        this.$message.error(`手机应输入手机格式`);
        return
      }


      if((!this.ruleForm.jine)&& 'yonghu'==this.flag){
        this.$message.error('金额不能为空');
        return
      }


      if( 'yonghu' ==this.flag && this.ruleForm.jine&&(!isNumber(this.ruleForm.jine))){
        this.$message.error(`金额应输入数字`);
        return
      }
      if((!this.ruleForm.zhanghao)&& 'qihuogongsi'==this.flag){
        this.$message.error('账号不能为空');
        return
      }


      if((!this.ruleForm.mima)&& 'qihuogongsi'==this.flag){
        this.$message.error('密码不能为空');
        return
      }


      if((!this.ruleForm.fuzerenxingming)&& 'qihuogongsi'==this.flag){
        this.$message.error('负责人姓名不能为空');
        return
      }






        if(this.ruleForm.touxiang!=null) {
                this.ruleForm.touxiang = this.ruleForm.touxiang.replace(new RegExp(this.$base.url,"g"),"");
        }




      if( 'qihuogongsi' ==this.flag && this.ruleForm.youxiang&&(!isEmail(this.ruleForm.youxiang))){
        this.$message.error(`邮箱应输入邮箱格式`);
        return
      }


      if( 'qihuogongsi' ==this.flag && this.ruleForm.lianxidianhua&&(!isMobile(this.ruleForm.lianxidianhua))){
        this.$message.error(`手机应输入手机格式`);
        return
      }


      if('users'==this.flag && this.ruleForm.username.trim().length<1) {
	this.$message.error(`用户名不能为空`);
        return	
      }
      this.$http({
        url: `${this.$storage.get("sessionTable")}/update`,
        method: "post",
        data: this.ruleForm
      }).then(({ data }) => {
        if (data && data.code === 0) {
          this.$message({
            message: "修改信息成功",
            type: "success",
            duration: 1500,
            onClose: () => {
            }
          });
        } else {
          this.$message.error(data.msg);
        }
      });
    }
  }
};
</script>
<style lang="scss" scoped>
	.el-date-editor.el-input {
		width: auto;
	}
	
	.add-update-preview .el-form-item /deep/ .el-form-item__label {
	  	  padding: 0 10px 0 0;
	  	  color: inherit;
	  	  background: none;
	  	  font-weight: 500;
	  	  display: inline-block;
	  	  width: 200px;
	  	  font-size: inherit;
	  	  line-height: 40px;
	  	  text-align: right;
	  	}
	
	.add-update-preview .el-form-item /deep/ .el-form-item__content {
	  margin-left: 200px;
	}
	
	.add-update-preview .el-input /deep/ .el-input__inner {
	  	  border: 1px solid #C7D5E0;
	  	  border-radius: 4px;
	  	  padding: 0 12px;
	  	  box-shadow: 0 0 0px rgba(64, 158, 255, .5);
	  	  outline: none;
	  	  color: inherit;
	  	  background: #fff;
	  	  width: 400px;
	  	  font-size: 16px;
	  	  height: 36px;
	  	}
	
	.add-update-preview .el-select /deep/ .el-input__inner {
	  	  border: 1px solid #C7D5E0;
	  	  border-radius: 4px;
	  	  padding: 0 10px;
	  	  box-shadow: 0 0 0px rgba(64, 158, 255, .5);
	  	  outline: none;
	  	  color: inherit;
	  	  background: #fff;
	  	  width: auto;
	  	  font-size: 16px;
	  	  min-width: 350px;
	  	  height: 36px;
	  	}
	
	.add-update-preview .el-date-editor /deep/ .el-input__inner {
	  	  border: 1px solid #C7D5E0;
	  	  border-radius: 4px;
	  	  padding: 0 10px 0 30px;
	  	  box-shadow: 0 0 0px rgba(64, 158, 255, .5);
	  	  outline: none;
	  	  color: inherit;
	  	  background: none;
	  	  width: auto;
	  	  font-size: 16px;
	  	  min-width: 250px;
	  	  height: 36px;
	  	}
	
	.add-update-preview /deep/ .el-upload--picture-card {
		background: transparent;
		border: 0;
		border-radius: 0;
		width: auto;
		height: auto;
		line-height: initial;
		vertical-align: middle;
	}
	
	.add-update-preview /deep/ .el-upload-list .el-upload-list__item {
	  	  border: 1px solid #C7D5E0;
	  	  cursor: pointer;
	  	  border-radius: 4px;
	  	  color: #aaa;
	  	  background: #fff;
	  	  object-fit: cover;
	  	  width: 180px;
	  	  font-size: 32px;
	  	  line-height: 100px;
	  	  text-align: center;
	  	  height: 100px;
	  	}
	
	.add-update-preview /deep/ .el-upload .el-icon-plus {
	  	  border: 1px solid #C7D5E0;
	  	  cursor: pointer;
	  	  border-radius: 4px;
	  	  color: #aaa;
	  	  background: #fff;
	  	  object-fit: cover;
	  	  width: 180px;
	  	  font-size: 32px;
	  	  line-height: 100px;
	  	  text-align: center;
	  	  height: 100px;
	  	}
	
	.add-update-preview .el-textarea /deep/ .el-textarea__inner {
	  	  border: 1px solid #C7D5E0;
	  	  border-radius: 4px;
	  	  padding: 12px;
	  	  box-shadow: 0 0 0px rgba(64, 158, 255, .5);
	  	  outline: none;
	  	  color: inherit;
	  	  background: #fff;
	  	  width: 500px;
	  	  font-size: 16px;
	  	  height: 140px;
	  	}
	
	.add-update-preview .btn3 {
				border: 0px solid rgba(126, 96, 16, .2);
				cursor: pointer;
				border-radius: 4px;
				padding: 0 20px;
				margin: 0px 4px;
				outline: none;
				color: #fff;
				background: #45B6B0;
				width: auto;
				font-size: 16px;
				line-height: 24px;
				height: 40px;
			}
	
	.add-update-preview .btn3:hover {
				opacity: 0.8;
			}
	
	.editor>.avatar-uploader {
		line-height: 0;
		height: 0;
	}
</style>
