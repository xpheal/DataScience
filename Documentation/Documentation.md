Settings:
1) useSettings: Boolean: Use the given settings file
2) save_html_to_directory: Boolean: Save html files to given directory
3) save_data_to_csv: Boolean: Scrape data with the regex expression and save to csv
4) allowed_domains: List of strings = only crawl domains in the list, filter off other domains
5) start_urls: List of strings = start crawling from the first url in the list, then move on to the next
6) csv_output_file: String = name of the csv output file
7) html_directory_name: String = name of the directory for saving html files
8) save_file_regex: String = regex to match the url and use the first regex group as the name of the page
	Example: url: "http://www.example.com", regex: '([^./]*).com$', will save file as example.html
9) remove_url_query: Boolean = Filter off the query string of the url when crawling
10) page_regex: String = regex to match the url and if the url matches, data will be scraped from that page
11) randomize_download_delay: Integer = 0, no randomize delay, 1+, randomize delay
12) download_delay: Integer = 0, no download delay, 1+, multiply with random_delay to get the download_delay
13) depth_priority: Integer = 0, no depth priority, 1+, priority given to lower depth pages
14) data_extract_path:
		colName: The column name for the data in the csv file
		xPathString: The xPath to the data in the html document
