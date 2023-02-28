## Function for the weighted least-squares background calculation of T-dependent INS data. 

import numpy as np
import statsmodels.api as sm 
from patsy import dmatrices 
import statsmodels.formula.api as smf 
from mantid import plots
import pandas
from reduce_data_to_MDE import *
from slice_utils import *

def dim2array(d,center=True):
    """
    Create a numpy array containing bin centers along the dimension d
    input: d - IMDDimension
    return: numpy array, from min+st/2 to max-st/2 with step st  
    """
    dmin=d.getMinimum()
    dmax=d.getMaximum()
    dstep=d.getX(1)-d.getX(0)
    if center:
        return np.arange(dmin+dstep/2,dmax,dstep)
    else:
        return np.linspace(dmin,dmax,d.getNBins()+1)

def pre(delta):
	return (1.0-delta)/2.0

def detailedbalance_wls_singleQ(energies,cutmatrix,errmatrix,temperatures):
	'''
	Provided energies, intensities, errors, and temperatures from INS data,
	returns a temperature indepdnent background found by a weighted ordinary
	least-squares approach. 
	'''
	#Outputs will be extracted background and SQW for all energies. 
	I_mat_list = []
	Err_mat_list = []
	bkg_I = np.copy(cutmatrix[-1,:])
	bkg_Err = np.copy(errmatrix[-1,:])
	err_ct=0
	#First restructure the data into a pandas dframe 

	for i,E in enumerate(energies):
		Temps = [] #Temperatures 
		I_list=[] #Measured intensities
		Err_list = [] # Measured errors
		prefactor_list = [] #Overall prefactors
		delta_list = [] #Flag to denote plus or minus transfer
		omega_list = [] #Energy transfer
		abkgp = [] #prefactor for postive transfer
		abkgm = [] #negative transfer
		s_str_list = []
		s_arr = []
		cols = ['T','I','Err','a','delta','omega','A_bkgp','A_bkgm']
		out_dict={}
		if E<0: 
			#Skip the negative transfers. 
			continue 
		else: 
			#Generate a column for each temperature. 
			for j,T in enumerate(temperatures):
				I = cutmatrix[j,i] #Intensity at positive transfer
				Err = errmatrix[j,i] #Error at postivie transfer
				Eminus_i = np.argmin(np.abs(E+energies))
				Em = energies[Eminus_i] #Matching negative transfer
				Im = cutmatrix[j,Eminus_i] #Negative transfer intensity
				Errm = errmatrix[j,Eminus_i] #Postive transfer intensity 
				I_list.append(I)
				Err_list.append(Err)
				#Account for zero counts in the negative channel 
				if Im==0 or np.isnan(Im):
					Im = I / 1e5
					Errm = Err 
				#Add both to the overall list . 
				I_list.append(Im)
				Err_list.append(Errm)
				beta = 1.0/(T*8.62e-2)
				sqw_pre_minus = np.exp(Em*beta)
				sqw_pre_plus = 1.0 
				prefactor_list.append(sqw_pre_plus) #Bose-population plus
				prefactor_list.append(sqw_pre_minus) #Bose-population minus
				Temps.append(T) #Temperature is the same for both points
				Temps.append(T) 
				delta_list.append(1.0)
				delta_list.append(-1.0)
				omega_list.append(E)
				omega_list.append(Em)
				abkgp.append(pre(-1))
				abkgm.append(pre(1))
				abkgp.append(pre(1))
				abkgm.append(pre(-1))
				cols.append('S_'+f'T_{temperatures[j]:.3f}K'.replace('.','p'))
				s_str_list.append('S_'+f"T_{temperatures[j]:.3f}K".replace('.','p'))
				s_list = [0]*2*len(temperatures)
				s_list[2*j] = sqw_pre_plus 
				s_list[2*j+1]=sqw_pre_minus
				s_arr.append(s_list)
		#Now that the arrays are prepared, we begin the weighted wls formalism 
		if np.sum(np.isnan(I_list))>0 or np.sum(np.isnan(Err_list))>0:
			for i in range(len(cols)):
				out_dict[cols[i]]=[np.nan,np.nan]
		else:
			try: 
				matrix = np.array([Temps,I_list,Err_list,prefactor_list,delta_list,omega_list,\
					abkgp,abkgm,*s_arr]).T
				#Store in pandas dframe 
				df = pandas.DataFrame(matrix,columns=cols)
				weights = 1.0 / np.array(Err_list)
				
				#Write out our matrices using patsy, need all temperatures. -1 gets rid of default constant. 
				s_string = '+'.join([''+s_str_list[i] for i in range(len(s_str_list))])
				eq_string = 'I~A_bkgp+A_bkgm+'+s_string+'-1'
				res = smf.wls(formula=eq_string,data=df,weights=weights)
				#Columns are obs intensity 
				tab = res.fit().summary().tables[1] 
				#Collect results into dictionary 
				cell_bkgp = tab.data[1]
				cell_bkgm = tab.data[2]
				bkgp_val = float(cell_bkgp[1])
				bkgp_stderr = np.sqrt(float(cell_bkgp[2]))
				bkgm_val = float(cell_bkgm[1])
				bkgm_stderr = np.sqrt(float(cell_bkgm[2]))
				for k,col in enumerate(cols):
					ind = k+6 
					if ind>(len(cols)-1):
						break 
					col_label = cols[ind] 
					param_val = float(tab.data[k+1][1])
					param_err = np.abs(float(tab.data[k+1][2]))
					out_dict[col_label]=[param_val,param_err]
			except Exception as error:
				print(f"Warning at omega={E} meV")
				print(error)
				print(df)
				err_ct+=1 
				#Sometimes errors occur due to convergence failures 
				t_index = 0 
				for k,col in enumerate(cols):
					ind = k+6 
					if ind>(len(cols)-1):
						break 
					col_label = cols[ind]
					if 'bkg' not in col_label:
						param_val = I_list[t_index]
						param_err = Err_list[t_index]
						t_index+=1
					else:
						param_val = 1e-8 
						param_err = Err_list[t_index]*1.0 
					out_dict[col_label]=[param_val,param_err]
		#for this energy we now have the correct values for background and SQW for each temp 
		#Update the matrix to reflect this. 
		for k in range(len(temperatures)):
			I_mat = cutmatrix[k,:]
			Err_mat = errmatrix[k,:]
			I_mat[i]=out_dict[cols[k+8]][0]
			err_calc = np.abs(out_dict[cols[k+8]][1])
			orig_err = Err_mat[i]
			if err_calc<orig_err:
				#This is unfeasible, default to expt 
				err_cal = orig_err 
			Err_mat[i]=err_calc 
			cutmatrix[k,:]=I_mat 
			errmatrix[k,:]=Err_mat 
		#Update the background on both positive and negative transfer sides 
		bkg_I[i] = out_dict['A_bkgp'][0]
		bkg_I[Eminus_i] = out_dict['A_bkgm'][0]
		bkg_Err[i] = out_dict['A_bkgp'][1]
		bkg_Err[Eminus_i] = out_dict['A_bkgm'][1]
	#We can now return background and sqw for each temperature. 
	return bkg_I,bkg_Err,cutmatrix,errmatrix 

