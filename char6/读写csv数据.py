#from urllib import urlretrieve
#urlretrieve('http://table.finance.yahoo.com/table.csv?s=000001.sz','pingan.csv')

import csv
'''rf = open('pingan.csv','rb')
reader = csv.reader(rf)
for row in reader:
	print row

wf = open('pingan_cp.csv','wb')
writer = csv.writer(wf)
writer.writerow(['data'])'''

with open('pingan.csv','rb') as rf:
	reader = csv.reader(rf)
	with open ('pingan2.csv','wb') as wf:
		writer = csv.writer(wf)
		headers = reader.next()
		writer.writerow(headers)
		for row in reader:
			if row[0] < '2016-01-01':
				break
			if int(row[5]) >=50000000:
				writer.writerow(row)