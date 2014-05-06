#!/usr/bin/python

#This routine


filter_file = open('Filter16_IRAC_ch4.txt','r')
outfilename = '3columns_Filter16_IRAC_ch4.txt'
new_filter_file = open(outfilename,'w')

counter=1


for line in filter_file:
	line.rstrip("\n")	
	wavel,transmission = line.split()
        new_filter_file.write("%s %s %s \n" % (counter,wavel,transmission))
	counter+=1

filter_file.close()
new_filter_file.close()



