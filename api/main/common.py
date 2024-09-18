# coding:utf-8
# author:ila
import re
from flask import request, jsonify, session

from utils.jwt_auth import Auth
from utils.codes import *

from . import main_bp


@main_bp.before_request
def before_request():
    request__url = session.get('request__url')
    if request.method == 'GET':
        get_list = [
            "/",
            "/apidocs/",
             "/python206jhypi/examusers/login" ,
            "/python206jhypi/examusers/register",
            '/python206jhypi/defaultuser/login',
            '/python206jhypi/users/login',

        ]  # 免认证list
        

        # 重置密码时获取验证码不检测token。
        if request__url not in get_list and "/static/" not in request__url and "/js/" not in request__url  and "/css/" not in request__url and "/img/" not in request__url  and "/fonts/" not in request__url   and  "detail" not in request__url   and "templates" not in request__url and "/forum/flist" not in request__url and "/forum/list" not in request__url and "/upload/" not in request__url and "/examusers/login" not in request__url and "/examusers/register" not in request__url and  request__url[-5:]!="/list" and "/login" not in request__url  and "/dist" not in request__url and "/admin" not in request__url and "/autoSort" not in request__url and '/option' not in request__url and '/security' not in request__url and '/sendemail' not in request__url and '/updateBrowseDuration' not in request__url and '/sendsms' not in request__url or "autoSort2" in request__url:
            result = Auth.identify(Auth, request)

            if result.get('code') != normal_code:
                print('jwt auth success')
                return jsonify(result)



    elif request.method == 'POST':
        post_list = [
            '/python206jhypi/defaultuser/register',
            '/python206jhypi/defaultuser/login',
            '/python206jhypi/users/register',
            '/python206jhypi/users/login',
            "/python206jhypi/examusers/login" ,
            "/python206jhypi/examusers/register"
        ]  # 免认证list
        if request__url not in post_list and "register" not in request__url and "login" not in request__url and "faceLogin" not in request__url and '/file/upload' not in request__url and '/update' not in request__url:  # 注册时不检测token。
            result = Auth.identify(Auth, request)

            if result.get('code') != normal_code:
                print('jwt auth fail')
                return jsonify(result)
