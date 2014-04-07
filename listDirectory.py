import re
from os import listdir
from os.path import isfile, join
mypath = "."
#onlyfiles = [ f.strip("[JJ Log |.aup") for f in listdir(mypath) if isfile(join(mypath,f)) ]
onlyfiles = [ re.match(r'\d+-\d+-\d+', f) for f in listdir(mypath) if isfile(join(mypath,f)) ]

for files in onlyfiles:
	if(files.group()):
		print(files.group())

print(onlyfiles)