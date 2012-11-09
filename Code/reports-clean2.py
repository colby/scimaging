#!/usr/bin/env python

import os
import envoy
import shutil

path = "/Users/administrator/Desktop/SCI_Diag_Reports"

def walk(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            verify(root, file)

def verify(root, file):
    slug = os.path.join(root, file)
    if file == ".DS_Store":
        os.remove(slug)
    else:
        date      =  envoy.run("wvWare %s | grep DOE" % slug) 
        if date.std_out.split():
            date  = date.std_out.split()[-1]
            file_date =  file.split('_')[-2]
            if len(date) == 10:
                doc_date  =  date.translate(None,'/')
                if len(file_date) == 6:
                    isold = 0
                else:
                    isold = 1
                    file_date = file.split('_')[-1].rstrip('.doc')
                if file_date != doc_date:
                    rename(root, file, date, doc_date, isold)
                else:
                    relocate(root, file, date)
            else:
                unknown(root, file)

def unknown(root, file):
    path2 = os.path.join(path,'Unconfirmed')
    shutil.move(os.path.join(root,file),os.path.join(path2,file))

def rename(root, file, date, doc_date, isold):
    new_file     = file.split('_')
    if isold:
        new_file[-1] = doc_date
    else:
        new_file[-2] = doc_date
    new_file     = '_'.join(new_file)
    new_file    += '.doc'
    os.rename(os.path.join(root, file), os.path.join(root,new_file))
    relocate(root, new_file, date)

def relocate(root, file, date):
    current_dir = root.split('/')
    new_dir     = date.split('/')[::-1]
    new_dir     = '/'.join(new_dir)
    if not os.path.exists(os.path.join(path,new_dir)):
        os.makedirs(os.path.join(path,new_dir))
    print "Moving %s to %s" % (file, os.path.join(path,new_dir,file))
    shutil.move(os.path.join(root,file),os.path.join(path,new_dir,file))

def main():
    walk(path)

if __name__ == '__main__':
    main()
