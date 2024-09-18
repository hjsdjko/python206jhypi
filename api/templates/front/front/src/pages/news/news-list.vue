<template>
<div>
	<div :style='{"border":"1px solid #D8D8D8","padding":"16px 20px 10px","margin":"65px auto 20px","borderRadius":"0","background":"transparent","borderWidth":"0 0 3px","width":"68%"}' class="breadcrumb-preview">
		<el-breadcrumb :separator="'》'" :style='{"fontSize":"14px","lineHeight":"1"}'>
			<el-breadcrumb-item class="item1"><a href="/index/home">首页</a></el-breadcrumb-item>
			<el-breadcrumb-item class="item2" v-for="(item, index) in breadcrumbItem" :key="index"><a href="/index/home">{{item.name}}</a></el-breadcrumb-item>
		</el-breadcrumb>
	</div>
	
	<div class="news-preview-pv" :style='{"margin":"10px auto","alignItems":"flex-start","flexWrap":"wrap","background":"#F6F6F6","display":"flex","width":"68%","position":"relative"}'>
		<el-form :inline="true" :model="formSearch" class="list-form-pv" :style='{"padding":"10px 0","alignItems":"center","background":"transparent","display":"flex","width":"20%","position":"absolute","justifyContent":"center","height":"auto"}'>
			<el-form-item :style='{"width":"90%","margin":"0 0"}'>
				<el-input v-model="title" placeholder="标题"></el-input>
			</el-form-item>
			<el-button type="primary" @click="getNewsList(1)" :style='{"cursor":"pointer","border":"0","padding":"0px 15px","margin":"0 0 0 -20px","color":"#fff","outline":"none","borderRadius":"50px","background":"#AD8936","width":"auto","fontSize":"14px","lineHeight":"42px","height":"42px","zIndex":"9"}'>
				<span class="icon iconfont icon-chakan14" :style='{"color":"#fff","margin":"0 10px 0 0","fontSize":"14px"}'></span>
				搜索
			</el-button>
		</el-form>
		
		<!-- category -->
		<div class="category" :style='{"padding":"0","margin":"70px 0","flexWrap":"wrap","background":"#fff","display":"flex","width":"20%","height":"auto"}'>
		  <div class="item" @click="categoryClick(0)" :class="categoryIndex == 0 ? 'active' : ''">全部</div>
		  <div v-for="(item,index) in categoryList" @click="categoryClick(index+1)" :key="index" class="item" :class="categoryIndex == index+1 ? 'active' : ''">{{item.typename}}</div>
		</div>
	
				
				
				
				
				
				
				
				
				<div :style='{"padding":"0 0 20px","margin":"0 0 0 2%","flexWrap":"wrap","background":"transparent","display":"flex","width":"78%","justifyContent":"space-between","height":"auto"}' class="list9 index-pv1">
		  <div v-for="item,index in newsList" :key="index" @click="toNewsDetail(item)" :style='{"width":"32%","margin":"0 0 20px","overflow":"hidden","position":"relative","background":"#fff","height":"350px"}' class="item animation-box">
		    <img class="image" :src="baseUrl + item.picture" >
		    <div class="info">
		      <div :style='{"width":"100%","lineHeight":"32px","fontSize":"16px","color":"#fff","order":"1"}'>{{item.title}}</div>
		      <div :style='{"overflow":"hidden","color":"#fff","display":"-webkit-box","width":"100%","lineHeight":"21px","fontSize":"14px","textOverflow":"ellipsis","-webkit-box-orient":"vertical","-webkit-line-clamp":"3","order":"2"}'>{{item.introduction}}</div>
		      <div :style='{"width":"60%","padding":"0","display":"inline-block","order":"7"}'>
		        <span class="icon iconfont icon-shijian21" :style='{"margin":"0 2px 0 0","lineHeight":"1.5","fontSize":"14px","color":"#fff"}'></span>
		        <span :style='{"color":"#fff","lineHeight":"1.5","fontSize":"14px"}'>{{item.addtime}}</span>
		      </div>
		      <div :style='{"width":"40%","padding":"0","display":"inline-block","order":"6"}'>
		        <span class="icon iconfont icon-geren16" :style='{"margin":"0 2px 0 0","lineHeight":"1.5","fontSize":"14px","color":"#fff"}'></span>
		        <span :style='{"color":"#fff","lineHeight":"1.5","fontSize":"14px"}'>{{item.name}}</span>
		      </div>
		      <div :style='{"width":"calc(100% / 3)","padding":"0","display":"inline-block","order":"3"}'>
		        <span class="icon iconfont icon-zan10" :style='{"margin":"0 2px 0 0","lineHeight":"1.5","fontSize":"14px","color":"#fff"}'></span>
		        <span :style='{"color":"#fff","lineHeight":"1.5","fontSize":"14px"}'>{{item.thumbsupnum}}</span>
		      </div>
		      <div :style='{"width":"calc(100% / 3)","padding":"0","display":"inline-block","order":"4"}'>
		        <span class="icon iconfont icon-shoucang10" :style='{"margin":"0 2px 0 0","lineHeight":"1.5","fontSize":"14px","color":"#fff"}'></span>
		        <span :style='{"color":"#fff","lineHeight":"1.5","fontSize":"14px"}'>{{item.storeupnum}}</span>
		      </div>
		      <div :style='{"width":"calc(100% / 3)","padding":"0","display":"inline-block","order":"5"}'>
		        <span class="icon iconfont icon-chakan9" :style='{"margin":"0 2px 0 0","lineHeight":"1.5","fontSize":"14px","color":"#fff"}'></span>
		        <span :style='{"color":"#fff","lineHeight":"1.5","fontSize":"14px"}'>{{item.clicknum}}</span>
		      </div>
		      <div :style='{"border":"1px solid #fff","padding":"0 10px","color":"#fff","textAlign":"center","background":"transparent","display":"block","width":"80px","fontSize":"14px","lineHeight":"32px","order":"7"}' class="tags">查看详情</div>
		    </div>
		  </div>
		</div>
				
		<el-pagination
		  background
		  id="pagination" class="pagination"
		  :pager-count="7"
		  :page-size="pageSize"
		  :page-sizes="pageSizes"
		  prev-text="<"
		  next-text=">"
		  :hide-on-single-page="true"
		  :layout='["prev","pager","next"].join()'
		  :total="total"
		  :style='{"width":"100%","padding":"0 16%","margin":"10px auto","whiteSpace":"nowrap","color":"#333","fontWeight":"500"}'
		  @current-change="curChange"
		  @prev-click="prevClick"
		  @next-click="nextClick"
		></el-pagination>

		<!-- 热门信息 -->
		<div class="hot" :style='{"boxShadow":"none","left":"0","background":"#fff","bottom":"182px","width":"20%","position":"absolute","height":"auto"}'>
		  <div :style='{"color":"#AD8936","textAlign":"center","background":"#fff","width":"100%","lineHeight":"44px","fontSize":"18px","fontWeight":"bold"}'>热门信息</div>
		  <div :style='{"width":"100%","padding":"0 0 5px 0","background":"#fff","height":"auto"}'>
		    <div v-for="item in hotList" :key="item.id" :style='{"padding":"10px","flexWrap":"wrap","background":"#fff","flexDirection":"column","display":"flex","width":"100%","height":"100px"}' @click="toNewsDetail(item)">
		      <img :style='{"width":"80px","objectFit":"cover","display":"block","height":"80px"}' :src="baseUrl + item.picture" alt="">
		      <div :style='{"padding":"4px 5px 0","overflow":"hidden","whiteSpace":"nowrap","color":"#000","alignItems":"center","display":"inline-block","width":"calc(100% - 80px)","lineHeight":"1","fontSize":"14px","textOverflow":"ellipsis","height":"50%"}'>{{ item.title }}</div>
		      <div :style='{"padding":"0 5px","color":"#9e9e9e","alignItems":"center","display":"flex","lineHeight":"12px","fontSize":"12px","height":"50%"}'>{{item.addtime}}</div>
		    </div>
		  </div>
		</div>
		<!-- 最新动态 -->
		<div class="news" :style='{"width":"100%","background":"#fff","height":"auto"}'>
		  <div :style='{"padding":"0 20px","color":"#AD8936","background":"#fff","width":"100%","lineHeight":"44px","fontSize":"18px","fontWeight":"bld"}'>最新动态</div>
		  <div :style='{"padding":"0","flexWrap":"wrap","background":"#fff","display":"flex","width":"100%","justifyContent":"space-between","height":"auto"}'>
		    <div v-for="item in recommendList" :key="item.id" :style='{"padding":"10px","flexWrap":"wrap","background":"#fff","flexDirection":"column","display":"flex","width":"23%","height":"100px"}' @click="toNewsDetail(item)">
		      <img :style='{"width":"80px","objectFit":"cover","display":"block","height":"80px"}' :src="baseUrl + item.picture" alt="">
		      <div :style='{"padding":"0 10px","overflow":"hidden","whiteSpace":"nowrap","color":"#9E9E9E","alignItems":"center","display":"inline-block","width":"calc(100% - 80px)","lineHeight":"32px","fontSize":"16px","textOverflow":"ellipsis","height":"50%"}'>{{ item.title }}</div>
		      <div :style='{"padding":"0 10px","color":"#9E9E9E","alignItems":"center","display":"flex","width":"calc(100% - 80px)","lineHeight":"12px","fontSize":"14px","height":"50%"}'>{{item.addtime}}</div>
		    </div>
		  </div>
		</div>
	</div>
