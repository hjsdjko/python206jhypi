# coding:utf-8
import random
from datetime import datetime
from sqlalchemy import text,TIMESTAMP

from api.models.models import Base_model
from api.exts import db
from sqlalchemy.dialects.mysql import DOUBLE,LONGTEXT
# 个人信息
class yonghu(Base_model):
    __doc__ = u'''yonghu'''
    __tablename__ = 'yonghu'

    __loginUser__='yonghuming'


    __authTables__={}
    __authPeople__='是'
    __authSeparate__='否'
    __thumbsUp__='否'
    __intelRecom__='否'
    __browseClick__='否'
    __foreEndListAuth__='否'
    __foreEndList__='否'
    __isAdmin__='否'
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=False,comment='主键')
    addtime = db.Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'))
    yonghuming=db.Column( db.VARCHAR(255), nullable=False,unique=True,comment='用户名' )
    mima=db.Column( db.VARCHAR(255), nullable=False, unique=False,comment='密码' )
    xingming=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='姓名' )
    xingbie=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='性别' )
    touxiang=db.Column( db.Text,  nullable=True, unique=False,comment='头像' )
    nianling=db.Column( db.Integer,default=0,  nullable=True, unique=False,comment='年龄' )
    youxiang=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='邮箱' )
    shouji=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='手机' )
    kahao=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='账户卡号' )
    jine=db.Column( db.Float,default=0, nullable=False, unique=False,comment='金额' )


class qihuogongsi(Base_model):
    __doc__ = u'''qihuogongsi'''
    __tablename__ = 'qihuogongsi'

    __loginUser__='zhanghao'


    __authTables__={}
    __authPeople__='是'
    __authSeparate__='否'
    __thumbsUp__='否'
    __intelRecom__='否'
    __browseClick__='否'
    __foreEndListAuth__='否'
    __foreEndList__='否'
    __isAdmin__='是'
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=False,comment='主键')
    addtime = db.Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'))
    zhanghao=db.Column( db.VARCHAR(255), nullable=False,unique=True,comment='账号' )
    mima=db.Column( db.VARCHAR(255), nullable=False, unique=False,comment='密码' )
    fuzerenxingming=db.Column( db.VARCHAR(255), nullable=False, unique=False,comment='负责人姓名' )
    xingbie=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='性别' )
    touxiang=db.Column( db.Text,  nullable=True, unique=False,comment='头像' )
    gongsimingcheng=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='公司名称' )
    youxiang=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='邮箱' )
    lianxidianhua=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='手机' )
    gongsijianjie=db.Column( db.Text,  nullable=True, unique=False,comment='公司简介' )


class kaihuxinxi(Base_model):
    __doc__ = u'''kaihuxinxi'''
    __tablename__ = 'kaihuxinxi'



    __authTables__={'yonghuming':'yonghu',}
    __authPeople__='否'
    __authSeparate__='否'
    __thumbsUp__='否'
    __intelRecom__='否'
    __browseClick__='否'
    __foreEndListAuth__='否'
    __foreEndList__='否'
    __isAdmin__='否'
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=False,comment='主键')
    addtime = db.Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'))
    zhanghukahao=db.Column( db.VARCHAR(255), nullable=False,unique=True,comment='账户卡号' )
    yonghuming=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='用户名' )
    xingming=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='姓名' )
    kaihushijian=db.Column( db.DateTime,  nullable=True, unique=False,comment='开户时间' )
    beizhu=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='备注' )


class chongzhixinxi(Base_model):
    __doc__ = u'''chongzhixinxi'''
    __tablename__ = 'chongzhixinxi'



    __authTables__={'yonghuming':'yonghu',}
    __authPeople__='否'
    __authSeparate__='否'
    __thumbsUp__='否'
    __intelRecom__='否'
    __browseClick__='否'
    __foreEndListAuth__='否'
    __foreEndList__='是'
    __isAdmin__='否'
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=False,comment='主键')
    addtime = db.Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'))
    zhanghukahao=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='账户卡号' )
    yonghuming=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='用户名' )
    xingming=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='姓名' )
    touxiang=db.Column( db.Text,  nullable=True, unique=False,comment='头像' )
    jine=db.Column( db.Float,default=0, nullable=False, unique=False,comment='金额' )
    chongzhiriqi=db.Column( db.DateTime,  nullable=True, unique=False,comment='充值日期' )
    ispay=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='是否支付' )


