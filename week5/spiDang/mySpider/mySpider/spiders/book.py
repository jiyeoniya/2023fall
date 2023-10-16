import scrapy
import csv


class BookSpider(scrapy.Spider):
    name = "book"
    allowed_domains = ["dangdang.com"]
    start_urls = ["http://search.dangdang.com/?key=%BC%C6%CB%E3%BB%FA&act=input"]

    def parse(self, response):
        book_node_list = response.xpath('/html/body/div[2]/div/div[3]/div[1]/div[1]/div[2]/div/ul/li')
        data = []
        for node in book_node_list:
            temp = {}
            # 将所有字符串拼接成一个字符串
            temp["book_name"] = ''.join(node.xpath("./p[1]/a/font/text() | ./p[1]/a/text()").getall())
            print(temp["book_name"])
            data.append(temp)
            yield temp
        with open('dangcombooks.csv', 'a', newline='', encoding='gbk') as csv_file:
            fieldnames = ['book_name']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            for item in data:
                writer.writerow(item)
        next_page_url = response.xpath('//a[@title="下一页"]/@href').get()
        if next_page_url:
            yield scrapy.Request(response.urljoin(next_page_url), callback=self.parse)
