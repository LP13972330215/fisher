#! /usr/bin/env python3


from app import create_app

__author__ = '七月'

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=app.config['DEBUG'], port=81, threaded=True)
    #单进程、单线程
    # processes = 1
    # 10 个请求
