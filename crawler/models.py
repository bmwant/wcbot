import attr


@attr.s
class Resource(object):
    name: str = attr.ib()
    url: str = attr.ib()
    use_proxy: bool = attr.ib(default=False)
