<template>
<div class="home-preview" :style='{"width":"100%","margin":"80px auto 0","flexDirection":"column","display":"flex"}'>



		<!-- 关于我们 -->
		<div id="about" class="animate__animated" :style='{"padding":"30px 0 150px","boxShadow":"0 0px 0px rgba(255, 255, 255, .3)","margin":"0 0 0","flexWrap":"wrap","background":"url(http://codegen.caihongy.cn/20231025/b7aa459607b743c587451d684aa31a30.png)","display":"flex","width":"100%","backgroundSize":"cover","backgroundPosition":"center center","backgroundRepeat":"no-repeat","height":"auto","order":"2"}'>
		  <div :style='{"padding":"44px 90px 0 0","margin":"0 auto","color":"#fff","textAlign":"center","background":"url(http://codegen.caihongy.cn/20231025/8439cbf5f69143a1b4d8d164de9bc0a2.png)","width":"450px","fontSize":"32px","backgroundSize":"cover","backgroundPosition":"center center","backgroundRepeat":"no-repeat","height":"104px"}'>{{aboutUsDetail.title}}</div>
		  <div :style='{"padding":"0","margin":" -85px 0 110px 0px","color":"#fff","textAlign":"center","width":"100%","lineHeight":"1","fontSize":"18px"}'>{{aboutUsDetail.subtitle}}</div>
		  <div :style='{"width":"100%","padding":"0 10px","flexWrap":"wrap","display":"flex","height":"auto"}'>
		    <img :style='{"margin":"0 10px","objectFit":"cover","bottom":"90px","display":"block","width":"350px","position":"absolute","right":"20%","height":"500px"}' :src="baseUrl + aboutUsDetail.picture1">
		    <img :style='{"margin":"0 10px","objectFit":"cover","flex":1,"display":"none","height":"120px"}' :src="baseUrl + aboutUsDetail.picture2">
		    <img :style='{"margin":"0 10px","objectFit":"cover","flex":1,"display":"none","height":"120px"}' :src="baseUrl + aboutUsDetail.picture3">
		  </div>
		  <div :style='{"border":"4px solid #fff","padding":"90px 24% 160px 100px","margin":"40px 16% 0","color":"#fff","display":"-webkit-box","overflow":"hidden","width":"78%","lineHeight":"2","fontSize":"16px","textOverflow":"ellips","-webkit-box-orient":"vertical","-webkit-line-clamp":"4","height":"auto"}' v-html="aboutUsDetail.content"></div>
		  <div :style='{"width":"285px","background":"url(http://codegen.caihongy.cn/20201114/7856ba26477849ea828f481fa2773a95.jpg) 0% 0% / cover no-repeat","display":"none","height":"100px"}' />
		  <div :style='{"width":"285px","background":"url(http://codegen.caihongy.cn/20201114/7856ba26477849ea828f481fa2773a95.jpg) 0% 0% / cover no-repeat","display":"none","height":"100px"}' />
		  <div :style='{"width":"285px","background":"url(http://codegen.caihongy.cn/20201114/7856ba26477849ea828f481fa2773a95.jpg) 0% 0% / cover no-repeat","display":"none","height":"100px"}' />
		  <div :style='{"width":"285px","background":"url(http://codegen.caihongy.cn/20201114/7856ba26477849ea828f481fa2773a95.jpg) 0% 0% / cover no-repeat","display":"none","height":"100px"}' />
		  <div :style='{"border":"2px solid #fff","margin":"10px auto","textAlign":"center","left":"calc(16% + 100px)","background":"transparent","bottom":"27%","display":"block","width":"220px","lineHeight":"60px","position":"absolute","height":"60px"}' @click="toDetail('aboutusDetail',aboutUsDetail)">
		    <span :style='{"color":"#f5f5f5","fontSize":"18px"}'>更多</span>
		    <span class="icon iconfont icon-gengduo1" :style='{"color":"#f5f5f5","fontSize":"18px"}'></span>
		  </div>
		</div>
		<!-- 关于我们 -->

		<!-- 系统简介 -->
		<div id="system" class="animate__animated" :style='{"padding":"50px 0 160px","boxShadow":"0 1px 6px rgba(255, 255, 255, .3)","margin":"0 0 10px","display":"flex","flexWrap":"wrap","background":"url(http://codegen.caihongy.cn/20231025/d7494b7e1ab04022bb82c7952a918407.png)","width":"100%","backgroundSize":"cover","backgroundPosition":"center center","position":"relative","backgroundRepeat":"no-repeat","height":"auto","order":"4"}'>
		  <div :style='{"padding":"44px 90px 0 0","margin":"0 auto","color":"#fff","textAlign":"center","background":"url(http://codegen.caihongy.cn/20231025/8439cbf5f69143a1b4d8d164de9bc0a2.png)","width":"450px","fontSize":"32px","backgroundSize":"cover","backgroundPosition":"center center","backgroundRepeat":"no-repeat","height":"104px"}'>{{systemIntroductionDetail.title}}</div>
		  <div :style='{"width":"100%","margin":" -85px 0 110px 0px","lineHeight":"1","fontSize":"18px","color":"#fff","textAlign":"center"}'>{{systemIntroductionDetail.subtitle}}</div>
		  <div :style='{"width":"100%","padding":"0 10px","flexWrap":"wrap","display":"none","height":"auto"}'>
		    <img :style='{"margin":"0 10px","objectFit":"cover","flex":1,"display":"block","height":"120px"}' :src="baseUrl + systemIntroductionDetail.picture1">
		    <img :style='{"margin":"0 10px","objectFit":"cover","flex":1,"display":"block","height":"120px"}' :src="baseUrl + systemIntroductionDetail.picture2">
		    <img :style='{"margin":"0 10px","objectFit":"cover","flex":1,"display":"block","height":"120px"}' :src="baseUrl + systemIntroductionDetail.picture3">
		  </div>
		  <div :style='{"padding":"60px 90px ","margin":"0 auto","color":"#9E9E9E","borderRadius":"10px","background":"#fff","width":"68%","lineHeight":"2","fontSize":"18px","height":"302px"}' v-html="systemIntroductionDetail.content"></div>
		  <div :style='{"width":"285px","background":"url(http://codegen.caihongy.cn/20201114/7856ba26477849ea828f481fa2773a95.jpg) 0% 0% / cover no-repeat","display":"none","height":"100px"}' />
		  <div :style='{"width":"285px","background":"url(http://codegen.caihongy.cn/20201114/7856ba26477849ea828f481fa2773a95.jpg) 0% 0% / cover no-repeat","display":"none","height":"100px"}' />
		  <div :style='{"width":"285px","background":"url(http://codegen.caihongy.cn/20201114/7856ba26477849ea828f481fa2773a95.jpg) 0% 0% / cover no-repeat","display":"none","height":"100px"}' />
		  <div :style='{"width":"285px","background":"url(http://codegen.caihongy.cn/20201114/7856ba26477849ea828f481fa2773a95.jpg) 0% 0% / cover no-repeat","display":"none","height":"100px"}' />
		  <div :style='{"border":"2px solid #4D4D4D","margin":"0 0 0 -110px","textAlign":"center","left":"50%","background":"transparent","bottom":"180px","display":"block","width":"220px","lineHeight":"60px","position":"absolute","height":"60px"}' @click="toDetail('systemintroDetail',systemIntroductionDetail)">
		    <span :style='{"color":"#4D4D4D","fontSize":"18px"}'>更多信息</span>
		    <span class="icon iconfont icon-jiantou25" :style='{"color":"#4D4D4D","fontSize":"18px"}'></span>
		  </div>
		</div>
		<!-- 系统简介 -->
		
	<!-- 新闻资讯 -->
	<div id="animate_newsnews" class="news animate__animated" :style='{"width":"100%","padding":"120px 16% 76px","margin":"0 0 10px","position":"relative","background":"#fff","order":"5"}'>
		<div v-if="false" class="idea newsIdea" :style='{"padding":"20px","flexWrap":"wrap","background":"#efefef","justifyContent":"space-between","display":"flex"}'>
			<div class="box1" :style='{"width":"20%","background":"#fff","height":"80px"}'></div>
			<div class="box2" :style='{"width":"20%","background":"#fff","height":"80px"}'></div>
			<div class="box3" :style='{"width":"20%","background":"#fff","height":"80px"}'></div>
			<div class="box4" :style='{"width":"20%","background":"#fff","height":"80px"}'></div>
			<div class="box5" :style='{"width":"20%","background":"#fff","display":"none","height":"80px"}'></div>
			<div class="box6" :style='{"width":"20%","background":"#fff","display":"none","height":"80px"}'></div>
			<div class="box7" :style='{"width":"20%","background":"#fff","display":"none","height":"80px"}'></div>
			<div class="box8" :style='{"width":"20%","background":"#fff","display":"none","height":"80px"}'></div>
			<div class="box9" :style='{"width":"20%","background":"#fff","display":"none","height":"80px"}'></div>
			<div class="box10" :style='{"width":"20%","background":"#fff","display":"none","height":"80px"}'></div>
		</div>
		
		<div class="title" :style='{"margin":"10px auto 20px 40%","textAlign":"center","background":"url(http://codegen.caihongy.cn/20231025/2eada494f8664736b38e1c6fb445cc03.png)","width":"450px","lineHeight":"90px","backgroundSize":"cover","backgroundPosition":"center center","backgroundRepeat":"no-repeat","height":"104px"}'>
			<span :style='{"color":"#4D4D4D","letterSpacing":"6px","fontSize":"40px"}'>资讯信息</span>
		</div>
		
			
			
			
			
			
			
			
			
			
			
			<!-- 样式十 -->
		<div v-if="newsList.length" class="list list10 index-pv1" :style='{"width":"100%","padding":"0","background":"transparent","display":"flex","height":"auto"}'>
		  <div v-if="newsList.length>0" @click="toDetail('newsDetail', newsList[0])" :style='{"padding":"36px 45px 18px","margin":"0 10px","flexWrap":"wrap","background":"#f5f5f5","display":"flex","width":"35%","position":"relative","height":"520px"}' class="new10-list-item animation-box">
		    <img :style='{"width":"100%","margin":"0 0 38px","objectFit":"cover","display":"block","height":"300px"}' :src="baseUrl + newsList[0].picture" alt="">
			<div :style='{"padding":"0 10px","fontSize":"18px","lineHeight":"32px","color":"#000","order":"1"}' class="new9-list-item-title line1">{{newsList[0].title}}</div>
		    <div :style='{"padding":"0 10px 6px","whiteSpace":"nowrap","overflow":"hidden","color":"#666","fontSize":"16px","lineHeight":"32px","textOverflow":"ellipsis","order":"2"}' class="new9-list-item-descript line2">{{newsList[0].introduction}}</div>
			<div :style='{"width":"100%","padding":"6px 10px 0","order":"9"}'>
			  <span class="icon iconfont icon-shijian21" :style='{"margin":"0 2px 0 0","lineHeight":"1.5","fontSize":"13px","color":"#4D4D4D"}'></span>
			  <span class="text" :style='{"color":"#666","lineHeight":"1.5","fontSize":"12px"}'>{{newsList[0].addtime}}</span>
			</div>
			<div :style='{"width":"25%","padding":"0 10px","textAlign":"center","order":"7"}'>
			  <span class="icon iconfont icon-geren16" :style='{"margin":"0 2px 0 0","lineHeight":"1.5","fontSize":"13px","color":"#4D4D4D"}'></span>
			  <span class="text" :style='{"color":"#4D4D4D","lineHeight":"1.5","fontSize":"13px"}'>{{newsList[0].name}}</span>
			</div>
			<div :style='{"width":"25%","padding":"0 10px","textAlign":"center","order":"3"}'>
			  <span class="icon iconfont icon-zan10" :style='{"margin":"0 2px 0 0","lineHeight":"1.5","fontSize":"13px","color":"#4D4D4D"}'></span>
			  <span class="text" :style='{"color":"#4D4D4D","lineHeight":"1.5","fontSize":"13px"}'>{{newsList[0].thumbsupnum}}</span>
			</div>
			<div :style='{"width":"25%","padding":"0 10px","textAlign":"center","order":"6"}'>
			  <span class="icon iconfont icon-shoucang10" :style='{"margin":"0 2px 0 0","lineHeight":"1.5","fontSize":"13px","color":"#4D4D4D"}'></span>
			  <span class="text" :style='{"color":"#4D4D4D","lineHeight":"1.5","fontSize":"13px"}'>{{newsList[0].storeupnum}}</span>
			</div>
			<div :style='{"width":"25%","padding":"0 10px","textAlign":"center","order":"5"}'>
			  <span class="icon iconfont icon-chakan9" :style='{"margin":"0 2px 0 0","lineHeight":"1.5","fontSize":"13px","color":"#4D4D4D"}'></span>
			  <span class="text" :style='{"color":"#4D4D4D","lineHeight":"1.5","fontSize":"13px"}'>{{newsList[0].clicknum}}</span>
			</div>
			<div :style='{"padding":"0","margin":"0","color":"#fff","textAlign":"center","display":"inline-block","top":"311px","left":"45px","background":"#AD8936","width":"130px","fontSize":"16px","lineHeight":"50px","position":"absolute","height":"50px"}' class="new9-list-item-identification">新闻动态</div>
		  </div>
		  <div v-if="newsList.length>1" :style='{"padding":"0 0 0 30px","margin":"0","background":"transparent","flexDirection":"column","display":"flex","width":"65%","position":"relative","justifyContent":"space-between","height":"520px"}'>
		    <div v-for="(item,index) in newsList" v-if="index<4 && index>0" :key="index" @click="toDetail('newsDetail', item)" :style='{"padding":"10px 20px 10px 80px","flexWrap":"wrap","background":"#f5f5f5","flexDirection":"column","display":"flex","width":"100%","position":"relative","height":"30%"}' class="new10-list-item animation-box">
		        <div :style='{"padding":"0 10px","color":"#000","alignItems":"center","display":"flex","width":"80%","fontSize":"20px","lineHeight":"28px","fontWeight":"bold","height":"40%","order":"1"}' class="new9-list-item-title line1">{{ item.title }}</div>
				<div :style='{"padding":"0 10px","color":"#4D4D4D","alignItems":"center","display":"-webkit-box","overflow":"hidden","width":"80%","fontSize":"14px","lineHeight":"2","textOverflow":"ellipsis","-webkit-box-orient":"vertical","-webkit-line-clamp":"2","height":"25%","order":"2"}' class="new9-list-item-descript line2">{{ item.introduction }}</div>
				<div :style='{"width":"80%","padding":"0 10px","alignItems":"center","display":"flex","height":"30%","order":"3"}'>
				  <span class="icon iconfont icon-shijian21" :style='{"margin":"0 2px 0 0","lineHeight":"1.5","fontSize":"13px","color":"#4D4D4D"}'></span>
				  <span class="text" :style='{"padding":"0 0 0 6px","lineHeight":"1.5","fontSize":"13px","color":"#4D4D4D"}'>{{item.addtime}}</span>
				</div>
				<div :style='{"padding":"0 10px","alignItems":"center","display":"flex","order":"7","height":"25%"}'>
				  <span class="icon iconfont icon-geren16" :style='{"margin":"0 2px 0 0","lineHeight":"1.5","fontSize":"13px","color":"#4D4D4D"}'></span>
				  <span class="text" :style='{"color":"#4D4D4D","lineHeight":"1.5","fontSize":"13px"}'>{{item.name}}</span>
				</div>
				<div :style='{"padding":"0 10px","alignItems":"center","display":"flex","order":"4","height":"25%"}'>
				  <span class="icon iconfont icon-zan10" :style='{"margin":"0 2px 0 0","lineHeight":"1.5","fontSize":"13px","color":"#4D4D4D"}'></span>
				  <span class="text" :style='{"color":"#4D4D4D","lineHeight":"1.5","fontSize":"13px"}'>{{item.thumbsupnum}}</span>
				</div>
				<div :style='{"padding":"0 10px","alignItems":"center","display":"flex","order":"5","height":"25%"}'>
				  <span class="icon iconfont icon-shoucang10" :style='{"margin":"0 2px 0 0","lineHeight":"1.5","fontSize":"13px","color":"#4D4D4D"}'></span>
				  <span class="text" :style='{"color":"#4D4D4D","lineHeight":"1.5","fontSize":"13px"}'>{{item.storeupnum}}</span>
				</div>
				<div :style='{"padding":"0 10px","alignItems":"center","display":"flex","order":"6","height":"25%"}'>
				  <span class="icon iconfont icon-chakan9" :style='{"margin":"0 2px 0 0","lineHeight":"1.5","fontSize":"12px","color":"#666"}'></span>
				  <span class="text" :style='{"color":"#666","lineHeight":"1.5","fontSize":"12px"}'>{{item.clicknum}}</span>
				</div>
				<div :style='{"padding":"0 20px","color":"#fff","top":"0","alignItems":"center","left":"0","background":"#AD8936","display":"flex","width":"60px","fontSize":"18px","lineHeight":"1.5","position":"absolute","height":"100%"}' class="new9-list-item-identification">新闻动态</div>
		    </div>
		  </div>
		</div>
		











		<div @click="moreBtn('news')" :style='{"border":"2px solid #4D4D4D","margin":"10px auto","top":"150px","textAlign":"center","background":"transparent","display":"block","width":"220px","lineHeight":"60px","position":"absolute","right":"16%","height":"60px"}'>
			<span :style='{"color":"#4D4D4D","fontSize":"18px"}'>更多</span>
			<i :style='{"color":"#4D4D4D","fontSize":"18px"}' class="icon iconfont icon-gengduo1"></i>
		</div>
		
		</div>
	<!-- 新闻资讯 -->