class qihuoleixing(Base_model):
    __doc__ = u'''qihuoleixing'''
    __tablename__ = 'qihuoleixing'



    __authTables__={}
    __authPeople__='否'
    __authSeparate__='否'
    __thumbsUp__='否'
    __intelRecom__='否'
    __browseClick__='否'
    __foreEndListAuth__='否'
    __foreEndList__='否'
    __isAdmin__='否'
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=False,comment='主键')
    addtime = db.Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'))
    qihuoleixing=db.Column( db.VARCHAR(255), nullable=False, unique=False,comment='期货类型' )
    image=db.Column( db.Text, nullable=False, unique=False,comment='image' )


class qihuoxinxi(Base_model):
    __doc__ = u'''qihuoxinxi'''
    __tablename__ = 'qihuoxinxi'



    __authTables__={'zhanghao':'qihuogongsi',}
    __authPeople__='否'
    __authSeparate__='否'
    __thumbsUp__='否'
    __intelRecom__='是'
    __browseClick__='否'
    __foreEndListAuth__='否'
    __foreEndList__='是'
    __isAdmin__='否'
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=False,comment='主键')
    addtime = db.Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'))
    qihuodaima=db.Column( db.VARCHAR(255), nullable=False,unique=True,comment='期货代码' )
    qihuomingcheng=db.Column( db.VARCHAR(255), nullable=False,unique=True,comment='期货名称' )
    qihuoleixing=db.Column( db.VARCHAR(255), nullable=False, unique=False,comment='期货类型' )
    gongsimingcheng=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='公司名称' )
    qihuozhangshi=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='期货涨势' )
    jiage=db.Column( db.Float,default=0, nullable=False, unique=False,comment='当前价格' )
    jiaoyijiage=db.Column( db.Float,default=0, nullable=False, unique=False,comment='交易价格' )
    tupian=db.Column( db.Text,  nullable=True, unique=False,comment='图片' )
    kaishishijian=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='开市时间' )
    qihuojieshao=db.Column( db.Text,  nullable=True, unique=False,comment='期货介绍' )
    zhanghao=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='账号' )
    fuzerenxingming=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='姓名' )
    lianxidianhua=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='联系电话' )
    clicktime=db.Column( db.DateTime,  nullable=True, unique=False,comment='最近点击时间' )
    discussnum=db.Column( db.Integer,default=0,  nullable=True, unique=False,comment='评论数' )
    storeupnum=db.Column( db.Integer,default=0,  nullable=True, unique=False,comment='收藏数' )


class qihuotouzi(Base_model):
    __doc__ = u'''qihuotouzi'''
    __tablename__ = 'qihuotouzi'



    __authTables__={'zhanghao':'qihuogongsi','yonghuming':'yonghu',}
    __authPeople__='否'
    __authSeparate__='否'
    __thumbsUp__='否'
    __intelRecom__='否'
    __browseClick__='否'
    __foreEndListAuth__='否'
    __foreEndList__='是'
    __isAdmin__='否'
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=False,comment='主键')
    addtime = db.Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'))
    qihuodaima=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='期货代码' )
    qihuomingcheng=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='期货名称' )
    qihuoleixing=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='期货类型' )
    tupian=db.Column( db.Text,  nullable=True, unique=False,comment='图片' )
    zhanghao=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='账号' )
    jiaoyijiage=db.Column( db.Float,default=0,  nullable=True, unique=False,comment='交易价格' )
    jiage=db.Column( db.Float,default=0,  nullable=True, unique=False,comment='当前价格' )
    shuliang=db.Column( db.Integer,default=0,  nullable=True, unique=False,comment='仓数' )
    touzishijian=db.Column( db.DateTime,  nullable=True, unique=False,comment='投资时间' )
    jine=db.Column( db.Float,default=0,  nullable=True, unique=False,comment='总额' )
    yonghuming=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='用户名' )
    xingming=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='姓名' )
    kahao=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='账户卡号' )
    yonghujine=db.Column( db.Float,default=0,  nullable=True, unique=False,comment='金额' )


class quxiaotouzi(Base_model):
    __doc__ = u'''quxiaotouzi'''
    __tablename__ = 'quxiaotouzi'



    __authTables__={'zhanghao':'qihuogongsi','yonghuming':'yonghu',}
    __authPeople__='否'
    __authSeparate__='否'
    __thumbsUp__='否'
    __intelRecom__='否'
    __browseClick__='否'
    __foreEndListAuth__='否'
    __foreEndList__='是'
    __isAdmin__='否'
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=False,comment='主键')
    addtime = db.Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'))
    qihuodaima=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='期货代码' )
    qihuomingcheng=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='期货名称' )
    qihuoleixing=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='期货类型' )
    tupian=db.Column( db.Text,  nullable=True, unique=False,comment='图片' )
    zhanghao=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='账号' )
    jiage=db.Column( db.Float,default=0,  nullable=True, unique=False,comment='当前价格' )
    shuliang=db.Column( db.Integer,default=0,  nullable=True, unique=False,comment='仓数' )
    jine=db.Column( db.Float,default=0,  nullable=True, unique=False,comment='总额' )
    touzishijian=db.Column( db.DateTime,  nullable=True, unique=False,comment='投资时间' )
    yonghuming=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='用户名' )
    xingming=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='姓名' )
    kahao=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='账户卡号' )
    crossuserid=db.Column( db.BigInteger,  nullable=True, unique=False,comment='跨表用户id' )
    crossrefid=db.Column( db.BigInteger,  nullable=True, unique=False,comment='跨表主键id' )


