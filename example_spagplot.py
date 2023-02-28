import matplotlib.pyplot as plt
import sys
#sys.path.append('/SNS/groups/dgs/DGS_SC_scripts')
from mantid import plots
from reduce_data_to_MDE import *
from slice_utils import *
import define_data_bcao_v
import define_slices_bcao_v
import gen_spag_descs_mantid
import gen_spag_figax
from imp import reload
import matplotlib
import os
import numpy as np
#############################################
# MAIN PROGRAM
#############################################
reload(define_data_bcao_v)
reload(define_slices_bcao_v)
reload(gen_spag_descs_mantid)
reload(gen_spag_figax)
datasets=define_data_bcao_v.define_data_set()

ds_ei6p59_I = datasets[3]
ds_ei6p59_I_bkgsub = datasets[14]
ds_ei6p59_I_30K = datasets[13]

reduce_data_to_MDE([ds_ei6p59_I,ds_ei6p59_I_bkgsub,ds_ei6p59_I_30K])

#Example spaghetti plot done here.

spag_descs=gen_spag_descs_mantid.gen_spag_descs_mantid(a=5.0180,b=5.0180,c=23.3563,alpha = 90.0,beta=90.0,gamma=120.0,\
        HKLpts=[[0,0,0],[1.0,0.0,0],[4.0/3.0,1.0/3.0,0.0],[1.0,1.0,0.0],[1.0/3.0,1.0/3.0,0.0]],dQ0=0.03,\
        dQ1=1.44*0.05,dQ2=5.0,Emin=0.0,Emax=6.0,dE=0.1,vmin=1e-4,vmax=4e-3,cmap='Spectral_r',SymOps='-3',extra='_spg')

Qlabels = [r'$\Gamma_{(000)}$',r'$M_2$ (100)',r'$K_2$ ($\frac{4}{3}\frac{1}{3}0$)',\
        r'$\Gamma_{(110)}$',r'$K_1 (\frac{1}{3}\frac{1}{3}0)$']



fig,axs = gen_spag_figax.gen_spag_figax(ds_ei6p59_I,spag_descs,Qlabels=Qlabels,figwid=3.54*2,\
        figheight=3.0,wid_ax_frac=0.85)
fig.show()

fig.savefig('BCAOV_spagplot_0p25K.pdf',bbox_inches='tight',dpi=400)
