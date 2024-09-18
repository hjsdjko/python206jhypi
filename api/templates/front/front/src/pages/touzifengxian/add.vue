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
          <el-form-item :style='{"width":"32%","padding":"10px","margin":"0 0 10px","background":"transparent"}' label="投资名称" prop="touzimingcheng">
            <el-input  v-model="ruleForm.touzimingcheng" 
                placeholder="投资名称" clearable :readonly=" false  ||ro.touzimingcheng"></el-input>
          </el-form-item>
          <el-form-item :style='{"width":"32%","padding":"10px","margin":"0 0 10px","background":"transparent"}' label="投资类型" prop="touzileixing">
            <el-input  v-model="ruleForm.touzileixing" 
                placeholder="投资类型" clearable :readonly=" false  ||ro.touzileixing"></el-input>
          </el-form-item>
          <el-form-item :style='{"width":"32%","padding":"10px","margin":"0 0 10px","background":"transparent"}' label="风险等级" prop="fengxiandengji">
            <el-input  v-model="ruleForm.fengxiandengji" 
                placeholder="风险等级" clearable :readonly=" false  ||ro.fengxiandengji"></el-input>
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
          <el-form-item :style='{"width":"32%","padding":"10px","margin":"0 0 10px","background":"transparent"}' label="发布时间" prop="fabushijian">
              <el-date-picker
				  :disabled=" false  ||ro.fabushijian"
                  value-format="yyyy-MM-dd HH:mm:ss"
                  v-model="ruleForm.fabushijian" 
                  type="datetime"
                  placeholder="发布时间">
              </el-date-picker>
          </el-form-item>
          <el-form-item :style='{"width":"32%","padding":"10px","margin":"0 0 10px","background":"transparent"}' label="风险说明" prop="fengxianshuoming">
            <el-input
              type="textarea"
              :rows="8"
              placeholder="风险说明"
              v-model="ruleForm.fengxianshuoming">
            </el-input>
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
        baseUrl: '',
        ro:{
            touzimingcheng : false,
            touzileixing : false,
            fengxiandengji : false,
            tupian : false,
            fengxianshuoming : false,
            fabushijian : false,
            discussnum : false,
            storeupnum : false,
        },
        type: '',
        userTableName: localStorage.getItem('UserTableName'),
        ruleForm: {
          touzimingcheng: '',
          touzileixing: '',
          fengxiandengji: '',
          tupian: '',
          fengxianshuoming: '',
          fabushijian: '',
          discussnum: '',
          storeupnum: '',
        },


        rules: {
          touzimingcheng: [
          ],
          touzileixing: [
            { required: true, message: '投资类型不能为空', trigger: 'blur' },
          ],
          fengxiandengji: [
            { required: true, message: '风险等级不能为空', trigger: 'blur' },
          ],
          tupian: [
          ],
          fengxianshuoming: [
          ],
          fabushijian: [
          ],
          discussnum: [
            { validator: this.$validate.isIntNumer, trigger: 'blur' },
          ],
          storeupnum: [
            { validator: this.$validate.isIntNumer, trigger: 'blur' },
          ],
        },
		centerType: false,
      };
    },
    computed: {



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
      this.ruleForm.fabushijian = this.getCurDateTime()
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
            if(o=='touzimingcheng'){
              this.ruleForm.touzimingcheng = obj[o];
              this.ro.touzimingcheng = true;
              continue;
            }
            if(o=='touzileixing'){
              this.ruleForm.touzileixing = obj[o];
              this.ro.touzileixing = true;
              continue;
            }
            if(o=='fengxiandengji'){
              this.ruleForm.fengxiandengji = obj[o];
              this.ro.fengxiandengji = true;
              continue;
            }
            if(o=='tupian'){
              this.ruleForm.tupian = obj[o].split(",")[0];
              this.ro.tupian = true;
              continue;
            }
            if(o=='fengxianshuoming'){
              this.ruleForm.fengxianshuoming = obj[o];
              this.ro.fengxianshuoming = true;
              continue;
            }
            if(o=='fabushijian'){
              this.ruleForm.fabushijian = obj[o];
              this.ro.fabushijian = true;
              continue;
            }
            if(o=='discussnum'){
              this.ruleForm.discussnum = obj[o];
              this.ro.discussnum = true;
              continue;
            }
            if(o=='storeupnum'){
              this.ruleForm.storeupnum = obj[o];
              this.ro.storeupnum = true;
              continue;
            }
          }
        }else if(type=='edit'){
			this.info()
		}
        // 获取用户信息
        this.$http.get(this.userTableName + '/session', {emulateJSON: true}).then(res => {
          if (res.data.code == 0) {
            var json = res.data.data;
          }
        });
      },

    // 多级联动参数
      // 多级联动参数
      info() {
        this.$http.get(`touzifengxian/detail/${this.$route.query.id}`, {emulateJSON: true}).then(res => {
          if (res.data.code == 0) {
            this.ruleForm = res.data.data;
          }
        });
      },
      // 提交
      onSubmit() {

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
                 this.$http.get('touzifengxian/list', {
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


                          this.$http.post(`touzifengxian/${this.ruleForm.id?'update':this.centerType?'save':'add'}`, this.ruleForm).then(res => {
                              if (res.data.code == 0) {
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


                  this.$http.post(`touzifengxian/${this.ruleForm.id?'update':this.centerType?'save':'add'}`, this.ruleForm).then(res => {
                     if (res.data.code == 0) {
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
