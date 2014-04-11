import re
from datetime import date

dateList = ["JJ Log 5-7-11.aup", "JJ Log 5-8-11.mp3", "This is my cool pants", "JJ Log 5-9-11.mp3", "JJ Log 5-10-11.aup", "JJ Log 4-7-11.aup", "JJ Log 12-13-11.aup", "JJ Log 11-15-11.mp3", "JJ Log 3-13-33.mp3"]

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
	for x in range(0, length):
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

dateListTmp = []
for dates in dateList:
	#dates = re.sub(r'[(\|a-z|A-Z|\.|\s]', '', dates)
	dates = re.sub(r'\..+', '', dates)
	dates = re.sub(r'[^\d|\-]', '', dates)
	dateListTmp.append(dates)
dateList = dateListTmp

actualDates = stringListToDateList(dateList)
actualSortDates = sortDateArray(actualDates)

print(actualSortDates)
