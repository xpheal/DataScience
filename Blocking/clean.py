#!/usr/bin/env python3
import csv

def convert(x):
	if x == 'Music':
		return 'Musical'
	elif x == 'Game-Show':
		return 'Television'
	elif x == 'Reality-TV':
		return 'Television'
	elif x == 'Talk-Show':
		return 'Television'
	elif x == 'Thriller':
		return 'Mystery'
	else:
		return x

def main():
	with open('setA.csv', 'r') as in_f:
		with open('setA2.csv', 'w') as out_f:
			cr = csv.reader(in_f)
			otr = csv.writer(out_f)

			for row in cr:
				cats = row[2].split(",")

				for i,j in enumerate(cats):
					cats[i] = convert(j)

				row[2] = ','.join(cats)

				otr.writerow(row)

if __name__ == '__main__':
	main()