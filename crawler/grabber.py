"""
Grab information needed from a resource and store it.
"""


class Grabber(object):
    def __init__(self, base_url, requester=None, parser=None):
        self.base_url = base_url
        self.requester = requester
        self.parser = parser
