#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging; logging.basicConfig(level=logging.INFO)

import asyncio, os, json, time
from datetime import datetime

from aiohttp import web


def index(req):
    return web.Response(body='<h1>Hello web</h1>')

async def init(loop):
    hostname = '127.0.0.1'
    port = 9100
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', index)
    srv = await loop.create_server(app.make_handler(), hostname, port)
    logging.info('server start at http://%s:%s' % (hostname, port))
    return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()