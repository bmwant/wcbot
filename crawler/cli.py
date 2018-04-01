# -*- coding: utf-8 -*-
import asyncio
import click

from crawler.factory import Factory
from crawler.scheduler import Scheduler


@click.group()
def cli():
    pass


async def test_me():
    factory = Factory()
    await factory.init_cache()
    factory.load_meta()
    tasks = factory.create()
    scheduler = Scheduler(tasks=tasks)
    await scheduler.run()
    # Add cleanup for scheduler


@cli.command()
def test():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(test_me())


@cli.command()
def check_drivers():
    pass


if __name__ == '__main__':
    cli()
