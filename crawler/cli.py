# -*- coding: utf-8 -*-

"""Console script for wcbot."""
import asyncio
import click

from crawler import factory


@click.group()
def cli():
    pass


async def test_me():
    g = factory.main()
    r = g.requester
    await r.request('http://httpbin.org/get')
    await r.close()


@cli.command()
def test():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(test_me())


if __name__ == '__main__':
    cli()
