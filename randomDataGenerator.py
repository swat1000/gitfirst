import numpy as np 
import os
import glob
import csv
import random as random

dataRow = np.ones((2,31),float)

LOW_M3 = 4900
HIGH_M3 =5400
DAYS = 31

randomlist = random.sample(range(LOW_M3,HIGH_M3), DAYS)
for i in range (0,DAYS):
	randomlist[i]/= 4546.09
	dataRow[0][i] = randomlist[i]

print(randomlist)

with open("randomRows.csv", 'w') as csvfile:  
    csvwriter = csv.writer(csvfile)  
    csvwriter.writerows(dataRow)