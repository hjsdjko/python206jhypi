<template>
<div :style='{"width":"68%","padding":"80px 0","margin":"10px auto","position":"relative","background":"transparent"}'>
    <el-form
	  :style='{"width":"100%","position":"relative","flexWrap":"wrap","display":"flex"}'
      class="add-update-preview"
      ref="ruleForm"
      :model="ruleForm"
      :rules="rules"
      label-width="80px"
    >
          <el-form-item :style='{"width":"32%","padding":"10px","margin":"0 0 10px","background":"transparent"}' label="期货代码" prop="qihuodaima">
            <el-input  v-model="ruleForm.qihuodaima" 
                placeholder="期货代码" clearable :readonly=" false  ||ro.qihuodaima"></el-input>
          </el-form-item>
          <el-form-item :style='{"width":"32%","padding":"10px","margin":"0 0 10px","background":"transparent"}' label="期货名称" prop="qihuomingcheng">
            <el-input  v-model="ruleForm.qihuomingcheng" 
                placeholder="期货名称" clearable :readonly=" false  ||ro.qihuomingcheng"></el-input>
          </el-form-item>
          <el-form-item :style='{"width":"32%","padding":"10px","margin":"0 0 10px","background":"transparent"}' label="期货类型" prop="qihuoleixing">
            <el-input  v-model="ruleForm.qihuoleixing" 
                placeholder="期货类型" clearable :readonly=" false  ||ro.qihuoleixing"></el-input>
          </el-form-item>
          <el-form-item :style='{"width":"32%","padding":"10px","margin":"0 0 10px","background":"transparent"}' label="图片" v-if="type!='cross' || (type=='cross' && !ro.tupian)" prop="tupian">
            <file-upload
            tip="点击上传图片"
            action="file/upload"
            :limit="3"
            :multiple="true"
            :fileUrls="ruleForm.tupian?ruleForm.tupian:''"
            @change="tupianUploadChange"
            ></file-upload>
          </el-form-item>
            <el-form-item :style='{"width":"32%","padding":"10px","margin":"0 0 10px","background":"transparent"}' class="upload" v-else label="图片" prop="tupian">
                <img v-if="ruleForm.tupian.substring(0,4)=='http'" class="upload-img" style="margin-right:20px;" v-bind:key="index" :src="ruleForm.tupian.split(',')[0]" width="100" height="100">
                <img v-else class="upload-img" style="margin-right:20px;" v-bind:key="index" v-for="(item,index) in ruleForm.tupian.split(',')" :src="baseUrl+item" width="100" height="100">
            </el-form-item>
          <el-form-item :style='{"width":"32%","padding":"10px","margin":"0 0 10px","background":"transparent"}' label="交易价格" prop="jiaoyijiage">
            <el-input type="number" v-model.number="ruleForm.jiaoyijiage" 
                placeholder="交易价格" clearable :readonly=" false  ||ro.jiaoyijiage"></el-input>
          </el-form-item>
          <el-form-item :style='{"width":"32%","padding":"10px","margin":"0 0 10px","background":"transparent"}' label="仓数" prop="shuliang">
            <el-input  v-model.number="ruleForm.shuliang" 
                placeholder="仓数" clearable :readonly=" false  ||ro.shuliang"></el-input>
          </el-form-item>
          <el-form-item :style='{"width":"32%","padding":"10px","margin":"0 0 10px","background":"transparent"}' label="总价格" prop="jine">
              <el-input v-model="jine" placeholder="总价格" readonly></el-input>
          </el-form-item>
          <el-form-item :style='{"width":"32%","padding":"10px","margin":"0 0 10px","background":"transparent"}' label="交易时间" prop="jiaoyishijian">
              <el-date-picker
				  :disabled=" false  ||ro.jiaoyishijian"
                  format="yyyy 年 MM 月 dd 日"
                  value-format="yyyy-MM-dd"
                  v-model="ruleForm.jiaoyishijian" 
                  type="date"
                  placeholder="交易时间">
              </el-date-picker> 
          </el-form-item>
          <el-form-item :style='{"width":"32%","padding":"10px","margin":"0 0 10px","background":"transparent"}' label="账号" prop="zhanghao">
            <el-input  v-model="ruleForm.zhanghao" 
                placeholder="账号" clearable :readonly=" false  ||ro.zhanghao"></el-input>
          </el-form-item>
          <el-form-item :style='{"width":"32%","padding":"10px","margin":"0 0 10px","background":"transparent"}' label="用户名" prop="yonghuming">
            <el-input  v-model="ruleForm.yonghuming" 
                placeholder="用户名" clearable :readonly=" false  ||ro.yonghuming"></el-input>
          </el-form-item>
          <el-form-item :style='{"width":"32%","padding":"10px","margin":"0 0 10px","background":"transparent"}' label="姓名" prop="xingming">
            <el-input  v-model="ruleForm.xingming" 
                placeholder="姓名" clearable :readonly=" false  ||ro.xingming"></el-input>
          </el-form-item>
          <el-form-item :style='{"width":"32%","padding":"10px","margin":"0 0 10px","background":"transparent"}' label="账户卡号" prop="kahao">
            <el-input  v-model="ruleForm.kahao" 
                placeholder="账户卡号" clearable :readonly=" false  ||ro.kahao"></el-input>
          </el-form-item>

      <el-form-item :style='{"padding":"0","margin":"0"}'>
        <el-button :style='{"border":"0","cursor":"pointer","padding":"6px 30px","margin":"0 20px 0 0","outline":"none","color":"rgba(255, 255, 255, 1)","borderRadius":"4px","background":"#000","width":"auto","fontSize":"16px","height":"auto"}'  type="primary" @click="onSubmit">提交</el-button>
        <el-button :style='{"border":"0px solid rgba(64, 158, 255, 1)","cursor":"pointer","padding":"6px 30px","margin":"0","outline":"none","color":"#fff","borderRadius":"4px","background":"#9E9E9E","width":"auto","fontSize":"16px","height":"auto"}' @click="back()">返回</el-button>
      </el-form-item>
    </el-form>
