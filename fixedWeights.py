import numpy as num
import pandas as pd

def Rvalue(fname, zipcode, weights): # function to calculate and return R value
	df = pd.read_csv(fname)

	maxvalues = {}
	for label, column in df.items(): # initialize maxvalues to all 0s
		if label == "Zip_Codes":
			continue
		else:
			maxvalues[label] = 0

	zipdata = {} # data for the zipcode from the csv file

	for ind in df.index:
		correctrow = False
		if int(df["Zip_Codes"][ind]) == int(zipcode): # the correct row
			correctrow = True
		for label, column in df.items(): # update maxvalues
			if label == "Zip_Codes": continue
			else:
				if df.loc[ind, label] > maxvalues[label]:
					maxvalues[label] = df[label][ind]
				if correctrow:
					zipdata[label] = df[label][ind]
	R = 0
	count = 0 # holds place in weights
	for key in zipdata:
		R += (float(zipdata[key])/maxvalues[key])*float(weights[count])
		count += 1
	return R

fin = open('test.in', 'r')
fout = open('test.csv', 'w')
fw = open('weights.in', 'r')

zipcodes = fin.readline().split() # load in zipcodes to a list
fout.write("Zip_Code, R_Value\n") # write the csv file heading
weights = fw.readline().split() # load in weights to a list

for zipcode in zipcodes: # for each zipcode, calculate and write out R value
	R = Rvalue('Data by Zipcode - Sheet1.csv', zipcode, weights)
	fout.write(str(zipcode) + ", " + str(R) + '\n')

fout.close()
