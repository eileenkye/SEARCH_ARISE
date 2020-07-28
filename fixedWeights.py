import csv

def loadInFile() {
	#load in zipcode data from csv file

}

def main() {
	loadInFile()

	# 0: senior center, 1: elderly, 2: kids under 5, 3: cooling center, 4: caregiver organization, 5: 100% poverty
	# 6: 100%-150% poverty, 7: 150% poverty, 8: affordable housing building, 9: affordable housing unit
	maxvalues = [8, 29.07, 14.00, 6, 2, 35.6, 38.5, 71, 160, 15396]

	zipcode = input() # the zipcode of the power outage
	zipdata = [] # data for the zipcode from the csv file

	R = 0
	W = 1/10 # 10 vulnerability categories in the dataset

	for i in range(10): # senior center to caregiver organization
		R += (zipdata[i]/maxvalues[i])*W
}


