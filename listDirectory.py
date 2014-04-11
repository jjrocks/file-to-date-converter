import re
from os import listdir
from os.path import isfile, join
from datetime import date

def stringListToDateList(stringList):
	dateList = []
	for dates in stringList:
		currentDateString = dates.split("-")
		if len(currentDateString) == 3:
			dateList.append(date(int(currentDateString[2])+2000, int(currentDateString[0]), int(currentDateString[1])))
	return dateList

def sortDateArray(dateList):
	arrayA = []
	arrayB = []
	if (len(dateList) == 0 or len(dateList) == 1):
		return dateList
	else:
		length = len(dateList)
		halfLength = int(length/2)
		arrayA = sortDateArray(dateList[0:halfLength])
		arrayB = sortDateArray(dateList[halfLength:])
	arrayC = []
	length = 0
	if len(arrayA) > len(arrayB):
		length = len(arrayA)
	else:
		length = len(arrayB)
	p = 0
	q = 0
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

def checkLog(dateList):
	todayDate = date.today()
	dateList = sortDateArray(dateList)
	for dates in dateList:
		dateOffset = dates.replace(year = dates.year + 3)
		if(todayDate == dateOffset):
			print("You have a log to listen to today")
			return
		if todayDate < dateOffset:
			message = "There is no log for today. The next one will be " + dateOffset.strftime("%m-%d-%y")
			print("There is no log for today")
			return
	print("There is no log for today and never will be. The path is empty.")



mypath = "."
#onlyfiles = [ f.strip("[JJ Log |.aup") for f in listdir(mypath) if isfile(join(mypath,f)) ]
onlyfiles = [ re.sub(r'[^\d|\-]', '', re.sub(r'\..+', '', f)) for f in listdir(mypath) if isfile(join(mypath,f)) ]

dateList = stringListToDateList(onlyfiles)
checkLog(dateList)
