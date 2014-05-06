
#!/usr/bin/python
import math
import fileinput
import sys

def replaceAll(file,searchExp,replaceExp):
    for line in fileinput.input(file, inplace=1):
        if searchExp in line:
            line = line.replace(searchExp,replaceExp)
        sys.stdout.write(line)


data = open('Data_training.cat','r') # original file is gs_all_tf_h_120919a_multi_training.cat

speczfile = open('CANDELS_GOODSS_Specz.dat','w') #we are creating this file so we open it for writing

lam = []

replaceAll("Data_training.cat","0.00000E+00  -0.99000E+02","0.0     10000.0")

replaceAll("Data_training.cat","-0.99000E+02  -0.99000E+02","0.0     10000.0")

replaceAll("Data_training.cat","-99.00000000 -99.00000000","0.0     10000.0")

data.close()

data = open('Data_training.cat','r')

counter=0

output_file = open('eazyerr7_CANDELS.cat','w')


output_file.write("%s \n" % ("# id F127 E127 F103 E103 F1 E1 F4 E4 F5 E5 F7 E7 F128 E128 F129 E129 F130 E130 F131 E131 F37 E37 F132 E132 F18 E18 F19 E19 F20 E20 F21 E21 spec_z "))
                             
for line in data.readlines():
    if not line.startswith(('#')):
        counter += 1

        index, ra, dec, apcorr, fctioU, errctioU, fvimosU, errvimosU, f435, err435, f606, err606, f775, err775, f850, err850, f980, err980, f1050, err1050, f1250, err1250, f1600, err1600, fisaack, errisaack, fhawkik, errhawkk, f3600, err3600, f4500, err4500, f5800, err5800, f8000, err8000, dummy, dummy, dummy, dummy, dummy, dummy, dummy, dummy, dummy, dummy, dummy,specz, dummy, dummy, dummy, dummy, dummy, dummy, dummy, dummy, dummy, dummy  = map(float, line.split()) #this line reads in all the input, splitting them on a blank space
        
        n_ctioU= (((fctioU*.05)**2)+(errctioU**2))**.5
        n_vimosU=(((fvimosU*.05)**2)+(errvimosU**2))**.5
        n_435=(((f435*.05)**2)+(err435**2))**.5
        n_606=(((f606*.05)**2)+(err606**2))**.5
        n_775=(((f775*.05)**2)+(err775**2))**.5
        n_850=(((f850*.05)**2)+(err850**2))**.5
        n_980=(((f980*.05)**2)+(err980**2))**.5
        n_1050=(((f1050*.05)**2)+(err1050**2))**.5
        n_1250=(((f1250*.05)**2)+(err1250**2))**.5
        n_1600=(((f1600*.05)**2)+(err1600**2))**.5
        n_isaack=(((fisaack*.25)**2)+(errisaack**2))**.5
        n_hawkk=(((fhawkik*.25)**2)+(errhawkk**2))**.5
        n_3600=(((f3600*.2)**2)+(err3600**2))**.5
        n_4500=(((f4500*.2)**2)+(err4500**2))**.5
        n_5800=(((f5800*.2)**2)+(err5800**2))**.5
        n_8000=(((f8000*.2)**2)+(err8000**2))**.5
        
        print n_ctioU, errctioU
        
        speczfile.write("%s \n" % (specz)) #this line writes the spec z to file

        output_file.write("%s \t %s \t %s \t %s \t %s \t %s \t %s \t %s \t %s \t %s \t %s \t %s \t %s \t %s \t %s \t %s \t %s \t %s \t %s \t %s \t %s \t %s \t %s \t %s \t %s \t %s \t %s \t %s \t %s \t %s \t %s \t %s \t %s \t %s \n" % (counter, fctioU, n_ctioU, fvimosU, n_vimosU, f435, n_435, f606, n_606, f775, n_775, f850, n_850, f980, n_980, f1050, n_1050, f1250, n_1250, f1600, n_1600, fisaack, n_isaack, fhawkik, n_hawkk, f3600, n_3600, f4500, n_4500, f5800, n_5800, f8000, n_8000, "-1.000"))
            

data.close()                              
speczfile.close()
output_file.close()