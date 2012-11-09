#!/bin/bash

/usr/bin/find ~/Dropbox/SCI_Diag_Reports -name .DS_Store -delete -print
/usr/bin/find /Volumes/Data/imac-nas -name .DS_Store -delete -print

#/usr/bin/python ~/Code/reports-clean.py

/usr/bin/rsync -varP ~/Dropbox/SCI_Diag_Reports /Volumes/Data/imac-nas/

/usr/bin/rsync -varP ~/Dropbox/SCI_Diag_Reports/2012 /Volumes/Data/imac-nas/PHYCOM/Reports
