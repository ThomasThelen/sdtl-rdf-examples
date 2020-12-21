import pandas as pd
import io
import os
import numpy as np

os.chdir(r'C:\\Users\\altergc\\Documents\\ICPSR\\Project development\\metadata_capture\\scripts\\GSS_sample\\Python')

cdata = pd.read_csv("GSS_sample.csv")

##********** compute with 2 inputs  ****************.
cdata = cdata.assign(pctFamIncome = 100*cdata['REALRINC']/cdata['REALINC'] )

##********* first change to agestd  *****************
cdata = cdata.assign(agestd = ((cdata['AGE'] - 45.99)/.07) )


##********* SAVE FILE  1 **********************************
cdata.to_csv("GSS_sample_save1.csv")


##********* first change to agestd  *****************
cdata = cdata.assign(agestd = cdata['AGE']*.07 )


##********* SAVE FILE 2 **********************************
cdata.to_csv("GSS_sample_save2.csv")