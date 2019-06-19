#!/usr/bin/env python

#stuff that needs to be imported
import csv

#clean up the other output file before creating the new one
from subprocess import call
call(["rm", "contact_upload.csv"])

#read in the files
f = open('users-list.csv')
usersopen = open('users.txt')
useroutput = open("contact_upload.csv","w")

csv_f = csv.reader(f)
a = usersopen.readlines()
for row in csv_f:
	for line in a:
		writer = csv.writer(useroutput)
		writer.writerow([line.rstrip('\n'), row[0], row[1], row[2], row[3], row[4]])
    
f.close()
useroutput.close()
usersopen.close()        
            
