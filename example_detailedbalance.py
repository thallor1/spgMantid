### Script to test a detailed balance function for spaghetti plots. 

import matplotlib.pyplot as plt
import sys
sys.path.append('/SNS/CNCS/IPTS-29413/shared/spgpython/')
from mantid import plots
from reduce_data_to_MDE import *
from slice_utils import *
import gen_spag_descs_mantid
import gen_spag_figax
from imp import reload
import matplotlib
import os
import numpy as np
import define_data_bcao_v
import define_slices_bcao_v
import dbbkg_wls as DBWLS

datasets=define_data_bcao_v.define_data_set()


#############################################
# MAIN PROGRAM
#############################################
reload(define_data_bcao_v)
reload(define_slices_bcao_v)
reload(gen_spag_descs_mantid)
reload(gen_spag_figax)
reload(DBWLS)

'''
Main idea is that the input of the function is the following:
	1. Energy dimension
	2. Array of cuts along the energy dimension
	3. Errors of these cuts
	4. Temperatures of each cut

A weighted least-squares method then finds the best possible background 
	at each energy. This is repeated for every point in Q along the spg
	plot.
'''

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

#Example spaghetti plot done here.
fig = plt.figure(figsize=(3.54*2,9.489))
spag_descs=gen_spag_descs_mantid.gen_spag_descs_mantid(a=5.0180,b=5.0180,c=23.3563,alpha = 90.0,beta=90.0,gamma=120.0,\
        HKLpts=[[0,0,0],[1.0,0.0,0],[4.0/3.0,1.0/3.0,0.0],[1.0,1.0,0.0],[1.0/3.0,1.0/3.0,0.0]],dQ0=0.03,\
        dQ1=1.44*0.05,dQ2=5.0,Emin=-6.0,Emax=6.0,dE=0.1,vmin=1e-4,vmax=4e-3,cmap='Spectral_r',SymOps='-3',extra='_spg')

Qlabels = [r'$\Gamma_{(000)}$',r'$M_2$ (100)',r'$K_2$ ($\frac{4}{3}\frac{1}{3}0$)',\
        r'$\Gamma_{(110)}$',r'$K_1 (\frac{1}{3}\frac{1}{3}0)$']

fig,axs = gen_spag_figax.gen_spag_figax(ds_ei6p59_I,spag_descs,Qlabels=Qlabels,figwid=3.54*2,\
        figheight=3.0,wid_ax_frac=0.85,infig=fig,ax_top=0.95,ax_bottom=0.7)

#Above simply plots the standard data - now try a detailed balance subtraction. 
temperatures = [0.25,20.0,30.0,2.0,0.92,5.0,9.0]
dslist = [ds_ei6p59_I,ds_ei6p59_I_20K,ds_ei6p59_I_30K,ds_ei6p59_I_2K,ds_ei6p59_I_920mK,ds_ei6p59_I_5K,ds_ei6p59_I_9K]

descs_list = [] #List that contains the slice descriptions of all temperatures
sqw_MDs_list = [] #Will contain MDworkspaces for extracted SQW
for t in temperatures:
	#Make a copy of the spag_descs with temperature in the name.
	spag_descs2=gen_spag_descs_mantid.gen_spag_descs_mantid(a=5.0180,b=5.0180,c=23.3563,alpha = 90.0,beta=90.0,gamma=120.0,\
	        HKLpts=[[0,0,0],[1.0,0.0,0],[4.0/3.0,1.0/3.0,0.0],[1.0,1.0,0.0],[1.0/3.0,1.0/3.0,0.0]],dQ0=0.03,\
	        dQ1=1.44*0.05,dQ2=5.0,\
	        Emin=-6.0,Emax=6.0,dE=0.1,vmin=1e-4,vmax=4e-3,\
	        cmap='Spectral_r',SymOps='-3',extra=f'_spg_{t:.2f}K')
	descs_list.append(spag_descs2)
