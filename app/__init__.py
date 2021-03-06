﻿# -*- coding: utf-8 -*-

# 导入包
from datetime import timedelta

from flask import Flask, session
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_moment import Moment
from flask_mail import Mail
from flask_pagedown import PageDown
from flask_wtf.csrf import CsrfProtect


# 导入配置
from config import config


# 实例化拓展模块
bootstrap = Bootstrap()
login_manager = LoginManager()
db = SQLAlchemy()
moment = Moment()
mail = Mail()
pagedown = PageDown()
csrf = CsrfProtect()

# 设置登陆管理
# 用户会话安全等级
login_manager.session_protection = "strong"
# 要在用户登录时重定向到的视图的名称
login_manager.login_view = '.login'
# 进行登录检查没有通过时显示的信息
login_manager.login_message = '登录后才能访问'
# login_message的类型
login_manager.login_message_category = 'info'
# cookie过期时间 默认为1年
login_manager.remember_cookie_duration=timedelta(days=1)


def create_app(config_name):
    """程序工厂函数"""

    app = Flask(__name__)
    # 进行app配置 把自己的config设定导入到app中
    # from_object会把参数的所有的大写名属性导入到app的config中
    app.config.from_object(config[config_name])
    # 初始化app配置
    config[config_name].init_app(app)

    # 为app加上各种拓展模块
    bootstrap.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    pagedown.init_app(app)
    csrf.init_app(app)

    return app
