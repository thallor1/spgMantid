import numpy as np
from matplotlib.colors import LogNorm
import matplotlib

def get_color(val,vmin,vmax,cmap):
    cmap=matplotlib.cm.get_cmap(cmap)
    norm = matplotlib.colors.Normalize(vmin=vmin,vmax=vmax)
    rgba = cmap(norm(val))
    return rgba

def define_norm_slices(extra='',T=0.25,color='k'):
    dsl=[]
    #First slice is along the ordering wavevector, to look at 
    #00L dependence
    description={'QDimension0':'1,0,0',
                 'QDimension1':'-1,2,0',
                 'QDimension2':'0,0,1',
                 'Dimension0Name':'QDimension0',
                 'Dimension0Binning':'0.0,0.03,2.0',
                 'Dimension1Name':'QDimension1',
                 'Dimension1Binning':'-0.05,0.05',
                 'Dimension2Name':'QDimension2',
                 'Dimension2Binning':'-2,0.05,2',
                 'Dimension3Name':'DeltaE',
                 'Dimension3Binning':'-6,0.05,6',
                 'SymmetryOperations':'-3',
                 #'SymmetryOperations':'x,y,z;-x,y,z;x,y,-z;-x,y,-z',
                 'ConvertToChi':False,
                 'Plot_parameters':{'mfc':color,'ls':' ','marker':'o','color':color,'label':f"T={T:.2f} K"},#vmin=1e-4,vmax=1e-1
                 'Axes_parameters':{'xrange':None,'yrange':None, 'xtitle':None, 'ytitle':None, 'title':'BCAO-V 110 cut', 'aspect_ratio':None, 'tight_axes':True, 'grid':True},
                 'Name':f'Slice_H00vs00L_T_{T:.2f}K_DB'+extra}
    dsl.append(description)
    return dsl

def define_dbcut_110(extra='',T=0.25,color='k'):
    dsl=[]
    description={'QDimension0':'1,1,0',
                 'QDimension1':'-1,1,0',
                 'QDimension2':'0,0,1',
                 'Dimension0Name':'QDimension0',
                 'Dimension0Binning':'0.9,1.1',
                 'Dimension1Name':'QDimension1',
                 'Dimension1Binning':'-0.1,0.1',
                 'Dimension2Name':'QDimension2',
                 'Dimension2Binning':'-2,2',
                 'Dimension3Name':'DeltaE',
                 'Dimension3Binning':'-6,0.05,6',
                 'SymmetryOperations':'-3',
                 #'SymmetryOperations':'x,y,z;-x,y,z;x,y,-z;-x,y,-z',
                 'ConvertToChi':False,
                 'Plot_parameters':{'mfc':color,'ls':' ','marker':'o','color':color,'label':f"T={T:.2f} K"},#vmin=1e-4,vmax=1e-1
                 'Axes_parameters':{'xrange':None,'yrange':None, 'xtitle':None, 'ytitle':None, 'title':'BCAO-V 110 cut', 'aspect_ratio':None, 'tight_axes':True, 'grid':True},
                 'Name':f'110_cut_T_{T:.2f}K_DB'+extra}
    dsl.append(description)
    return dsl
