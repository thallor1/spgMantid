import numpy as np
import matplotlib.pyplot as plt

def gen_spag_descs_mantid(a,b,c,alpha,beta,gamma,HKLpts,dQ0,dQ1,dQ2,Emin,Emax,dE,vmin,vmax,cmap,extra='',SymOps=None,norm_Q =[0,0,1],integrate_E=False):
    '''
    Function to generate dispersion plots (spaghetti plots) using Andrei's MANTID format
    Should work for any arbitrary lattice, but one limitation is that the paths must be orthogonal.
    Inputs:
    -a,b,c: lattice vector lengths in Angstrom
    -alpha,beta,gamma: lattice angles
    -HKLpts: List of HKL pts in format [[H0,K0,L0],[H1,K1,L1],...]
    -dQ1: Width of averaging window in plane of propagation between HKL points (Ang^-1)
    -dQ2: Width of averaging window perpendicular to propagaion (Ang^-1)
    -Emin: Minimum energy for slices
    -Emax: Maximum energy for slices
    -dE: Energy step for slices
    -vmin: Colormap Minimum
    -vmax: Colormap Maximum
    -cmap: Colormap string
    -extra: String to add to description.
    -SymOps: Symmetry operations to apply before taking slices, in MANTID notation.
    -norm_Q: Default normal vector for scattering plane if the normal vector can't be found.
    Returns :
        A list of descriptions that fits into the "define_slices" function like so:

        def define_data_slices(extra=''):
            dsl = []
            description1 = {...} #some generic slice
            dsl.append(description1)
            spag_descs = gen_spac_descs_mantid(...) #List of spag plot descs
            for desc in spag_descs:
                dsl.append(desc)
            return dsl
    '''
    alpha_rad,beta_rad,gamma_rad = alpha*np.pi/180.0,beta*np.pi/180.0,gamma*np.pi/180.0
    avec = np.array([a,0,0])
    bvec = np.array([b*np.cos(gamma_rad),b*np.sin(gamma_rad),0])
    cvec = np.array([c*np.cos(beta_rad),\
                    c*(np.cos(alpha_rad)-np.cos(beta_rad)*np.cos(gamma_rad))/np.sin(gamma_rad),\
                    c*np.sqrt(1.0-np.cos(beta_rad)**2 - ((np.cos(alpha_rad)-np.cos(beta_rad)*np.cos(gamma_rad))/np.sin(gamma_rad))**2)])
    Vrecip = np.dot(avec,np.cross(bvec,cvec))
    astar = 2.0*np.pi*np.cross(bvec,cvec)/Vrecip
    bstar = 2.0*np.pi*np.cross(cvec,avec)/Vrecip
    cstar = 2.0*np.pi*np.cross(avec,bvec)/Vrecip
    hmag = np.linalg.norm(astar)
    kmag = np.linalg.norm(bstar)
    lmag = np.linalg.norm(cstar) #Get the momentum transfer of each index
    #Get the vectors connecting each HKL point
    HKLvecs = []
    for i in range(len(HKLpts)-1):
        pt0=np.array(HKLpts[i])
        pt1=np.array(HKLpts[i+1])
        hklvec = pt1-pt0
        HKLvecs.append(hklvec)

    #Plot this path in Q-space along with the first brillioun zone
    BZ_pts_hkl=[np.array(1.0/3.0*astar+1.0/3.0*bstar)[0:2]]
    for i in range(6):
        R = np.array([[np.cos(np.pi/3),-np.sin(np.pi/3)],[np.sin(np.pi/3),np.cos(np.pi/3)]])
        newpt = np.matmul(R,np.array(BZ_pts_hkl[-1]))
        BZ_pts_hkl.append(list(newpt))
    BZ_pts_hkl=np.array(BZ_pts_hkl)
    fig,ax = plt.subplots(1,1,figsize=(3.54,3),subplot_kw={'aspect':'equal'})
    Qpt_list = []
    Q3Dpt_list = []
    HKLQ_list = []
    HKLQ_3D_list = []
    Qpath_lengths = []
    for i in range(len(HKLpts)):
        hkl = HKLpts[i]
        q = hkl[0]*astar[0:2]+hkl[1]*bstar[0:2]
        q3d = hkl[0]*astar+hkl[1]*bstar+hkl[2]*cstar
        Qpt_list.append(q)
        Q3Dpt_list.append(q3d)
        if i<max(range(len(HKLpts))):
            vec = HKLvecs[i]
            vecQ = vec[0]*astar + vec[1]*bstar
            vecQ3D = vec[0]*astar+vec[1]*bstar+vec[2]*cstar
            HKLQ_list.append(vecQ)
            HKLQ_3D_list.append(vecQ3D)
            Qpath_lengths.append(np.linalg.norm(vecQ3D))

    #Get the two perpendicular vectors for each point
    Qdim0_list = []
    Qdim1_list = []
    Qdim2_list = []
    Qmid_list = []
    
    for i in range(len(HKLvecs)):
        #Assume that Qdim2 is the cross product of an adjacent path and the current one.
        if i<len(HKLvecs)-1:
            #Not at the final path
            currpath = HKLvecs[i]
            nextpath = HKLvecs[i+1]
        else:
            #If at final path, simply use the previous path instead.
            currpath = HKLvecs[i]
            nextpath = HKLvecs[i-1]
        delQ = currpath[0]*astar+currpath[1]*bstar+currpath[2]*cstar
        delQ_norm = delQ/np.linalg.norm(delQ)

        delQ_next= nextpath[0]*astar+nextpath[1]*bstar+nextpath[2]*cstar
        perpdir2 = np.cross(delQ,delQ_next) #Generally the (00L) direction for 2D BZs
        hkl = HKLpts[i]
        q = Qpt_list[i]
        Q0 = Qpt_list[i]
        perpdir2=perpdir2#/np.linalg.norm(perpdir2) #Qdimension2
        if np.linalg.norm(perpdir2)<1e-4:
            #Coplanar point input, default to the input vector. 
            perpdir2 = np.array(norm_Q)
        orig_dir = currpath#/np.linalg.norm(currpath)
        perpdir1=np.cross(perpdir2,delQ)

        perpdir1=perpdir1#/np.linalg.norm(perpdir1) #Qdimension1
        #Now show the physical width of integration instead
        perpdir1_window = perpdir1*dQ1
        perpdir2_window = perpdir2*dQ2
        Qmid = Q0+delQ[0:2]/2.0
        Qmid_list.append(Qmid)
        #All three normalized direction appended to respective lists.
        Qdim0_list.append(delQ)
        Qdim1_list.append(perpdir1)
        Qdim2_list.append(perpdir2)
    Qdimension0_list = []
    Qdimension1_list = []
    Qdimension2_list = []
    Qdimension0_strs = []
    Qdimension1_strs = []
    Qdimension2_strs = []
    Qdimension0_binstrs = []
    Qdimension1_binstrs = []
    Qdimension2_binstrs = []
    energy_binstrs = []
    #All HKL points, the vectors connecting them, and their perpendicular vectors are now stored in Ang^-1.
    #Need to project onto the different Qdimensions now
    for i in range(len(HKLvecs)):
        #QDimension0 is simply defined by the first HKL path
        Qdim0_lab = Qdim0_list[i] #In dimension of Qdimension 0, along slice
        Qdim1_lab = Qdim1_list[i] #In direction of Qdimension 1, perp to slice in plane
        Qdim2_lab = Qdim2_list[i] #In direction of Qdimension 2, perp to slice out of plane
        # We use some linear algebra to project each vector into the HKL frame.
        BasisM = np.array([astar,bstar,cstar]).T
        M0 = np.linalg.inv(np.matmul(BasisM.T,BasisM))
        M1 = np.matmul(M0,BasisM.T)
        Y0 = np.matmul(M1,Qdim0_lab)
        Y1 = np.matmul(M1,Qdim1_lab)
        Y2 = np.matmul(M1,Qdim2_lab)
        # These vectors Y0, Y1, and Y2 are the HKL vectors we have sought.
        Qdimension0_list.append(Y0)
        Qdimension1_list.append(Y1)
        Qdimension2_list.append(Y2)
        #print(f"Basis vector 0 = {Y0}")
        #print(f"Basis vector 1 = {Y1}")
        #print(f"Basis vector 2 = {Y2}")
        #Now that the HKL vectors have found, find extents in the basis of these vectors
        BasisMy = np.array([Qdim0_lab,Qdim1_lab,Qdim2_lab]).T
        M0y = np.linalg.inv(np.matmul(BasisMy.T,BasisMy))
        M1y = np.matmul(M0y,BasisMy.T)
        init_pt = Q3Dpt_list[i]
        next_pt = Q3Dpt_list[i+1]
        delQpt = next_pt-init_pt
        delQ_ybasis = np.matmul(M1y,delQpt)
        #Find the initial point in the new basis, this does not work for the gamma point.
        Q0 = np.array([0.0,0.0,0.0])
        Qpt = Q3Dpt_list[i+1]
        Qybasis = np.matmul(M1y,Qpt)
        QyCart = Qybasis[0]*Qdim0_lab + Qybasis[1]*Qdim1_lab+Qybasis[2]*Qdim2_lab
        #Now, Qdimension 0 goes from init_Q to init_Q+1,
        #  Qdim1 and Qdim 1 now need extents in the Qybasis
        Qdim0_len = np.linalg.norm(Qdim0_lab)
        dim0_step = round(dQ0/Qdim0_len,4)
        Qdim1_len = np.linalg.norm(Qdim1_lab)
        Qdim2_len = np.linalg.norm(Qdim2_lab)
        frac_Qdim1 = dQ1 / Qdim1_len
        frac_Qdim2 = dQ2 / Qdim2_len
        Qdim1_min = Qybasis[1]-frac_Qdim1/2.0
        Qdim1_max = Qybasis[1]+frac_Qdim1/2.0
        Qdim2_min = Qybasis[2]-frac_Qdim2/2.0
        Qdim2_max = Qybasis[2]+frac_Qdim2/2.0
        #Plot each Q1 vector to make sure it makes sense
        Q1vec =  Qdim1_max*Qdim1_lab - Qdim1_min*Qdim1_lab
        initpt_plt = Qmid_list[i]-Q1vec[0:2]
        ptplt_f = Qmid_list[i]+Q1vec[0:2]
        ptsx = [initpt_plt[0],ptplt_f[0]]
        ptsy = [initpt_plt[1],ptplt_f[1]]

        #print(f"Qdim1 range in new basis = {[Qdim1_min,Qdim1_max]}")
        #print(f"Qdim1 range in cartesian = {[Qdim1_min*Qdim1_lab,Qdim1_max*Qdim1_lab]}")
        #We may now prepare each string!
        Qdimension0_strs.append(f"{Y0[0]:.3f},{Y0[1]:.3f},{Y0[2]:.3f}")
        Qdimension1_strs.append(f"{Y1[0]:.3f},{Y1[1]:.3f},{Y1[2]:.3f}")
        Qdimension2_strs.append(f"{Y2[0]:.3f},{Y2[1]:.3f},{Y2[2]:.3f}")
        Qdimension0_binstrs.append(f"{Qybasis[0]-1:.3f},{dim0_step:.3f},{Qybasis[0]:.3f}")#Slice direction
        Qdimension1_binstrs.append(f"{Qdim1_min:.3f},{Qdim1_max:.3f}")#Integrated
        Qdimension2_binstrs.append(f"{Qdim2_min:.3f},{Qdim2_max:.3f}")#integrated
        #Now also prepare the energy str
        if integrate_E is False:
            energy_binstrs.append(f"{Emin:.4f},{dE:.4f},{Emax:.4f}")
        else:
            #User desires a cut binned in energy along this path rather than slice.
            energy_binstrs.append(f"{Emin:.4f},{Emax:.2f}")

    #Now we can finally build the description objects
    out_dsl = []
    for i in range(len(HKLvecs)):
        description={'QDimension0':Qdimension0_strs[i],
                     'QDimension1':Qdimension1_strs[i],
                     'QDimension2':Qdimension2_strs[i],
                     'Dimension0Name':'QDimension0',
                     'Dimension0Binning':Qdimension0_binstrs[i],
                     'Dimension1Name':'QDimension1',
                     'Dimension1Binning':Qdimension1_binstrs[i],
                     'Dimension2Name':'QDimension2',
                     'Dimension2Binning':Qdimension2_binstrs[i],
                     'Dimension3Name':'DeltaE',
                     'Dimension3Binning':energy_binstrs[i],
                     'SymmetryOperations':SymOps,
                     #'SymmetryOperations':'x,y,z;-x,y,z;x,y,-z;-x,y,-z',
                     'ConvertToChi':False,
                     'Plot_parameters':{'vmin':vmin,'vmax':vmax,'cmap':cmap,'rasterized':True},#vmin=1e-4,vmax=1e-1
                     'Axes_parameters':{'xrange':None,'yrange':None, 'xtitle':None, 'ytitle':None, 'title':None, 'aspect_ratio':None, \
                            'tight_axes':True, 'grid':True},
                     'Name':'Disp_plot_'+f"({HKLpts[i][0]:.3f},{HKLpts[i][1]:.3f},{HKLpts[i][2]:.3f})_to_({HKLpts[i+1][0]:.3f},{HKLpts[i+1][1]:.3f},{HKLpts[i+1][2]:.3f})_slice"+extra,\
                     'Qlength':Qpath_lengths[i]}
        out_dsl.append(description)
    return out_dsl