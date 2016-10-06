import os
import json
import re
import scrapy
import csv
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class simple_spider(CrawlSpider):
	# Default Settings
	name = 'generic_spider'
	allowed_domains = ['waynedev.me']
	start_urls = ['http://waynedev.me']
	html_directory_name = 'htmlFiles'
	save_file_regex = 'http://(.*)'
	save_html_to_directory = True
	save_data_to_csv = False
	data_extract_path = None
	csv_output_file = "csv_output_file.csv"

	# Customize functions
	# Hashmap to make sure there's no repetition when parsing url to follow
	global url_hashMap
	url_hashMap = dict()

	# Remove query string in url if set to true, true by default
	global remove_url_query
	remove_url_query = True

	# The Regex for the page that you are looking for
	global page_regex
	page_regex = None

	# Crawler Settings
	randomize_download_delay = 0
	download_delay = 0
	depth_priority = 0


	# Load settings from json
	settings_file = "quoteSettings.json"
	dataSettings = None

	try:
		with open(settings_file, 'r') as jFile:
			dataSettings = json.load(jFile)
	except FileNotFoundError as ex:
		print("SETTINGS FILE NOT FOUND")
		print("RUN SCRAPER USING DEFAULT SETTINGS:")
		print("SCRAPE WAYNEDEV.ME AND SAVE ALL HTML FILES")
	except ValueError as ex:
		print("SETTINGS FILE CORRUPTED OR INVALID JSON FORMAT")
		print("RUN SCRAPER USING DEFAULT SETTINGS:")
		print("SCRAPE WAYNEDEV.ME AND SAVE ALL HTML FILES")

	if dataSettings:
		if dataSettings['useSettings']:
			save_html_to_directory = dataSettings["save_html_to_directory"]
			save_data_to_csv = dataSettings["save_data_to_csv"]
			allowed_domains = dataSettings["allowed_domains"]
			start_urls = dataSettings["start_urls"]
			csv_output_file = dataSettings["csv_output_file"]
			html_directory_name = dataSettings["html_directory_name"]
			save_file_regex = dataSettings["save_file_regex"]
			remove_url_query = dataSettings["remove_url_query"]
			page_regex = dataSettings["page_regex"]
			randomize_download_delay = dataSettings["randomize_download_delay"]
			download_delay = dataSettings["download_delay"]
			data_extract_path = dataSettings["data_extract_path"]

	# Set crawler settings
	custom_settings = {
		'RANDOMIZE_DOWNLOAD_DELAY': randomize_download_delay,
		'DOWNLOAD_DELAY': download_delay,
		'DEPTH_PRIORITY': depth_priority,
	}

	# Parse the url to be followed, remove query string and disallow repetition
	def process_url(url):
		'''
		Process the url before the spider starts to crawl that page
		Remove the query string and check for repetition
		If that page has not been crawled before, store in dictionary and return url, else return None
		'''
		if not remove_url_query:
			return url

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
		Rule(LinkExtractor(process_value=process_url, allow=(page_regex)), callback='parse_items', follow=True),
		Rule(LinkExtractor(process_value=process_url), follow=True)
	)

	# Write top row of csv file
	if save_data_to_csv:
		with open(csv_output_file, 'w') as csv_out:
			csv.writer(csv_out).writerow([i['colName'] for i in data_extract_path])

	# Write content to filename, create directory if it doesn't exist
	def write_html_file(self, filename, content):
		'''
		Create a file name filename and write the content to the file
		'''
		try:
			os.makedirs(re.sub('/[^/]*$', '', filename), exist_ok=True)
		except OSError as ex:
			print("FAILED TO CREATE DIRECTORY: " + re.sub('/[^/]*$', '', filename))
			print(format(ex))
			return

		with open(filename, 'wb') as htmlfile:
			htmlfile.write(content)

	def parse_items(self, response):
		'''
		Parse the response
		Save the body of the response to a unique html file
		Parse the data into an object to be stored in data format (JSON, CSV, XML)
		'''
		# Save the html pages to a folder htmlFiles
		if self.save_html_to_directory:
			page_id = re.match(self.save_file_regex, response.url)
			filename = self.html_directory_name + '/%s.html' % page_id.group(1)
			self.write_html_file(filename, response.body)

		# Save the data to csv file
		if self.save_data_to_csv:
			with open(self.csv_output_file, 'a') as csv_out:
				csv.writer(csv_out).writerow(",".join(response.xpath(i["xPathString"]).extract()) for i in self.data_extract_path)