import re
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class extractLink(CrawlSpider):
	item_id = 0
	name = 'mainspider'
	allowed_domains = ['www.imdb.com']
	start_urls = ['http://imdb.com']
	
	# Hashmap to make sure there's no repetition when parsing url to follow
	global url_hashMap
	url_hashMap = dict()

	# The Regex for the page that we are looking for, in the case of imdb, the movie page
	global page_re
	page_re = 'com\/title\/tt[0-9]+\/?$'

	# Parse the url to be followed, remove query string and disallow repetition
	def process_url(url):
		'''
		Process the url before the spider starts to crawl that page
		Remove the query string and check for repetition
		If that page has not been crawled before, store in dictionary and return url, else return None
		'''
		result = re.match('(http:\/\/.*)\?', url)

		# Make sure that there's no repetition using a dictionary
		if result:
			result_url = result.group(1).strip("/")

			if result_url not in url_hashMap:
				url_hashMap[result_url] = None
				return result_url
			else:
				return None
		else:
			if url not in url_hashMap:
				url_hashMap[url] = None
				return url
			else:
				return None

	# Spider will start by crawling start_urls
	# If any url match the rules, it will execute the first matched rules and any given callback function
	# If follow=true, it will follow the url that it matches

	# Rules to follow, crawl all pages, repeated pages are process at process_url, callback parse_items if match movie page
	rules = (
		Rule(LinkExtractor(process_value=process_url, allow=(page_re)), callback='parse_items', follow=True),
		Rule(LinkExtractor(process_value=process_url), follow=True)
	)

	# 
	def save_page_to_file(self, filename, content):
		'''
		Create a file name filename and write the content to the file
		'''
		with open(filename, 'wb') as htmlfile:
			htmlfile.write(content)

	def parse_items(self, response):
		'''
		Parse the response
		Save the body of the response to a unique html file
		Parse the data into an object to be stored in data format (JSON, CSV, XML)
		'''
		# Save the html pages to a folder htmlFiles
		page_id = response.url.split("/")[-2]
		filename = 'htmlFiles/%s.html' % page_id
		self.save_page_to_file(filename, response.body)

		yield{
			'response': response.url,
		}