<!-- 商品推荐 -->
<div id="animate_recommendqihuoxinxi" class="recommend animate__animated" :style='{"width":"100%","padding":"0 16%","margin":"0 0 0","background":"transparent","order":"1"}'>
	<div v-if="false" class="idea recommendIdea" :style='{"padding":"20px","flexWrap":"wrap","background":"#efefef","justifyContent":"space-between","display":"flex"}'>
		<div class="box1" :style='{"width":"20%","background":"#fff","height":"80px"}'></div>
		<div class="box2" :style='{"width":"20%","background":"#fff","height":"80px"}'></div>
		<div class="box3" :style='{"width":"20%","background":"#fff","height":"80px"}'></div>
		<div class="box4" :style='{"width":"20%","background":"#fff","height":"80px"}'></div>
		<div class="box5" :style='{"width":"20%","background":"#fff","display":"none","height":"80px"}'></div>
		<div class="box6" :style='{"width":"20%","background":"#fff","display":"none","height":"80px"}'></div>
		<div class="box7" :style='{"width":"20%","background":"#fff","display":"none","height":"80px"}'></div>
		<div class="box8" :style='{"width":"20%","background":"#fff","display":"none","height":"80px"}'></div>
		<div class="box9" :style='{"width":"20%","background":"#fff","display":"none","height":"80px"}'></div>
		<div class="box10" :style='{"width":"20%","background":"#fff","display":"none","height":"80px"}'></div>
	</div>
	
    <div class="title" :style='{"margin":"10px auto","textAlign":"center","background":"url(http://codegen.caihongy.cn/20231025/2eada494f8664736b38e1c6fb445cc03.png)","width":"450px","backgroundSize":"cover","lineHeight":"90px","backgroundPosition":"center center","backgroundRepeat":"no-repeat","height":"104px"}'>
		<span :style='{"color":"#4D4D4D","letterSpacing":"6px","fontSize":"40px"}'>期货信息推荐</span>
	</div>
	
	
	
	
	
	
	
	
	
	


	<div v-if="qihuoxinxiRecommend.length" class="list list11 index-pv1" :style='{"width":"100%","padding":"10px","background":"transparent","justifyContent":"space-between","display":"flex","height":"auto"}'>
	  <div class="tab" :style='{"width":"20%","padding":"0 20px 0 0","margin":"0 20px 0 0","flexDirection":"column","display":"flex","height":"auto"}'>
		<template v-for="(item,index) in recommendList11qihuoxinxi">
	    <div v-if="index < 6" :style='{"cursor":"pointer","padding":"2px 20px","boxShadow":"0px 4px 10px 0px rgba(0,0,0,0.302)","margin":"10px 0","borderColor":"#efefef","alignItems":"center","borderWidth":"0","display":"flex","width":"100%","borderStyle":"solid","height":"auto"}' class="item" @click="recommendIndexClick11(item,'qihuoxinxi')">
	      <span class="icon iconfont icon-jiantou09" :style='{"margin":"0 5px 0 0","lineHeight":"44px","fontSize":"20px","color":"#AD8936"}'></span>
	      <img v-if="item.image" :style='{"width":"36px","margin":"0 10px","objectFit":"cover","display":"inline-block","height":"36px"}' :src="baseUrl + (item.image?item.image.split(',')[0]:'')">
		  <span :style='{"lineHeight":"44px","fontSize":"16px","color":"#AD8936","fontWeight":"600"}'>{{item[recommendColumn11qihuoxinxi]}}</span>
	    </div>
		</template>
		<div :style='{"cursor":"pointer","padding":"2px 20px","boxShadow":"0px 4px 10px 0px rgba(0,0,0,0.302)","margin":"10px 0","borderColor":"#efefef","alignItems":"center","flexDirection":"row-reverse","display":"flex","justifyContent":"center","borderWidth":"0","width":"100%","borderStyle":"solid","height":"auto"}' class="more" @click="moreBtn('qihuoxinxi')">
		  <span class="icon iconfont icon-jiantou25" :style='{"margin":"0 5px 0 0","lineHeight":"44px","fontSize":"24px","color":"#AD8936"}'></span>
		  <div :style='{"padding":"0 6px","lineHeight":"44px","fontSize":"16px","color":"#AD8936","fontWeight":"600"}'>更多</div>
		</div>
	  </div>
	  <div class="list" :style='{"flexWrap":"wrap","flex":"1","background":"transparent","justifyContent":"space-between","display":"flex","height":"auto"}'>
	    <div :style='{"width":"31%","margin":"0 0 20px","position":"relative","background":"#fff","height":"auto"}' class="item list-item animation-box" v-for="item,index in qihuoxinxiRecommend" :key="index" @click="toDetail('qihuoxinxiDetail', item)">
			<img :name="item.id" :style='{"width":"100%","objectFit":"cover","display":"block","height":"200px"}' v-if="preHttp(item.tupian)" :src="item.tupian.split(',')[0]" alt="" />
			<img :name="item.id" :style='{"width":"100%","objectFit":"cover","display":"block","height":"200px"}' v-else :src="baseUrl + (item.tupian?item.tupian.split(',')[0]:'')" alt="" />
			<div class="line1" :style='{"padding":"4px 10px","lineHeight":"32px","fontSize":"16px","color":"#000","textAlign":"center","fontWeight":"bold"}'>{{item.qihuomingcheng}}</div>
			<div class="line1" :style='{"padding":"4px 10px","lineHeight":"32px","fontSize":"16px","color":"#000","textAlign":"center","fontWeight":"bold"}'>{{item.qihuoleixing}}</div>
			<div class="line1" :style='{"padding":"4px 10px","lineHeight":"32px","fontSize":"16px","color":"#000","textAlign":"center","fontWeight":"bold"}'>当前价格:{{item.jiage}}</div>
			<div class="line1" :style='{"padding":"4px 10px","lineHeight":"32px","fontSize":"16px","color":"#000","textAlign":"center","fontWeight":"bold"}'>交易价格:{{item.jiaoyijiage}}</div>
	    </div>
	  </div>
	</div>





	
	<div @click="moreBtn('qihuoxinxi')" :style='{"border":"0","margin":"10px auto","textAlign":"center","background":"#409EFF","display":"none","width":"80px","lineHeight":"32px"}'>
		<span :style='{"color":"#f5f5f5","fontSize":"12px"}'>更多</span>
		<i :style='{"color":"#f5f5f5","fontSize":"12px"}' class="icon iconfont icon-gengduo1"></i>
	</div>
	