</div>
</template>

<script>
  export default {
    data() {
      return {
        id: '',
        uObject: null,
        baseUrl: '',
        ro:{
            qihuodaima : false,
            qihuomingcheng : false,
            qihuoleixing : false,
            tupian : false,
            jiaoyijiage : false,
            shuliang : false,
            jine : false,
            jiaoyishijian : false,
            zhanghao : false,
            yonghuming : false,
            xingming : false,
            kahao : false,
        },
        type: '',
        userTableName: localStorage.getItem('UserTableName'),
        ruleForm: {
          qihuodaima: '',
          qihuomingcheng: '',
          qihuoleixing: '',
          tupian: '',
          jiaoyijiage: '',
          shuliang: '',
          jine: '',
          jiaoyishijian: '',
          zhanghao: '',
          yonghuming: '',
          xingming: '',
          kahao: '',
        },


        rules: {
          qihuodaima: [
          ],
          qihuomingcheng: [
          ],
          qihuoleixing: [
          ],
          tupian: [
          ],
          jiaoyijiage: [
            { validator: this.$validate.isNumber, trigger: 'blur' },
          ],
          shuliang: [
            { validator: this.$validate.isIntNumer, trigger: 'blur' },
          ],
          jine: [
            { validator: this.$validate.isNumber, trigger: 'blur' },
          ],
          jiaoyishijian: [
          ],
          zhanghao: [
          ],
          yonghuming: [
          ],
          xingming: [
          ],
          kahao: [
          ],
        },
		centerType: false,
      };
    },
    computed: {


        jine:{
            get: function () {
                return 1*this.ruleForm.jiaoyijiage*this.ruleForm.shuliang
            }
        },

    },
    components: {
    },
    created() {
		if(this.$route.query.centerType){
			this.centerType = true
		}
	  //this.bg();
      let type = this.$route.query.type ? this.$route.query.type : '';
      this.init(type);
      this.baseUrl = this.$config.baseUrl;
      this.ruleForm.jiaoyishijian = this.getCurDate()
    },
    methods: {
      getMakeZero(s) {
          return s < 10 ? '0' + s : s;
      },
      // 下载
      download(file){
        window.open(`${file}`)
      },
      // 初始化
      init(type) {
        this.type = type;
        if(type=='cross'){
          var obj = JSON.parse(localStorage.getItem('crossObj'));
          for (var o in obj){
            if(o=='qihuodaima'){
              this.ruleForm.qihuodaima = obj[o];
              this.ro.qihuodaima = true;
              continue;
            }
            if(o=='qihuomingcheng'){
              this.ruleForm.qihuomingcheng = obj[o];
              this.ro.qihuomingcheng = true;
              continue;
            }
            if(o=='qihuoleixing'){
              this.ruleForm.qihuoleixing = obj[o];
              this.ro.qihuoleixing = true;
              continue;
            }
            if(o=='tupian'){
              this.ruleForm.tupian = obj[o].split(",")[0];
              this.ro.tupian = true;
              continue;
            }
            if(o=='jiaoyijiage'){
              this.ruleForm.jiaoyijiage = obj[o];
              this.ro.jiaoyijiage = true;
              continue;
            }
            if(o=='shuliang'){
              this.ruleForm.shuliang = obj[o];
              this.ro.shuliang = true;
              continue;
            }
            if(o=='jine'){
              this.ruleForm.jine = obj[o];
              this.ro.jine = true;
              continue;
            }
            if(o=='jiaoyishijian'){
              this.ruleForm.jiaoyishijian = obj[o];
              this.ro.jiaoyishijian = true;
              continue;
            }
            if(o=='zhanghao'){
              this.ruleForm.zhanghao = obj[o];
              this.ro.zhanghao = true;
              continue;
            }
            if(o=='yonghuming'){
              this.ruleForm.yonghuming = obj[o];
              this.ro.yonghuming = true;
              continue;
            }
            if(o=='xingming'){
              this.ruleForm.xingming = obj[o];
              this.ro.xingming = true;
              continue;
            }
            if(o=='kahao'){
              this.ruleForm.kahao = obj[o];
              this.ro.kahao = true;
              continue;
            }
          }
          this.ruleForm.shuliang = 0
		  this.ro.shuliang = false;
        }else if(type=='edit'){
			this.info()
		}
        // 获取用户信息
        this.$http.get(this.userTableName + '/session', {emulateJSON: true}).then(res => {
          if (res.data.code == 0) {
            var json = res.data.data;
            this.uObject = res.data.data;
            if((json.yonghuming!=''&&json.yonghuming) || json.yonghuming==0){
                this.ruleForm.yonghuming = json.yonghuming
            }
            if((json.xingming!=''&&json.xingming) || json.xingming==0){
                this.ruleForm.xingming = json.xingming
            }
            if((json.kahao!=''&&json.kahao) || json.kahao==0){
                this.ruleForm.kahao = json.kahao
            }
          }
        });
      },

    // 多级联动参数
      // 多级联动参数
      info() {
        this.$http.get(`qihuomaichu/detail/${this.$route.query.id}`, {emulateJSON: true}).then(res => {
          if (res.data.code == 0) {
            this.ruleForm = res.data.data;
          }
        });
      },
      // 提交
      onSubmit() {

          this.ruleForm.jine = this.jine
		if(!this.ruleForm.shuliang){
			this.$message.error("仓数不能为空");
			return
		}
        var obj = JSON.parse(localStorage.getItem('crossObj'));
        var table = localStorage.getItem('crossTable');
        obj.shuliang = obj.shuliang - this.ruleForm.shuliang
        if(obj.shuliang<0){
          this.$message.error("仓数不足");
          return
        }
      
        //this.$http.post(table+`/update`, obj).then(res => {});
        //更新跨表属性
        var crossuserid;
        var crossrefid;
        var crossoptnum;
        this.$refs["ruleForm"].validate(valid => {
          if(valid) {
            if(this.type=='cross'){
                 var statusColumnName = localStorage.getItem('statusColumnName');
                 var statusColumnValue = localStorage.getItem('statusColumnValue');
                 if(statusColumnName && statusColumnName!='') {
                     var obj = JSON.parse(localStorage.getItem('crossObj'));
                     if(!statusColumnName.startsWith("[")) {
                         for (var o in obj){
                             if(o==statusColumnName){
                                 obj[o] = statusColumnValue;
                             }
                         }
                         var table = localStorage.getItem('crossTable');
                         this.$http.post(table+'/update', obj).then(res => {});
                     } else {
                            crossuserid=Number(localStorage.getItem('userid'));
                            crossrefid=obj['id'];
                            crossoptnum=localStorage.getItem('statusColumnName');
                            crossoptnum=crossoptnum.replace(/\[/,"").replace(/\]/,"");
                     }
                 }
            }
            if(crossrefid && crossuserid) {
                 this.ruleForm.crossuserid=crossuserid;
                 this.ruleForm.crossrefid=crossrefid;
                 var params = {
                     page: 1,
                     limit: 10,
                     crossuserid:crossuserid,
                     crossrefid:crossrefid,
                 }
                 this.$http.get('qihuomaichu/list', {
                  params: params
                 }).then(res => {
                     if(res.data.data.total>=crossoptnum) {
                         this.$message({
                          message: localStorage.getItem('tips'),
                          type: 'success',
                          duration: 1500,
                         });
                          return false;
                     } else {
                         // 跨表计算
                          var obj = JSON.parse(localStorage.getItem('crossObj'));
                          var table = localStorage.getItem('crossTable');

                          obj.shuliang = parseFloat(obj.shuliang) - parseFloat(this.ruleForm.shuliang)

                          this.$http.post(table+`/update`,obj).then(res => {});
                          this.$http.post(`qihuomaichu/${this.ruleForm.id?'update':this.centerType?'save':'add'}`, this.ruleForm).then(res => {
                              if (res.data.code == 0) {
                                  if(this.uObject.jine>=0){
                                      this.uObject.jine = parseFloat(this.uObject.jine) + parseFloat(this.ruleForm.jine)
                                      this.$http.post(this.userTableName+'/update', this.uObject).then(res => {});
									  localStorage.setItem('sessionForm',JSON.stringify(this.uObject))
                                  }
                                  this.$message({
                                      message: '操作成功',
                                      type: 'success',
                                      duration: 1500,
                                      onClose: () => {
                                          this.$router.go(-1);
                                      }
                                  });
                              } else {
                                  this.$message({
                                      message: res.data.msg,
                                      type: 'error',
                                      duration: 1500
                                  });
                              }
                          });
                     }
                 });
             } else {
                  var obj = JSON.parse(localStorage.getItem('crossObj'));
                  var table = localStorage.getItem('crossTable');

                  obj.shuliang = parseFloat(obj.shuliang) - parseFloat(this.ruleForm.shuliang)

                  this.$http.post(table+`/update`,obj).then(res => {});
                  this.$http.post(`qihuomaichu/${this.ruleForm.id?'update':this.centerType?'save':'add'}`, this.ruleForm).then(res => {
                     if (res.data.code == 0) {
                          if(this.uObject.jine>=0){
                              this.uObject.jine = parseFloat(this.uObject.jine) + parseFloat(this.ruleForm.jine)
                              this.$http.post(this.userTableName+'/update', this.uObject).then(res => {});
							  localStorage.setItem('sessionForm',JSON.stringify(this.uObject))
                          }
                          this.$message({
                              message: '操作成功',
                              type: 'success',
                              duration: 1500,
                              onClose: () => {
                                  this.$router.go(-1);
                              }
                          });
                      } else {
                          this.$message({
                              message: res.data.msg,
                              type: 'error',
                              duration: 1500
                          });
                      }
                  });
             }
          }
        });
      },
      // 获取uuid
      getUUID () {
        return new Date().getTime();
      },
      // 返回
      back() {
        this.$router.go(-1);
      },
      tupianUploadChange(fileUrls) {
          this.ruleForm.tupian = fileUrls.replace(new RegExp(this.$config.baseUrl,"g"),"");;
      },
    }
  };
