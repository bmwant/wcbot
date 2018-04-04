import asyncio

import aiohttp_jinja2
from aiohttp import web

from webapp.utils import (
    load_teams,
    load_resources,
    get_cached_value,
    refresh_data,
)


@aiohttp_jinja2.template('index.html')
async def index(request):
    logger = request.app.logger
    logger.info('Accessing index page')
    cache = request.app['cache']

    teams = await load_teams()
    available_resources = await load_resources()

    resources = {}
    has_data = False
    for resource in available_resources:
        resource_data = await get_cached_value(cache=cache,
                                               key=resource)
        if resource_data is not None:
            has_data = True
        resources[resource] = resource_data

    if not has_data:
        loading_url = request.app.router['loading'].url_for()
        return web.HTTPFound(loading_url)

    return {
        'teams': teams,
        'resources': resources
    }


@aiohttp_jinja2.template('loading.html')
async def loading(request):
    logger = request.app.logger
    cache = request.app['cache']
    logger.info('Accessing loading page')
    in_progress = await cache.get('refreshing')
    if not in_progress:
        loop = asyncio.get_event_loop()
        loop.call_soon(refresh_data)
        await cache.set('refreshing', 1)


async def check_refresh_done(request):
    cache = request.app['cache']
    refreshing = bool(await cache.get('refreshing'))

    return web.json_response({
        'refreshing': refreshing
    })
