<template>
	<div class="addEdit-block" :style='{"minHeight":"calc(100vh - 200px)","padding":"30px","margin":"0 auto","color":"#666","background":"#f5f5f5","width":"calc(100% - 60px)","fontSize":"16px","height":"100%"}'>
		<el-form
			:style='{"border":"1px solid rgba(255,255,255,1)","padding":"30px 0","boxShadow":"0 2px 3px 0px rgba(100,100,100,.05)","borderColor":"#fceaee","alignItems":"flex-start","borderRadius":"4px","flexWrap":"wrap","background":"rgba(255,255,255,1)","borderWidth":"0px","display":"flex","fontSize":"inherit","borderStyle":"double"}'
			class="add-update-preview"
			ref="ruleForm"
			:model="ruleForm"
			:rules="rules"
			label-width="200px"
		>
			<template >
				<el-form-item :style='{"padding":"2px 0","margin":"0 auto 4px","color":"inherit","borderRadius":"4px","background":"#f6f6f6","width":"60%","fontSize":"inherit"}' class="input" v-if="type!='info'" label="期货代码" prop="qihuodaima">
					<el-input v-model="ruleForm.qihuodaima" placeholder="期货代码" readonly></el-input>
				</el-form-item>
				<el-form-item :style='{"padding":"2px 0","margin":"0 auto 4px","color":"inherit","borderRadius":"4px","background":"#f6f6f6","width":"60%","fontSize":"inherit"}' class="input" v-else-if="ruleForm.qihuodaima" label="期货代码" prop="qihuodaima">
					<el-input v-model="ruleForm.qihuodaima" placeholder="期货代码" readonly></el-input>
				</el-form-item>
				<el-form-item :style='{"padding":"2px 0","margin":"0 auto 4px","color":"inherit","borderRadius":"4px","background":"#f6f6f6","width":"60%","fontSize":"inherit"}' class="input" v-if="type!='info'"  label="期货名称" prop="qihuomingcheng">
					<el-input  v-model="ruleForm.qihuomingcheng" placeholder="期货名称" clearable  :readonly="ro.qihuomingcheng"></el-input>
				</el-form-item>
				<el-form-item :style='{"padding":"2px 0","margin":"0 auto 4px","color":"inherit","borderRadius":"4px","background":"#f6f6f6","width":"60%","fontSize":"inherit"}' v-else class="input" label="期货名称" prop="qihuomingcheng">
					<el-input v-model="ruleForm.qihuomingcheng" placeholder="期货名称" readonly></el-input>
				</el-form-item>
				<el-form-item :style='{"padding":"2px 0","margin":"0 auto 4px","color":"inherit","borderRadius":"4px","background":"#f6f6f6","width":"60%","fontSize":"inherit"}' class="select" v-if="type!='info'"  label="期货类型" prop="qihuoleixing">
					<el-select :disabled="ro.qihuoleixing" v-model="ruleForm.qihuoleixing" placeholder="请选择期货类型" >
						<el-option
							v-for="(item,index) in qihuoleixingOptions"
							v-bind:key="index"
							:label="item"
							:value="item">
						</el-option>
					</el-select>
				</el-form-item>
				<el-form-item :style='{"padding":"2px 0","margin":"0 auto 4px","color":"inherit","borderRadius":"4px","background":"#f6f6f6","width":"60%","fontSize":"inherit"}' v-else class="input" label="期货类型" prop="qihuoleixing">
					<el-input v-model="ruleForm.qihuoleixing"
						placeholder="期货类型" readonly></el-input>
				</el-form-item>
				<el-form-item :style='{"padding":"2px 0","margin":"0 auto 4px","color":"inherit","borderRadius":"4px","background":"#f6f6f6","width":"60%","fontSize":"inherit"}' class="input" v-if="type!='info'"  label="公司名称" prop="gongsimingcheng">
					<el-input  v-model="ruleForm.gongsimingcheng" placeholder="公司名称" clearable  :readonly="ro.gongsimingcheng"></el-input>
				</el-form-item>
				<el-form-item :style='{"padding":"2px 0","margin":"0 auto 4px","color":"inherit","borderRadius":"4px","background":"#f6f6f6","width":"60%","fontSize":"inherit"}' v-else class="input" label="公司名称" prop="gongsimingcheng">
					<el-input v-model="ruleForm.gongsimingcheng" placeholder="公司名称" readonly></el-input>
				</el-form-item>
				<el-form-item :style='{"padding":"2px 0","margin":"0 auto 4px","color":"inherit","borderRadius":"4px","background":"#f6f6f6","width":"60%","fontSize":"inherit"}' class="input" v-if="type!='info'"  label="期货涨势" prop="qihuozhangshi">
					<el-input  v-model="ruleForm.qihuozhangshi" placeholder="期货涨势" clearable  :readonly="ro.qihuozhangshi"></el-input>
				</el-form-item>
				<el-form-item :style='{"padding":"2px 0","margin":"0 auto 4px","color":"inherit","borderRadius":"4px","background":"#f6f6f6","width":"60%","fontSize":"inherit"}' v-else class="input" label="期货涨势" prop="qihuozhangshi">
					<el-input v-model="ruleForm.qihuozhangshi" placeholder="期货涨势" readonly></el-input>
				</el-form-item>
				<el-form-item :style='{"padding":"2px 0","margin":"0 auto 4px","color":"inherit","borderRadius":"4px","background":"#f6f6f6","width":"60%","fontSize":"inherit"}' class="input" v-if="type!='info'"  label="当前价格" prop="jiage">
					<el-input type="number" v-model.number="ruleForm.jiage" placeholder="当前价格" clearable  :readonly="ro.jiage"></el-input>
				</el-form-item>
				<el-form-item :style='{"padding":"2px 0","margin":"0 auto 4px","color":"inherit","borderRadius":"4px","background":"#f6f6f6","width":"60%","fontSize":"inherit"}' v-else class="input" label="当前价格" prop="jiage">
					<el-input v-model="ruleForm.jiage" placeholder="当前价格" readonly></el-input>
				</el-form-item>
				<el-form-item :style='{"padding":"2px 0","margin":"0 auto 4px","color":"inherit","borderRadius":"4px","background":"#f6f6f6","width":"60%","fontSize":"inherit"}' class="input" v-if="type!='info'"  label="交易价格" prop="jiaoyijiage">
					<el-input type="number" v-model.number="ruleForm.jiaoyijiage" placeholder="交易价格" clearable  :readonly="ro.jiaoyijiage"></el-input>
				</el-form-item>
				<el-form-item :style='{"padding":"2px 0","margin":"0 auto 4px","color":"inherit","borderRadius":"4px","background":"#f6f6f6","width":"60%","fontSize":"inherit"}' v-else class="input" label="交易价格" prop="jiaoyijiage">
					<el-input v-model="ruleForm.jiaoyijiage" placeholder="交易价格" readonly></el-input>
				</el-form-item>
				<el-form-item :style='{"padding":"2px 0","margin":"0 auto 4px","color":"inherit","borderRadius":"4px","background":"#f6f6f6","width":"60%","fontSize":"inherit"}' class="upload" v-if="type!='info' && !ro.tupian" label="图片" prop="tupian">
					<file-upload
						tip="点击上传图片"
						action="file/upload"
						:limit="3"
						:multiple="true"
						:fileUrls="ruleForm.tupian?ruleForm.tupian:''"
						@change="tupianUploadChange"
					></file-upload>
				</el-form-item>
				<el-form-item :style='{"padding":"2px 0","margin":"0 auto 4px","color":"inherit","borderRadius":"4px","background":"#f6f6f6","width":"60%","fontSize":"inherit"}' class="upload" v-else-if="ruleForm.tupian" label="图片" prop="tupian">
					<img v-if="ruleForm.tupian.substring(0,4)=='http'" class="upload-img" style="margin-right:20px;" v-bind:key="index" :src="ruleForm.tupian.split(',')[0]" width="100" height="100">
					<img v-else class="upload-img" style="margin-right:20px;" v-bind:key="index" v-for="(item,index) in ruleForm.tupian.split(',')" :src="$base.url+item" width="100" height="100">
				</el-form-item>
				<el-form-item :style='{"padding":"2px 0","margin":"0 auto 4px","color":"inherit","borderRadius":"4px","background":"#f6f6f6","width":"60%","fontSize":"inherit"}' class="input" v-if="type!='info'"  label="开市时间" prop="kaishishijian">
					<el-input  v-model="ruleForm.kaishishijian" placeholder="开市时间" clearable  :readonly="ro.kaishishijian"></el-input>
				</el-form-item>
				<el-form-item :style='{"padding":"2px 0","margin":"0 auto 4px","color":"inherit","borderRadius":"4px","background":"#f6f6f6","width":"60%","fontSize":"inherit"}' v-else class="input" label="开市时间" prop="kaishishijian">
					<el-input v-model="ruleForm.kaishishijian" placeholder="开市时间" readonly></el-input>
				</el-form-item>
				<el-form-item :style='{"padding":"2px 0","margin":"0 auto 4px","color":"inherit","borderRadius":"4px","background":"#f6f6f6","width":"60%","fontSize":"inherit"}' class="input" v-if="type!='info'"  label="账号" prop="zhanghao">
					<el-input  v-model="ruleForm.zhanghao" placeholder="账号" clearable  :readonly="ro.zhanghao"></el-input>
				</el-form-item>
				<el-form-item :style='{"padding":"2px 0","margin":"0 auto 4px","color":"inherit","borderRadius":"4px","background":"#f6f6f6","width":"60%","fontSize":"inherit"}' v-else class="input" label="账号" prop="zhanghao">
					<el-input v-model="ruleForm.zhanghao" placeholder="账号" readonly></el-input>
				</el-form-item>
				<el-form-item :style='{"padding":"2px 0","margin":"0 auto 4px","color":"inherit","borderRadius":"4px","background":"#f6f6f6","width":"60%","fontSize":"inherit"}' class="input" v-if="type!='info'"  label="姓名" prop="fuzerenxingming">
					<el-input  v-model="ruleForm.fuzerenxingming" placeholder="姓名" clearable  :readonly="ro.fuzerenxingming"></el-input>
				</el-form-item>
				<el-form-item :style='{"padding":"2px 0","margin":"0 auto 4px","color":"inherit","borderRadius":"4px","background":"#f6f6f6","width":"60%","fontSize":"inherit"}' v-else class="input" label="姓名" prop="fuzerenxingming">
					<el-input v-model="ruleForm.fuzerenxingming" placeholder="姓名" readonly></el-input>
				</el-form-item>
				<el-form-item :style='{"padding":"2px 0","margin":"0 auto 4px","color":"inherit","borderRadius":"4px","background":"#f6f6f6","width":"60%","fontSize":"inherit"}' class="input" v-if="type!='info'"  label="联系电话" prop="lianxidianhua">
					<el-input  v-model="ruleForm.lianxidianhua" placeholder="联系电话" clearable  :readonly="ro.lianxidianhua"></el-input>
				</el-form-item>
				<el-form-item :style='{"padding":"2px 0","margin":"0 auto 4px","color":"inherit","borderRadius":"4px","background":"#f6f6f6","width":"60%","fontSize":"inherit"}' v-else class="input" label="联系电话" prop="lianxidianhua">
					<el-input v-model="ruleForm.lianxidianhua" placeholder="联系电话" readonly></el-input>
				</el-form-item>
			</template>
				<el-form-item :style='{"padding":"2px 0","margin":"0 auto 4px","color":"inherit","borderRadius":"4px","background":"#f6f6f6","width":"60%","fontSize":"inherit"}' v-if="type!='info'"  label="期货介绍" prop="qihuojieshao">
					<editor 
						style="min-width: 200px; max-width: 600px;"
						v-model="ruleForm.qihuojieshao" 
						class="editor" 
						action="file/upload">
					</editor>
				</el-form-item>
				<el-form-item :style='{"padding":"2px 0","margin":"0 auto 4px","color":"inherit","borderRadius":"4px","background":"#f6f6f6","width":"60%","fontSize":"inherit"}' v-else-if="ruleForm.qihuojieshao" label="期货介绍" prop="qihuojieshao">
                    <span :style='{"fontSize":"16px","lineHeight":"40px","color":"inherit","fontWeight":"500","display":"inline-block"}' v-html="ruleForm.qihuojieshao"></span>
                </el-form-item>
			<el-form-item :style='{"padding":"0","margin":"30px auto","alignItems":"center","textAlign":"center","background":"none","display":"flex","width":"60%","fontSize":"48px"}' class="btn">
				<el-button class="btn3"  v-if="type!='info'" type="success" @click="onSubmit">
					<span class="icon iconfont icon-tijiao16" :style='{"color":"inherit","margin":"0 2px","fontSize":"18px"}'></span>
					保存
				</el-button>
				<el-button class="btn4" v-if="type!='info'" type="success" @click="back()">
					<span class="icon iconfont icon-quxiao09" :style='{"color":"inherit","margin":"0 2px","fontSize":"18px"}'></span>
					取消
				</el-button>
				<el-button class="btn5" v-if="type=='info'" type="success" @click="back()">
					<span class="icon iconfont icon-fanhui01" :style='{"color":"inherit","margin":"0 2px","fontSize":"18px"}'></span>
					返回
				</el-button>
			</el-form-item>
		</el-form>
    

  </div>
