#!/usr/bin/env python

import sys
import envoy
import os

path = "/Users/administrator/Desktop/reports"

def walk(path):
    for root, dirs, files in os.walk(path, topdown=False):
        for file in files:
            clean(os.path.join(root,file))
            #print "%s --> %s" % (file, root)

def clean(target):
    target = envoy.run("catdoc %s" % target)
    index = target.std_out

    print index

    #Patient name
    NAME = index.find('NAME')
    NAME2 = index.find('MRN')
    #print index[NAME:NAME2].strip()[6:]

    #Study DOS
    DOE = index.find('DOE')
    #print index[DOE:DOE + 16].strip()[-10:]

    #Modality
    MOD = index.find('PROCEDURE')
    MOD2 = index[MOD:DOE].strip()[11:].upper()
    if 'VIEW' in MOD2 or 'X-RAY' in MOD2 or 'XRAY' in MOD2:
        #pass
        print "xray: %s" % MOD2
    else:
        print MOD2

    #Body part
    if 'VIEW' in MOD2:
        pass
        #print "body1: %s" % MOD2.split(' ')
    else:
        pass
        #print "body2: %s" % '-'.join(MOD2.split(' ')[3:5])

    #Radiologist
    RAD = index.find('lly Signed')
    RAD2 = index.find('Dictated')
    #print index[RAD:RAD2].split(' ')[2].rstrip(',').upper()

if __name__ == "__main__":
   walk(path)
