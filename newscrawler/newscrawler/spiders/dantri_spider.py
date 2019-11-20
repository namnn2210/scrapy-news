import scrapy
from ..items import NewscrawlerItem


class DantriSpider(scrapy.Spider):
    name = "dantri"
    page_number = 2
    start_urls = ["https://vnexpress.net/the-thao/p1"]

    def parse(self, response):
        all_div_news = response.css("section.sidebar_1")

        for div in all_div_news:
            title = div.css("article.list_news h4.title_news a::text")[0].extract()
            href = "https://dantri.com.vn" + div.css("a.fon6").xpath('@href')[0].extract()

            if href:
                request = scrapy.Request(url=href, callback=self.raw_content_parse)
                request.meta['title'] = title
                yield request

        next_page = "https://dantri.com.vn/the-thao/trang-" + str(DantriSpider.page_number) + ".htm"
        if DantriSpider.page_number <= 1:
            DantriSpider.page_number += 1
            yield response.follow(next_page, callback=self.parse)

    def raw_content_parse(self, response):
        title = response.meta.get('title')
        href = response.url
        str = ''
        for raw_content in response.css("div.detail-content p::text").extract():
            str += raw_content
        print(str)
        print("=============================")
        # items = NewscrawlerItem()
        # items['title'] = title
        # items['href'] = href
        # items['raw_content'] = str
        # yield items