</template>
<script>
// 数字，邮件，手机，url，身份证校验
import { isNumber,isIntNumer,isEmail,isPhone, isMobile,isURL,checkIdCard } from "@/utils/validate";
export default {
	data() {
		let self = this
		var validateIdCard = (rule, value, callback) => {
			if(!value){
				callback();
			} else if (!checkIdCard(value)) {
				callback(new Error("请输入正确的身份证号码"));
			} else {
				callback();
			}
		};
		var validateUrl = (rule, value, callback) => {
			if(!value){
				callback();
			} else if (!isURL(value)) {
				callback(new Error("请输入正确的URL地址"));
			} else {
				callback();
			}
		};
		var validateMobile = (rule, value, callback) => {
			if(!value){
				callback();
			} else if (!isMobile(value)) {
				callback(new Error("请输入正确的手机号码"));
			} else {
				callback();
			}
		};
		var validatePhone = (rule, value, callback) => {
			if(!value){
				callback();
			} else if (!isPhone(value)) {
				callback(new Error("请输入正确的电话号码"));
			} else {
				callback();
			}
		};
		var validateEmail = (rule, value, callback) => {
			if(!value){
				callback();
			} else if (!isEmail(value)) {
				callback(new Error("请输入正确的邮箱地址"));
			} else {
				callback();
			}
		};
		var validateNumber = (rule, value, callback) => {
			if(!value){
				callback();
			} else if (!isNumber(value)) {
				callback(new Error("请输入数字"));
			} else {
				callback();
			}
		};
		var validateIntNumber = (rule, value, callback) => {
			if(!value){
				callback();
			} else if (!isIntNumer(value)) {
				callback(new Error("请输入整数"));
			} else {
				callback();
			}
		};
		return {
			id: '',
			type: '',
			
			
			ro:{
				qihuodaima : false,
				qihuomingcheng : false,
				qihuoleixing : false,
				gongsimingcheng : false,
				qihuozhangshi : false,
				jiage : false,
				jiaoyijiage : false,
				tupian : false,
				kaishishijian : false,
				qihuojieshao : false,
				zhanghao : false,
				fuzerenxingming : false,
				lianxidianhua : false,
				clicktime : false,
				discussnum : false,
				storeupnum : false,
			},
			
			
			ruleForm: {
				qihuodaima: this.getUUID(),
				qihuomingcheng: '',
				qihuoleixing: '',
				gongsimingcheng: '',
				qihuozhangshi: '',
				jiage: '',
				jiaoyijiage: '',
				tupian: '',
				kaishishijian: '',
				qihuojieshao: '',
				zhanghao: '',
				fuzerenxingming: '',
				lianxidianhua: '',
				clicktime: '',
			},
		
			qihuoleixingOptions: [],

			
			rules: {
				qihuodaima: [
					{ required: true, message: '期货代码不能为空', trigger: 'blur' },
				],
				qihuomingcheng: [
					{ required: true, message: '期货名称不能为空', trigger: 'blur' },
				],
				qihuoleixing: [
					{ required: true, message: '期货类型不能为空', trigger: 'blur' },
				],
				gongsimingcheng: [
				],
				qihuozhangshi: [
				],
				jiage: [
					{ required: true, message: '当前价格不能为空', trigger: 'blur' },
					{ validator: validateNumber, trigger: 'blur' },
				],
				jiaoyijiage: [
					{ required: true, message: '交易价格不能为空', trigger: 'blur' },
					{ validator: validateNumber, trigger: 'blur' },
				],
				tupian: [
				],
				kaishishijian: [
				],
				qihuojieshao: [
				],
				zhanghao: [
				],
				fuzerenxingming: [
				],
				lianxidianhua: [
					{ validator: validateMobile, trigger: 'blur' },
				],
				clicktime: [
				],
				discussnum: [
					{ validator: validateIntNumber, trigger: 'blur' },
				],
				storeupnum: [
					{ validator: validateIntNumber, trigger: 'blur' },
				],
			}
		};
	},
	props: ["parent"],
	computed: {



	},
    components: {
    },
	created() {
	},
	methods: {
		
		// 下载
		download(file){
			window.open(`${file}`)
		},
		// 初始化
		init(id,type) {
			if (id) {
				this.id = id;
				this.type = type;
			}
			if(this.type=='info'||this.type=='else'){
				this.info(id);
			}else if(this.type=='logistics'){
				this.logistics=false;
				this.info(id);
			}else if(this.type=='cross'){
				var obj = this.$storage.getObj('crossObj');
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
						if(o=='gongsimingcheng'){
							this.ruleForm.gongsimingcheng = obj[o];
							this.ro.gongsimingcheng = true;
							continue;
						}
						if(o=='qihuozhangshi'){
							this.ruleForm.qihuozhangshi = obj[o];
							this.ro.qihuozhangshi = true;
							continue;
						}
						if(o=='jiage'){
							this.ruleForm.jiage = obj[o];
							this.ro.jiage = true;
							continue;
						}
						if(o=='jiaoyijiage'){
							this.ruleForm.jiaoyijiage = obj[o];
							this.ro.jiaoyijiage = true;
							continue;
						}
						if(o=='tupian'){
							this.ruleForm.tupian = obj[o];
							this.ro.tupian = true;
							continue;
						}
						if(o=='kaishishijian'){
							this.ruleForm.kaishishijian = obj[o];
							this.ro.kaishishijian = true;
							continue;
						}
						if(o=='qihuojieshao'){
							this.ruleForm.qihuojieshao = obj[o];
							this.ro.qihuojieshao = true;
							continue;
						}
						if(o=='zhanghao'){
							this.ruleForm.zhanghao = obj[o];
							this.ro.zhanghao = true;
							continue;
						}
						if(o=='fuzerenxingming'){
							this.ruleForm.fuzerenxingming = obj[o];
							this.ro.fuzerenxingming = true;
							continue;
						}
						if(o=='lianxidianhua'){
							this.ruleForm.lianxidianhua = obj[o];
							this.ro.lianxidianhua = true;
							continue;
						}
						if(o=='clicktime'){
							this.ruleForm.clicktime = obj[o];
							this.ro.clicktime = true;
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
				
















			}
			
			
			// 获取用户信息
			this.$http({
				url: `${this.$storage.get('sessionTable')}/session`,
				method: "get"
			}).then(({ data }) => {
				if (data && data.code === 0) {
					
					var json = data.data;
					if(((json.zhanghao!=''&&json.zhanghao) || json.zhanghao==0) && this.$storage.get("role")!="管理员"){
						this.ruleForm.zhanghao = json.zhanghao
						this.ro.zhanghao = true;
					}
					if(((json.fuzerenxingming!=''&&json.fuzerenxingming) || json.fuzerenxingming==0) && this.$storage.get("role")!="管理员"){
						this.ruleForm.fuzerenxingming = json.fuzerenxingming
						this.ro.fuzerenxingming = true;
					}
					if(((json.lianxidianhua!=''&&json.lianxidianhua) || json.lianxidianhua==0) && this.$storage.get("role")!="管理员"){
						this.ruleForm.lianxidianhua = json.lianxidianhua
						this.ro.lianxidianhua = true;
					}
				} else {
					this.$message.error(data.msg);
				}
			});
			
            this.$http({
				url: `option/qihuoleixing/qihuoleixing`,
				method: "get"
            }).then(({ data }) => {
				if (data && data.code === 0) {
					this.qihuoleixingOptions = data.data;
				} else {
					this.$message.error(data.msg);
				}
            });
			
		},
    // 多级联动参数

    info(id) {
      this.$http({
        url: `qihuoxinxi/info/${id}`,
        method: "get"
      }).then(({ data }) => {
        if (data && data.code === 0) {
        this.ruleForm = data.data;
        //解决前台上传图片后台不显示的问题
        let reg=new RegExp('../../../upload','g')//g代表全部
        this.ruleForm.qihuojieshao = this.ruleForm.qihuojieshao.replace(reg,'../../../python206jhypi/upload');
        } else {
          this.$message.error(data.msg);
        }
      });
    },


    // 提交
    onSubmit() {
		if(this.ruleForm.qihuodaima) {
			this.ruleForm.qihuodaima = String(this.ruleForm.qihuodaima)
		}
















	if(this.ruleForm.tupian!=null) {
		this.ruleForm.tupian = this.ruleForm.tupian.replace(new RegExp(this.$base.url,"g"),"");
	}

















var objcross = this.$storage.getObj('crossObj');

      //更新跨表属性
       var crossuserid;
       var crossrefid;
       var crossoptnum;
       if(this.type=='cross'){
                var statusColumnName = this.$storage.get('statusColumnName');
                var statusColumnValue = this.$storage.get('statusColumnValue');
                if(statusColumnName!='') {
                        var obj = this.$storage.getObj('crossObj');
                       if(statusColumnName && !statusColumnName.startsWith("[")) {
                               for (var o in obj){
                                 if(o==statusColumnName){
                                   obj[o] = statusColumnValue;
                                 }
                               }
                               var table = this.$storage.get('crossTable');
                             this.$http({
                                 url: `${table}/update`,
                                 method: "post",
                                 data: obj
                               }).then(({ data }) => {});
                       } else {
                               crossuserid=this.$storage.get('userid');
                               crossrefid=obj['id'];
                               crossoptnum=this.$storage.get('statusColumnName');
                               crossoptnum=crossoptnum.replace(/\[/,"").replace(/\]/,"");
                        }
                }
        }
       this.$refs["ruleForm"].validate(valid => {
         if (valid) {
		 if(crossrefid && crossuserid) {
			 this.ruleForm.crossuserid = crossuserid;
			 this.ruleForm.crossrefid = crossrefid;
			let params = { 
				page: 1, 
				limit: 10, 
				crossuserid:this.ruleForm.crossuserid,
				crossrefid:this.ruleForm.crossrefid,
			} 
			this.$http({ 
				url: "qihuoxinxi/page", 
				method: "get", 
				params: params 
			}).then(({ 
				data 
			}) => { 
				if (data && data.code === 0) { 
				       if(data.data.total>=crossoptnum) {
					     this.$message.error(this.$storage.get('tips'));
					       return false;
				       } else {
					 this.$http({
					   url: `qihuoxinxi/${!this.ruleForm.id ? "save" : "update"}`,
					   method: "post",
					   data: this.ruleForm
					 }).then(({ data }) => {
					   if (data && data.code === 0) {
					     this.$message({
					       message: "操作成功",
					       type: "success",
					       duration: 1500,
					       onClose: () => {
						 this.parent.showFlag = true;
						 this.parent.addOrUpdateFlag = false;
						 this.parent.qihuoxinxiCrossAddOrUpdateFlag = false;
						 this.parent.search();
						 this.parent.contentStyleChange();
					       }
					     });
					   } else {
					     this.$message.error(data.msg);
					   }
					 });

				       }
				} else { 
				} 
			});
		 } else {
			 this.$http({
			   url: `qihuoxinxi/${!this.ruleForm.id ? "save" : "update"}`,
			   method: "post",
			   data: this.ruleForm
			 }).then(({ data }) => {
			   if (data && data.code === 0) {
			     this.$message({
			       message: "操作成功",
			       type: "success",
			       duration: 1500,
			       onClose: () => {
				 this.parent.showFlag = true;
				 this.parent.addOrUpdateFlag = false;
				 this.parent.qihuoxinxiCrossAddOrUpdateFlag = false;
				 this.parent.search();
				 this.parent.contentStyleChange();
			       }
			     });
			   } else {
			     this.$message.error(data.msg);
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
      this.parent.showFlag = true;
      this.parent.addOrUpdateFlag = false;
      this.parent.qihuoxinxiCrossAddOrUpdateFlag = false;
      this.parent.contentStyleChange();
    },
    tupianUploadChange(fileUrls) {
	    this.ruleForm.tupian = fileUrls;
    },
  }
};
</script>
<style lang="scss" scoped>
	.amap-wrapper {
		width: 100%;
		height: 500px;
	}
	
	.search-box {
		position: absolute;
	}
	
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
	
	.add-update-preview /deep/ .upload .upload-img {
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
	
	.add-update-preview .btn .btn1 {
				border: 0px solid rgba(126, 96, 16, .2);
				cursor: pointer;
				padding: 0 20px;
				margin: 0px 4px;
				color: #fff;
				display: inline-block;
				font-size: 16px;
				line-height: 24px;
				border-radius: 4px;
				outline: none;
				background: #A8BDCF;
				width: auto;
				height: 40px;
			}
	
	.add-update-preview .btn .btn1:hover {
				opacity: 0.8;
			}
	
	.add-update-preview .btn .btn2 {
				border: 0px solid rgba(126, 96, 16, .2);
				cursor: pointer;
				border-radius: 4px;
				padding: 0 20px;
				margin: 0px 4px;
				outline: none;
				color: #fff;
				background: #428bca;
				width: auto;
				font-size: 16px;
				line-height: 24px;
				height: 40px;
			}
	
	.add-update-preview .btn .btn2:hover {
				opacity: 0.8;
			}
	
	.add-update-preview .btn .btn3 {
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
	
	.add-update-preview .btn .btn3:hover {
				opacity: 0.8;
			}
	
	.add-update-preview .btn .btn4 {
				border: 0px solid rgba(126, 96, 16, .2);
				cursor: pointer;
				border-radius: 4px;
				padding: 0 20px;
				margin: 0px 4px;
				outline: none;
				color: #fff;
				background: #FF6B6B;
				width: auto;
				font-size: 16px;
				line-height: 24px;
				height: 40px;
			}
	
	.add-update-preview .btn .btn4:hover {
				opacity: 0.8;
			}
	
	.add-update-preview .btn .btn5 {
				border: 0px solid rgba(126, 96, 16, .2);
				cursor: pointer;
				border-radius: 3px;
				padding: 0 20px;
				margin: 4px;
				outline: none;
				color: #fff;
				background: #65C3DF;
				width: auto;
				font-size: 16px;
				line-height: 24px;
				height: 40px;
			}
	
	.add-update-preview .btn .btn5:hover {
				opacity: 0.8;
			}
</style>
