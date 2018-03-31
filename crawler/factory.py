"""
Create `Grabber` instances for list of resources we need to grab information
from.
"""
from crawler.requester import Requester
from crawler.parser import BaseParser
from crawler.grabber import Grabber


class Factory(object):
    def __init__(self, resources=None):
        self.resources = resources or []

    def load_meta(self):
        pass

    def create(self):
        grabbers = []
        for res in self.resources:
            requester = Requester(base_url=res)
            parser = BaseParser()
            grabber = Grabber(
                base_url=res,
                requester=requester,
                parser=parser,
            )
            grabbers.append(grabber)
        return grabbers


def main():
    # Load description from yaml file
    resources = [
        'http://httpbin.org/get',
    ]
    factory = Factory(resources=resources)
    grabbers = factory.create()
    return grabbers[0]
