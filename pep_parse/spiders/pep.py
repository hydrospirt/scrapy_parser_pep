import scrapy
from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        pep_links = response.css('#numerical-index a::attr(href)').extract()
        for pep_link in pep_links:
            if pep_link and pep_link != '#numerical-index':
                yield response.follow(pep_link, callback=self.parse_pep)

    def parse_pep(self, response):
        data = {
            'number': int(response.css(
                '#pep-content h1::text').re_first(r'\d+')),
            'name': response.css(
                '#pep-content h1::text').get().split('–')[1].strip(),
            'status': response.css(
                'dt:contains("Status") + dd abbr::text').get()
        }
        yield PepParseItem(data)
