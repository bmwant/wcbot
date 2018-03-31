import aiohttp_jinja2


@aiohttp_jinja2.template('index.html')
async def index(request):
    logger = request.app.logger
    logger.info('Accessing index page')
    cache = request.app['cache']
    value = await cache.get('key')
    return value
