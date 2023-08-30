from typing import Generator

import scrapy
from scrapy.http.response.html import HtmlResponse

from pep_parse.items import PepParseItem
from pep_parse.settings import DOMAIN


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = [DOMAIN]
    start_urls = [f'https://{DOMAIN}/']

    def parse(self, response: HtmlResponse) -> Generator:
        pep_links = response.css('#numerical-index a::attr(href)').extract()
        for pep_link in pep_links:
            if pep_link and pep_link != '#numerical-index':
                yield response.follow(pep_link, callback=self.parse_pep)

    def parse_pep(self, response: HtmlResponse) -> Generator:
        data = {
            'number': int(response.css(
                '#pep-content h1::text').re_first(r'\d+')),
            'name': response.css(
                '#pep-content h1::text').get().split('–')[1].strip(),
            'status': response.css(
                'dt:contains("Status") + dd abbr::text').get()
        }
        yield PepParseItem(data)