</div>
<!-- 商品推荐 -->


<!-- 特价商品 -->
<div id="animate_listqihuoxinxi" class="lists animate__animated" :style='{"padding":"30px 16%","margin":"0 0 0","position":"relative","background":"transparent","order":"3"}'>
	<div v-if="false" class="idea" :style='{"padding":"20px","flexWrap":"wrap","background":"#efefef","justifyContent":"space-between","display":"flex"}'>
		<div class="box1" :style='{"width":"20%","background":"#fff","height":"80px"}'></div>
		<div class="box2" :style='{"width":"20%","background":"#fff","height":"80px"}'></div>
		<div class="box3" :style='{"width":"20%","background":"#fff","height":"80px"}'></div>
		<div class="box4" :style='{"width":"20%","background":"#fff","height":"80px"}'></div>
		<div class="box5" :style='{"width":"20%","background":"#fff","display":"none","height":"80px"}'></div>
		<div class="box6" :style='{"width":"20%","background":"#fff","display":"none","height":"80px"}'></div>
		<div class="box7" :style='{"width":"20%","background":"#fff","display":"none","height":"80px"}'></div>
		<div class="box8" :style='{"width":"20%","background":"#fff","display":"none","height":"80px"}'></div>
		<div class="box9" :style='{"width":"20%","background":"#fff","display":"none","height":"80px"}'></div>
		<div class="box10" :style='{"width":"20%","background":"#fff","display":"none","height":"80px"}'></div>
	</div>
	
	<div class="title" :style='{"margin":"0 auto","textAlign":"center","background":"url(http://codegen.caihongy.cn/20231025/2eada494f8664736b38e1c6fb445cc03.png)","width":"450px","lineHeight":"90px","backgroundSize":"cover","backgroundPosition":"center center","backgroundRepeat":"no-repeat","height":"104px"}'>
	  <span :style='{"color":"#4D4D4D","letterSpacing":"6px","fontSize":"40px"}'>期货信息展示</span>
	</div>
	
	
	
	
	
	
	
	
	
	






	<div class="list list15 index-pv1" :style='{"width":"100%","padding":"50px 0","alignItems":"flex-start","justifyContent":"center","display":"flex","height":"auto"}'>
	  <div :style='{"width":"32%","height":"auto"}' class="list left">
		<template v-if="qihuoxinxiList.length">
	    <template v-for="item,index in qihuoxinxiList">
		<div v-if="index == 0" @click="toDetail('qihuoxinxiDetail', item)" :style='{"width":"100%","margin":"0 0 15px","position":"relative","background":"#fff","height":"244px"}' class="box1 list-item animation-box">
		  <img :name="item.id" :style='{"width":"100% ","objectFit":"cover","display":"block","height":"100%"}' v-if="preHttp(item.tupian)" :src="item.tupian.split(',')[0]" alt="" />
		  <img :name="item.id" :style='{"width":"100% ","objectFit":"cover","display":"block","height":"100%"}' v-else :src="baseUrl + (item.tupian?item.tupian.split(',')[0]:'')" alt="" />
		  <div class="info">
			<div class="line1" :style='{"width":"100%","fontSize":"24px","lineHeight":"54px","color":"#fff","textAlign":"center"}'>{{item.qihuomingcheng}}</div>
			<div class="line1" :style='{"width":"100%","fontSize":"24px","lineHeight":"54px","color":"#fff","textAlign":"center"}'>{{item.qihuoleixing}}</div>
			<div class="line1" :style='{"width":"100%","fontSize":"24px","lineHeight":"54px","color":"#fff","textAlign":"center"}'>当前价格:{{item.jiage}}</div>
			<div class="line1" :style='{"width":"100%","fontSize":"24px","lineHeight":"54px","color":"#fff","textAlign":"center"}'>交易价格:{{item.jiaoyijiage}}</div>
	      </div>
	    </div>
		</template>
		</template>
		<template v-if="qihuoxinxiList.length > 1">
		<template v-for="item,index in qihuoxinxiList">
	    <div v-if="index == 1" @click="toDetail('qihuoxinxiDetail', item)" :style='{"width":"100%","margin":"0","position":"relative","background":"#fff","height":"244px"}' class="box2 list-item animation-box">
		  <img :name="item.id" :style='{"width":"100% ","objectFit":"cover","display":"block","height":"100%"}' v-if="preHttp(item.tupian)" :src="item.tupian.split(',')[0]" alt="" />
		  <img :name="item.id" :style='{"width":"100% ","objectFit":"cover","display":"block","height":"100%"}' v-else :src="baseUrl + (item.tupian?item.tupian.split(',')[0]:'')" alt="" />
		  <div class="info">
			<div class="line1" :style='{"width":"100%","fontSize":"24px","lineHeight":"54px","color":"#fff","textAlign":"center"}'>{{item.qihuomingcheng}}</div>
			<div class="line1" :style='{"width":"100%","fontSize":"24px","lineHeight":"54px","color":"#fff","textAlign":"center"}'>{{item.qihuoleixing}}</div>
			<div class="line1" :style='{"width":"100%","fontSize":"24px","lineHeight":"54px","color":"#fff","textAlign":"center"}'>当前价格:{{item.jiage}}</div>
			<div class="line1" :style='{"width":"100%","fontSize":"24px","lineHeight":"54px","color":"#fff","textAlign":"center"}'>交易价格:{{item.jiaoyijiage}}</div>
	      </div>
	    </div>
		</template>
		</template>
	  </div>
	  <div :style='{"width":"32%","margin":"0 2%","height":"auto"}' class="list center">
		<template v-if="qihuoxinxiList.length > 2">
		<template v-for="item,index in qihuoxinxiList">
	    <div v-if="index == 2" @click="toDetail('qihuoxinxiDetail', item)" :style='{"width":"100%","margin":"0","position":"relative","background":"#fff","height":"170px"}' class="box1 list-item animation-box">
		  <img :name="item.id" :style='{"width":"100% ","objectFit":"cover","display":"block","height":"100%"}' v-if="preHttp(item.tupian)" :src="item.tupian.split(',')[0]" alt="" />
		  <img :name="item.id" :style='{"width":"100% ","objectFit":"cover","display":"block","height":"100%"}' v-else :src="baseUrl + (item.tupian?item.tupian.split(',')[0]:'')" alt="" />
		  <div class="info">
			<div class="line1" :style='{"width":"100%","fontSize":"24px","lineHeight":"54px","color":"#fff","textAlign":"center"}'>{{item.qihuomingcheng}}</div>
			<div class="line1" :style='{"width":"100%","fontSize":"24px","lineHeight":"54px","color":"#fff","textAlign":"center"}'>{{item.qihuoleixing}}</div>
			<div class="line1" :style='{"width":"100%","fontSize":"24px","lineHeight":"54px","color":"#fff","textAlign":"center"}'>当前价格:{{item.jiage}}</div>
			<div class="line1" :style='{"width":"100%","fontSize":"24px","lineHeight":"54px","color":"#fff","textAlign":"center"}'>交易价格:{{item.jiaoyijiage}}</div>
		  </div>
	    </div>
		</template>
		</template>
	    <div :style='{"margin":"16px 0","alignItems":"center","background":"#AD8936","flexDirection":"column","display":"flex","width":"100%","justifyContent":"center","height":"130px"}' class="box2">
	      <div :style='{"color":"#fff","fontSize":"24px","lineHeight":"54px"}' class="title">{{qihuoxinxiList[2].qihuomingcheng}}</div>
	    </div>
		<template v-if="qihuoxinxiList.length > 3">
		<template v-for="item,index in qihuoxinxiList">
	    <div v-if="index == 3" @click="toDetail('qihuoxinxiDetail', item)" :style='{"width":"100%","margin":"0","position":"relative","background":"#fff","height":"170px"}' class="box3 list-item animation-box">
		  <img :name="item.id" :style='{"width":"100% ","objectFit":"cover","display":"block","height":"100%"}' v-if="preHttp(item.tupian)" :src="item.tupian.split(',')[0]" alt="" />
		  <img :name="item.id" :style='{"width":"100% ","objectFit":"cover","display":"block","height":"100%"}' v-else :src="baseUrl + (item.tupian?item.tupian.split(',')[0]:'')" alt="" />
		  <div class="info">
			<div class="line1" :style='{"width":"100%","fontSize":"24px","lineHeight":"54px","color":"#fff","textAlign":"center"}'>{{item.qihuomingcheng}}</div>
			<div class="line1" :style='{"width":"100%","fontSize":"24px","lineHeight":"54px","color":"#fff","textAlign":"center"}'>{{item.qihuoleixing}}</div>
			<div class="line1" :style='{"width":"100%","fontSize":"24px","lineHeight":"54px","color":"#fff","textAlign":"center"}'>当前价格:{{item.jiage}}</div>
			<div class="line1" :style='{"width":"100%","fontSize":"24px","lineHeight":"54px","color":"#fff","textAlign":"center"}'>交易价格:{{item.jiaoyijiage}}</div>
		  </div>
	    </div>
		</template>
		</template>
	  </div>
	  <div :style='{"width":"32%","height":"auto"}' class="list right">
	    <template v-if="qihuoxinxiList.length > 4">
	    <template v-for="item,index in qihuoxinxiList">
	    <div v-if="index == 4" @click="toDetail('qihuoxinxiDetail', item)" :style='{"width":"100%","margin":"0","position":"relative","background":"#fff","height":"244px"}' class="box1 list-item animation-box">
		  <img :name="item.id" :style='{"width":"100% ","objectFit":"cover","display":"block","height":"100%"}' v-if="preHttp(item.tupian)" :src="item.tupian.split(',')[0]" alt="" />
		  <img :name="item.id" :style='{"width":"100% ","objectFit":"cover","display":"block","height":"100%"}' v-else :src="baseUrl + (item.tupian?item.tupian.split(',')[0]:'')" alt="" />
		  <div class="info">
			<div class="line1" :style='{"width":"100%","fontSize":"24px","lineHeight":"54px","color":"#fff","textAlign":"center"}'>{{item.qihuomingcheng}}</div>
			<div class="line1" :style='{"width":"100%","fontSize":"24px","lineHeight":"54px","color":"#fff","textAlign":"center"}'>{{item.qihuoleixing}}</div>
			<div class="line1" :style='{"width":"100%","fontSize":"24px","lineHeight":"54px","color":"#fff","textAlign":"center"}'>当前价格:{{item.jiage}}</div>
			<div class="line1" :style='{"width":"100%","fontSize":"24px","lineHeight":"54px","color":"#fff","textAlign":"center"}'>交易价格:{{item.jiaoyijiage}}</div>
	      </div>
	    </div>
		</template>
		</template>
		<template v-if="qihuoxinxiList.length > 5">
		<template v-for="item,index in qihuoxinxiList">
	    <div v-if="index == 5" @click="toDetail('qihuoxinxiDetail', item)" :style='{"width":"100%","margin":"15px 0 0","position":"relative","background":"#fff","height":"244px"}' class="box2 list-item animation-box">
		  <img :name="item.id" :style='{"width":"100% ","objectFit":"cover","display":"block","height":"100%"}' v-if="preHttp(item.tupian)" :src="item.tupian.split(',')[0]" alt="" />
		  <img :name="item.id" :style='{"width":"100% ","objectFit":"cover","display":"block","height":"100%"}' v-else :src="baseUrl + (item.tupian?item.tupian.split(',')[0]:'')" alt="" />
	      <div class="info">
			<div class="line1" :style='{"width":"100%","fontSize":"24px","lineHeight":"54px","color":"#fff","textAlign":"center"}'>{{item.qihuomingcheng}}</div>
			<div class="line1" :style='{"width":"100%","fontSize":"24px","lineHeight":"54px","color":"#fff","textAlign":"center"}'>{{item.qihuoleixing}}</div>
			<div class="line1" :style='{"width":"100%","fontSize":"24px","lineHeight":"54px","color":"#fff","textAlign":"center"}'>当前价格:{{item.jiage}}</div>
			<div class="line1" :style='{"width":"100%","fontSize":"24px","lineHeight":"54px","color":"#fff","textAlign":"center"}'>交易价格:{{item.jiaoyijiage}}</div>
	      </div>
	    </div>
		</template>
		</template>
	  </div>
	</div>
	
	
	<div @click="moreBtn('qihuoxinxi')" :style='{"border":"0","boxShadow":"0px 4px 10px 0px rgba(0,0,0,0.302)","margin":"10px auto","top":"64px","textAlign":"center","background":"#fff","display":"block","width":"220px","lineHeight":"60px","position":"absolute","right":"16%","height":"60px"}'>
		<span :style='{"color":"#AD8936","fontSize":"18px"}'>MORE</span>
		<i :style='{"color":"#AD8936","fontSize":"18px"}' class="icon iconfont icon-gengduo1"></i>
	</div>
	

