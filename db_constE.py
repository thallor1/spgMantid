### Script to test a detailed balance function for constE plots. 
import matplotlib.pyplot as plt
import sys
sys.path.append('/SNS/CNCS/IPTS-29413/shared/BCVO-Paper-Figure-Scripts/python_dependencies')
from mantid import plots
from reduce_data_to_MDE import *
from slice_utils import *
from imp import reload
import matplotlib
import os
import numpy as np
import define_data
import define_slices
import dbbkg_wls as DBWLS

import numpy as np
import statsmodels.api as sm 
from patsy import dmatrices 
import statsmodels.formula.api as smf 
from mantid import plots
import pandas
from reduce_data_to_MDE import *
from slice_utils import *


datasets=define_data.define_data_set()
#############################################
# MAIN PROGRAM
#############################################
reload(define_data)
reload(define_slices)
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

energy = 0.8
dE = 0.1
deltaE = 0.05 # This parameter represents a nonphyiscal offset of the elastic line. 

#Below, I use Andrei's scripts to generate the positive and negative energy transfer slices. 
# In practice these can be generated however you like. 
for i,t in enumerate(temperatures):
	#Make a copy of the descs with temperature in the name.
	ds = dslist[i]
	ConstE_slice_desc = define_slices.define_constEslice_Ei6p59(extra=f"T{t:.2f}K",T=t,deltaE=(energy-deltaE),dE=dE)
	slice_description = ConstE_slice_desc[0]
	slice_description['Plot_parameters']={'vmin':vmin,'vmax':vmax}
	name = slice_description['Name']
	if name not in mtd:
		slicename = make_slice(ds,slice_description, solid_angle_ws=None, ASCII_slice_folder='')
	slicenames_list.append(slice_description['Name'])
	ConstE_slice_desc_minus = define_slices.define_constEslice_Ei6p59(extra=f"T{t:.2f}K",T=t,deltaE=-energy-deltaE,dE=dE)
	slice_description_minus = ConstE_slice_desc_minus[0]
	slice_description_minus['Plot_parameters']={'vmin':vmin,'vmax':vmax}
	name = slice_description_minus['Name']
	if name not in mtd:
		slicename_minus = make_slice(ds,slice_description_minus, solid_angle_ws=None, ASCII_slice_folder='')
	slicenames_list_minus.append(slice_description_minus['Name'])

	
SQW_md_list, BKG_md = DBWLS.detailedBalance_MDslices_ConstE(slicenames_list,slicenames_list_minus,temperatures,OutputSuffix='_DBBKG')

fig,ax = plt.subplots(3,1,figsize=(3.45,5),subplot_kw={'projection':'mantid'},constrained_layout=True) #Aspect from recip-lattice vectors
plotmd = mtd[slicenames_list[0]]
smooth_bkg = SmoothMD(BKG_md,3)
diffmd = plotmd-smooth_bkg
ax[0].pcolormesh(plotmd,vmin=vmin,vmax=vmax,rasterized=True)
ax[1].pcolormesh(BKG_md,vmin=vmin,vmax=vmax,rasterized=True)
ax[2].pcolormesh(diffmd,vmin=vmin,vmax=vmax,rasterized=True)
for a in ax:
    a.set_xlim(-1.6,1.6)
    a.set_ylim(0,2.2)
ax[1].set_xlabel('')
ax[0].set_xlabel('')
ax[0].text(0.05,0.9,'(a)',transform=ax[0].transAxes,horizontalalignment='left',verticalalignment='top')
ax[0].text(0.95,0.9,r'$I_{350 mK}$',transform=ax[0].transAxes,horizontalalignment='right',verticalalignment='top')
ax[1].text(0.05,0.9,'(b)',transform=ax[1].transAxes,horizontalalignment='left',verticalalignment='top')
ax[1].text(0.95,0.9,r'$I_{bkg}$',transform=ax[1].transAxes,horizontalalignment='right',verticalalignment='top')
ax[2].text(0.05,0.9,'(c)',transform=ax[2].transAxes,horizontalalignment='left',verticalalignment='top')
ax[2].text(0.95,0.9,r'$S_{350 mK}$',transform=ax[2].transAxes,horizontalalignment='right',verticalalignment='top')
#ax[0].set_title(f"BCVO [{energy-dE:.2f},{energy+dE:.2f}] meV")
#ax[1].set_title(f"BCVO T-indep BKG")
#ax[2].set_title(r"BCVO $S(\overrightarrow{Q}$,"+f"{energy:.2f})")
cdir = '/SNS/CNCS/IPTS-29413/shared/Dbfunc/'
scale = 1.4e3 / 6 # Factor of six for per Co

