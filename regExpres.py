import re

dateList = ["JJ Log 5-7-11.aup", "JJ Log 5-8-11.aup", "JJ Log 5-9-11.aup", "JJ Log 5-10-11.aup", "JJ Log 4-7-11.aup", "JJ Log 12-13-11.aup", "JJ Log 11-15-11.aup", "JJ Log 5-11-11.aup"]


for dates in dateList:
	dates = re.sub(r'[a-z|A-Z|\.|\s]', '', dates)
	print(dates)