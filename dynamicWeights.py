import numpy as num
import pandas as pd

def Rvalue(fname, zipcode, weights, dynamicdata): # function to calculate and return R value
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
	R /= 2

	# testing writing to csv
	dd = pd.read_csv(dynamicdata)
	for ind in dd.index:
		dd.set_value(ind, 'Max_Value', 1)
		dd.to_csv(dynamicdata, index=False)

	for ind in dd.index:
		if int(dd["Zip_Code"][ind]) == int(zipcode): # the correct row
			today = dd.loc[ind, 'Today_Temp']
			dd.loc[ind, 'Average_Temp'] = (dd.loc[ind, 'Num_Before']*dd.loc[ind, 'Average_Temp'] + today)/(dd.loc[ind, 'Num_Before'] + 1)
			dd.loc[ind, 'Num_Before'] = dd.loc[ind, 'Num_Before'] + 1
			if today > dd.loc[ind, 'Max_Temp']:
				dd.loc[ind, 'Max_Temp'] = today
			if today > dd.loc[ind, 'Min_Temp']:
				dd.loc[ind, 'Min_Temp'] = today
			
			if today < dd.loc[ind, 'Average_Temp']: # use Min_Value
				maxcold = dd.loc[ind, 'Average_Temp'] - dd.loc[ind,'Min_Temp']
				thisdif = dd.loc[ind, 'Average_Temp'] - today
				R += (thisdif/maxcold)*(weights[count])*0.5
			if today > dd.loc[ind, 'Average_Temp']: # use Max Value
				maxwarm = dd.loc[ind, 'Max_Temp'] - dd.loc[ind, 'Average_Temp']
				thisdif = today - dd.loc[ind, 'Average_Temp']
				R += (float(thisdif)/float(maxwarm))*float(weights[count])*0.5

	return R


fin = open('test.in', 'r')
fout = open('testd.csv', 'w')
fw = open('weights.in', 'r')

zipcodes = fin.readline().split() # load in zipcodes to a list
fout.write("Zip_Code, R_Value\n") # write the csv file heading
weights = fw.readline().split() # load in weights to a list

for zipcode in zipcodes: # for each zipcode, calculate and write out R value
	R = Rvalue('Data by Zipcode - Sheet1.csv', zipcode, weights, 'dynamic.csv')
	fout.write(str(zipcode) + ", " + str(R) + '\n')

fout.close()