def define_data_slices_Ei12(extra=''):
    dsl=[]
    for E in [0.0]:
        dE=0.5
        description={'QDimension0':'1,1,0',
                     'QDimension1':'-1,1,0',
                     'QDimension2':'0,0,1',
                     'Dimension0Name':'QDimension0',
                     'Dimension0Binning':'-2.,0.025,2.',
                     'Dimension1Name':'QDimension1',
                     'Dimension1Binning':'-2.5,0.025,2.5',
                     'Dimension2Name':'QDimension2',
                     'Dimension2Binning':'-2,2',
                     'Dimension3Name':'DeltaE',
                     'Dimension3Binning':'{},{}'.format(E-dE,E+dE),
                     'SymmetryOperations':'-3',
                     #'SymmetryOperations':'x,y,z;-x,y,z;x,y,-z;-x,y,-z',
                     'ConvertToChi':False,
                     'Plot_parameters':{'vmin':0.0,'vmax':0.5},#vmin=1e-4,vmax=1e-1
                     'Axes_parameters':{'xrange':None,'yrange':None, 'xtitle':None, 'ytitle':None, 'title':'CNCS E=[{},{}]meV'.format(E-dE,E+dE), 'aspect_ratio':None, 'tight_axes':True, 'grid':True},
                     'Name':'HK0_slice_{0:.1f}meV'.format(E)+extra}
        dsl.append(description)

    #Q-E cut along (H00) direction
    description={'QDimension0':'1,0,0',
                     'QDimension1':'-1,2,0',
                     'QDimension2':'0,0,1',
                     'Dimension0Name':'QDimension0',
                     'Dimension0Binning':'-3.,0.025,3.',
                     'Dimension1Name':'QDimension1',
                     'Dimension1Binning':'-0.1,0.1',
                     'Dimension2Name':'QDimension2',
                     'Dimension2Binning':'-2,2',
                     'Dimension3Name':'DeltaE',
                     'Dimension3Binning':'0,0.1,11.1',
                     'SymmetryOperations':'-3',
                     #'SymmetryOperations':'x,y,z;-x,y,z;x,y,-z;-x,y,-z',
                     'ConvertToChi':False,
                     'Plot_parameters':{'vmin':0.0,'vmax':0.008},#vmin=1e-4,vmax=1e-1
                     'Axes_parameters':{'xrange':None,'yrange':None, 'xtitle':None, 'ytitle':None, 'title':'CNCS E=[{},{}]meV'.format(E-dE,E+dE), 'aspect_ratio':None, 'tight_axes':True, 'grid':True},
        'Name':'HK0_slice_{0:.1f}meV'.format(E)+extra}
    dsl.append(description)

    #Q-E cut along (HH0) direction
    description={'QDimension0':'1,1,0',
                     'QDimension1':'-1,1,0',
                     'QDimension2':'0,0,1',
                     'Dimension0Name':'QDimension0',
                     'Dimension0Binning':'-2.,0.025,2.',
                     'Dimension1Name':'QDimension1',
                     'Dimension1Binning':'-0.1,0.1',
                     'Dimension2Name':'QDimension2',
                     'Dimension2Binning':'-2,2',
                     'Dimension3Name':'DeltaE',
                     'Dimension3Binning':'0,0.1,11.1',
                     'SymmetryOperations':'-3',
                     #'SymmetryOperations':'x,y,z;-x,y,z;x,y,-z;-x,y,-z',
                     'ConvertToChi':False,
                     'Plot_parameters':{'vmin':0.0,'vmax':0.008},#vmin=1e-4,vmax=1e-1
                     'Axes_parameters':{'xrange':None,'yrange':None, 'xtitle':None, 'ytitle':None, 'title':'CNCS E=[{},{}]meV'.format(E-dE,E+dE), 'aspect_ratio':None, 'tight_axes':True, 'grid':True},
        'Name':'HH0vsE_slice_{0:.1f}meV'.format(E)+extra}
    dsl.append(description)

    #Now some const E slices (inelastic)
    for E in [1.8,1.0]:
        dE=0.2
        description={'QDimension0':'1,1,0',
                     'QDimension1':'-1,1,0',
                     'QDimension2':'0,0,1',
                     'Dimension0Name':'QDimension0',
                     'Dimension0Binning':'-2.,0.035,2.',
                     'Dimension1Name':'QDimension1',
                     'Dimension1Binning':'-3,0.035,3.0',
                     'Dimension2Name':'QDimension2',
                     'Dimension2Binning':'-2,2',
                     'Dimension3Name':'DeltaE',
                     'Dimension3Binning':'{},{}'.format(E-dE,E+dE),
                     'SymmetryOperations':'-3',
                     #'SymmetryOperations':'x,y,z;-x,y,z;x,y,-z;-x,y,-z',
                     'ConvertToChi':False,
                     'Plot_parameters':{'vmin':0.0,'vmax':8e-3},#vmin=1e-4,vmax=1e-1
                     'Axes_parameters':{'xrange':None,'yrange':None, 'xtitle':None, 'ytitle':None, 'title':'CNCS E=[{},{}]meV'.format(E-dE,E+dE), 'aspect_ratio':None, 'tight_axes':True, 'grid':True},
                     'Name':'HK0_slice_{0:.1f}meV'.format(E)+extra}
        dsl.append(description)

    # Energy vs intensity at (110) and (100)
    description={'QDimension0':'1,1,0',
                 'QDimension1':'-1,1,0',
                 'QDimension2':'0,0,1',
                 'Dimension0Name':'QDimension0',
                 'Dimension0Binning':'0.95,1.05',
                 'Dimension1Name':'QDimension1',
                 'Dimension1Binning':'-0.05,0.05',
                 'Dimension2Name':'QDimension2',
                 'Dimension2Binning':'-2,2',
                 'Dimension3Name':'DeltaE',
                 'Dimension3Binning':'0,0.1,10',
                 'SymmetryOperations':'-3',
                 #'SymmetryOperations':'x,y,z;-x,y,z;x,y,-z;-x,y,-z',
                 'ConvertToChi':False,
                 'Plot_parameters':{'color':'k','marker':'o','mfc':'k','mec':'k','ls':' ','capsize':3,'label':'(110)'},#vmin=1e-4,vmax=1e-1
                 'Axes_parameters':{'xrange':None,'yrange':None, 'xtitle':None, 'ytitle':None, 'title':'CNCS (110) Ei=12 meV', 'aspect_ratio':None, 'tight_axes':True, 'grid':True},
                 'Name':'cutvsE_110_{0:.1f}meV_Ei12'.format(E)+extra}
    dsl.append(description)
    description={'QDimension0':'1,0,0',
                 'QDimension1':'-1,2,0',
                 'QDimension2':'0,0,1',
                 'Dimension0Name':'QDimension0',
                 'Dimension0Binning':'0.95,1.05',
                 'Dimension1Name':'QDimension1',
                 'Dimension1Binning':'-0.05,0.05',
                 'Dimension2Name':'QDimension2',
                 'Dimension2Binning':'-2,2',
                 'Dimension3Name':'DeltaE',
                 'Dimension3Binning':'0,0.1,10',
                 'SymmetryOperations':'-3',
                 #'SymmetryOperations':'x,y,z;-x,y,z;x,y,-z;-x,y,-z',
                 'ConvertToChi':False,
                 'Plot_parameters':{'color':'b','marker':'o','mfc':'w','mec':'b','ls':' ','capsize':3,'label':'(100)'},#vmin=1e-4,vmax=1e-1
                 'Axes_parameters':{'xrange':None,'yrange':None, 'xtitle':None, 'ytitle':None, 'title':'CNCS (100) Ei=12 meV', 'aspect_ratio':None, 'tight_axes':True, 'grid':True},
                 'Name':'cutvsE_100_{0:.1f}meV_Ei12'.format(E)+extra}
    dsl.append(description)
    return dsl

