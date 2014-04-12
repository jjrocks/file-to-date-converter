import re
from os import listdir
from os.path import isfile, join
from datetime import date

#This will take an array labled and convert it to date. So anything with "X-X-X will change to the date version"
def stringListToDateList(stringList):
	dateList = [] #Create an empty list to fill it wih dates
	for dates in stringList:
		currentDateString = dates.split("-") #This will split it 
		if len(currentDateString) == 3:
			dateList.append(date(int(currentDateString[2])+2000, int(currentDateString[0]), int(currentDateString[1]))) #This assumes that the it's M-D-Y
	return dateList

#This is literally a merge sort It's bottom up. Not the cleanest version of it but it works.
def sortDateArray(dateList):
	arrayA = []
	arrayB = []
	if (len(dateList) == 0 or len(dateList) == 1):
		return dateList
	else:
		halfLength = int(len(dateList)/2)
		arrayA = sortDateArray(dateList[0:halfLength])
		arrayB = sortDateArray(dateList[halfLength:])
	arrayC = [] #An array that'll be used to return the final data
	length = 0
	#This block of code helps decide how long the for loop should go (Though this could be done with a while loop)
	if len(arrayA) > len(arrayB):
		length = len(arrayA)
	else:
		length = len(arrayB)
	p = 0
	q = 0
	#This goes through both arrays
	for x in range(0, length*2):
		if arrayA[p] < arrayB[q]:
			arrayC.append(arrayA[p])
			p+= 1
		else:
			arrayC.append(arrayB[q])
			q+= 1
		if p >= len(arrayA):
			arrayC = arrayC + arrayB[q:]
			break
		elif q >= len(arrayB):
			arrayC = arrayC + arrayA[p:]
			break
	return arrayC

#This will go through the dateList. Sort through the list and check if there is a day that matches 3 days ago
def checkLog(dateList):
	todayDate = date.today()
	dateList = sortDateArray(dateList)
	for dates in dateList:
		dateOffset = dates.replace(year = dates.year + 3) #This dateOffset allows you to account for how the years that have changed.
		if(todayDate == dateOffset):
			print("You have a log to listen to today")
			return
		if todayDate < dateOffset:
			message = "There is no log for today. The next one will be " + dateOffset.strftime("%m-%d-%y")
			print(message)
			return
	print("There is no log for today and never will be. The path is empty.")



mypath = "."
#onlyfiles = [ f.strip("[JJ Log |.aup") for f in listdir(mypath) if isfile(join(mypath,f)) ]
onlyfiles = [ re.sub(r'[^\d|\-]', '', re.sub(r'\..+', '', f)) for f in listdir(mypath) if isfile(join(mypath,f)) ]

dateList = stringListToDateList(onlyfiles)
checkLog(dateList)
