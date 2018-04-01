import os
from pathlib import Path


PROJECT_ROOT = Path(os.path.dirname(os.path.realpath(__file__)))
TEMPLATES_DIR = PROJECT_ROOT / 'templates'

REDIS_URI = 'redis://localhost'

UPDATE_PERIOD = 10

RESOURCES_FILEPATH = PROJECT_ROOT / 'resources.yml'

GECKO_DRIVER_PATH = PROJECT_ROOT / 'lib' / 'geckodriver'
CHROME_DRIVER_PATH = PROJECT_ROOT / 'lib' / 'chromedriver'