</div>
<!-- 特价商品 -->
	
</div>
</template>

<script>
import 'animate.css'
import Swiper from "swiper";

  export default {
    //数据集合
    data() {
      return {
        baseUrl: '',
        aboutUsDetail: {},
        systemIntroductionDetail: {},
        newsList: [],
        qihuoxinxiRecommend: [],

        qihuoxinxiList: [],


		recommendIndex11qihuoxinxi: '',
		recommendList11qihuoxinxi: [],
		recommendColumn11qihuoxinxi: '',


      }
    },
    created() {
		this.baseUrl = this.$config.baseUrl;
		this.getNewsList();
		this.getAboutUs();
		this.getSystemIntroduction();
		this.getList();
		this.qihuoxinxiRecommendCate()
    },
	mounted() {
		window.addEventListener('scroll', this.handleScroll)
		setTimeout(()=>{
			this.handleScroll()
		},100)
		
		this.swiperChanges()
	},
	beforeDestroy() {
	  window.removeEventListener('scroll', this.handleScroll)
	},
    //方法集合
    methods: {
		swiperChanges() {








































































			setTimeout(()=>{




































			},250)
		},
		qihuoxinxiRecommendCate(){
			this.$http.get('qihuoleixing/lists').then(res => {
			  if (res.data.code == 0) {
				this.recommendList11qihuoxinxi = res.data.data;
			  }
			});
			this.recommendColumn11qihuoxinxi = 'qihuoleixing'
		},
		recommendIndexClick11(index, name) {
			this['recommendIndex11' + name] = index[this['recommendColumn11' + name]]
			this.getList()
		},


		handleScroll() {
			let arr = [
				{id:'search',css:'animate__bounce'},
				{id:'about',css:'animate__shakeX'},
				{id:'system',css:'animate__rotateInUpRight'},
				{id:'animate_recommendqihuoxinxi',css:'animate__bounce'},
				{id:'animate_listqihuoxinxi',css:'animate__flipInY'},
				{id:'animate_newsnews',css:'animate__fadeInTopLeft'},
				{id:'msgs',css:'animate__zoomInUp'},
				{id:'friendly',css:'animate__heartBeat'}
			]
			
			for (let i in arr) {
				let doc = document.getElementById(arr[i].id)
				if (doc) {
					let top = doc.offsetTop
					let win_top = window.innerHeight + window.pageYOffset
					// console.log(top,win_top)
					if (win_top > top && doc.classList.value.indexOf(arr[i].css) < 0) {
						// console.log(doc)
						doc.classList.add(arr[i].css)
					}
				}
			}
		},
      preHttp(str) {
          return str && str.substr(0,4)=='http';
      },
      getAboutUs() {
          this.$http.get('aboutus/detail/1', {}).then(res => {
            if(res.data.code == 0) {
              this.aboutUsDetail = res.data.data;
            }
          })
      },
      getSystemIntroduction() {
          this.$http.get('systemintro/detail/1', {}).then(res => {
            if(res.data.code == 0) {
              this.systemIntroductionDetail = res.data.data;
            }
          })
      },
		getNewsList() {
			let data = {
				page: 1,
				limit: 6,
                sort: 'addtime',
				order: 'desc'
			}
			this.$http.get('news/list', {params: data}).then(res => {
				if (res.data.code == 0) {
					this.newsList = res.data.data.list;
					
					
				}
			});
		},
		getList() {
			let autoSortUrl = "";
			let data = {}
          autoSortUrl = "qihuoxinxi/autoSort";
			data = {
				page: 1,
				limit: 6,
			}
				if(this.recommendIndex11qihuoxinxi){
					data.qihuoleixing = this.recommendIndex11qihuoxinxi
				}
			this.$http.get(autoSortUrl, {params: data}).then(res => {
				if (res.data.code == 0) {
					this.qihuoxinxiRecommend = res.data.data.list;
					
					
					// 商品列表样式五
					
				}
			});
			
			data = {
				page: 1,
				limit: 6,
			}
			this.$http.get('qihuoxinxi/list', {params: data}).then(res => {
				if (res.data.code == 0) {
					this.qihuoxinxiList = res.data.data.list;
					
					// 商品列表样式五
					
				}
			});
		},
		toDetail(path, item) {
			this.$router.push({path: '/index/' + path, query: {id: item.id}});
		},
		moreBtn(path) {
			this.$router.push({path: '/index/' + path});
		}
    }
  }
