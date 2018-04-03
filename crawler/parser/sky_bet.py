from html.parser import HTMLParser

from crawler.parser import BaseParser, BaseEngine


class _HTMLParserEngine(HTMLParser, BaseEngine):
    def __init__(self):
        super().__init__()

        self.resulting_html = ''
        self._appending = False
        self._data_buf = ''
        self._tags_stack = []
        self._data = {}
        self._ip = 0  # index pointer
        self._required_stack = [
            'avb-item',
            'ui-scoreboard-coupon',
            'ui-scoreboard-runner',
            'span',
        ]

    def process(self, html):
        pass

    @staticmethod
    def _wrap_in_tag(tag, data):
        return '<{tag}>{data}</{tag}>'.format(tag=tag, data=data.lstrip())

    def handle_starttag(self, tag, attrs):
        # print('Found tag', tag)
        # if tag == 'avb-item':
        #     print('Found avb-item')
        #     return
        #
        # if tag == 'ng-switch':
        #     print('Found ng-switch')
        #     return

        if tag == 'customtag':
            print('Found custom tag')

        if tag == 'sport-header':
            print(tag)
            return

        if tag == 'content-managed-page':
            print(tag)
            return

        if tag == 'promotion':
            print(tag)
            return

        if tag == 'single-market-default-layout':
            print(tag)
            return

    def handle_endtag(self, tag):
        pass

    def handle_data(self, data):
        pass


class SkyBetParser(BaseParser):
    def __init__(self, engine=_HTMLParserEngine):
        self.engine = engine

    def parse(self, html):
        self.engine.process(html)
        return self.engine.data


"""
Tree
"""
