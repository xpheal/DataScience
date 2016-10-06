import argparse
import csv
import json
from io import StringIO
from lxml import etree
from os import listdir

# arguments check
parser = argparse.ArgumentParser(description='Parse data from html files and store in csv')
parser.add_argument('s', metavar='<Settings>', help='JSON settings file, see documentation for more info')
parser.add_argument('o', metavar='<CSVOutput>', help='output result to this file path')
parser.add_argument('-i', metavar='<HTMLInput>', help='html input to be parsed')
parser.add_argument('-d', metavar='<Directory>', help='the input directory to be parsed')

args = parser.parse_args()

# Get input
jsonFile = args.s
inputFile = args.i
directory = args.d
outputFile = args.o

# Get xPath settings [{"colName": "xxx", "xPathString": "yyy"}, {...}, ...]
dataSettings = None
with open(jsonFile, 'r') as jFile:
	dataSettings = json.load(jFile)['data_extract_path']

def parseList(tree, xPathString):
	'''
	Given the tree and the xPathString, return the matched data
	return none if no data is matched
	'''
	result = tree.xpath(xPathString)

	if len(result) <= 0:
		return None
	else:
		return ",".join(result).encode('utf-8').strip()

with open(outputFile, 'w') as csvfile:
	# Name for the top row
	topRow = [i['colName'] for i in dataSettings]
	# Number of Columns
	lenCol = len(dataSettings)

	writer = csv.writer(csvfile)
	writer.writerow(topRow)

	# Parse html files
	if inputFile:
		with open(inputFile, 'r') as f:
			# Store the parsed data
			row = []
			# Parse html file into a tree
			tree = etree.parse(f, etree.HTMLParser())

			for i in range(lenCol):
				row.append(parseList(tree,dataSettings[i]["xPathString"]))

			writer.writerow(row)

	# Parse all files in directory
	if directory:
		for fname in listdir(directory):
			with open(directory + '/' + fname, 'r') as f:
				# Store the parsed data
					row = []
					# Parse html file into a tree
					tree = etree.parse(f, etree.HTMLParser())

					for i in range(lenCol):
						row.append(parseList(tree,dataSettings[i]["xPathString"]))

					writer.writerow(row)