</script>

<style rel="stylesheet/scss" lang="scss" scoped>
	.home-preview {
		// -------- search --------
		.search .select /deep/ .el-input__inner {
			border: 1px solid #D8D8D8;
			border-radius: 0;
			padding: 0 30px 0 10px;
			box-shadow: 0 0 0px rgba(64, 158, 255, .3);
			outline: none;
			color: #000;
			width: 180px;
			font-size: 14px;
			border-width: 0 1px 0 0;
			text-align: center;
			height: 50px;
		}
		
		.search .input /deep/ .el-input__inner {
			border: 0;
			border-radius: 4px;
			padding: 0 10px;
			box-shadow: 0 0 0px rgba(64, 158, 255, .3);
			outline: none;
			color: rgba(64, 158, 255, 1);
			width: 100%;
			font-size: 14px;
			height: 50px;
		}
		// -------- search --------
		.recommend {
			.list3 .swiper-button-prev {
				left: 10px;
				right: auto;
			}
			
			.list3 .swiper-button-prev::after {
				color: rgb(64, 158, 255);
			}
			
			.list3 .swiper-button-next {
				left: auto;
				right: 10px;
			}
			
			.list3 .swiper-button-next::after {
				color: rgb(64, 158, 255);
			}
			
			.list5 .swiper-button-prev {
				left: 10px;
				right: auto;
			}
			
			.list5 .swiper-button-prev::after {
				color: rgb(64, 158, 255);
        }
        
        .list5 .swiper-button-next {
				left: auto;
				right: 10px;
			}
			
			.list5 .swiper-button-next::after {
				color: rgb(64, 158, 255);
			}
			
			.list5 {
				.swiper-slide-prev {
					position: relative;
					z-index: 3;
				}
		
				.swiper-slide-next {
					position: relative;
					z-index: 3;
				}
		
				.swiper-slide-active {
					position: relative;
					z-index: 5;
				}
			}
			
			.index-pv1 .animation-box {
				transform: rotate(0deg) scale(1) skew(0deg, 0deg) translate3d(0px, 0px, 0px);
				z-index: initial;
			}
			
			.index-pv1 .animation-box:hover {
				transform: rotate(0deg) scale(1) skew(0deg, 0deg) translate3d(0px, 10px, 0px);
				-webkit-perspective: 1000px;
				perspective: 1000px;
				transition: 0.3s;
				z-index: 1;
			}
			
			.index-pv1 .animation-box img {
				transform: rotate(0deg) scale(1) skew(0deg, 0deg) translate3d(0px, 0px, 0px);
			}
			
			.index-pv1 .animation-box img:hover {
				transform: rotate(0deg) scale(1.1) skew(0deg, 0deg) translate3d(0px, 0px, 0px);
				-webkit-perspective: 1000px;
				perspective: 1000px;
				transition: 0.3s;
			}
		}
		
		.news {
			.list3 .swiper-button-prev {
				left: 10px;
				right: auto;
			}
			
			.list3 .swiper-button-prev::after {
				color: rgb(64, 158, 255);
			}
			
			.list3 .swiper-button-next {
				left: auto;
				right: 10px;
			}
			
			.list3 .swiper-button-next::after {
				color: rgb(64, 158, 255);
			}
			
			.list6 .swiper-button-prev {
				left: 10px;
				right: auto;
			}
			
			.list6 .swiper-button-prev::after {
				color: rgb(64, 158, 255);
			}
			
			.list6 .swiper-button-next {
				left: auto;
				right: 10px;
			}
			
			.list6 .swiper-button-next::after {
				color: rgb(64, 158, 255);
			}
			
			.index-pv1 .animation-box {
				transform: rotate(0deg) scale(1) skew(0deg, 0deg) translate3d(0px, 0px, 0px);
				z-index: initial;
			}
			
			.index-pv1 .animation-box:hover {
				transform: rotate(0deg) scale(1) skew(0deg, 0deg) translate3d(0px, 10px, 0px);
				-webkit-perspective: 1000px;
				perspective: 1000px;
				transition: 0.3s;
				z-index: 1;
			}
			
			.index-pv1 .animation-box img {
				transform: rotate(0deg) scale(1) skew(0deg, 0deg) translate3d(0px, 0px, 0px);
			}
			
			.index-pv1 .animation-box img:hover {
				transform: rotate(0deg) scale(1.1) skew(0deg, 0deg) translate3d(0px, 0px, 0px);
				-webkit-perspective: 1000px;
				perspective: 1000px;
				transition: 0.3s;
			}
		}
	
		.lists {
			.list3 .swiper-button-prev {
				left: 10px;
				right: auto;
			}
			
			.list3 .swiper-button-prev::after {
				color: rgb(64, 158, 255);
			}
			
			.list3 .swiper-button-next {
				left: auto;
				right: 10px;
        }
        
        .list3 .swiper-button-next::after {
				color: rgb(64, 158, 255);
			}
			
			.list5 .swiper-button-prev {
				left: 10px;
				right: auto;
			}
			
			.list5 .swiper-button-prev::after {
				color: rgb(64, 158, 255);
			}
			
			.list5 .swiper-button-next {
            left: auto;
            right: 10px;
			}
			
			.list5 .swiper-button-next::after {
				color: rgb(64, 158, 255);
			}
			
			.list5 {
				.swiper-slide-prev {
					position: relative;
					z-index: 3;
				}
		
				.swiper-slide-next {
					position: relative;
					z-index: 3;
				}
		
				.swiper-slide-active {
					position: relative;
					z-index: 5;
				}
			}
			
			.index-pv1 .animation-box {
				transform: rotate(0deg) scale(1) skew(0deg, 0deg) translate3d(0px, 0px, 0px);
				z-index: initial;
			}
			
			.index-pv1 .animation-box:hover {
				transform: rotate(0deg) scale(1) skew(0deg, 0deg) translate3d(0px, 10px, 0px);
				-webkit-perspective: 1000px;
				perspective: 1000px;
				transition: 0.3s;
				z-index: 1;
			}
			
			.index-pv1 .animation-box img {
				transform: rotate(0deg) scale(1) skew(0deg, 0deg) translate3d(0px, 0px, 0px);
			}
			
			.index-pv1 .animation-box img:hover {
				transform: rotate(0deg) scale(1.1) skew(0deg, 0deg) translate3d(0px, 0px, 0px);
				-webkit-perspective: 1000px;
				perspective: 1000px;
				transition: 0.3s;
			}
		}
	}
	










	.home-preview .lists .list15 .left .box1 .info {
				left: 0;
				background: rgba(173, 137, 54, 0.3);
				bottom: 0;
				display: flex;
				width: 100%;
				justify-content: center;
				align-items: center;
				position: absolute;
				opacity: 0;
				flex-wrap: wrap;
				transition: all .3s;
				height: 100%;
			}
	
	.home-preview .lists .list15 .left .box1 .info:hover {
				opacity: 1;
			}
	
	.home-preview .lists .list15 .left .box2 .info {
				left: 0;
				background: rgba(173, 137, 54, 0.3);
				bottom: 0;
				display: flex;
				width: 100%;
				justify-content: center;
				align-items: center;
				position: absolute;
				opacity: 0;
				flex-wrap: wrap;
				transition: all .3s;
				height: 100%;
			}
	
	.home-preview .lists .list15 .left .box2 .info:hover {
				opacity: 1;
			}
	
	.home-preview .lists .list15 .center .box1 .info {
				left: 0;
				background: rgba(173, 137, 54, 0.3);
				bottom: 0;
				display: flex;
				width: 100%;
				justify-content: center;
				align-items: center;
				position: absolute;
				opacity: 0;
				flex-wrap: wrap;
				transition: all .3s;
				height: 100%;
			}
	
	.home-preview .lists .list15 .center .box1 .info:hover {
				opacity: 1;
			}
	
	.home-preview .lists .list15 .center .box3 .info {
				left: 0;
				background: rgba(173, 137, 54, 0.3);
				bottom: 0;
				display: flex;
				width: 100%;
				justify-content: center;
				align-items: center;
				position: absolute;
				opacity: 0;
				flex-wrap: wrap;
				transition: all .3s;
				height: 100%;
			}
	
	.home-preview .lists .list15 .center .box3 .info:hover {
				opacity: 1;
			}
	
	.home-preview .lists .list15 .right .box1 .info {
				left: 0;
				background: rgba(173, 137, 54, 0.3);
				bottom: 0;
				display: flex;
				width: 100%;
				justify-content: center;
				align-items: center;
				position: absolute;
				opacity: 0;
				flex-wrap: wrap;
				transition: all .3s;
				height: 100%;
			}
	
	.home-preview .lists .list15 .right .box1 .info:hover {
				opacity: 1;
			}
	
	.home-preview .lists .list15 .right .box2 .info {
				left: 0;
				background: rgba(173, 137, 54, 0.3);
				bottom: 0;
				display: flex;
				width: 100%;
				justify-content: center;
				align-items: center;
				position: absolute;
				opacity: 0;
				flex-wrap: wrap;
				transition: all .3s;
				height: 100%;
			}
	
	.home-preview .lists .list15 .right .box2 .info:hover {
				opacity: 1;
			}
</style>
