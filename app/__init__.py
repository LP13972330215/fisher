"""
 Created by 七月 on 2018-2-5.
"""
from flask import Flask
from flask_login import LoginManager
from app.models.book import db
from flask_mail import Mail
# from flask_cache import Cache
from app.libs.limiter import Limiter

login_manager = LoginManager()
mail = Mail()
# cache = Cache(config={'CACHE_TYPE': 'simple'})
limiter = Limiter()


def create_app():
    app = Flask(__name__)  #初始化app
    app.config.from_object('app.secure')
    app.config.from_object('app.setting')#读取配置
    register_blueprint(app) #注册蓝图

    db.init_app(app) #将flask 对象app注册到db中
    login_manager.init_app(app)
    login_manager.login_view = 'web.login'
    login_manager.login_message = '请先登录或注册'

    mail.init_app(app)


    # db.create_all(app=app) 这两种方法都可以
    with app.app_context():
        db.create_all() #创建数据库
    return app


def register_blueprint(app):
    from app.web.book import web
    app.register_blueprint(web)
