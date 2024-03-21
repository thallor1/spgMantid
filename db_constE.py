### Script to test a detailed balance function for constE plots. 
import matplotlib.pyplot as plt
import sys
sys.path.append('/SNS/CNCS/IPTS-29413/shared/Scripts/')
from mantid import plots
from reduce_data_to_MDE import *
from slice_utils import *
from imp import reload
import matplotlib
import os
import numpy as np
import define_data_bcao_v
import define_slices_bcao_v
import dbbkg_wls as DBWLS

import numpy as np
import statsmodels.api as sm 
from patsy import dmatrices 
import statsmodels.formula.api as smf 
from mantid import plots
import pandas
from reduce_data_to_MDE import *
from slice_utils import *


datasets=define_data_bcao_v.define_data_set()
#############################################
# MAIN PROGRAM
#############################################
reload(define_data_bcao_v)
reload(define_slices_bcao_v)
reload(DBWLS)
# This is a simple script to show how to generate a constant energy slice using the detailed balance method.
def dim2array(d):
	"""
	Create a numpy array containing bin centers along the dimension d
	input: d - IMDDimension
	return: numpy array, from min+st/2 to max-st/2 with step st
	"""
	dmin=d.getMinimum()
	dmax=d.getMaximum()
	dstep=d.getX(1)-d.getX(0)
	return np.arange(dmin+dstep/2,dmax,dstep)


ds_ei6p59_I = datasets[3]
ds_ei6p59_I_920mK = datasets[4]
ds_ei6p59_I_2K = datasets[5]
ds_ei6p59_I_5K = datasets[6]
ds_ei6p59_I_7K = datasets[7]
ds_ei6p59_I_9K = datasets[8]
ds_ei6p59_I_11K = datasets[9]
ds_ei6p59_I_13K = datasets[10]
ds_ei6p59_I_6K = datasets[11]
ds_ei6p59_I_20K = datasets[12]
ds_ei6p59_I_30K = datasets[13]
ds_ei6p59_I_sub30K = datasets[14]
ds_ei6p59_I_20Km30K = datasets[15]
ds_ei6p59_I_3K = datasets[16]
ds_ei6p59_I_4K = datasets[17]
ds_ei6p59_I_3p5K = datasets[18]

reduce_data_to_MDE([ds_ei6p59_I,ds_ei6p59_I_20K,\
	ds_ei6p59_I_30K,ds_ei6p59_I_2K,ds_ei6p59_I_920mK,ds_ei6p59_I_5K,ds_ei6p59_I_9K])
	
	
vmin=0
vmax=2e-3
temperatures = [0.35,20.0,30.0,2.0,0.92,5.0,9.0]
dslist = [ds_ei6p59_I,ds_ei6p59_I_20K,ds_ei6p59_I_30K,ds_ei6p59_I_2K,ds_ei6p59_I_920mK,ds_ei6p59_I_5K,ds_ei6p59_I_9K]

slicenames_list = [] #List that contains the slice descriptions of all temperatures
slicenames_list_minus = [] #Will contain MDworkspaces for extracted SQW
Imat_plus = [] #Will contain MDworkspaces for extracted SQW
Imat_minus = [] #Will contain MDworkspaces for extracted SQW
Errmat_plus = [] #Will contain MDworkspaces for extracted SQW
Errmat_minus = [] #Will contain MDworkspaces for extracted SQW

energy = 0.3
dE = 0.05
deltaE = -0.08 # This parameter represents a nonphyiscal offset of the elastic line. 

#Below, I use Andrei's scripts to generate the positive and negative energy transfer slices. 
# In practice these can be generated however you like. 
for i,t in enumerate(temperatures):
	#Make a copy of the descs with temperature in the name.
	ds = dslist[i]
	ConstE_slice_desc = define_slices_bcao_v.define_constEslice_Ei6p59(extra=f"T{t:.2f}K",T=t,deltaE=(energy-deltaE),dE=dE)
	slice_description = ConstE_slice_desc[0]
	slice_description['Plot_parameters']={'vmin':vmin,'vmax':vmax}
	name = slice_description['Name']
	if name not in mtd:
		slicename = make_slice(ds,slice_description, solid_angle_ws=None, ASCII_slice_folder='')
	slicenames_list.append(slice_description['Name'])
	ConstE_slice_desc_minus = define_slices_bcao_v.define_constEslice_Ei6p59(extra=f"T{t:.2f}K",T=t,deltaE=-energy-deltaE,dE=dE)
	slice_description_minus = ConstE_slice_desc_minus[0]
	slice_description_minus['Plot_parameters']={'vmin':vmin,'vmax':vmax}
	name = slice_description_minus['Name']
	if name not in mtd:
		slicename_minus = make_slice(ds,slice_description_minus, solid_angle_ws=None, ASCII_slice_folder='')
	slicenames_list_minus.append(slice_description_minus['Name'])
	
	
SQW_md_list, BKG_md = DBWLS.detailedBalance_MDslices_ConstE(slicenames_list,slicenames_list_minus,temperatures,OutputSuffix='_DBBKG')

fig,ax = plt.subplots(1,3,subplot_kw={'projection':'mantid','aspect':1.0/1.5},constrained_layout=True) #Aspect from recip-lattice vectors
plotmd = mtd[slicenames_list[0]]
ax[0].pcolormesh(plotmd,vmin=vmin,vmax=vmax)
ax[1].pcolormesh(BKG_md,vmin=vmin,vmax=vmax)
ax[2].pcolormesh(SQW_md_list[0],vmin=vmin,vmax=vmax)
ax[1].set_ylabel('')
ax[2].set_ylabel('')
ax[0].set_title(f"BCVO [{energy-dE:.2f},{energy+dE:.2f}] meV")
ax[1].set_title(f"BCVO T-indep BKG")
ax[2].set_title(r"BCVO $S(\overrightarrow{Q}$,"+f"{energy:.2f})")
fig.show()

