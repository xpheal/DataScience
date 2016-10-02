import argparse
import csv
from io import StringIO
from lxml import etree
from os import listdir

# arguments check
parser = argparse.ArgumentParser(description='Parse data from html files and store in csv')
parser.add_argument('-i', metavar='<HTMLInput>', help='html input to be parsed')
parser.add_argument('-o', metavar='<CSVOutput>', help='output result to this file path')
parser.add_argument('-d', metavar='<Directory>', help='the input directory to be parsed')
args = parser.parse_args()

# Get input
# inputFile = args.i
outputFile = args.o
directory = args.d

files = None

# if inputFile:
	# files = inputFile

# if directory:
	# files = listdir(directory)

def parseList(list):
	print(list)

with open(outputFile, 'w') as csvfile:
	writer = csv.writer(csvfile)
	
	data = ("name", "duration", "year", "genre", "release", "rating", "ratingCount", "director", "cast",
		 "numUserReview", "numCritic")	
	writer.writerow(data)

	for file in listdir(directory):
		print(directory + '/' + file)
		with open(directory + '/' + file, 'r') as f:

			treeParser = etree.HTMLParser()
			tree = etree.parse(StringIO(f.read()), treeParser)

			# Data to collect
			name = tree.xpath('//*[@id="title-overview-widget"]/div[2]/div[2]/div/div[2]/div[2]/h1/text()')[0].strip()
			duration = tree.xpath('//*[@id="title-overview-widget"]/div[2]/div[2]/div/div[2]/div[2]/div/time/text()')[0].strip()
			year = tree.xpath('//*[@id="titleYear"]/a/text()')[0].strip()
			genre = join(tree.xpath('//*[@id="title-overview-widget"]/div[2]/div[2]/div/div[2]/div[2]/div/a/span/text()'))
			release = tree.xpath('//*[@id="title-overview-widget"]/div[2]/div[2]/div/div[2]/div[2]/div/a[3]/text()')[0].strip()
			rating = tree.xpath('//*[@id="title-overview-widget"]/div[2]/div[2]/div/div[1]/div[1]/div[1]/strong/span/text()')[0].strip()
			ratingCount = tree.xpath('//*[@id="title-overview-widget"]/div[2]/div[2]/div/div[1]/div[1]/a/span/text()')[0].strip()
			director = tree.xpath('//*[@id="title-overview-widget"]/div[3]/div[2]/div[1]/div[2]/span/a/span/text()')[0].strip()
			cast = ",".join(tree.xpath('//*[@id="title-overview-widget"]/div[3]/div[2]/div[1]/div[4]/span/a/span/text()'))
			numUserReview = tree.xpath('//*[@id="title-overview-widget"]/div[3]/div[2]/div[2]/div/div[2]/span/a[1]/text()')[0].strip()
			numCritic = tree.xpath('//*[@id="title-overview-widget"]/div[3]/div[2]/div[2]/div/div[2]/span/a[2]/text()')[0].strip()
			# story = tree.xpath('//*[@id="titleStoryLine"]/div[1]/p/text()')[0].strip()
			# language = ",".join(tree.xpath('//*[@id="titleDetails"]/div[3]/a/text()'))
			# country = tree.xpath('//*[@id="titleDetails"]/div[2]/a/text()')[0].strip()
			# filmingLocation = tree.xpath('//*[@id="titleDetails"]/div[6]/a/text()')[0].strip()
			# productionCompany = ",".join(tree.xpath('//*[@id="titleDetails"]/div[7]/span/a/span/text()'))
			# soundMix = tree.xpath('//*[@id="titleDetails"]/div[9]/a/text()')[0].strip()
			# color = tree.xpath('//*[@id="titleDetails"]/div[10]/a/text()')[0].strip()

			writer.writerow((name, duration, year, genre, release, rating, ratingCount, director, cast, numUserReview, numCritic))
# Debug
# print(name)
# print(duration)
# print(year)
# print(genre)
# print(release)
# print(rating)
# print(ratingCount)
# print(director)
# print(cast)
# print(numUserReview)
# print(numCritic)
# print(story)
# print(language)
# print(country)
# print(filmingLocation)
# print(productionCompany)
# print(soundMix)
# print(color)