from crawler.parser.paddy_power import PaddyPowerParser


def test_paddy_power_parser(page_html):
    # html = page_html('paddy_power')
    html = page_html('paddy_power')
    parser = PaddyPowerParser()

    data = parser.parse(html=html)
    print(data)
