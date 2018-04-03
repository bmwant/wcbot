from crawler.parser.paddy_power import PaddyPowerParser
from crawler.parser.sky_bet import SkyBetParser


def test_paddy_power_parser(page_html):
    html = page_html('paddy_power')
    parser = PaddyPowerParser()

    data = parser.parse(html=html)
    print(data)


def test_sky_bet_parser(page_html):
    html = page_html('sky_bet')
    parser = SkyBetParser()
    data = parser.parse(html)
    assert 'Brazil' in data
    assert 'Poland' in data
    assert 'Russia' in data
    assert all([isinstance(k, str) for k in data.keys()])
    assert all([isinstance(v, float) for v in data.values()])


