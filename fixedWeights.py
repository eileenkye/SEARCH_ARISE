import numpy as num
import pandas as pd

df = pd.read_csv('Data by Zipcode - Sheet1.csv')

maxvalues = {}
for label, column in df.items(): # initialize maxvalues to all 0s
	if label == "Zip_Codes":
		continue
	else:
		maxvalues[label] = 0

fin = open ('test.in', 'r')
fout = open('test.out', 'w')

zipcode = fin.readline().strip()
zipdata = {} # data for the zipcode from the csv file

for ind in df.index:
	correctrow = False
	if int(df["Zip_Codes"][ind]) == int(zipcode): #the correct row
		correctrow = True
	for label, column in df.items(): #update maxvalues
		if label == "Zip_Codes": continue
		else:
			if df.loc[ind, label] > maxvalues[label]:
				maxvalues[label] = df[label][ind]
			if correctrow:
				zipdata[label] = df[label][ind]

R = 0
W = 1/10 # 10 vulnerability categories in the dataset

for key in zipdata:
	R += (float(zipdata[key])/maxvalues[key])*W

fout.write (str(R))
fout.close()

