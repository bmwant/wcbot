# -*- coding: utf-8 -*-
import asyncio
import click

from crawler.factory import Factory
from crawler.scheduler import Scheduler
from utils import get_logger


@click.group()
def cli():
    pass


async def schedule_monitoring():
    logger = get_logger()
    factory = Factory()
    await factory.init_cache()
    factory.load_resources()
    factory.load_teams()
    tasks = factory.create()
    scheduler = Scheduler(tasks=tasks)
    try:
        await scheduler.run_forever()
    except KeyboardInterrupt:
        logger.warning('Exiting...')
    finally:
        await scheduler.cleanup()


@cli.command()
def monitor():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(schedule_monitoring())


@cli.command()
def check_drivers():
    pass


if __name__ == '__main__':
    cli()
