filter_file = open('Filter02_VIMOS_U.txt','r')
outfilename = '3col_Filter02_VIMOS_U.txt'
new_filter_file = open(outfilename, 'w')

counter=1


for line in filter_file:
    line.rstrip("\n")
    wavel,transmission = line.split()
        new_filter_file.write"%s %s %s \n" % (counter,wavel,transmission))
    counter+=1

filter_file.close()
new_filter_file.close()