</div>
</template>

<script>
	export default {
		//数据集合
		data() {
			return {
				baseUrl: this.$config.baseUrl,
				breadcrumbItem: [
				  {
					name: '资讯信息'
				  }
				],
				newsList: [],
				total: 1,
				pageSize: 10,
				pageSizes: [10,20,30,50],
				totalPage: 1,
				layouts: '',
				title: '',
				categoryIndex: 0,
				categoryList: [],
				hotList: [],
				recommendList: [],
			}
		},
		created() {
			this.getCategoryList()
			this.getNewsList(1);
			this.getHotList()
			if(localStorage.getItem('Token')) {
				this.getRecommendList()
			}
		},
		//方法集合
		methods: {
			getCategoryList(){
				this.$http.get('newstype/list', {}).then(res => {
					if (res.data.code == 0) {
						this.categoryList = res.data.data.list
					}
				});
			},
			categoryClick(index) {
				this.categoryIndex = index
				this.getNewsList()
			},
			getNewsList(page) {
				let params = {page, limit: this.pageSize,sort:'addtime',order:'desc'};
				let searchWhere = {};
				if(this.title != '') searchWhere.title = '%' + this.title + '%';
				if(this.categoryIndex!=0){
					searchWhere.typename = this.categoryList[this.categoryIndex - 1].typename
				}
				this.$http.get('news/list', {params: Object.assign(params, searchWhere)}).then(res => {
					if (res.data.code == 0) {
						this.newsList = res.data.data.list;
						this.total = res.data.data.total;
						this.pageSize = Number(res.data.data.pageSize);
						this.pageSizes = [this.pageSize, this.pageSize*2, this.pageSize*3, this.pageSize*5];
						this.totalPage = res.data.data.totalPage;
					}
				});
			},
			getHotList(){
				let params = {page:1, limit: 4,sort:'addtime',order:'desc'};
				this.$http.get('news/autoSort', {params: params}).then(res => {
					if (res.data.code == 0) {
						this.hotList = res.data.data.list;
					}
				});
			},
			getRecommendList(){
				let params = {page:1, limit: 4,sort:'addtime',order:'desc'};
				this.$http.get('news/autoSort2', {params: params}).then(res => {
					if (res.data.code == 0) {
						this.recommendList = res.data.data.list;
					}
				});
			},
			curChange(page) {
				this.getNewsList(page);
			},
			prevClick(page) {
				this.getNewsList(page);
			},
			nextClick(page) {
				this.getNewsList(page);
			},
			toNewsDetail(item) {
				this.$router.push({path: '/index/newsDetail', query: {id: item.id}});
			}
		}
	}
