###
# Makefile for webcrawler, crawling imdb.com
###

# define the flags
SPIDER = spider.py
FLAGS = -o $(CSV) -t csv
CSV = test.csv
XPATHSETTINGS = settings.json
DEBUGFILE = debug.txt

parse:
	python htmlParser.py $(XPATHSETTINGS) $(CSV) -d htmlFiles 

spider: $(SPIDER) htmlFiles 
	scrapy runspider $(SPIDER) $(FLAGS)

debug: $(SPIDER) htmlFiles
	scrapy runspider $(SPIDER) $(FLAGS) > $(DEBUGFILE)	

htmlFiles:
	mkdir htmlFiles

cleanAll:
	rm -rf htmlFiles *.pyc debug.txt

clean:
	rm -rf *.pyc debug.txt
