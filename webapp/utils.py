import operator
import yaml
import config


async def load_yaml(filepath):
    with open(filepath) as f:
        return yaml.load(f.read())


async def load_teams():
    data = await load_yaml(config.TEAMS_FILEPATH)
    return data


async def load_resources():
    data = await load_yaml(config.RESOURCES_FILEPATH)
    return map(operator.itemgetter('name'), data)