class touzifengxian(Base_model):
    __doc__ = u'''touzifengxian'''
    __tablename__ = 'touzifengxian'



    __authTables__={}
    __authPeople__='否'
    __authSeparate__='否'
    __thumbsUp__='否'
    __intelRecom__='否'
    __browseClick__='否'
    __foreEndListAuth__='否'
    __foreEndList__='是'
    __isAdmin__='否'
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=False,comment='主键')
    addtime = db.Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'))
    touzimingcheng=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='投资名称' )
    touzileixing=db.Column( db.VARCHAR(255), nullable=False, unique=False,comment='投资类型' )
    fengxiandengji=db.Column( db.VARCHAR(255), nullable=False, unique=False,comment='风险等级' )
    tupian=db.Column( db.Text,  nullable=True, unique=False,comment='图片' )
    fengxianshuoming=db.Column( db.Text,  nullable=True, unique=False,comment='风险说明' )
    fabushijian=db.Column( db.DateTime,  nullable=True, unique=False,comment='发布时间' )
    discussnum=db.Column( db.Integer,default=0,  nullable=True, unique=False,comment='评论数' )
    storeupnum=db.Column( db.Integer,default=0,  nullable=True, unique=False,comment='收藏数' )


class qihuomaichu(Base_model):
    __doc__ = u'''qihuomaichu'''
    __tablename__ = 'qihuomaichu'



    __authTables__={'zhanghao':'qihuogongsi','yonghuming':'yonghu',}
    __authPeople__='否'
    __authSeparate__='否'
    __thumbsUp__='否'
    __intelRecom__='否'
    __browseClick__='否'
    __foreEndListAuth__='否'
    __foreEndList__='是'
    __isAdmin__='否'
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=False,comment='主键')
    addtime = db.Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'))
    qihuodaima=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='期货代码' )
    qihuomingcheng=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='期货名称' )
    qihuoleixing=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='期货类型' )
    tupian=db.Column( db.Text,  nullable=True, unique=False,comment='图片' )
    jiaoyijiage=db.Column( db.Float,default=0,  nullable=True, unique=False,comment='交易价格' )
    shuliang=db.Column( db.Integer,default=0,  nullable=True, unique=False,comment='仓数' )
    jine=db.Column( db.Float,default=0,  nullable=True, unique=False,comment='总价格' )
    jiaoyishijian=db.Column( db.Date,  nullable=True, unique=False,comment='交易时间' )
    zhanghao=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='账号' )
    yonghuming=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='用户名' )
    xingming=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='姓名' )
    kahao=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='账户卡号' )


class newstype(Base_model):
    __doc__ = u'''newstype'''
    __tablename__ = 'newstype'



    __authTables__={}
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=False,comment='主键')
    addtime = db.Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'))
    typename=db.Column( db.VARCHAR(255), nullable=False, unique=False,comment='分类名称' )


class news(Base_model):
    __doc__ = u'''news'''
    __tablename__ = 'news'



    __authTables__={}
    __thumbsUp__='是'
    __intelRecom__='是'
    __browseClick__='是'
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=False,comment='主键')
    addtime = db.Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'))
    title=db.Column( db.VARCHAR(255), nullable=False, unique=False,comment='标题' )
    introduction=db.Column( db.Text,  nullable=True, unique=False,comment='简介' )
    typename=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='分类名称' )
    name=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='发布人' )
    headportrait=db.Column( db.Text,  nullable=True, unique=False,comment='头像' )
    clicknum=db.Column( db.Integer,default=0,  nullable=True, unique=False,comment='点击次数' )
    clicktime=db.Column( db.DateTime,  nullable=True, unique=False,comment='最近点击时间' )
    thumbsupnum=db.Column( db.Integer,default=0,  nullable=True, unique=False,comment='赞' )
    crazilynum=db.Column( db.Integer,default=0,  nullable=True, unique=False,comment='踩' )
    storeupnum=db.Column( db.Integer,default=0,  nullable=True, unique=False,comment='收藏数' )
    picture=db.Column( db.Text, nullable=False, unique=False,comment='图片' )
    content=db.Column( db.Text, nullable=False, unique=False,comment='内容' )