def detailedBalance_MDSlices(slicenames,temperatures,OutputSuffix='_DBBKG'):
	'''
	Provided a list of names of slices, iterates through every point in Q 
	and calculates both a temperature independent background and SQW for each temperature 
	'''

	#The WLS detailed balance function takes a matrix of dimension [t,i] where t 
	# is the number of temperatures and i is the energy dimension. 

	#First check if all of the workspaces are of the same size. 
	md0 = mtd[slicenames[0]]
	prevshape = np.shape(md0.getSignalArray())
	#Not all slices have the same number of Q points. 
	Qarr_list = []
	Earr_list = []
	for name in slicenames: 
		md = mtd[name]
		shape = np.shape(md.getSignalArray())
		if shape!=prevshape:
			print("ERROR: Slice {name} is not of correct shape. ")
			print("Check that your slice definitions are correct. ")
			break 
		dims = md.getNonIntegratedDimensions()
		Qarr,Earr = dim2array(dims[0]),dim2array(dims[1])
		Qarr_list.append(Qarr)
		Earr_list.append(Earr)
	#Make copies of each for output. 
	outmd_list = []
	for name in slicenames:
		md = mtd[name]
		mdout = CloneWorkspace(md,OutputWorkspace=name+'_SQW_calculated')
		outmd_list.append(mdout)
	bkgout = CloneWorkspace(md0,OutputWorkspace=name+'_DBBKG_calculated')
	#Iterate through the Q-dimension to generate the input to the main function
	for ii,Qarr in enumerate(Qarr_list):
		e = Earr_list[ii]
		for i,q in enumerate(Qarr):
			ecutmatrix = np.zeros((len(temperatures),len(e)))
			errcutmatrix = np.zeros(np.shape(ecutmatrix))
			for j,name in enumerate(slicenames):
				md = mtd[name]
				I = np.copy(md.getSignalArray())
				Err = np.sqrt(np.copy(md.getErrorSquaredArray()))
				ecut = I[i,0,0,:]
				errcut = Err[i,0,0,:]
				ecutmatrix[j,:]=ecut 
				errcutmatrix[j,:]=errcut 
			#Now calculate the background, sqw's. 
			bkg_I,bkg_Err,sqwmatrix,errmatrix = detailedbalance_wls_singleQ(e,ecutmatrix,errcutmatrix,temperatures)
			#Edit the output MDworkspaces 
			for ii,name in enumerate(slicenames):
				md = mtd[name+'_SQW_calculated']
				Isqw = np.copy(md.getSignalArray())
				Errsqw = np.sqrt(np.copy(md.getErrorSquaredArray()))

				Isqw[i,0,0,:]=sqwmatrix[ii,:]
				Errsqw[i,0,0,:]=errmatrix[ii,:] 
				md.setSignalArray(Isqw)
				md.setErrorSquaredArray(Errsqw**2)
			#Also the background workspace
			md = mtd[name+'_DBBKG_calculated']
			Ibkg= np.copy(md.getSignalArray())
			Errbkg = np.sqrt(np.copy(md.getErrorSquaredArray()))
			Ibkg[i,:]=bkg_I
			Errbkg[i,:]=bkg_Err
			md.setSignalArray(Ibkg)
			md.setErrorSquaredArray(Errbkg**2)

		#Return the md list and the background MD
		bkgmd = mtd[name+'_DBBKG_calculated']
	return outmd_list, bkgmd 