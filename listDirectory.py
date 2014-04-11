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

def checkLog(dateList):
	todayDate = date.today()
	for dates in dateList:
		if(date.today() == dates.replace(year = dates.year + 3)):
			print("You have a log to listen to today")
	print("There is no log for today")

def sortDateArray(dateList):
	if (len(dateList) == 0 || len(dateList) == 1):
		return dateList
	else:
		length = len(dateList)/2
		halfLength = length/2
		sortDateArray(dateList[0:halfLength]-1)
		sortDateArray(dateList[halfLength:length-1])
	



mypath = "."
#onlyfiles = [ f.strip("[JJ Log |.aup") for f in listdir(mypath) if isfile(join(mypath,f)) ]
onlyfiles = [ re.sub(r'[^\d|\-]', '', re.sub(r'\..+', '', f)) for f in listdir(mypath) if isfile(join(mypath,f)) ]

dateList = stringListToDateList(onlyfiles)
checkLog(dateList)