def define_data_slices_Ei3p32(extra=''):
    dsl=[]
    for E in [0.0]:
        dE=0.1
        description={'QDimension0':'1,1,0',
                     'QDimension1':'-1,1,0',
                     'QDimension2':'0,0,1',
                     'Dimension0Name':'QDimension0',
                     'Dimension0Binning':'-2.,0.025,2.',
                     'Dimension1Name':'QDimension1',
                     'Dimension1Binning':'-2.5,0.025,2.5',
                     'Dimension2Name':'QDimension2',
                     'Dimension2Binning':'-2,2',
                     'Dimension3Name':'DeltaE',
                     'Dimension3Binning':'{},{}'.format(E-dE,E+dE),
                     'SymmetryOperations':'-3',
                     #'SymmetryOperations':'x,y,z;-x,y,z;x,y,-z;-x,y,-z',
                     'ConvertToChi':False,
                     'Plot_parameters':{'vmin':0,'vmax':1.5},#vmin=1e-4,vmax=1e-1
                     'Axes_parameters':{'xrange':None,'yrange':None, 'xtitle':None, 'ytitle':None, 'title':'CNCS E=[{},{}]meV'.format(E-dE,E+dE), 'aspect_ratio':None, 'tight_axes':True, 'grid':True},
                     'Name':'HH0vsHmH0_slice_{0:.1f}meV_Ei3p32'.format(E)+extra}
        dsl.append(description)

    #Q-E cut along (H00) direction
    description={'QDimension0':'1,0,0',
                     'QDimension1':'-1,2,0',
                     'QDimension2':'0,0,1',
                     'Dimension0Name':'QDimension0',
                     'Dimension0Binning':'-2.,0.025,2.',
                     'Dimension1Name':'QDimension1',
                     'Dimension1Binning':'-0.1,0.1',
                     'Dimension2Name':'QDimension2',
                     'Dimension2Binning':'-2,2',
                     'Dimension3Name':'DeltaE',
                     'Dimension3Binning':'0,0.025,3.1',
                     'SymmetryOperations':'-3',
                     #'SymmetryOperations':'x,y,z;-x,y,z;x,y,-z;-x,y,-z',
                     'ConvertToChi':False,
                     'Plot_parameters':{'vmin':0.0,'vmax':0.01},#vmin=1e-4,vmax=1e-1
                     'Axes_parameters':{'xrange':None,'yrange':None, 'xtitle':None, 'ytitle':None, 'title':'CNCS E=[{},{}]meV'.format(E-dE,E+dE), 'aspect_ratio':None, 'tight_axes':True, 'grid':True},
                     'Name':'H00vsE_slice_{0:.1f}meV_Ei3p32'.format(E)+extra}
    dsl.append(description)

    #Q-E cut along (HH0) direction
    description={'QDimension0':'1,1,0',
                     'QDimension1':'-1,1,0',
                     'QDimension2':'0,0,1',
                     'Dimension0Name':'QDimension0',
                     'Dimension0Binning':'-2.,0.025,2.',
                     'Dimension1Name':'QDimension1',
                     'Dimension1Binning':'-0.1,0.1',
                     'Dimension2Name':'QDimension2',
                     'Dimension2Binning':'-2,2',
                     'Dimension3Name':'DeltaE',
                     'Dimension3Binning':'0,0.025,3.1',
                     'SymmetryOperations':'-3',
                     #'SymmetryOperations':'x,y,z;-x,y,z;x,y,-z;-x,y,-z',
                     'ConvertToChi':False,
                     'Plot_parameters':{'vmin':0.0,'vmax':0.008},#vmin=1e-4,vmax=1e-1
                     'Axes_parameters':{'xrange':None,'yrange':None, 'xtitle':None, 'ytitle':None, 'title':'BCAO-V', 'aspect_ratio':None, 'tight_axes':True, 'grid':True},
        'Name':'HH0vsE_slice_{0:.1f}meV_Ei3p32'.format(E)+extra}
    dsl.append(description)
    #Now some const E slices (inelastic)
    for E in [0.4]:
        dE=0.1
        description={'QDimension0':'1,1,0',
                     'QDimension1':'-1,1,0',
                     'QDimension2':'0,0,1',
                     'Dimension0Name':'QDimension0',
                     'Dimension0Binning':'-2.,0.025,2.',
                     'Dimension1Name':'QDimension1',
                     'Dimension1Binning':'-2.5,0.025,2.5',
                     'Dimension2Name':'QDimension2',
                     'Dimension2Binning':'-2,2',
                     'Dimension3Name':'DeltaE',
                     'Dimension3Binning':'{},{}'.format(E-dE,E+dE),
                     'SymmetryOperations':'-3',
                     #'SymmetryOperations':'x,y,z;-x,y,z;x,y,-z;-x,y,-z',
                     'ConvertToChi':False,
                     'Plot_parameters':{'vmin':0.0,'vmax':5e-3},#vmin=1e-4,vmax=1e-1
                     'Axes_parameters':{'xrange':None,'yrange':None, 'xtitle':None, 'ytitle':None, 'title':'CNCS E=[{},{}]meV'.format(E-dE,E+dE), 'aspect_ratio':None, 'tight_axes':True, 'grid':True},
                     'Name':'HK0_slice_{0:.1f}meV_Ei3p32'.format(E)+extra}
        dsl.append(description)

    # Energy vs intensity at (110) and (100)
    description={'QDimension0':'1,1,0',
                 'QDimension1':'-1,1,0',
                 'QDimension2':'0,0,1',
                 'Dimension0Name':'QDimension0',
                 'Dimension0Binning':'0.95,1.05',
                 'Dimension1Name':'QDimension1',
                 'Dimension1Binning':'-0.05,0.05',
                 'Dimension2Name':'QDimension2',
                 'Dimension2Binning':'-2,2',
                 'Dimension3Name':'DeltaE',
                 'Dimension3Binning':'0,0.025,3',
                 'SymmetryOperations':'-3',
                 #'SymmetryOperations':'x,y,z;-x,y,z;x,y,-z;-x,y,-z',
                 'ConvertToChi':False,
                 'Plot_parameters':{'color':'k','marker':'o','mfc':'k','mec':'k','ls':' ','capsize':3,'label':'(110)'},#vmin=1e-4,vmax=1e-1
                 'Axes_parameters':{'xrange':None,'yrange':None, 'xtitle':None, 'ytitle':None, 'title':'CNCS (110) Ei=3.32 meV', 'aspect_ratio':None, 'tight_axes':True, 'grid':True},
                 'Name':'cutvsE_110_{0:.1f}meV_Ei3p32'.format(E)+extra}
    dsl.append(description)
    description={'QDimension0':'1,0,0',
                 'QDimension1':'-1,2,0',
                 'QDimension2':'0,0,1',
                 'Dimension0Name':'QDimension0',
                 'Dimension0Binning':'0.95,1.05',
                 'Dimension1Name':'QDimension1',
                 'Dimension1Binning':'-0.05,0.05',
                 'Dimension2Name':'QDimension2',
                 'Dimension2Binning':'-2,2',
                 'Dimension3Name':'DeltaE',
                 'Dimension3Binning':'0,0.025,3',
                 'SymmetryOperations':'-3',
                 #'SymmetryOperations':'x,y,z;-x,y,z;x,y,-z;-x,y,-z',
                 'ConvertToChi':False,
                 'Plot_parameters':{'color':'b','marker':'o','mfc':'w','mec':'b','ls':' ','capsize':3,'label':'(100)'},#vmin=1e-4,vmax=1e-1
                 'Axes_parameters':{'xrange':None,'yrange':None, 'xtitle':None, 'ytitle':None, 'title':'CNCS (100) Ei=3.32 meV', 'aspect_ratio':None, 'tight_axes':True, 'grid':True},
                 'Name':'cutvsE_100_{0:.1f}meV_Ei3p32'.format(E)+extra}
    dsl.append(description)
    return dsl

