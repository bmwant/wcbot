import pytest

from crawler.fetcher.browser import BrowserFetcher


@pytest.fixture
def browser_fetcher(loop):
    fetcher = BrowserFetcher(None)
    yield fetcher
    loop.run_until_complete(fetcher.close())


@pytest.mark.run_loop
@pytest.mark.external
async def test_browser_fetcher(browser_fetcher):
    url = ('https://www.paddypower.com/'
           'football/2018-fifa-world-cup?tab=outrights')
    resp = await browser_fetcher.request(url)
    with open('f.html', 'w') as f:
        f.write(resp)

    assert 'Brazil' in resp
    # Check hidden element is on page too
    assert 'South Korea' in resp
    assert 'Costa Rica' in resp
