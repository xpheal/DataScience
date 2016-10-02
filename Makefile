###
# Makefile for webcrawler, crawling imdb.com
###

# define the flags
SPIDER = spider.py
FLAGS = -o $(CSV) -t csv -s $(SETTINGS)
SETTINGS = RANDOMIZE_DOWNLOAD_DELAY=True DOWNLOAD_DELAY=0.5 DEPTH_PRIORITY=1
CSV = data.csv
DEBUGFILE = debug.txt

main: $(SPIDER) htmlFiles 
	scrapy runspider $(SPIDER) $(FLAGS)

debug: $(SPIDER) htmlFiles
	scrapy runspider $(SPIDER) $(FLAGS) > $(DEBUGFILE)	

htmlFiles:
	mkdir htmlFiles

clean:
	rm -rf htmlFiles *.pyc debug.txt