</script>

<style rel="stylesheet/scss" lang="scss" scoped>
	.el-date-editor.el-input {
		width: auto;
	}
	
	.add-update-preview .el-form-item /deep/ .el-form-item__label {
	  padding: 0 10px 0 0;
	  color: #000;
	  font-weight: 500;
	  width: 80px;
	  font-size: 14px;
	  line-height: 40px;
	  text-align: right;
	}
	
	.add-update-preview .el-form-item /deep/ .el-form-item__content {
	  margin-left: 80px;
	}
	
	.add-update-preview .el-input /deep/ .el-input__inner {
	  border: 0;
	  border-radius: 0;
	  padding: 0 12px;
	  box-shadow: none;
	  outline: none;
	  color: #000;
	  background: #fff;
	  width: 240px;
	  font-size: 14px;
	  height: 40px;
	}
	
	.add-update-preview .el-select /deep/ .el-input__inner {
	  border: 0;
	  border-radius: 0;
	  padding: 0 10px;
	  box-shadow: none;
	  outline: none;
	  color: #000;
	  background: #fff;
	  width: 240px;
	  font-size: 14px;
	  height: 40px;
	}
	
	.add-update-preview .el-date-editor /deep/ .el-input__inner {
	  border: 0;
	  border-radius: 0;
	  padding: 0 10px 0 30px;
	  box-shadow: none;
	  outline: none;
	  color: #000;
	  background: #fff;
	  width: 240px;
	  font-size: 14px;
	  height: 40px;
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
	
	.add-update-preview /deep/ .upload .upload-img {
	  border: none;
	  cursor: pointer;
	  border-radius: 6px;
	  color: #000;
	  background: #fff;
	  width: 150px;
	  font-size: 32px;
	  line-height: 40px;
	  text-align: center;
	  height: 40px;
	}
	
	.add-update-preview /deep/ .el-upload-list .el-upload-list__item {
	  border: none;
	  cursor: pointer;
	  border-radius: 6px;
	  color: #000;
	  background: #fff;
	  width: 150px;
	  font-size: 32px;
	  line-height: 40px;
	  text-align: center;
	  height: 40px;
	}
	
	.add-update-preview /deep/ .el-upload .el-icon-plus {
	  border: none;
	  cursor: pointer;
	  border-radius: 6px;
	  color: #000;
	  background: #fff;
	  width: 150px;
	  font-size: 32px;
	  line-height: 40px;
	  text-align: center;
	  height: 40px;
	}
	
	.add-update-preview .el-textarea /deep/ .el-textarea__inner {
	  border: 0;
	  border-radius: 0;
	  padding: 12px;
	  box-shadow: none;
	  outline: none;
	  color: #000;
	  background: #fff;
	  width: 240px;
	  font-size: 14px;
	  height: 120px;
	}
</style>