</script>

<style rel="stylesheet/scss" lang="scss" scoped>
	.breadcrumb-preview .el-breadcrumb /deep/ .el-breadcrumb__separator {
		margin: 0 9px;
		color: #ccc;
		font-weight: 500;
	}
	
	.breadcrumb-preview .el-breadcrumb .item1 /deep/ .el-breadcrumb__inner a {
		color: #9E9E9E;
		display: inline-block;
	}
	
	.breadcrumb-preview .el-breadcrumb .item2 /deep/ .el-breadcrumb__inner a {
		color: #9E9E9E;
		display: inline-block;
	}
	
	.news-wrap {
	  width: 1000px;
	  margin: 0 auto;
	}
	.news-item {
	  height: 200px;
	  width: auto;
	  margin-bottom: 30px;
	  cursor: pointer;
	}
	.news-item-text {
	  width: calc(100% - 215px);
	  display: inline-block;
	  vertical-align: top;
	  margin-left: 15px;
	}
	.news-item-text-title {
	  font-size: 16px;
	  margin-bottom: 15px;
	}
	.news-item-text-intro {
	  font-size: 14px;
	  color: #666;
	}
	
	.hide1 {
		text-overflow: ellipsis;
		display: -webkit-box;
		-webkit-line-clamp: 1;
		-webkit-box-orient: vertical;
		overflow:hidden;
		text-overflow:ellipsis;
	}
	.hide2 {
		text-overflow: ellipsis;
		display: -webkit-box;
		-webkit-line-clamp: 2;
		-webkit-box-orient: vertical;
		overflow:hidden;
		text-overflow:ellipsis;
	}
	.hide3 {
		text-overflow: ellipsis;
		display: -webkit-box;
		-webkit-line-clamp: 3;
		-webkit-box-orient: vertical;
		overflow:hidden;
		text-overflow:ellipsis;
	}
	
	.index-pv1 .animation-box {
		transform: rotate(0deg) scale(1) skew(0deg, 0deg) translate3d(0px, 0px, 0px);
		z-index: initial;
	}
	
	.index-pv1 .animation-box:hover {
				transform: rotate(0deg) scale(1) skew(0deg, 0deg) translate3d(0px, 0px, 0px);
				-webkit-perspective: 1000px;
				background: #AD8936;
				perspective: 1000px;
				transition: 0.3s;
				z-index: 1;
	}
	
	.index-pv1 .animation-box img {
		transform: rotate(0deg) scale(1) skew(0deg, 0deg) translate3d(0px, 0px, 0px);
	}
	
	.index-pv1 .animation-box img:hover {
				transform: rotate(0deg) scale(1) skew(0deg, 0deg) translate3d(0px, 0px, 0px);
				-webkit-perspective: 1000px;
				perspective: 1000px;
				transition: 0.3s;
			}
		
	#pagination.el-pagination /deep/ .el-pagination__total {
				margin: 0 10px 0 0;
				color: #666;
				font-weight: 400;
				display: inline-block;
				vertical-align: top;
				font-size: 13px;
				line-height: 28px;
				height: 28px;
			}
	
	#pagination.el-pagination /deep/ .btn-prev {
				border: none;
				border-radius: 2px;
				padding: 0;
				margin: 0 5px;
				color: #666;
				background: #f4f4f5;
				display: inline-block;
				vertical-align: top;
				font-size: 13px;
				line-height: 28px;
				min-width: 35px;
				height: 28px;
			}
	
	#pagination.el-pagination /deep/ .btn-next {
				border: none;
				border-radius: 2px;
				padding: 0;
				margin: 0 5px;
				color: #666;
				background: #f4f4f5;
				display: inline-block;
				vertical-align: top;
				font-size: 13px;
				line-height: 28px;
				min-width: 35px;
				height: 28px;
			}
	
	#pagination.el-pagination /deep/ .btn-prev:disabled {
				border: none;
				cursor: not-allowed;
				border-radius: 2px;
				padding: 0;
				margin: 0 5px;
				color: #C0C4CC;
				background: #f4f4f5;
				display: inline-block;
				vertical-align: top;
				font-size: 13px;
				line-height: 28px;
				height: 28px;
			}
	
	#pagination.el-pagination /deep/ .btn-next:disabled {
				border: none;
				cursor: not-allowed;
				border-radius: 2px;
				padding: 0;
				margin: 0 5px;
				color: #C0C4CC;
				background: #f4f4f5;
				display: inline-block;
				vertical-align: top;
				font-size: 13px;
				line-height: 28px;
				height: 28px;
			}
	
	#pagination.el-pagination /deep/ .el-pager {
				padding: 0;
				margin: 0;
				display: inline-block;
				vertical-align: top;
			}
	
	#pagination.el-pagination /deep/ .el-pager .number {
				cursor: pointer;
				padding: 0 4px;
				margin: 0 5px;
				color: #666;
				display: inline-block;
				vertical-align: top;
				font-size: 13px;
				line-height: 28px;
				border-radius: 2px;
				background: #f4f4f5;
				text-align: center;
				min-width: 30px;
				height: 28px;
			}
	
	#pagination.el-pagination /deep/ .el-pager .number:hover {
				cursor: pointer;
				padding: 0 4px;
				margin: 0 5px;
				color: #fff;
				display: inline-block;
				vertical-align: top;
				font-size: 13px;
				line-height: 28px;
				border-radius: 2px;
				background: #AD8936;
				text-align: center;
				min-width: 30px;
				height: 28px;
			}
	
	#pagination.el-pagination /deep/ .el-pager .number.active {
				cursor: default;
				padding: 0 4px;
				margin: 0 5px;
				color: #FFF;
				display: inline-block;
				vertical-align: top;
				font-size: 13px;
				line-height: 28px;
				border-radius: 2px;
				background: #AD8936;
				text-align: center;
				min-width: 30px;
				height: 28px;
			}
	
	#pagination.el-pagination /deep/ .el-pagination__sizes {
				display: inline-block;
				vertical-align: top;
				font-size: 13px;
				line-height: 28px;
				height: 28px;
			}
	
	#pagination.el-pagination /deep/ .el-pagination__sizes .el-input {
				margin: 0 5px;
				width: 100px;
				position: relative;
			}
	
	#pagination.el-pagination /deep/ .el-pagination__sizes .el-input .el-input__inner {
				border: 1px solid #DCDFE6;
				cursor: pointer;
				padding: 0 25px 0 8px;
				color: #606266;
				display: inline-block;
				font-size: 13px;
				line-height: 28px;
				border-radius: 3px;
				outline: 0;
				background: #FFF;
				width: 100%;
				text-align: center;
				height: 28px;
			}
	
	#pagination.el-pagination /deep/ .el-pagination__sizes .el-input span.el-input__suffix {
				top: 0;
				position: absolute;
				right: 0;
				height: 100%;
			}
	
	#pagination.el-pagination /deep/ .el-pagination__sizes .el-input .el-input__suffix .el-select__caret {
				cursor: pointer;
				color: #C0C4CC;
				width: 25px;
				font-size: 14px;
				line-height: 28px;
				text-align: center;
			}
	
	#pagination.el-pagination /deep/ .el-pagination__jump {
				margin: 0 0 0 24px;
				color: #606266;
				display: inline-block;
				vertical-align: top;
				font-size: 13px;
				line-height: 28px;
				height: 28px;
			}
	
	#pagination.el-pagination /deep/ .el-pagination__jump .el-input {
				border-radius: 3px;
				padding: 0 2px;
				margin: 0 2px;
				display: inline-block;
				width: 50px;
				font-size: 14px;
				line-height: 18px;
				position: relative;
				text-align: center;
				height: 28px;
			}
	
	#pagination.el-pagination /deep/ .el-pagination__jump .el-input .el-input__inner {
				border: 1px solid #DCDFE6;
				cursor: pointer;
				padding: 0 3px;
				color: #606266;
				display: inline-block;
				font-size: 14px;
				line-height: 28px;
				border-radius: 3px;
				outline: 0;
				background: #FFF;
				width: 100%;
				text-align: center;
				height: 28px;
			}
	
	.news-preview-pv .el-input /deep/ .el-input__inner {
				border: 0;
				border-radius: 50px 0 0 50px;
				padding: 0 10px;
				margin: 0;
				outline: none;
				color: #333;
				width: 100%;
				font-size: 14px;
				line-height: 42px;
				height: 42px;
			}
	
	.news-preview-pv .category .item {
				cursor: pointer;
				margin: 0;
				color: #9E9E9E;
				display: flex;
				font-size: 16px;
				line-height: 36px;
				border-radius: 0;
				background: #fff;
				width: 100%;
				justify-content: center;
				align-items: center;
				text-align: center;
				height: 50px;
			}
	
	.news-preview-pv .category .item:hover {
				color: #000;
				background: transparent;
			}
	
	.news-preview-pv .category .item.active {
				border: 1px solid #D8D8D8;
				color: #000;
				background: transparent;
				border-width: 0 0 1px;
			}
	
	.news-preview-pv .list9 .item .image {
				padding: 20px;
				object-fit: cover;
				display: block;
				width: 100%;
				transition: 0.3s;
				height: 100%;
			}
	
	.news-preview-pv .list9 .item:hover .image {
				transform: scale(1);
			}
	
	.news-preview-pv .list9 .item .info {
				padding: 20px 40px;
				left: 20px;
				bottom: -100%;
				background: rgba(0,0,0,.3);
				display: flex;
				width: calc(100% - 40px);
				justify-content: center;
				align-items: flex-start;
				position: absolute;
				flex-wrap: wrap;
				transition: 0.3s;
				height: calc(100% - 40px);
			}
	
	.news-preview-pv .list9 .item:hover .info {
				bottom: 20px;
			}
</style>
