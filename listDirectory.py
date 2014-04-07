import re
from os import listdir
from os.path import isfile, join
mypath = "."
#onlyfiles = [ f.strip("[JJ Log |.aup") for f in listdir(mypath) if isfile(join(mypath,f)) ]
onlyfiles = [ re.sub(r'[\.(mp3)|a-z|A-Z|\.|\s]', '', f) for f in listdir(mypath) if isfile(join(mypath,f)) ]


print(onlyfiles)