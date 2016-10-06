import scrapy
from scrapy.crawler import CrawlerProcess
from simple_spider import simple_spider

process = CrawlerProcess({
	'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; WINDOWS NT 5.1'
})

process.crawl(simple_spider)
process.start()