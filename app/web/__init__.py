"""
 Created by 七月 on 2018/1/26.
 微信公众号：林间有风
"""
from flask import Blueprint
from flask import render_template

__author__ = '七月'

web = Blueprint('web', __name__)


@web.app_errorhandler(404)
def not_found(e):
    # AOP 思想
    return render_template('404.html'), 404


from app.web import book
from app.web import auth
from app.web import drift
from app.web import gift
from app.web import main
from app.web import wish
from app.web import test
# from app.web import user
