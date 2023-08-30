from pathlib import Path

BOT_NAME = 'pep_parse'

NEWSPIDER_MODULE = f'{BOT_NAME}.spiders'
SPIDER_MODULES = [NEWSPIDER_MODULE]

ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {'pep_parse.pipelines.PepParsePipeline': 300, }
BASE_DIR = Path(__file__).parent.parent
DT_FORMAT = '%Y-%M-%d_%H-%M-%S'
OUTPUT_DIR = BASE_DIR / 'results'
FILE_NAME = 'status_summary_{time}.csv'

FEEDS = {
    'results/pep_%(time)s.csv': {
        'format': 'csv',
        'fields': ['number', 'name', 'status'],
        'owerwrite': True
    }
}
