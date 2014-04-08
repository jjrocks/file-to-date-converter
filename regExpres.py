import re

dateList = ["JJ Log 5-7-11.aup", "JJ Log 5-8-11.mp3", "JJ Log 5-9-11.mp3", "JJ Log 5-10-11.aup", "JJ Log 4-7-11.aup", "JJ Log 12-13-11.aup", "JJ Log 11-15-11.mp3", "JJ Log 3-13-33.mp3"]


for dates in dateList:
	#dates = re.sub(r'[(\|a-z|A-Z|\.|\s]', '', dates)
	print("----------------")
	dates = dates.strip("mp3")
	print(dates)
	dates = re.sub(r'[^\d|\-]', '', dates)
	print(dates)