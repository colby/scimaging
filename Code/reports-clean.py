#!/usr/bin/python

import os, shutil

path = "/Users/administrator/Dropbox/SCI_Diag_Reports/2012/"

def walkit(directory):
        for files in os.listdir(path):
		parseit(path,files)

def parseit(root,file):
	print root
	token = file.split('_')[-2]
	if (len(token) == 6):
		month = str(token[1:2]).zfill(2)
		day   = str(token[2:4]).zfill(2)
		moveit(root,file,month,day)
	else:
		pass

def moveit(root,file,month,day):
	source = os.path.join(root,file)
	dest = os.path.join(path,month,day)
	try:
		shutil.move(source,dest + "/" + file)
	except (IOError, os.error):
		os.mkdir(dest)
		moveit(root,file,month,day)

if __name__ == "__main__":
	walkit(path)
