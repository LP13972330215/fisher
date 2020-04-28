#! /usr/bin/env python3


from app import create_app


app = create_app()#第一步

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=app.config['DEBUG'], port=81, threaded=True)
    #单进程、单线程
    # processes = 1
    # 10 个请求
