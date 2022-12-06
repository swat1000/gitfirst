import numpy as np 
import os
import glob
import csv
import sys

rawData="April_2022/"
fileSearchKey = "*FEB21.CSV"
DAY_COUNT = 28

detailsCSV = csv.reader
allPanelDetails = []

with open(("panelDetails1.csv"),"r") as openCSV:
	detailsCSV = csv.reader(openCSV,delimiter=",")
	allPanelDetails = [d for d in detailsCSV]


panelFolderList = glob.glob(rawData+"/*")
panelFolderList.sort()
PANEL_COUNT = len(panelFolderList)

print(panelFolderList)

monthwiseData = []
monthwiseData = [['NA' for i in range(DAY_COUNT+1)] for j in range(PANEL_COUNT)]
monthwiseData.sort()

for i in range (0,PANEL_COUNT):
	
	panelDirectory = panelFolderList[i]+"/"+fileSearchKey
	
	panelNumber = panelFolderList[i][8:]

	monthCSVs = glob.glob(panelDirectory)
	panelLocation = [i]
	print(monthCSVs)
	print(panelLocation)
	
	#enable panel name, uncomment below

	for row in allPanelDetails:
		print (row[0])
		if row[0] == panelNumber:
			monthwiseData[i][0] = row[2]

	monthwiseData[i][0] = panelNumber

	print("Panel No: " + panelNumber)
	for j in range (0, len(monthCSVs)):
		currentDate = int(monthCSVs[j][-11:-9])
		print("\tDate: " + str(currentDate))
		with open(monthCSVs[j]) as dayCSV:
			reader=csv.reader(dayCSV)
			rows=[r for r in reader]
			monthwiseData[i][currentDate] = round((float(rows[2][6])/4546.09),6)

header = ["{}-Feb-2021".format(x) for x in range(1,DAY_COUNT+1)]
header = ["Panel Location"] + header

print(monthwiseData)

# writing to csv file  
with open("Feb_2021.csv", 'w', newline='') as csvfile:  
    # creating a csv writer object  
    csvwriter = csv.writer(csvfile)  
    # writing the fields
    csvwriter.writerow(header)  
    # writing the data rows
    csvwriter.writerows(monthwiseData)