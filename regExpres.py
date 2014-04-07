import re

dateList = ["JJ Log 5-7-11", "JJ Log 5-8-11", "JJ Log 5-9-11", "JJ Log 5-10-11", "JJ Log 4-7-11", "JJ Log 12-13-11", "JJ Log 11-15-11", "JJ Log 5-11-11"]

for dates in dateList:
	dates = re.sub(r'(?!o)', '', dates)
	print(dates)