def define_data_slices_Ei6p59_bkgsub(extra='',T=0.25,color='k'):
    dsl=[]
    for E in [0.0]:
        dE=0.2
        description={'QDimension0':'1,1,0',
                     'QDimension1':'-1,1,0',
                     'QDimension2':'0,0,1',
                     'Dimension0Name':'QDimension0',
                     'Dimension0Binning':'-2.,0.04,2.',
                     'Dimension1Name':'QDimension1',
                     'Dimension1Binning':'-2.5,0.04,2.5',
                     'Dimension2Name':'QDimension2',
                     'Dimension2Binning':'-2,2',
                     'Dimension3Name':'DeltaE',
                     'Dimension3Binning':'{},{}'.format(E-dE,E+dE),
                     'SymmetryOperations':'-3',
                     #'SymmetryOperations':'x,y,z;-x,y,z;x,y,-z;-x,y,-z',
                     'ConvertToChi':False,
                     'Plot_parameters':{'vmin':-0.05,'vmax':0.05,'cmap':'bwr'},#vmin=1e-4,vmax=1e-1
                     'Axes_parameters':{'xrange':None,'yrange':None, 'xtitle':None, 'ytitle':None, 'title':'CNCS E=[{},{}]meV'.format(E-dE,E+dE), 'aspect_ratio':None, 'tight_axes':True, 'grid':True},
                     'Name':'HH0vsHmH0_slice_{0:.1f}meV_Ei6p59'.format(E)+extra}
        dsl.append(description)

    #Q-E cut along (H00) direction
    description={'QDimension0':'1,0,0',
                     'QDimension1':'-1,2,0',
                     'QDimension2':'0,0,1',
                     'Dimension0Name':'QDimension0',
                     'Dimension0Binning':'-2.,0.05,2.',
                     'Dimension1Name':'QDimension1',
                     'Dimension1Binning':'-0.1,0.1',
                     'Dimension2Name':'QDimension2',
                     'Dimension2Binning':'-2,2',
                     'Dimension3Name':'DeltaE',
                     'Dimension3Binning':'-0,0.1,6.1',
                     'SymmetryOperations':'-3',
                     #'SymmetryOperations':'x,y,z;-x,y,z;x,y,-z;-x,y,-z',
                     'ConvertToChi':False,
                     'Plot_parameters':{'vmin':-0.003,'vmax':0.003,'cmap':'bwr'},#vmin=1e-4,vmax=1e-1
                     'Axes_parameters':{'xrange':None,'yrange':None, 'xtitle':None, 'ytitle':None, 'title':'CNCS E=[{},{}]meV'.format(E-dE,E+dE), 'aspect_ratio':None, 'tight_axes':True, 'grid':True},
                     'Name':'H00vsE_slice_{0:.1f}meV_Ei6p59'.format(E)+extra}
    dsl.append(description)

    #Q-E cut along (HH0) direction
    description={'QDimension0':'2,-1,0',
                     'QDimension1':'0,1,0',
                     'QDimension2':'0,0,1',
                     'Dimension0Name':'QDimension0',
                     'Dimension0Binning':'-2.,0.030,2.',
                     'Dimension1Name':'QDimension1',
                     'Dimension1Binning':'-0.1,0.1',
                     'Dimension2Name':'QDimension2',
                     'Dimension2Binning':'-2,2',
                     'Dimension3Name':'DeltaE',
                     'Dimension3Binning':'-3,0.05,6.1',
                     'SymmetryOperations':'-3',
                     #'SymmetryOperations':'x,y,z;-x,y,z;x,y,-z;-x,y,-z',
                     'ConvertToChi':False,
                     'Plot_parameters':{'vmin':-0.005,'vmax':0.005,'cmap':'bwr'},#vmin=1e-4,vmax=1e-1
                     'Axes_parameters':{'xrange':None,'yrange':None, 'xtitle':None, 'ytitle':None, 'title':'BCAO-V', 'aspect_ratio':None, 'tight_axes':True, 'grid':True},
        'Name':'HH0vsE_slice_{0:.1f}meV_Ei6p59'.format(E)+extra}
    dsl.append(description)
    #Now some const E slices (inelastic)
    for E in [2.6]:
        dE=0.15
        description={'QDimension0':'1,1,0',
                     'QDimension1':'-1,1,0',
                     'QDimension2':'0,0,1',
                     'Dimension0Name':'QDimension0',
                     'Dimension0Binning':'-2.,0.03,2.',
                     'Dimension1Name':'QDimension1',
                     'Dimension1Binning':'-2.5,0.03,2.5',
                     'Dimension2Name':'QDimension2',
                     'Dimension2Binning':'-5,5',
                     'Dimension3Name':'DeltaE',
                     'Dimension3Binning':'{},{}'.format(E-dE,E+dE),
                     'SymmetryOperations':'-3',
                     #'SymmetryOperations':'x,y,z;-x,y,z;x,y,-z;-x,y,-z',
                     'ConvertToChi':False,
                     'Plot_parameters':{'vmin':-1.5e-3,'vmax':1.5e-3,'cmap':'bwr'},#{'norm':LogNorm(vmin=3e-4,vmax=8e-3)},#vmin=1e-4,vmax=1e-1
                     'Axes_parameters':{'xrange':None,'yrange':None, 'xtitle':None, 'ytitle':None, 'title':'CNCS E=[{},{}]meV'.format(np.around(E-dE,2),E+dE), 'aspect_ratio':None, 'tight_axes':True, 'grid':True},
                     'Name':'HK0_slice_{0:.1f}meV_6p59'.format(E)+extra}
        dsl.append(description)

    # Energy vs intensity at (110) and (100)
    description={'QDimension0':'1,1,0',
                 'QDimension1':'-1,1,0',
                 'QDimension2':'0,0,1',
                 'Dimension0Name':'QDimension0',
                 'Dimension0Binning':'0.95,1.05',
                 'Dimension1Name':'QDimension1',
                 'Dimension1Binning':'-0.05,0.05',
                 'Dimension2Name':'QDimension2',
                 'Dimension2Binning':'-2,2',
                 'Dimension3Name':'DeltaE',
                 'Dimension3Binning':'-2,0.1,6',
                 'SymmetryOperations':'-3',
                 #'SymmetryOperations':'x,y,z;-x,y,z;x,y,-z;-x,y,-z',
                 'ConvertToChi':False,
                 'Plot_parameters':{'color':color,'marker':'o','mfc':color,'mec':color,'ls':' ','capsize':3,'label':f"{T:.2f} K"},#vmin=1e-4,vmax=1e-1
                 'Axes_parameters':{'xrange':None,'yrange':None, 'xtitle':None, 'ytitle':None, 'title':'CNCS (110) Ei=6p59 meV', 'aspect_ratio':None, 'tight_axes':True, 'grid':True},
                 'Name':'cutvsE_110_{0:.1f}meV_Ei6p59'.format(E)+extra}
    dsl.append(description)
    description={'QDimension0':'1,0,0',
                 'QDimension1':'-1,2,0',
                 'QDimension2':'0,0,1',
                 'Dimension0Name':'QDimension0',
                 'Dimension0Binning':'0.95,1.05',
                 'Dimension1Name':'QDimension1',
                 'Dimension1Binning':'-0.05,0.05',
                 'Dimension2Name':'QDimension2',
                 'Dimension2Binning':'-2,2',
                 'Dimension3Name':'DeltaE',
                 'Dimension3Binning':'-2,0.1,6',
                 'SymmetryOperations':'-3',
                 #'SymmetryOperations':'x,y,z;-x,y,z;x,y,-z;-x,y,-z',
                 'ConvertToChi':False,
                 'Plot_parameters':{'color':color,'marker':'o','mfc':color,'mec':color,'ls':' ','capsize':3,'label':f"{T:.2f} K"},#vmin=1e-4,vmax=1e-1
                 'Axes_parameters':{'xrange':None,'yrange':None, 'xtitle':None, 'ytitle':None, 'title':'CNCS (100) Ei=6p59 meV', 'aspect_ratio':None, 'tight_axes':True, 'grid':True},
                 'Name':'cutvsE_100_{0:.1f}meV_Ei6p59'.format(E)+extra}
    dsl.append(description)

    #Cuts along the (100) and (110) type directions
    description={'QDimension0':'1,0,0',
                 'QDimension1':'-1,2,0',
                 'QDimension2':'0,0,1',
                 'Dimension0Name':'QDimension0',
                 'Dimension0Binning':'-4,0.01,4',
                 'Dimension1Name':'QDimension1',
                 'Dimension1Binning':'-0.05,0.05',
                 'Dimension2Name':'QDimension2',
                 'Dimension2Binning':'-2,2',
                 'Dimension3Name':'DeltaE',
                 'Dimension3Binning':'-0.2,0.2',
                 'SymmetryOperations':'-3',
                 #'SymmetryOperations':'x,y,z;-x,y,z;x,y,-z;-x,y,-z',
                 'ConvertToChi':False,
                 'Plot_parameters':{'color':color,'marker':'o','mfc':color,'mec':color,'ls':' ','capsize':3,'label':f"{T:.2f} K"},#vmin=1e-4,vmax=1e-1
                 'Axes_parameters':{'xrange':None,'yrange':None, 'xtitle':None, 'ytitle':None, 'title':'CNCS (H00) Ei=6p59 meV', 'aspect_ratio':None, 'tight_axes':True, 'grid':True},
                 'Name':'Bragg_100cut_{0:.1f}K_Ei6p59'.format(T)+extra}
    dsl.append(description)
    return dsl

