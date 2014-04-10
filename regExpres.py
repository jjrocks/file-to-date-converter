import re
from datetime import date

dateList = ["JJ Log 5-7-11.aup", "JJ Log 5-8-11.mp3", "This is my cool pants", "JJ Log 5-9-11.mp3", "JJ Log 5-10-11.aup", "JJ Log 4-7-11.aup", "JJ Log 12-13-11.aup", "JJ Log 11-15-11.mp3", "JJ Log 3-13-33.mp3"]

def stringListToDateList(stringList):
	dateList = []
	for dates in stringList:
		currentDateString = dates.split("-")
		if len(currentDateString) == 3:
			dateList.append(date(int(currentDateString[2]), int(currentDateString[0]), int(currentDateString[1])))
	return dateList

dateListTmp = []
for dates in dateList:
	#dates = re.sub(r'[(\|a-z|A-Z|\.|\s]', '', dates)
	dates = re.sub(r'\..+', '', dates)
	dates = re.sub(r'[^\d|\-]', '', dates)
	dateListTmp.append(dates)
dateList = dateListTmp

actualDates = stringListToDateList(dateList)

print(actualDates)
