from html.parser import HTMLParser

from bs4 import BeautifulSoup

from crawler.parser import BaseParser, BaseEngine


class _BSEngine(BaseEngine):
    def parse(self, html):
        html = html.replace('<!---->', '')
        soup = BeautifulSoup(html, 'html5lib')
        team_elem = 'ui-scoreboard-runner'
        team_class = 'ui-scoreboard-runner__home'
        teams = [e.getText().strip()
                 for e in soup.find_all(team_elem, team_class)]

        get_odds_elems = lambda x: x.find('btn-odds',
                                          class_='avb-item__btn-odds')
        get_odds_text = lambda x: x.getText().strip()
        odds_elems = map(get_odds_elems, soup.find_all('avb-item'))
        odds = map(get_odds_text, odds_elems)
        odds_values = map(self.get_odd_value, odds)
        return dict(zip(teams, odds_values))

    def get_odd_value(self, text):
        if text == 'EVS':
            return text

        if '/' in text:
            nominator, denominator = map(int, text.split('/'))
            return nominator / denominator

        try:
            return float(text)
        except ValueError:
            return text


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

    @property
    def data(self):
        return self._data

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


class PaddyPowerParser(BaseParser):
    def __init__(self, engine=_BSEngine):
        self.engine = engine()

    def parse(self, html):
        return self.engine.parse(html)


"""
<avb-item.

<ui-scoreboard-coupon

ui-scoreboard-runner -> span #first team
ui-scoreboard-runner -> span #second team


x3 ->
<div class="avb-item__box grid grid__cell-2-12" 
-> home
-> draw
-> away
"""
