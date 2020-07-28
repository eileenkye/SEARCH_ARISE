import csv

# 0: senior center, 1: elderly, 2: kids under 5, 3: cooling center, 4: caregiver organization, 5: 100% poverty
# 6: 100%-150% poverty, 7: 150% poverty, 8: affordable housing building, 9: affordable housing unit
# could also add max values to the csv file and read in from there
maxvalues = [8, 29.07, 14.00, 6, 2, 35.6, 38.5, 71, 160, 15396]

fin = open ('test.in', 'r')
fout = open('test.out', 'w')

zipcode = fin.readline().strip()
zipdata = [] # data for the zipcode from the csv file

with open('Data by Zipcode - Sheet1.csv') as csvfile:
	readCSV = csv.reader(csvfile, delimiter=',')
	for row in readCSV:
		if (row[0] == zipcode):
			for i in range(1, 11):
				zipdata.append(row[i])

R = 0
W = 1/10 # 10 vulnerability categories in the dataset

for i in range(10):
	if zipdata[i][-1] == '%':
		zipdata[i] = zipdata[i][:-1]
	R += (float(zipdata[i])/maxvalues[i])*W

fout.write (str(R))
fout.close()



