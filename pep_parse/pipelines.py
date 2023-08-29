import csv
from datetime import datetime as dt
from pep_parse.settings import BASE_DIR

DT_FORMAT = '%Y-%M-%d_%H-%M-%S'
OUTPUT_DIR = BASE_DIR / 'results'
FILE_NAME = 'status_summary_{time}.csv'


class PepParsePipeline:

    def open_spider(self, spider):
        self.results = {}

    def process_item(self, item, spider):
        pep_status = item['status']
        if self.results.get(pep_status):
            self.results[pep_status] += 1
        else:
            self.results[pep_status] = 1
        return item

    def close_spider(self, spider):
        time = dt.now().strftime(DT_FORMAT)
        total = sum(self.results.values())
        file_path = BASE_DIR / FILE_NAME.format(time=time)
        with open(file_path, mode='w', encoding='utf-8') as csvfile:
            fieldnames = ('Статус', 'Количество')
            writer = csv.DictWriter(
                csvfile, dialect='unix', fieldnames=fieldnames)
            writer.writeheader()
            for status, amount in self.results.items():
                writer.writerow({'Статус': status, 'Количество': amount})
            writer.writerow({'Статус': 'Total', 'Количество': total})
