#!/usr/bin/env python3
import csv

def grab_row(row, cols):
	return [row[i] for i in cols]

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
	with open('setD3.csv', 'r') as in_f:
		with open('setD4.csv', 'w') as out_f:
			cr = csv.reader(in_f)
			otr = csv.writer(out_f)
			
			for row in cr:
				# print(row[5])
				row[5] = row[5].replace(',','')
				# if row[4].strip() == 'N/A' or not row[4]:
				# 	row[4] = None
				# else:
				# 	x = row[4].strip().split('/')
				# 	y = float(x[0]) * 20
				# 	row[4] = int(y)
				otr.writerow(row)

if __name__ == '__main__':
	main()