def define_data_slices_Ei6p59(extra='',T=0.25,color='k'):
    dsl=[]
    for E in [0.0]:
        dE=0.2
        description={'QDimension0':'1,1,0',
                     'QDimension1':'-1,1,0',
                     'QDimension2':'0,0,1',
                     'Dimension0Name':'QDimension0',
                     'Dimension0Binning':'-2.,0.04,2.',
                     'Dimension1Name':'QDimension1',
                     'Dimension1Binning':'-2.5,0.04,2.5',
                     'Dimension2Name':'QDimension2',
                     'Dimension2Binning':'-2,2',
                     'Dimension3Name':'DeltaE',
                     'Dimension3Binning':'{},{}'.format(E-dE,E+dE),
                     'SymmetryOperations':'-3',
                     #'SymmetryOperations':'x,y,z;-x,y,z;x,y,-z;-x,y,-z',
                     'ConvertToChi':False,
                     'Plot_parameters':{'vmin':0,'vmax':0.15},#vmin=1e-4,vmax=1e-1
                     'Axes_parameters':{'xrange':None,'yrange':None, 'xtitle':None, 'ytitle':None, 'title':'CNCS E=[{},{}]meV'.format(E-dE,E+dE), 'aspect_ratio':None, 'tight_axes':True, 'grid':True},
                     'Name':'HH0vsHmH0_slice_{0:.1f}meV_Ei6p59'.format(E)+extra}
        dsl.append(description)

    #Q-E cut along (H00) direction
    description={'QDimension0':'1,0,0',
                     'QDimension1':'-1,2,0',
                     'QDimension2':'0,0,1',
                     'Dimension0Name':'QDimension0',
                     'Dimension0Binning':'-2.,0.035,2.',
                     'Dimension1Name':'QDimension1',
                     'Dimension1Binning':'-0.1,0.1',
                     'Dimension2Name':'QDimension2',
                     'Dimension2Binning':'-2,2',
                     'Dimension3Name':'DeltaE',
                     'Dimension3Binning':'-0,0.05,6.1',
                     'SymmetryOperations':'-3',
                     #'SymmetryOperations':'x,y,z;-x,y,z;x,y,-z;-x,y,-z',
                     'ConvertToChi':False,
                     'Plot_parameters':{'vmin':0.0,'vmax':0.003},#vmin=1e-4,vmax=1e-1
                     'Axes_parameters':{'xrange':None,'yrange':None, 'xtitle':None, 'ytitle':None, 'title':'CNCS E=[{},{}]meV'.format(E-dE,E+dE), 'aspect_ratio':None, 'tight_axes':True, 'grid':True},
                     'Name':'H00vsE_slice_{0:.1f}meV_Ei6p59'.format(E)+extra}
    dsl.append(description)

    #Q-E cut along (HH0) direction
    description={'QDimension0':'2,-1,0',
                     'QDimension1':'0,1,0',
                     'QDimension2':'0,0,1',
                     'Dimension0Name':'QDimension0',
                     'Dimension0Binning':'-2.,0.015,2.',
                     'Dimension1Name':'QDimension1',
                     'Dimension1Binning':'-0.1,0.1',
                     'Dimension2Name':'QDimension2',
                     'Dimension2Binning':'-2,2',
                     'Dimension3Name':'DeltaE',
                     'Dimension3Binning':'-3,0.025,6.1',
                     'SymmetryOperations':'-3',
                     #'SymmetryOperations':'x,y,z;-x,y,z;x,y,-z;-x,y,-z',
                     'ConvertToChi':False,
                     'Plot_parameters':{'vmin':0.001,'vmax':0.006},#vmin=1e-4,vmax=1e-1
                     'Axes_parameters':{'xrange':None,'yrange':None, 'xtitle':None, 'ytitle':None, 'title':'BCAO-V', 'aspect_ratio':None, 'tight_axes':True, 'grid':True},
        'Name':'HH0vsE_slice_{0:.1f}meV_Ei6p59'.format(E)+extra}
    dsl.append(description)
    #Now some const E slices (inelastic)
    for E in [2.6]:
        dE=0.15
        description={'QDimension0':'1,1,0',
                     'QDimension1':'-1,1,0',
                     'QDimension2':'0,0,1',
                     'Dimension0Name':'QDimension0',
                     'Dimension0Binning':'-2.,0.025,2.',
                     'Dimension1Name':'QDimension1',
                     'Dimension1Binning':'-2.5,0.025,2.5',
                     'Dimension2Name':'QDimension2',
                     'Dimension2Binning':'-5,5',
                     'Dimension3Name':'DeltaE',
                     'Dimension3Binning':'{},{}'.format(E-dE,E+dE),
                     'SymmetryOperations':'-3',
                     #'SymmetryOperations':'x,y,z;-x,y,z;x,y,-z;-x,y,-z',
                     'ConvertToChi':False,
                     'Plot_parameters':{'vmin':3e-4,'vmax':3e-3},#{'norm':LogNorm(vmin=3e-4,vmax=8e-3)},#vmin=1e-4,vmax=1e-1
                     'Axes_parameters':{'xrange':None,'yrange':None, 'xtitle':None, 'ytitle':None, 'title':'CNCS E=[{},{}]meV'.format(np.around(E-dE,2),E+dE), 'aspect_ratio':None, 'tight_axes':True, 'grid':True},
                     'Name':'HK0_slice_{0:.1f}meV_6p59'.format(E)+extra}
        dsl.append(description)

    # Energy vs intensity at (110) and (100)
    description={'QDimension0':'1,1,0',
                 'QDimension1':'-1,1,0',
                 'QDimension2':'0,0,1',
                 'Dimension0Name':'QDimension0',
                 'Dimension0Binning':'0.95,1.05',
                 'Dimension1Name':'QDimension1',
                 'Dimension1Binning':'-0.05,0.05',
                 'Dimension2Name':'QDimension2',
                 'Dimension2Binning':'-2,2',
                 'Dimension3Name':'DeltaE',
                 'Dimension3Binning':'-2,0.1,6',
                 'SymmetryOperations':'-3',
                 #'SymmetryOperations':'x,y,z;-x,y,z;x,y,-z;-x,y,-z',
                 'ConvertToChi':False,
                 'Plot_parameters':{'color':color,'marker':'o','mfc':color,'mec':color,'ls':' ','capsize':3,'label':f"{T:.2f} K"},#vmin=1e-4,vmax=1e-1
                 'Axes_parameters':{'xrange':None,'yrange':None, 'xtitle':None, 'ytitle':None, 'title':'CNCS (110) Ei=6p59 meV', 'aspect_ratio':None, 'tight_axes':True, 'grid':True},
                 'Name':'cutvsE_110_{0:.1f}meV_Ei6p59'.format(E)+extra}
    dsl.append(description)
    description={'QDimension0':'1,0,0',
                 'QDimension1':'-1,2,0',
                 'QDimension2':'0,0,1',
                 'Dimension0Name':'QDimension0',
                 'Dimension0Binning':'0.95,1.05',
                 'Dimension1Name':'QDimension1',
                 'Dimension1Binning':'-0.05,0.05',
                 'Dimension2Name':'QDimension2',
                 'Dimension2Binning':'-2,2',
                 'Dimension3Name':'DeltaE',
                 'Dimension3Binning':'-2,0.1,6',
                 'SymmetryOperations':'-3',
                 #'SymmetryOperations':'x,y,z;-x,y,z;x,y,-z;-x,y,-z',
                 'ConvertToChi':False,
                 'Plot_parameters':{'color':color,'marker':'o','mfc':color,'mec':color,'ls':' ','capsize':3,'label':f"{T:.2f} K"},#vmin=1e-4,vmax=1e-1
                 'Axes_parameters':{'xrange':None,'yrange':None, 'xtitle':None, 'ytitle':None, 'title':'CNCS (100) Ei=6p59 meV', 'aspect_ratio':None, 'tight_axes':True, 'grid':True},
                 'Name':'cutvsE_100_{0:.1f}meV_Ei6p59'.format(E)+extra}
    dsl.append(description)

    #Cuts along the (100) and (110) type directions
    description={'QDimension0':'1,0,0',
                 'QDimension1':'-1,2,0',
                 'QDimension2':'0,0,1',
                 'Dimension0Name':'QDimension0',
                 'Dimension0Binning':'-4,0.01,4',
                 'Dimension1Name':'QDimension1',
                 'Dimension1Binning':'-0.05,0.05',
                 'Dimension2Name':'QDimension2',
                 'Dimension2Binning':'-2,2',
                 'Dimension3Name':'DeltaE',
                 'Dimension3Binning':'-0.2,0.2',
                 'SymmetryOperations':'-3',
                 #'SymmetryOperations':'x,y,z;-x,y,z;x,y,-z;-x,y,-z',
                 'ConvertToChi':False,
                 'Plot_parameters':{'color':color,'marker':'o','mfc':color,'mec':color,'ls':' ','capsize':3,'label':f"{T:.2f} K"},#vmin=1e-4,vmax=1e-1
                 'Axes_parameters':{'xrange':None,'yrange':None, 'xtitle':None, 'ytitle':None, 'title':'CNCS (H00) Ei=6p59 meV', 'aspect_ratio':None, 'tight_axes':True, 'grid':True},
                 'Name':'Bragg_100cut_{0:.1f}K_Ei6p59'.format(T)+extra}
    dsl.append(description)
    return dsl
