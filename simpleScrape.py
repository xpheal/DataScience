import re
import argparse
import scrapy
from scrapy.crawler import CrawlerProcess
from simple_spider import simple_spider

def start_crawler(settings_obj):
	process = CrawlerProcess({
		'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; WINDOWS NT 5.1'
	})

	# Load spider settings
	simple_spider.load_settings(simple_spider, settings_obj)

	# Start crawling
	process.crawl(simple_spider)
	process.start()

# Return default settings for spider
def get_default_settings_obj():
	settings_obj = {}
	settings_obj["save_html_to_directory"] = False
	settings_obj["save_data_to_csv"] = False
	settings_obj["allowed_domains"] = []
	settings_obj["start_urls"] = []
	settings_obj["csv_output_file"] = None
	settings_obj["html_directory_name"] = None
	settings_obj["save_file_regex"] = None
	settings_obj["remove_url_query"] = False
	settings_obj["page_regex"] = None
	settings_obj["randomize_download_delay"] = 0
	settings_obj["download_delay"] = 0
	settings_obj["depth_priority"] = 0
	settings_obj["data_extract_path"] = None
	return settings_obj

# Download argument
def download(args):
	settings_obj = get_default_settings_obj()
	settings_obj["save_html_to_directory"] = True
	settings_obj["start_urls"] = [args.url]
	settings_obj["allowed_domains"] = [re.match('https?://(.*)', args.url).group(1)]
	settings_obj["html_directory_name"] = "HTMLFiles"
	settings_obj["save_file_regex"] = "http://(.*)"

	start_crawler(settings_obj)

def run(args):
	print(args.settings)

def scrape(args):
	print(args.url)

# Add parser
parser = argparse.ArgumentParser(prog='simpleScrape', description='Download or scrape the given url, see documentation for more info.')
subparsers = parser.add_subparsers()

download_parser = subparsers.add_parser('download', help='Download all the html files and save it in a directory')
download_parser.add_argument('url', help='Start crawling from this url')
download_parser.set_defaults(func=download)

run_parser = subparsers.add_parser('run', help='Run the scraper using the settings file')
run_parser.add_argument('settings', help='Settings to be loaded')
run_parser.set_defaults(func=run)

scrape_parser = subparsers.add_parser('scrape', help='Scrape data using given xpath to a csv file')
scrape_parser.add_argument('url', help='Start crawling from this url')
scrape_parser.add_argument('xpaths', help='List of (column,xpaths) object to be crawled')
scrape_parser.set_defaults(func=scrape)

# Parse arguments
args = parser.parse_args()
args.func(args)

# try:
# 		with open(settings_file, 'r') as jFile:
# 			dataSettings = json.load(jFile)
# 	except FileNotFoundError as ex:
# 		print("SETTINGS FILE NOT FOUND")
# 		print("RUN SCRAPER USING DEFAULT SETTINGS:")
# 		print("SCRAPE WAYNEDEV.ME AND SAVE ALL HTML FILES")
# 	except ValueError as ex:
# 		print("SETTINGS FILE CORRUPTED OR INVALID JSON FORMAT")
# 		print("RUN SCRAPER USING DEFAULT SETTINGS:")
# 		print("SCRAPE WAYNEDEV.ME AND SAVE ALL HTML FILES")