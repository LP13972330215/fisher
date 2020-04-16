"""
 Created by 七月 on 2018/1/26.
 微信公众号：林间有风
"""
from sqlalchemy import Column, Integer, String

from app.models.base import db

__author__ = '七月'


class Book(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)
    author = Column(String(30), default='未名')
    binding = Column(String(20))
    publisher = Column(String(50))
    price = Column(String(20))
    pages = Column(Integer)
    pubdate = Column(String(20))
    isbn = Column(String(15), nullable=False, unique=True)
    summary = Column(String(1000))
    image = Column(String(50))

    # MVC M Model 只有数据 = 数据表
    # ORM 对象关系映射 Code First

    def sample(self):
        pass
