# import logging;logging.basicConfig(level=logging.INFO)
# #
# # import asyncio,os,json,time
# # from datetime import datetime
# #
# # from aiohttp import web
# #
# # def index(request):
# # 	return web.Response(body=b'<h1>Awesome</h1>')
# #
# # @asyncio.coroutine
# # def init(loop):
# # 	app=web.Application(loop=loop)
# # 	app.router.add_route('GET','/',index)
# # 	# srv=yield from loop.craete_sever(app.make_handler(),'127.0.0.1',8888)
# # 	srv = yield from loop.create_server(app.make_handler(), '127.0.0.1', 8888)
# # 	logging.info('server start at http://127.0.0.1:8888!!!!')
# # 	return srv
# #
# # loop=asyncio.get_event_loop()
# # # loop.run_until_complete(init(loop))
# # loop.run_until_complete(init(loop))
# # loop.run_forever()

import logging; logging.basicConfig(level=logging.INFO)
import asyncio
from aiohttp import web

## 定义服务器响应请求的的返回为 "Awesome Website"
async def index(request):
    return web.Response(body=b'<h1>Awesome Website</h1>', content_type='text/html')

## 建立服务器应用，持续监听本地9000端口的http请求，对首页"/"进行响应
def init():
    app = web.Application()
    app.router.add_get('/', index)
    web.run_app(app, host='127.0.0.1', port=9000)

if __name__ == "__main__":
    init()