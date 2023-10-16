import scrapy

from mySpider.items import MyspiderItem

class DangdangSpider(scrapy.Spider):
    name = "dangdang"
    allowed_domains = ["dangdang.com"]
    start_urls = ["http://search.dangdang.com/?key=%BC%C6%CB%E3%BB%FA%C0%E0&category_path=01.54.00.00.00.00#J_tab"]

    def parse(self, response):
        items = []
        books = response.css("ul.bigimg li")
        for book in books:
            item = MyspiderItem()
            item['name'] = book.css("p.name a::attr(title)").get()
            items.append(item)

        filename = "book.html"
        open(filename,'w').write(items)

        pass
