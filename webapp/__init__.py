# -*- coding: utf-8 -*-
import aioredis

import config
from . import views


def setup_routes(app):
    app.router.add_get('/', views.index)


def setup_static_routes(app):
    app.router.add_static('/static/',
                          path=config.PROJECT_ROOT / 'static',
                          name='static')
    app.router.add_static('/node_modules/',
                          path=config.PROJECT_ROOT / 'node_modules',
                          name='node_modules')


async def setup_cache(app):
    redis = await aioredis.create_redis(config.REDIS_URI)
    app['cache'] = redis


async def destroy_cache(app):
    redis = app['cache']
    redis.close()
    await redis.wait_closed()
