import re
from os import listdir
from os.path import isfile, join
from datetime import date

def stringListToDateList(stringList):
	dateList = []
	for dates in stringList:
		currentDateString = dates.split("-")
		if len(currentDateString) == 3:
			dateList.append(int(currentDateString[2]), int(currentDateString[0]), int(currentDateString[1]))
	return dateList



mypath = "."
#onlyfiles = [ f.strip("[JJ Log |.aup") for f in listdir(mypath) if isfile(join(mypath,f)) ]
onlyfiles = [ re.sub(r'[^\d|\-]', '', re.sub(r'\..+', '', f)) for f in listdir(mypath) if isfile(join(mypath,f)) ]



print(onlyfiles)