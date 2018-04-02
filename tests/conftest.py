import pytest

import config


TESTS_DIR = config.PROJECT_ROOT / 'tests'
PAGES_DIR = TESTS_DIR / 'pages'


@pytest.fixture
def page_html():
    def inner(page_name):
        filename = f'{PAGES_DIR}/{page_name}.html'
        with open(filename) as f:
            return f.read()
    return inner
