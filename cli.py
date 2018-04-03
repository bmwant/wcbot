# -*- coding: utf-8 -*-
import asyncio
import click

from crawler.factory import Factory
from crawler.scheduler import Scheduler


@click.group()
def cli():
    pass


async def schedule_monitoring():
    factory = Factory()
    await factory.init_cache()
    factory.load_resources()
    factory.load_teams()
    tasks = factory.create()
    scheduler = Scheduler(tasks=tasks)
    await scheduler.run()
    # todo: add cleanup for scheduler


@cli.command()
def monitor():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(schedule_monitoring())


@cli.command()
def check_drivers():
    pass


if __name__ == '__main__':
    cli()
