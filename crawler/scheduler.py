"""
Schedule periodic tasks and ensure their execution within given period.
"""
import asyncio

import config
from utils import get_logger


class Scheduler(object):
    def __init__(self, tasks=None, interval=config.UPDATE_PERIOD):
        self.tasks = tasks or []
        self.interval = interval
        self.logger = get_logger(self.__class__.__name__.lower())

    async def run(self):
        # todo: add exceptions handling within child processes
        while True:
            await asyncio.gather(*self.tasks)
            self.logger.info('Waiting %s seconds to make next update...' %
                             self.interval)
            await asyncio.sleep(self.interval)
