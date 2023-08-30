from pathlib import Path

BOT_NAME = 'pep_parse'
DOMAIN = 'peps.python.org'

NEWSPIDER_MODULE = f'{BOT_NAME}.spiders'
SPIDER_MODULES = [NEWSPIDER_MODULE]

ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {'pep_parse.pipelines.PepParsePipeline': 300, }
BASE_DIR = Path(__file__).parent.parent
DT_FORMAT = '%Y-%M-%d_%H-%M-%S'
OUTPUT_DIR = 'results'
FILE_NAME = '{OUTPUT_DIR}/status_summary_{time}.csv'

FEEDS = {
    f'{OUTPUT_DIR}/pep_%(time)s.csv': {
        'format': 'csv',
        'fields': ['number', 'name', 'status'],
        'owerwrite': True
    }
}