#Now iterate through the descriptions and generate the backgrounds.
bkgmd_names = [] 
for i,descs in enumerate(spag_descs2):
	slicenames = []
	descs_Q = np.array(descs_list,dtype='object')[:,i]
	for j,desc in enumerate(descs_Q):
		name = desc['Name']
		if name not in mtd or 1==1:
			slicename = make_slice(dslist[j],desc,solid_angle_ws=None, ASCII_slice_folder='')
		else:
			slicename=name
		slicenames.append(slicename)
	sqwmd_list,bkgmd = DBWLS.detailedBalance_MDSlices(slicenames,temperatures,OutputSuffix='_DBBKG')
	bkgmd_names.append(bkgmd.getName())
	sqw_MDs_list.append(sqwmd_list)
	#Function returns the Md's themselves rather than the names so to use the python scriting convention 
	# one must simply make a list with the names rather than the MD's, and make a copy of the slice
	# descriptions with the new names. 
#The descriptions have been generated so we may use the same method as before I think, the DS argument won't actually do anything

#Still need to arrange the right lists of slice descriptions. 
slicenames_sqw_0p25 = [sqw_MDs_list[i][0].getName() for i in range(len(spag_descs2))]
slicenames_sqw_30K = [sqw_MDs_list[i][2].getName() for i in range(len(spag_descs2))]
#Imitate these descriptions by changing the name 
sqw_spg_250mK_descs = descs_list[0].copy()
sqw_spg_30K_descs = descs_list[2].copy()
for i,desc in enumerate(sqw_spg_250mK_descs):
	desc['Name']=slicenames_sqw_0p25[i]
for i,desc in enumerate(sqw_spg_30K_descs):
	desc['Name']=slicenames_sqw_30K[i]


#Spaghetti plots begin here. 
fig = plt.figure(figsize=(3.54*2,9.489))
spag_descs=gen_spag_descs_mantid.gen_spag_descs_mantid(a=5.0180,b=5.0180,c=23.3563,alpha = 90.0,beta=90.0,gamma=120.0,\
        HKLpts=[[0,0,0],[1.0,0.0,0],[4.0/3.0,1.0/3.0,0.0],[1.0,1.0,0.0],[1.0/3.0,1.0/3.0,0.0]],dQ0=0.03,\
        dQ1=1.44*0.05,dQ2=5.0,Emin=-6.0,Emax=6.0,dE=0.1,vmin=1e-4,vmax=4e-3,cmap='Spectral_r',SymOps='-3',extra='_spg_SQW')


Qlabels = [r'$\Gamma_{(000)}$',r'$M_2$ (100)',r'$K_2$ ($\frac{4}{3}\frac{1}{3}0$)',\
        r'$\Gamma_{(110)}$',r'$K_1 (\frac{1}{3}\frac{1}{3}0)$']

fig,axs = gen_spag_figax.gen_spag_figax(ds_ei6p59_I,sqw_spg_250mK_descs,Qlabels=Qlabels,figwid=3.54*2,\
        figheight=3.0,wid_ax_frac=0.85,infig=fig,ax_top=0.95,ax_bottom=0.7)

fig,axs2 = gen_spag_figax.gen_spag_figax(ds_ei6p59_I_30K,sqw_spg_30K_descs,Qlabels=Qlabels,figwid=3.54*2,\
        figheight=3.0,wid_ax_frac=0.85,infig=fig,ax_top=0.6,ax_bottom=0.35)

bkgmd_descs = descs_list[0].copy()
for i,desc in enumerate(bkgmd_descs):
	desc['Name']=bkgmd_names[i]
#Plot the temperature indpendent background. 
fig,axs3 = gen_spag_figax.gen_spag_figax(ds_ei6p59_I,bkgmd_descs,Qlabels=Qlabels,figwid=3.54*2,\
        figheight=3.0,wid_ax_frac=0.85,infig=fig,ax_top=0.3,ax_bottom=0.05)

ylim = [0,6]
for axs_i in [axs,axs2,axs3]:
	for ax in axs_i:
		ax.set_ylim(ylim[0],ylim[1])
fig.tight_layout()
fig.show()