#Add a colorbar
l,b,w,h=ax[0].get_position().bounds
cax = fig.add_axes([0.13,1.05,0.87,0.02])
labelstr='I($Q,\omega$) (b/eV/sr/Co)'
norm = matplotlib.colors.Normalize(vmin*scale,vmax*scale)
cbar = plt.colorbar(matplotlib.cm.ScalarMappable(norm=norm,cmap='viridis'),orientation='horizontal',cax=cax)
cax.text(0.5,2.5,labelstr,transform=cax.transAxes,horizontalalignment='center',verticalalignment='center',rotation=0,fontsize=9)
cax.yaxis.set_major_formatter(matplotlib.ticker.FormatStrFormatter("%.0f"))
cax.tick_params(labelsize=9)

fig.savefig(cdir+"/BCVO_constE_example.pdf",bbox_inches='tight',dpi=300)
fig.show()
'''
#repeat for a lower energy transfer to look at "gap"

slicenames_list_lowE = [] #List that contains the slice descriptions of all temperatures
slicenames_list_minus_lowE = [] #Will contain MDworkspaces for extracted SQW
Imat_plus_lowE = [] #Will contain MDworkspaces for extracted SQW
Imat_minus_lowE = [] #Will contain MDworkspaces for extracted SQW
Errmat_plus_lowE = [] #Will contain MDworkspaces for extracted SQW
Errmat_minus_lowE = [] #Will contain MDworkspaces for extracted SQW

energy_lowE = 1.1
dE_lowE = 0.0
hight_i = -2
for i,t in enumerate(temperatures):
	#Make a copy of the descs with temperature in the name.
	ds = dslist[i]
	ConstE_slice_desc = define_slices.define_constEslice_Ei6p59(extra=f"T{t:.2f}K",T=t,deltaE=(energy-deltaE),dE=dE_lowE)
	slice_description = ConstE_slice_desc[0]
	slice_description['Plot_parameters']={'vmin':vmin,'vmax':vmax}
	name = slice_description['Name']
	if name not in mtd:
		slicename = make_slice(ds,slice_description, solid_angle_ws=None, ASCII_slice_folder='')
	slicenames_list_lowE.append(slice_description['Name'])
	ConstE_slice_desc_minus = define_slices.define_constEslice_Ei6p59(extra=f"T{t:.2f}K",T=t,deltaE=-energy-deltaE,dE=dE_lowE)
	slice_description_minus = ConstE_slice_desc_minus[0]
	slice_description_minus['Plot_parameters']={'vmin':vmin,'vmax':vmax}
	name = slice_description_minus['Name']
	if name not in mtd:
		slicename_minus = make_slice(ds,slice_description_minus, solid_angle_ws=None, ASCII_slice_folder='')
	slicenames_list_minus_lowE.append(slice_description_minus['Name'])

	
SQW_md_list_lowE, BKG_md_lowE = DBWLS.detailedBalance_MDslices_ConstE(slicenames_list_lowE,slicenames_list_minus_lowE
        ,temperatures,OutputSuffix='_DBBKG')



fig,ax = plt.subplots(1,2,subplot_kw={'projection':'mantid','aspect':1.0/1.5},constrained_layout=True) #Aspect from recip-lattice vectors
lowT_MD = SQW_md_list_lowE[0]
highT_MD = SQW_md_list_lowE[hight_i]
plotmd = lowT_MD - highT_MD
ax[0].pcolormesh(lowT_MD,vmin=vmin,vmax=vmax,rasterized=True,cmap='viridis')
ax[0].set_title(f"BCVO [{energy_lowE-dE_lowE:.2f},{energy_lowE+dE:.2f}] meV, {temperatures[0]:.2f} K")

ax[1].pcolormesh(plotmd,vmin=-vmax,vmax=vmax,rasterized=True,cmap='coolwarm')
ax[1].set_title(f"BCVO [{energy_lowE-dE_lowE:.2f},{energy_lowE+dE:.2f}] meV, {temperatures[0]:.2f} K-{temperatures[hight_i]:.2f} K")
cdir = '/SNS/CNCS/IPTS-29413/shared/Dbfunc/'
fig.savefig(cdir+"/BCVO_constE_tsub.pdf",bbox_inches='tight',dpi=300)
fig.show()
'''