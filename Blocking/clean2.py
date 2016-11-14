#!/usr/bin/env python3
import csv

def convert(x):
	if x == 'Anime':
		return 'Animation'
	elif x == 'Manga':
		return 'Animation'
	elif x == 'Suspense':
		return 'Mystery'
	elif x == 'Lesbian':
		return 'Adult'
	elif x == 'Gay':
		return 'Adult'
	else:
		return x

def main():
	with open('setB.csv', 'r') as in_f:
		with open('setB2.csv', 'w') as out_f:
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