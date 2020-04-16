"""
 Created by 七月 on 2018/1/26.
 微信公众号：林间有风
"""
__author__ = '七月'


def is_isbn_or_key(word):
    """
    """
    isbn_or_key = 'key'
    if len(word) == 13 and word.isdigit():
        isbn_or_key = 'isbn'
    short_word = word.replace('-', '')
    if '-' in word and len(short_word) == 10 and short_word.isdigit:
        isbn_or_key = 'isbn'
    return isbn_or_key
