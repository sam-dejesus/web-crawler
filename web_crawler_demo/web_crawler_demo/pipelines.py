# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from itemadapter import ItemAdapter
import json
import datetime

class JsonPipeline:

    def open_spider(self, spider):
        timestamp = datetime.datetime.now().strftime("%m-%d-%Y_%H-%M-%S")
        filename = f'output_{timestamp}.json'
        self.file = open(filename, 'w', encoding='utf-8')
        self.file.write('[\n')
        self.first_item = True

    def close_spider(self, spider):
        self.file.write('\n]')
        self.file.close()

    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False)
        if not self.first_item:
            self.file.write(',\n')
        else:
            self.first_item = False
        self.file.write(line)
        return item