class storeup(Base_model):
    __doc__ = u'''storeup'''
    __tablename__ = 'storeup'



    __authTables__={}
    __authSeparate__='是'
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=False,comment='主键')
    addtime = db.Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'))
    userid=db.Column( db.BigInteger, nullable=False, unique=False,comment='用户id' )
    refid=db.Column( db.BigInteger,  nullable=True, unique=False,comment='商品id' )
    tablename=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='表名' )
    name=db.Column( db.VARCHAR(255), nullable=False, unique=False,comment='名称' )
    picture=db.Column( db.Text, nullable=False, unique=False,comment='图片' )
    type=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='类型(1:收藏,21:赞,22:踩,31:竞拍参与,41:关注)' )
    inteltype=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='推荐类型' )
    remark=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='备注' )


class aboutus(Base_model):
    __doc__ = u'''aboutus'''
    __tablename__ = 'aboutus'



    __authTables__={}
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=False,comment='主键')
    addtime = db.Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'))
    title=db.Column( db.VARCHAR(255), nullable=False, unique=False,comment='标题' )
    subtitle=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='副标题' )
    content=db.Column( db.Text, nullable=False, unique=False,comment='内容' )
    picture1=db.Column( db.Text,  nullable=True, unique=False,comment='图片1' )
    picture2=db.Column( db.Text,  nullable=True, unique=False,comment='图片2' )
    picture3=db.Column( db.Text,  nullable=True, unique=False,comment='图片3' )


class systemintro(Base_model):
    __doc__ = u'''systemintro'''
    __tablename__ = 'systemintro'



    __authTables__={}
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=False,comment='主键')
    addtime = db.Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'))
    title=db.Column( db.VARCHAR(255), nullable=False, unique=False,comment='标题' )
    subtitle=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='副标题' )
    content=db.Column( db.Text, nullable=False, unique=False,comment='内容' )
    picture1=db.Column( db.Text,  nullable=True, unique=False,comment='图片1' )
    picture2=db.Column( db.Text,  nullable=True, unique=False,comment='图片2' )
    picture3=db.Column( db.Text,  nullable=True, unique=False,comment='图片3' )


class messages(Base_model):
    __doc__ = u'''messages'''
    __tablename__ = 'messages'



    __authTables__={}
    __hasMessage__='是'
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=False,comment='主键')
    addtime = db.Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'))
    userid=db.Column( db.BigInteger, nullable=False, unique=False,comment='留言人id' )
    username=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='用户名' )
    avatarurl=db.Column( db.Text,  nullable=True, unique=False,comment='头像' )
    content=db.Column( db.Text, nullable=False, unique=False,comment='留言内容' )
    cpicture=db.Column( db.Text,  nullable=True, unique=False,comment='留言图片' )
    reply=db.Column( db.Text,  nullable=True, unique=False,comment='回复内容' )
    rpicture=db.Column( db.Text,  nullable=True, unique=False,comment='回复图片' )


class discussqihuoxinxi(Base_model):
    __doc__ = u'''discussqihuoxinxi'''
    __tablename__ = 'discussqihuoxinxi'



    __authTables__={}
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=False,comment='主键')
    addtime = db.Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'))
    refid=db.Column( db.BigInteger, nullable=False, unique=False,comment='关联表id' )
    userid=db.Column( db.BigInteger, nullable=False, unique=False,comment='用户id' )
    avatarurl=db.Column( db.Text,  nullable=True, unique=False,comment='头像' )
    nickname=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='用户名' )
    content=db.Column( db.Text, nullable=False, unique=False,comment='评论内容' )
    reply=db.Column( db.Text,  nullable=True, unique=False,comment='回复内容' )


class discusstouzifengxian(Base_model):
    __doc__ = u'''discusstouzifengxian'''
    __tablename__ = 'discusstouzifengxian'



    __authTables__={}
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=False,comment='主键')
    addtime = db.Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'))
    refid=db.Column( db.BigInteger, nullable=False, unique=False,comment='关联表id' )
    userid=db.Column( db.BigInteger, nullable=False, unique=False,comment='用户id' )
    avatarurl=db.Column( db.Text,  nullable=True, unique=False,comment='头像' )
    nickname=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='用户名' )
    content=db.Column( db.Text, nullable=False, unique=False,comment='评论内容' )
    reply=db.Column( db.Text,  nullable=True, unique=False,comment='回复内容' )


