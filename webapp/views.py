import aiohttp_jinja2

from webapp.utils import load_teams, load_resources


@aiohttp_jinja2.template('index.html')
async def index(request):
    logger = request.app.logger
    logger.info('Accessing index page')
    cache = request.app['cache']

    teams = await load_teams()
    available_resources = await load_resources()

    resources = {}
    for resource in available_resources:
        resource_data = await cache.get(resource)
        resources[resource] = resource_data

    import pdb; pdb.set_trace()
    return {
        'teams': teams,
        'resources': resources
    }
