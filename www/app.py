#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Albert Zhang'

'''
async web application.
'''

import logging; logging.basicConfig(level = logging.INFO)

import asyncio, os, json, time
from datetime import datetime

from aiohttp import web

def index(request):
	return web.Response(body = b'<h1>Awesome Albert</h1>')

@asyncio.coroutine
def init(loop):
	app = web.Application(loop = loop)
	app.router.add_route('Get', '/', index)
	srv = yield from loop.create_server(app.make_handler(),'192.168.56.254', 9001)
	logging.info('server started at http://localhost:9001...')
	return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()
