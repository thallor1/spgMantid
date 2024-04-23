import numpy as np
import matplotlib.pyplot as plt
from mantid import plots
from reduce_data_to_MDE import *
from slice_utils import *

def gen_spag_figax(ds,spag_descs,Qlabels=None,figwid=3.54*2,\
        figheight=3.0,wid_ax_frac=0.85,title='',infig=None,ax_top=None,ax_bottom=None,\
        ax_left=None,ax_right=None):
    #A new field has been added to the dictionary for each slice, the Qlength.
    Qlens = []
    for desc in spag_descs:
        Qlens.append(desc['Qlength'])
    #With subplots of width of the correct ratios.
    if infig is None:
        fig = plt.figure(figsize=(figwid,figheight))
    else:
        fig=infig
    ax_wids = np.array(Qlens)*wid_ax_frac/np.sum(Qlens)
    spec = plt.GridSpec(nrows=1,ncols=len(spag_descs),width_ratios=ax_wids,hspace=0,wspace=0,\
            top=ax_top,bottom=ax_bottom,left=ax_left,right=ax_right)
    axlist=[]
    for i,desc in enumerate(spag_descs):
        ax = fig.add_subplot(spec[i],projection='mantid')
        if desc['Name'] not in mtd: #So we don't need to redo these NormMD calls...
            make_slice(ds,desc, solid_angle_ws=None, ASCII_slice_folder='')
        c=plot_slice(desc, ax=ax, cbar_label=None)
        set_axes_parameters(ax,**desc['Axes_parameters'])
        if i<len(spag_descs)-1 and Qlabels is not None:
            ax.text(0,-0.05,Qlabels[i],fontsize=10,transform=ax.transAxes,horizontalalignment='center',\
                verticalalignment='top')
            ax.text(1,-0.05,Qlabels[i+1],fontsize=10,transform=ax.transAxes,horizontalalignment='center',\
                verticalalignment='top')
        elif i==len(spag_descs)-1 and Qlabels is not None:
            ax.text(1,-0.05,Qlabels[i+1],fontsize=10,transform=ax.transAxes,horizontalalignment='center',\
                verticalalignment='top')
        if i>0:
            ax.set_ylabel('')
            ax.set_yticklabels([])
        ax.set_xticklabels([])
        ax.set_xlabel('')
        axlist.append(ax)
        plt.grid(None)
        if i==0:
            ax.text((wid_ax_frac*0.5)*(1.0/ax_wids[0]),1.02,title,\
                horizontalalignment='center',verticalalignment='bottom',transform=ax.transAxes)
            ax.set_ylabel("$\hbar\omega$ (meV)")
    return fig,axlist
