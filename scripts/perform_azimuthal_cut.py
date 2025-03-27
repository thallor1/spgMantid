import numpy as np
import matplotlib.pyplot as plt
import sys
#sys.path.append('/SNS/groups/dgs/DGS_SC_scripts')
from mantid import plots
from reduce_data_to_MDE import *
from slice_utils import *
import matplotlib
from imp import reload

def perform_azimuthal_cut(constEslicename,dphi=2.0*np.pi/180.0,rho0=0.75):
    #Specifically takes an azumuthal cut around the 1/2 0 0 position
    eslice = mtd[constEslicename]
    dims = eslice.getNonIntegratedDimensions()
    qx,qy = dim2array(dims[0]),dim2array(dims[1])
    #Scale qx by sqrt(3), now same length as (h00)
    qx_plot = qx*np.sqrt(3)
    qy_plot = qy
    Qx,Qy = np.meshgrid(qx_plot,qy_plot)
    fig,ax = plt.subplots(1,1)
    I,Err = np.copy(eslice.getSignalArray()),np.sqrt(np.copy(eslice.getErrorSquaredArray()))
    I = I[:,:,0,0].T
    Err = Err[:,:,0,0].T
    Phi = np.arctan2(Qy,Qx)
    Rho = np.sqrt(Qx**2 + Qy**2)
    goodi = np.where(np.abs(Rho-rho0)<0.06)
    #I[goodi]=1.0
    Iplt = I[goodi]
    Errplt = Err[goodi]
    Phiplt = Phi[goodi]
    phis = np.arange(0,2.0*np.pi,dphi)
    I_cut_f = []
    Err_cut_f = []
    for i in range(len(phis)-1):
        bin0 = phis[i]
        bin1 = phis[i+1]
        phi_i = np.intersect1d(np.where(Phiplt<=bin1)[0],np.where(Phiplt>bin0)[0])
        I_bin = Iplt[phi_i]
        Errbin = Iplt[phi_i]
        I_bin,Errbin = I_bin[~np.isnan(I_bin)],Errbin[~np.isnan(I_bin)]
        try:
            I_avg = np.average(I_bin,weights=1.0/Errbin)
            Err_avg = np.nansum(Errbin**2)/len(Errbin)
        except Exception as e:
            I_avg = np.nan
            Err_avg = np.nan
        I_cut_f.append(I_avg)
        Err_cut_f.append(Err_avg)
    phis = phis[1:]-np.abs(phis[1]-phis[0])/2.0
    return phis, I_cut_f, Err_cut_f
