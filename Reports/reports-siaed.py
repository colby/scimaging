#!/usr/bin/python

import re
import sys
import zipfile

def main(file):
        zip  = zipfile.ZipFile(file, "r")
        if "word/header2.xml" in zip.namelist():
                data = zip.read("word/header2.xml")
        else:
                data = zip.read("word/header1.xml")
        data = re.sub('<[^>]*>', '', data)
        sort(file, data.split())

def sort(file, list):
        index = list.index("NAME:")
        list[index + 1] = list[index + 1][:-1] 
        
        if list[index + 2][-4:] == 'MRN:':
                list[index + 2] = list[index + 2][:-4]

        index = "_".join(list[index + 1: index + 3])
        filename = file.split('-')
        print "%s_%s" % (index, filename[1])        

if __name__ == "__main__":
        main(sys.argv[1])
