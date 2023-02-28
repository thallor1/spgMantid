import os
import numpy as np

########################################################################################################
# Define list of dictionaries, each describing data (run) sets to be combined in a single mde workspace
# Authors: A. Savici, I. Zaliznyak, March 2019.
########################################################################################################
def define_data_set(**kwargs):
    shared_folder='/SNS/CNCS/IPTS-29413/shared/autoreduce/'
    raw_data_folder='/SNS/CNCS/IPTS-29413/nexus/'
    mde_folder='/SNS/CNCS/IPTS-29413/shared/MDE/'

    data_set_list=[]
    # T=0.25K Ei=3.32meV
    data_set_12meV={'Runs':range(479065,479423+1),          #List of runs, or list of lists of runs that are added together
              'BackgroundRuns':None,   #range(297325,297337)Options: None;list of runs that are added together
              'RawDataFolder':raw_data_folder,      #Options:raw_data_folder string
              'RawDataFolderBackground':None,       #Options:None (same as the raw data); bknd_raw_data_folder string
              'BackgroundScaling':1,             #Options: None (same as 1); scaling factor
              'MdeFolder':mde_folder,               #Options:mde_folder string
              'MdeName':'merged_mde_bcvo_12p0meV_0p25K',   #Options:mde_name string
              'BackgroundMdeName':None,      #Options:None;bg_mde_name string
              'MaskingDataFile':shared_folder+'van_449014.nxs',         #Options:None;data_file_name
              'NormalizationDataFile':shared_folder+'van_449014.nxs',   #Options:None;data_file_name
              'SampleLogVariables':{'OmegaMotorName':None,'Temperature':0.25,'MagneticField':0.0},   #Options:None;LogVariableName;number
              'UBSetup':{'a':5.0180,'b':5.0180,'c':23.3563,'alpha':90,'beta':90,'gamma':120,'u':'1.05,-0.05,0','v':'-0.95,1.05,0'},
               #Data reduction options
              'Ei':12.0,                            #Options: None;Ei_somehow_determined
              'T0':None,                            #Options: None;T0_determined_from_mantid
              'BadPulsesThreshold':None,            #Options: None;bg_pulses_threshold value
              'TimeIndepBackgroundWindow':'Default',    #Options: None;'Default';[Tib_min,Tib_max]
              'E_min':None,                         #Options: None;Emin if None the value is -0.95*Ei
              'E_max':None,                         #Options: None;Emax if None the value is 0.95*Ei
              'AdditionalDimensions':None,          #Options: None;list of triplets ("name", min, max)
               #Polarized data options
              'PolarizationState':None,             #Options:None;'SF_Px';'NSF_Px';'SF_Py';'NSF_Py';'SF_Pz';'NSF_Pz'
              'FlippingRatio':None,                 #Options:None;'14';'6.5+2.8*cos((omega+3.7)*pi/180),omega'
              'PolarizingSupermirrorDeflectionAdjustment':None, #Options:None;deflection_angle
              'EfCorrectionFunction':None,          #Options:None;'HYSPEC_default_correction';Custom_Ef_Correction_Function_Name
              }
    data_set_list.append(data_set_12meV)

    data_set_3p32meV={'Runs':list(range(479424,479746+1))+list(range(479749,479825+1)),          #List of runs, or list of lists of runs that are added together
              'BackgroundRuns':None,   #range(297325,297337)Options: None;list of runs that are added together
              'RawDataFolder':raw_data_folder,      #Options:raw_data_folder string
              'RawDataFolderBackground':None,       #Options:None (same as the raw data); bknd_raw_data_folder string
              'BackgroundScaling':1,             #Options: None (same as 1); scaling factor
              'MdeFolder':mde_folder,               #Options:mde_folder string
              'MdeName':'merged_mde_bcvo_3p32meV_0p25K',   #Options:mde_name string
              'BackgroundMdeName':None,      #Options:None;bg_mde_name string
              'MaskingDataFile':shared_folder+'van_449014.nxs',         #Options:None;data_file_name
              'NormalizationDataFile':shared_folder+'van_449014.nxs',   #Options:None;data_file_name
              'SampleLogVariables':{'OmegaMotorName':None,'Temperature':0.25,'MagneticField':0.0},   #Options:None;LogVariableName;number
              'UBSetup':{'a':5.0180,'b':5.0180,'c':23.3563,'alpha':90,'beta':90,'gamma':120,'u':'1.05,-0.05,0','v':'-0.95,1.05,0'},
               #Data reduction options
              'Ei':3.32,                            #Options: None;Ei_somehow_determined
              'T0':None,                            #Options: None;T0_determined_from_mantid
              'BadPulsesThreshold':None,            #Options: None;bg_pulses_threshold value
              'TimeIndepBackgroundWindow':'Default',    #Options: None;'Default';[Tib_min,Tib_max]
              'E_min':None,                         #Options: None;Emin if None the value is -0.95*Ei
              'E_max':None,                         #Options: None;Emax if None the value is 0.95*Ei
              'AdditionalDimensions':None,          #Options: None;list of triplets ("name", min, max)
               #Polarized data options
              'PolarizationState':None,             #Options:None;'SF_Px';'NSF_Px';'SF_Py';'NSF_Py';'SF_Pz';'NSF_Pz'
              'FlippingRatio':None,                 #Options:None;'14';'6.5+2.8*cos((omega+3.7)*pi/180),omega'
              'PolarizingSupermirrorDeflectionAdjustment':None, #Options:None;deflection_angle
              'EfCorrectionFunction':None,          #Options:None;'HYSPEC_default_correction';Custom_Ef_Correction_Function_Name
              }
    data_set_list.append(data_set_3p32meV)

    data_set_6p59meV={'Runs':range(479826,479950+1),          #List of runs, or list of lists of runs that are added together
              'BackgroundRuns':None,   #range(297325,297337)Options: None;list of runs that are added together
              'RawDataFolder':raw_data_folder,      #Options:raw_data_folder string
              'RawDataFolderBackground':None,       #Options:None (same as the raw data); bknd_raw_data_folder string
              'BackgroundScaling':1,             #Options: None (same as 1); scaling factor
              'MdeFolder':mde_folder,               #Options:mde_folder string
              'MdeName':'merged_mde_bcvo_6p59_0p25K',   #Options:mde_name string
              'BackgroundMdeName':None,      #Options:None;bg_mde_name string
              'MaskingDataFile':shared_folder+'van_449014.nxs',         #Options:None;data_file_name
              'NormalizationDataFile':shared_folder+'van_449014.nxs',   #Options:None;data_file_name
              'SampleLogVariables':{'OmegaMotorName':None,'Temperature':0.25,'MagneticField':0.0},   #Options:None;LogVariableName;number
              'UBSetup':{'a':5.0180,'b':5.0180,'c':23.3563,'alpha':90,'beta':90,'gamma':120,'u':'1.05,-0.05,0','v':'-0.95,1.05,0'},
               #Data reduction options
              'Ei':6.59,                            #Options: None;Ei_somehow_determined
              'T0':None,                            #Options: None;T0_determined_from_mantid
              'BadPulsesThreshold':None,            #Options: None;bg_pulses_threshold value
              'TimeIndepBackgroundWindow':'Default',    #Options: None;'Default';[Tib_min,Tib_max]
              'E_min':None,                         #Options: None;Emin if None the value is -0.95*Ei
              'E_max':None,                         #Options: None;Emax if None the value is 0.95*Ei
              'AdditionalDimensions':None,          #Options: None;list of triplets ("name", min, max)
               #Polarized data options
              'PolarizationState':None,             #Options:None;'SF_Px';'NSF_Px';'SF_Py';'NSF_Py';'SF_Pz';'NSF_Pz'
              'FlippingRatio':None,                 #Options:None;'14';'6.5+2.8*cos((omega+3.7)*pi/180),omega'
              'PolarizingSupermirrorDeflectionAdjustment':None, #Options:None;deflection_angle
              'EfCorrectionFunction':None,          #Options:None;'HYSPEC_default_correction';Custom_Ef_Correction_Function_Name
              }
    data_set_list.append(data_set_6p59meV)

    data_set_6p59meV_I={'Runs':range(479954,480133+1),    #List of runs, or list of lists of runs that are added together
              'BackgroundRuns':None,   #range(297325,297337)Options: None;list of runs that are added together
              'RawDataFolder':raw_data_folder,      #Options:raw_data_folder string
              'RawDataFolderBackground':None,       #Options:None (same as the raw data); bknd_raw_data_folder string
              'BackgroundScaling':1,             #Options: None (same as 1); scaling factor
              'MdeFolder':mde_folder,               #Options:mde_folder string
              'MdeName':'merged_mde_bcvo_6p59_I_0p25K',   #Options:mde_name string
              'BackgroundMdeName':None,      #Options:None;bg_mde_name string
              'MaskingDataFile':shared_folder+'van_449014.nxs',         #Options:None;data_file_name
              'NormalizationDataFile':shared_folder+'van_449014.nxs',   #Options:None;data_file_name
              'SampleLogVariables':{'OmegaMotorName':None,'Temperature':0.25,'MagneticField':0.0},   #Options:None;LogVariableName;number
              'UBSetup':{'a':5.0180,'b':5.0180,'c':23.3563,'alpha':90,'beta':90,'gamma':120,'u':'1.05,-0.05,0','v':'-0.95,1.05,0'},
               #Data reduction options
              'Ei':6.59,                            #Options: None;Ei_somehow_determined
              'T0':None,                            #Options: None;T0_determined_from_mantid
              'BadPulsesThreshold':None,            #Options: None;bg_pulses_threshold value
              'TimeIndepBackgroundWindow':'Default',    #Options: None;'Default';[Tib_min,Tib_max]
              'E_min':None,                         #Options: None;Emin if None the value is -0.95*Ei
              'E_max':None,                         #Options: None;Emax if None the value is 0.95*Ei
              'AdditionalDimensions':None,          #Options: None;list of triplets ("name", min, max)
               #Polarized data options
              'PolarizationState':None,             #Options:None;'SF_Px';'NSF_Px';'SF_Py';'NSF_Py';'SF_Pz';'NSF_Pz'
              'FlippingRatio':None,                 #Options:None;'14';'6.5+2.8*cos((omega+3.7)*pi/180),omega'
              'PolarizingSupermirrorDeflectionAdjustment':None, #Options:None;deflection_angle
              'EfCorrectionFunction':None,          #Options:None;'HYSPEC_default_correction';Custom_Ef_Correction_Function_Name
              }
    data_set_list.append(data_set_6p59meV_I)
    data_set_6p59meV_I_920mK={'Runs':range(480134,480284+1),    #List of runs, or list of lists of runs that are added together
              'BackgroundRuns':None,   #range(297325,297337)Options: None;list of runs that are added together
              'RawDataFolder':raw_data_folder,      #Options:raw_data_folder string
              'RawDataFolderBackground':None,       #Options:None (same as the raw data); bknd_raw_data_folder string
              'BackgroundScaling':1,             #Options: None (same as 1); scaling factor
              'MdeFolder':mde_folder,               #Options:mde_folder string
              'MdeName':'merged_mde_bcvo_6p59_I_0p92K',   #Options:mde_name string
              'BackgroundMdeName':None,      #Options:None;bg_mde_name string
              'MaskingDataFile':shared_folder+'van_449014.nxs',         #Options:None;data_file_name
              'NormalizationDataFile':shared_folder+'van_449014.nxs',   #Options:None;data_file_name
              'SampleLogVariables':{'OmegaMotorName':None,'Temperature':0.92,'MagneticField':0.0},   #Options:None;LogVariableName;number
              'UBSetup':{'a':5.0180,'b':5.0180,'c':23.3563,'alpha':90,'beta':90,'gamma':120,'u':'1.05,-0.05,0','v':'-0.95,1.05,0'},
               #Data reduction options
              'Ei':6.59,                            #Options: None;Ei_somehow_determined
              'T0':None,                            #Options: None;T0_determined_from_mantid
              'BadPulsesThreshold':None,            #Options: None;bg_pulses_threshold value
              'TimeIndepBackgroundWindow':'Default',    #Options: None;'Default';[Tib_min,Tib_max]
              'E_min':None,                         #Options: None;Emin if None the value is -0.95*Ei
              'E_max':None,                         #Options: None;Emax if None the value is 0.95*Ei
              'AdditionalDimensions':None,          #Options: None;list of triplets ("name", min, max)
               #Polarized data options
              'PolarizationState':None,             #Options:None;'SF_Px';'NSF_Px';'SF_Py';'NSF_Py';'SF_Pz';'NSF_Pz'
              'FlippingRatio':None,                 #Options:None;'14';'6.5+2.8*cos((omega+3.7)*pi/180),omega'
              'PolarizingSupermirrorDeflectionAdjustment':None, #Options:None;deflection_angle
              'EfCorrectionFunction':None,          #Options:None;'HYSPEC_default_correction';Custom_Ef_Correction_Function_Name
              }
    data_set_list.append(data_set_6p59meV_I_920mK)

    data_set_6p59meV_I_2K={'Runs':range(480285,480358+1),    #List of runs, or list of lists of runs that are added together
              'BackgroundRuns':None,   #range(297325,297337)Options: None;list of runs that are added together
              'RawDataFolder':raw_data_folder,      #Options:raw_data_folder string
              'RawDataFolderBackground':None,       #Options:None (same as the raw data); bknd_raw_data_folder string
              'BackgroundScaling':1,             #Options: None (same as 1); scaling factor
              'MdeFolder':mde_folder,               #Options:mde_folder string
              'MdeName':'merged_mde_bcvo_6p59_I_2K',   #Options:mde_name string
              'BackgroundMdeName':None,      #Options:None;bg_mde_name string
              'MaskingDataFile':shared_folder+'van_449014.nxs',         #Options:None;data_file_name
              'NormalizationDataFile':shared_folder+'van_449014.nxs',   #Options:None;data_file_name
              'SampleLogVariables':{'OmegaMotorName':None,'Temperature':2.0,'MagneticField':0.0},   #Options:None;LogVariableName;number
              'UBSetup':{'a':5.0180,'b':5.0180,'c':23.3563,'alpha':90,'beta':90,'gamma':120,'u':'1.05,-0.05,0','v':'-0.95,1.05,0'},
               #Data reduction options
              'Ei':6.59,                            #Options: None;Ei_somehow_determined
              'T0':None,                            #Options: None;T0_determined_from_mantid
              'BadPulsesThreshold':None,            #Options: None;bg_pulses_threshold value
              'TimeIndepBackgroundWindow':'Default',    #Options: None;'Default';[Tib_min,Tib_max]
              'E_min':None,                         #Options: None;Emin if None the value is -0.95*Ei
              'E_max':None,                         #Options: None;Emax if None the value is 0.95*Ei
              'AdditionalDimensions':None,          #Options: None;list of triplets ("name", min, max)
               #Polarized data options
              'PolarizationState':None,             #Options:None;'SF_Px';'NSF_Px';'SF_Py';'NSF_Py';'SF_Pz';'NSF_Pz'
              'FlippingRatio':None,                 #Options:None;'14';'6.5+2.8*cos((omega+3.7)*pi/180),omega'
              'PolarizingSupermirrorDeflectionAdjustment':None, #Options:None;deflection_angle
              'EfCorrectionFunction':None,          #Options:None;'HYSPEC_default_correction';Custom_Ef_Correction_Function_Name
              }
    data_set_list.append(data_set_6p59meV_I_2K)

    data_set_6p59meV_I_5K={'Runs':range(480359,480419+1),    #List of runs, or list of lists of runs that are added together
              'BackgroundRuns':None,   #range(297325,297337)Options: None;list of runs that are added together
              'RawDataFolder':raw_data_folder,      #Options:raw_data_folder string
              'RawDataFolderBackground':None,       #Options:None (same as the raw data); bknd_raw_data_folder string
              'BackgroundScaling':1,             #Options: None (same as 1); scaling factor
              'MdeFolder':mde_folder,               #Options:mde_folder string
              'MdeName':'merged_mde_bcvo_6p59_I_5K',   #Options:mde_name string
              'BackgroundMdeName':None,      #Options:None;bg_mde_name string
              'MaskingDataFile':shared_folder+'van_449014.nxs',         #Options:None;data_file_name
              'NormalizationDataFile':shared_folder+'van_449014.nxs',   #Options:None;data_file_name
              'SampleLogVariables':{'OmegaMotorName':None,'Temperature':5.0,'MagneticField':0.0},   #Options:None;LogVariableName;number
              'UBSetup':{'a':5.0180,'b':5.0180,'c':23.3563,'alpha':90,'beta':90,'gamma':120,'u':'1.05,-0.05,0','v':'-0.95,1.05,0'},
               #Data reduction options
              'Ei':6.59,                            #Options: None;Ei_somehow_determined
              'T0':None,                            #Options: None;T0_determined_from_mantid
              'BadPulsesThreshold':None,            #Options: None;bg_pulses_threshold value
              'TimeIndepBackgroundWindow':'Default',    #Options: None;'Default';[Tib_min,Tib_max]
              'E_min':None,                         #Options: None;Emin if None the value is -0.95*Ei
              'E_max':None,                         #Options: None;Emax if None the value is 0.95*Ei
              'AdditionalDimensions':None,          #Options: None;list of triplets ("name", min, max)
               #Polarized data options
              'PolarizationState':None,             #Options:None;'SF_Px';'NSF_Px';'SF_Py';'NSF_Py';'SF_Pz';'NSF_Pz'
              'FlippingRatio':None,                 #Options:None;'14';'6.5+2.8*cos((omega+3.7)*pi/180),omega'
              'PolarizingSupermirrorDeflectionAdjustment':None, #Options:None;deflection_angle
              'EfCorrectionFunction':None,          #Options:None;'HYSPEC_default_correction';Custom_Ef_Correction_Function_Name
              }
    data_set_list.append(data_set_6p59meV_I_5K)

    data_set_6p59meV_I_7K={'Runs':range(480420,480480+1),    #List of runs, or list of lists of runs that are added together
              'BackgroundRuns':None,   #range(297325,297337)Options: None;list of runs that are added together
              'RawDataFolder':raw_data_folder,      #Options:raw_data_folder string
              'RawDataFolderBackground':None,       #Options:None (same as the raw data); bknd_raw_data_folder string
              'BackgroundScaling':1,             #Options: None (same as 1); scaling factor
              'MdeFolder':mde_folder,               #Options:mde_folder string
              'MdeName':'merged_mde_bcvo_6p59_I_7K',   #Options:mde_name string
              'BackgroundMdeName':None,      #Options:None;bg_mde_name string
              'MaskingDataFile':shared_folder+'van_449014.nxs',         #Options:None;data_file_name
              'NormalizationDataFile':shared_folder+'van_449014.nxs',   #Options:None;data_file_name
              'SampleLogVariables':{'OmegaMotorName':None,'Temperature':7.0,'MagneticField':0.0},   #Options:None;LogVariableName;number
              'UBSetup':{'a':5.0180,'b':5.0180,'c':23.3563,'alpha':90,'beta':90,'gamma':120,'u':'1.05,-0.05,0','v':'-0.95,1.05,0'},
               #Data reduction options
              'Ei':6.59,                            #Options: None;Ei_somehow_determined
              'T0':None,                            #Options: None;T0_determined_from_mantid
              'BadPulsesThreshold':None,            #Options: None;bg_pulses_threshold value
              'TimeIndepBackgroundWindow':'Default',    #Options: None;'Default';[Tib_min,Tib_max]
              'E_min':None,                         #Options: None;Emin if None the value is -0.95*Ei
              'E_max':None,                         #Options: None;Emax if None the value is 0.95*Ei
              'AdditionalDimensions':None,          #Options: None;list of triplets ("name", min, max)
               #Polarized data options
              'PolarizationState':None,             #Options:None;'SF_Px';'NSF_Px';'SF_Py';'NSF_Py';'SF_Pz';'NSF_Pz'
              'FlippingRatio':None,                 #Options:None;'14';'6.5+2.8*cos((omega+3.7)*pi/180),omega'
              'PolarizingSupermirrorDeflectionAdjustment':None, #Options:None;deflection_angle
              'EfCorrectionFunction':None,          #Options:None;'HYSPEC_default_correction';Custom_Ef_Correction_Function_Name
              }
    data_set_list.append(data_set_6p59meV_I_7K)

    data_set_6p59meV_I_9K={'Runs':range(480481,480541+1),    #List of runs, or list of lists of runs that are added together
              'BackgroundRuns':None,   #range(297325,297337)Options: None;list of runs that are added together
              'RawDataFolder':raw_data_folder,      #Options:raw_data_folder string
              'RawDataFolderBackground':None,       #Options:None (same as the raw data); bknd_raw_data_folder string
              'BackgroundScaling':1,             #Options: None (same as 1); scaling factor
              'MdeFolder':mde_folder,               #Options:mde_folder string
              'MdeName':'merged_mde_bcvo_6p59_I_9K',   #Options:mde_name string
              'BackgroundMdeName':None,      #Options:None;bg_mde_name string
              'MaskingDataFile':shared_folder+'van_449014.nxs',         #Options:None;data_file_name
              'NormalizationDataFile':shared_folder+'van_449014.nxs',   #Options:None;data_file_name
              'SampleLogVariables':{'OmegaMotorName':None,'Temperature':9.0,'MagneticField':0.0},   #Options:None;LogVariableName;number
              'UBSetup':{'a':5.0180,'b':5.0180,'c':23.3563,'alpha':90,'beta':90,'gamma':120,'u':'1.05,-0.05,0','v':'-0.95,1.05,0'},
               #Data reduction options
              'Ei':6.59,                            #Options: None;Ei_somehow_determined
              'T0':None,                            #Options: None;T0_determined_from_mantid
              'BadPulsesThreshold':None,            #Options: None;bg_pulses_threshold value
              'TimeIndepBackgroundWindow':'Default',    #Options: None;'Default';[Tib_min,Tib_max]
              'E_min':None,                         #Options: None;Emin if None the value is -0.95*Ei
              'E_max':None,                         #Options: None;Emax if None the value is 0.95*Ei
              'AdditionalDimensions':None,          #Options: None;list of triplets ("name", min, max)
               #Polarized data options
              'PolarizationState':None,             #Options:None;'SF_Px';'NSF_Px';'SF_Py';'NSF_Py';'SF_Pz';'NSF_Pz'
              'FlippingRatio':None,                 #Options:None;'14';'6.5+2.8*cos((omega+3.7)*pi/180),omega'
              'PolarizingSupermirrorDeflectionAdjustment':None, #Options:None;deflection_angle
              'EfCorrectionFunction':None,          #Options:None;'HYSPEC_default_correction';Custom_Ef_Correction_Function_Name
              }
    data_set_list.append(data_set_6p59meV_I_9K)

    data_set_6p59meV_I_11K={'Runs':range(480542,480602+1),    #List of runs, or list of lists of runs that are added together
              'BackgroundRuns':None,   #range(297325,297337)Options: None;list of runs that are added together
              'RawDataFolder':raw_data_folder,      #Options:raw_data_folder string
              'RawDataFolderBackground':None,       #Options:None (same as the raw data); bknd_raw_data_folder string
              'BackgroundScaling':1,             #Options: None (same as 1); scaling factor
              'MdeFolder':mde_folder,               #Options:mde_folder string
              'MdeName':'merged_mde_bcvo_6p59_I_11K',   #Options:mde_name string
              'BackgroundMdeName':None,      #Options:None;bg_mde_name string
              'MaskingDataFile':shared_folder+'van_449014.nxs',         #Options:None;data_file_name
              'NormalizationDataFile':shared_folder+'van_449014.nxs',   #Options:None;data_file_name
              'SampleLogVariables':{'OmegaMotorName':None,'Temperature':11.0,'MagneticField':0.0},   #Options:None;LogVariableName;number
              'UBSetup':{'a':5.0180,'b':5.0180,'c':23.3563,'alpha':90,'beta':90,'gamma':120,'u':'1.05,-0.05,0','v':'-0.95,1.05,0'},
               #Data reduction options
              'Ei':6.59,                            #Options: None;Ei_somehow_determined
              'T0':None,                            #Options: None;T0_determined_from_mantid
              'BadPulsesThreshold':None,            #Options: None;bg_pulses_threshold value
              'TimeIndepBackgroundWindow':'Default',    #Options: None;'Default';[Tib_min,Tib_max]
              'E_min':None,                         #Options: None;Emin if None the value is -0.95*Ei
              'E_max':None,                         #Options: None;Emax if None the value is 0.95*Ei
              'AdditionalDimensions':None,          #Options: None;list of triplets ("name", min, max)
               #Polarized data options
              'PolarizationState':None,             #Options:None;'SF_Px';'NSF_Px';'SF_Py';'NSF_Py';'SF_Pz';'NSF_Pz'
              'FlippingRatio':None,                 #Options:None;'14';'6.5+2.8*cos((omega+3.7)*pi/180),omega'
              'PolarizingSupermirrorDeflectionAdjustment':None, #Options:None;deflection_angle
              'EfCorrectionFunction':None,          #Options:None;'HYSPEC_default_correction';Custom_Ef_Correction_Function_Name
              }
    data_set_list.append(data_set_6p59meV_I_11K)

    data_set_6p59meV_I_13K={'Runs':range(480603,480663+1),    #List of runs, or list of lists of runs that are added together
              'BackgroundRuns':None,   #range(297325,297337)Options: None;list of runs that are added together
              'RawDataFolder':raw_data_folder,      #Options:raw_data_folder string
              'RawDataFolderBackground':None,       #Options:None (same as the raw data); bknd_raw_data_folder string
              'BackgroundScaling':1,             #Options: None (same as 1); scaling factor
              'MdeFolder':mde_folder,               #Options:mde_folder string
              'MdeName':'merged_mde_bcvo_6p59_I_13K',   #Options:mde_name string
              'BackgroundMdeName':None,      #Options:None;bg_mde_name string
              'MaskingDataFile':shared_folder+'van_449014.nxs',         #Options:None;data_file_name
              'NormalizationDataFile':shared_folder+'van_449014.nxs',   #Options:None;data_file_name
              'SampleLogVariables':{'OmegaMotorName':None,'Temperature':13.0,'MagneticField':0.0},   #Options:None;LogVariableName;number
              'UBSetup':{'a':5.0180,'b':5.0180,'c':23.3563,'alpha':90,'beta':90,'gamma':120,'u':'1.05,-0.05,0','v':'-0.95,1.05,0'},
               #Data reduction options
              'Ei':6.59,                            #Options: None;Ei_somehow_determined
              'T0':None,                            #Options: None;T0_determined_from_mantid
              'BadPulsesThreshold':None,            #Options: None;bg_pulses_threshold value
              'TimeIndepBackgroundWindow':'Default',    #Options: None;'Default';[Tib_min,Tib_max]
              'E_min':None,                         #Options: None;Emin if None the value is -0.95*Ei
              'E_max':None,                         #Options: None;Emax if None the value is 0.95*Ei
              'AdditionalDimensions':None,          #Options: None;list of triplets ("name", min, max)
               #Polarized data options
              'PolarizationState':None,             #Options:None;'SF_Px';'NSF_Px';'SF_Py';'NSF_Py';'SF_Pz';'NSF_Pz'
              'FlippingRatio':None,                 #Options:None;'14';'6.5+2.8*cos((omega+3.7)*pi/180),omega'
              'PolarizingSupermirrorDeflectionAdjustment':None, #Options:None;deflection_angle
              'EfCorrectionFunction':None,          #Options:None;'HYSPEC_default_correction';Custom_Ef_Correction_Function_Name
              }
    data_set_list.append(data_set_6p59meV_I_13K)

    data_set_6p59meV_I_6K={'Runs':list(range(480664,480714+1))+list(range(481114,481204+1)),#List of runs, or list of lists of runs that are added together
              'BackgroundRuns':None,   #range(297325,297337)Options: None;list of runs that are added together
              'RawDataFolder':raw_data_folder,      #Options:raw_data_folder string
              'RawDataFolderBackground':None,       #Options:None (same as the raw data); bknd_raw_data_folder string
              'BackgroundScaling':1,             #Options: None (same as 1); scaling factor
              'MdeFolder':mde_folder,               #Options:mde_folder string
              'MdeName':'merged_mde_bcvo_6p59_I_6K',   #Options:mde_name string
              'BackgroundMdeName':None,      #Options:None;bg_mde_name string
              'MaskingDataFile':shared_folder+'van_449014.nxs',         #Options:None;data_file_name
              'NormalizationDataFile':shared_folder+'van_449014.nxs',   #Options:None;data_file_name
              'SampleLogVariables':{'OmegaMotorName':None,'Temperature':6.0,'MagneticField':0.0},   #Options:None;LogVariableName;number
              'UBSetup':{'a':5.0180,'b':5.0180,'c':23.3563,'alpha':90,'beta':90,'gamma':120,'u':'1.05,-0.05,0','v':'-0.95,1.05,0'},
               #Data reduction options
              'Ei':6.59,                            #Options: None;Ei_somehow_determined
              'T0':None,                            #Options: None;T0_determined_from_mantid
              'BadPulsesThreshold':None,            #Options: None;bg_pulses_threshold value
              'TimeIndepBackgroundWindow':'Default',    #Options: None;'Default';[Tib_min,Tib_max]
              'E_min':None,                         #Options: None;Emin if None the value is -0.95*Ei
              'E_max':None,                         #Options: None;Emax if None the value is 0.95*Ei
              'AdditionalDimensions':None,          #Options: None;list of triplets ("name", min, max)
               #Polarized data options
              'PolarizationState':None,             #Options:None;'SF_Px';'NSF_Px';'SF_Py';'NSF_Py';'SF_Pz';'NSF_Pz'
              'FlippingRatio':None,                 #Options:None;'14';'6.5+2.8*cos((omega+3.7)*pi/180),omega'
              'PolarizingSupermirrorDeflectionAdjustment':None, #Options:None;deflection_angle
              'EfCorrectionFunction':None,          #Options:None;'HYSPEC_default_correction';Custom_Ef_Correction_Function_Name
              }
    data_set_list.append(data_set_6p59meV_I_6K)

    data_set_6p59meV_I_20K={'Runs':range(480715,480775+1),    #List of runs, or list of lists of runs that are added together
              'BackgroundRuns':None,   #range(297325,297337)Options: None;list of runs that are added together
              'RawDataFolder':raw_data_folder,      #Options:raw_data_folder string
              'RawDataFolderBackground':None,       #Options:None (same as the raw data); bknd_raw_data_folder string
              'BackgroundScaling':1,             #Options: None (same as 1); scaling factor
              'MdeFolder':mde_folder,               #Options:mde_folder string
              'MdeName':'merged_mde_bcvo_6p59_I_20K',   #Options:mde_name string
              'BackgroundMdeName':None,      #Options:None;bg_mde_name string
              'MaskingDataFile':shared_folder+'van_449014.nxs',         #Options:None;data_file_name
              'NormalizationDataFile':shared_folder+'van_449014.nxs',   #Options:None;data_file_name
              'SampleLogVariables':{'OmegaMotorName':None,'Temperature':20.0,'MagneticField':0.0},   #Options:None;LogVariableName;number
              'UBSetup':{'a':5.0180,'b':5.0180,'c':23.3563,'alpha':90,'beta':90,'gamma':120,'u':'1.05,-0.05,0','v':'-0.95,1.05,0'},
               #Data reduction options
              'Ei':6.59,                            #Options: None;Ei_somehow_determined
              'T0':None,                            #Options: None;T0_determined_from_mantid
              'BadPulsesThreshold':None,            #Options: None;bg_pulses_threshold value
              'TimeIndepBackgroundWindow':'Default',    #Options: None;'Default';[Tib_min,Tib_max]
              'E_min':None,                         #Options: None;Emin if None the value is -0.95*Ei
              'E_max':None,                         #Options: None;Emax if None the value is 0.95*Ei
              'AdditionalDimensions':None,          #Options: None;list of triplets ("name", min, max)
               #Polarized data options
              'PolarizationState':None,             #Options:None;'SF_Px';'NSF_Px';'SF_Py';'NSF_Py';'SF_Pz';'NSF_Pz'
              'FlippingRatio':None,                 #Options:None;'14';'6.5+2.8*cos((omega+3.7)*pi/180),omega'
              'PolarizingSupermirrorDeflectionAdjustment':None, #Options:None;deflection_angle
              'EfCorrectionFunction':None,          #Options:None;'HYSPEC_default_correction';Custom_Ef_Correction_Function_Name
              }
    data_set_list.append(data_set_6p59meV_I_20K)

    data_set_6p59meV_I_30K={'Runs':list(range(480778,480883+1))+list(range(480885,481021+1)),    #List of runs, or list of lists of runs that are added together
              'BackgroundRuns':None,   #range(297325,297337)Options: None;list of runs that are added together
              'RawDataFolder':raw_data_folder,      #Options:raw_data_folder string
              'RawDataFolderBackground':None,       #Options:None (same as the raw data); bknd_raw_data_folder string
              'BackgroundScaling':1,             #Options: None (same as 1); scaling factor
              'MdeFolder':mde_folder,               #Options:mde_folder string
              'MdeName':'merged_mde_bcvo_6p59_I_30K',   #Options:mde_name string
              'BackgroundMdeName':None,      #Options:None;bg_mde_name string
              'MaskingDataFile':shared_folder+'van_449014.nxs',         #Options:None;data_file_name
              'NormalizationDataFile':shared_folder+'van_449014.nxs',   #Options:None;data_file_name
              'SampleLogVariables':{'OmegaMotorName':None,'Temperature':30.0,'MagneticField':0.0},   #Options:None;LogVariableName;number
              'UBSetup':{'a':5.0180,'b':5.0180,'c':23.3563,'alpha':90,'beta':90,'gamma':120,'u':'1.05,-0.05,0','v':'-0.95,1.05,0'},
               #Data reduction options
              'Ei':6.59,                            #Options: None;Ei_somehow_determined
              'T0':None,                            #Options: None;T0_determined_from_mantid
              'BadPulsesThreshold':None,            #Options: None;bg_pulses_threshold value
              'TimeIndepBackgroundWindow':'Default',    #Options: None;'Default';[Tib_min,Tib_max]
              'E_min':None,                         #Options: None;Emin if None the value is -0.95*Ei
              'E_max':None,                         #Options: None;Emax if None the value is 0.95*Ei
              'AdditionalDimensions':None,          #Options: None;list of triplets ("name", min, max)
               #Polarized data options
              'PolarizationState':None,             #Options:None;'SF_Px';'NSF_Px';'SF_Py';'NSF_Py';'SF_Pz';'NSF_Pz'
              'FlippingRatio':None,                 #Options:None;'14';'6.5+2.8*cos((omega+3.7)*pi/180),omega'
              'PolarizingSupermirrorDeflectionAdjustment':None, #Options:None;deflection_angle
              'EfCorrectionFunction':None,          #Options:None;'HYSPEC_default_correction';Custom_Ef_Correction_Function_Name
              }
    data_set_list.append(data_set_6p59meV_I_30K)

    data_set_6p59meV_bkgsub={'Runs':range(479954,480133+1),          #List of runs, or list of lists of runs that are added together
              'BackgroundRuns':None,   #range(297325,297337)Options: None;list of runs that are added together
              'RawDataFolder':raw_data_folder,      #Options:raw_data_folder string
              'RawDataFolderBackground':None,       #Options:None (same as the raw data); bknd_raw_data_folder string
              'BackgroundScaling':1,             #Options: None (same as 1); scaling factor
              'MdeFolder':mde_folder,               #Options:mde_folder string
              'MdeName':'merged_mde_bcvo_6p59_0p25K_bkgsub',   #Options:mde_name string
              'BackgroundMdeName':'merged_mde_bcvo_6p59_I_20K',      #Options:None;bg_mde_name string
              'MaskingDataFile':shared_folder+'van_449014.nxs',         #Options:None;data_file_name
              'NormalizationDataFile':shared_folder+'van_449014.nxs',   #Options:None;data_file_name
              'SampleLogVariables':{'OmegaMotorName':None,'Temperature':0.25,'MagneticField':0.0},   #Options:None;LogVariableName;number
              'UBSetup':{'a':5.0180,'b':5.0180,'c':23.3563,'alpha':90,'beta':90,'gamma':120,'u':'1.05,-0.05,0','v':'-0.95,1.05,0'},
               #Data reduction options
              'Ei':6.59,                            #Options: None;Ei_somehow_determined
              'T0':None,                            #Options: None;T0_determined_from_mantid
              'BadPulsesThreshold':None,            #Options: None;bg_pulses_threshold value
              'TimeIndepBackgroundWindow':'Default',    #Options: None;'Default';[Tib_min,Tib_max]
              'E_min':None,                         #Options: None;Emin if None the value is -0.95*Ei
              'E_max':None,                         #Options: None;Emax if None the value is 0.95*Ei
              'AdditionalDimensions':None,          #Options: None;list of triplets ("name", min, max)
               #Polarized data options
              'PolarizationState':None,             #Options:None;'SF_Px';'NSF_Px';'SF_Py';'NSF_Py';'SF_Pz';'NSF_Pz'
              'FlippingRatio':None,                 #Options:None;'14';'6.5+2.8*cos((omega+3.7)*pi/180),omega'
              'PolarizingSupermirrorDeflectionAdjustment':None, #Options:None;deflection_angle
              'EfCorrectionFunction':None,          #Options:None;'HYSPEC_default_correction';Custom_Ef_Correction_Function_Name
              }
    data_set_list.append(data_set_6p59meV_bkgsub)

    data_set_6p59meV_I_20Km30K={'Runs':range(480715,480775+1),    #List of runs, or list of lists of runs that are added together
              'BackgroundRuns':None,   #range(297325,297337)Options: None;list of runs that are added together
              'RawDataFolder':raw_data_folder,      #Options:raw_data_folder string
              'RawDataFolderBackground':None,       #Options:None (same as the raw data); bknd_raw_data_folder string
              'BackgroundScaling':1,             #Options: None (same as 1); scaling factor
              'MdeFolder':mde_folder,               #Options:mde_folder string
              'MdeName':'merged_mde_bcvo_6p59_I_20Km30K',   #Options:mde_name string
              'BackgroundMdeName':'merged_mde_bcvo_6p59_I_30K',      #Options:None;bg_mde_name string
              'MaskingDataFile':shared_folder+'van_449014.nxs',         #Options:None;data_file_name
              'NormalizationDataFile':shared_folder+'van_449014.nxs',   #Options:None;data_file_name
              'SampleLogVariables':{'OmegaMotorName':None,'Temperature':20.0,'MagneticField':0.0},   #Options:None;LogVariableName;number
              'UBSetup':{'a':5.0180,'b':5.0180,'c':23.3563,'alpha':90,'beta':90,'gamma':120,'u':'1.05,-0.05,0','v':'-0.95,1.05,0'},
               #Data reduction options
              'Ei':6.59,                            #Options: None;Ei_somehow_determined
              'T0':None,                            #Options: None;T0_determined_from_mantid
              'BadPulsesThreshold':None,            #Options: None;bg_pulses_threshold value
              'TimeIndepBackgroundWindow':'Default',    #Options: None;'Default';[Tib_min,Tib_max]
              'E_min':None,                         #Options: None;Emin if None the value is -0.95*Ei
              'E_max':None,                         #Options: None;Emax if None the value is 0.95*Ei
              'AdditionalDimensions':None,          #Options: None;list of triplets ("name", min, max)
               #Polarized data options
              'PolarizationState':None,             #Options:None;'SF_Px';'NSF_Px';'SF_Py';'NSF_Py';'SF_Pz';'NSF_Pz'
              'FlippingRatio':None,                 #Options:None;'14';'6.5+2.8*cos((omega+3.7)*pi/180),omega'
              'PolarizingSupermirrorDeflectionAdjustment':None, #Options:None;deflection_angle
              'EfCorrectionFunction':None,          #Options:None;'HYSPEC_default_correction';Custom_Ef_Correction_Function_Name
              }
    data_set_list.append(data_set_6p59meV_I_20Km30K)
    data_set_6p59meV_I_3K={'Runs':range(481267,481328+1),    #List of runs, or list of lists of runs that are added together
              'BackgroundRuns':None,   #range(297325,297337)Options: None;list of runs that are added together
              'RawDataFolder':raw_data_folder,      #Options:raw_data_folder string
              'RawDataFolderBackground':None,       #Options:None (same as the raw data); bknd_raw_data_folder string
              'BackgroundScaling':1,             #Options: None (same as 1); scaling factor
              'MdeFolder':mde_folder,               #Options:mde_folder string
              'MdeName':'merged_mde_bcvo_6p59_I_3K',   #Options:mde_name string
              'BackgroundMdeName':None,      #Options:None;bg_mde_name string
              'MaskingDataFile':shared_folder+'van_449014.nxs',         #Options:None;data_file_name
              'NormalizationDataFile':shared_folder+'van_449014.nxs',   #Options:None;data_file_name
              'SampleLogVariables':{'OmegaMotorName':None,'Temperature':3.0,'MagneticField':0.0},   #Options:None;LogVariableName;number
              'UBSetup':{'a':5.0180,'b':5.0180,'c':23.3563,'alpha':90,'beta':90,'gamma':120,'u':'1.05,-0.05,0','v':'-0.95,1.05,0'},
               #Data reduction options
              'Ei':6.59,                            #Options: None;Ei_somehow_determined
              'T0':None,                            #Options: None;T0_determined_from_mantid
              'BadPulsesThreshold':None,            #Options: None;bg_pulses_threshold value
              'TimeIndepBackgroundWindow':'Default',    #Options: None;'Default';[Tib_min,Tib_max]
              'E_min':None,                         #Options: None;Emin if None the value is -0.95*Ei
              'E_max':None,                         #Options: None;Emax if None the value is 0.95*Ei
              'AdditionalDimensions':None,          #Options: None;list of triplets ("name", min, max)
               #Polarized data options
              'PolarizationState':None,             #Options:None;'SF_Px';'NSF_Px';'SF_Py';'NSF_Py';'SF_Pz';'NSF_Pz'
              'FlippingRatio':None,                 #Options:None;'14';'6.5+2.8*cos((omega+3.7)*pi/180),omega'
              'PolarizingSupermirrorDeflectionAdjustment':None, #Options:None;deflection_angle
              'EfCorrectionFunction':None,          #Options:None;'HYSPEC_default_correction';Custom_Ef_Correction_Function_Name
              }
    data_set_list.append(data_set_6p59meV_I_3K)

    data_set_6p59meV_I_4K={'Runs':list(range(481083,481200+1))+list(range(481321,481450+1)),    #List of runs, or list of lists of runs that are added together
              'BackgroundRuns':None,   #range(297325,297337)Options: None;list of runs that are added together
              'RawDataFolder':raw_data_folder,      #Options:raw_data_folder string
              'RawDataFolderBackground':None,       #Options:None (same as the raw data); bknd_raw_data_folder string
              'BackgroundScaling':1,             #Options: None (same as 1); scaling factor
              'MdeFolder':mde_folder,               #Options:mde_folder string
              'MdeName':'merged_mde_bcvo_6p59_I_4K',   #Options:mde_name string
              'BackgroundMdeName':None,      #Options:None;bg_mde_name string
              'MaskingDataFile':shared_folder+'van_449014.nxs',         #Options:None;data_file_name
              'NormalizationDataFile':shared_folder+'van_449014.nxs',   #Options:None;data_file_name
              'SampleLogVariables':{'OmegaMotorName':None,'Temperature':4.0,'MagneticField':0.0},   #Options:None;LogVariableName;number
              'UBSetup':{'a':5.0180,'b':5.0180,'c':23.3563,'alpha':90,'beta':90,'gamma':120,'u':'1.05,-0.05,0','v':'-0.95,1.05,0'},
               #Data reduction options
              'Ei':6.59,                            #Options: None;Ei_somehow_determined
              'T0':None,                            #Options: None;T0_determined_from_mantid
              'BadPulsesThreshold':None,            #Options: None;bg_pulses_threshold value
              'TimeIndepBackgroundWindow':'Default',    #Options: None;'Default';[Tib_min,Tib_max]
              'E_min':None,                         #Options: None;Emin if None the value is -0.95*Ei
              'E_max':None,                         #Options: None;Emax if None the value is 0.95*Ei
              'AdditionalDimensions':None,          #Options: None;list of triplets ("name", min, max)
               #Polarized data options
              'PolarizationState':None,             #Options:None;'SF_Px';'NSF_Px';'SF_Py';'NSF_Py';'SF_Pz';'NSF_Pz'
              'FlippingRatio':None,                 #Options:None;'14';'6.5+2.8*cos((omega+3.7)*pi/180),omega'
              'PolarizingSupermirrorDeflectionAdjustment':None, #Options:None;deflection_angle
              'EfCorrectionFunction':None,          #Options:None;'HYSPEC_default_correction';Custom_Ef_Correction_Function_Name
              }
    data_set_list.append(data_set_6p59meV_I_4K)
    data_set_6p59meV_I_3p5K={'Runs':range(481205,481265+1),    #List of runs, or list of lists of runs that are added together
              'BackgroundRuns':None,   #range(297325,297337)Options: None;list of runs that are added together
              'RawDataFolder':raw_data_folder,      #Options:raw_data_folder string
              'RawDataFolderBackground':None,       #Options:None (same as the raw data); bknd_raw_data_folder string
              'BackgroundScaling':1,             #Options: None (same as 1); scaling factor
              'MdeFolder':mde_folder,               #Options:mde_folder string
              'MdeName':'merged_mde_bcvo_6p59_I_3p5K',   #Options:mde_name string
              'BackgroundMdeName':None,      #Options:None;bg_mde_name string
              'MaskingDataFile':shared_folder+'van_449014.nxs',         #Options:None;data_file_name
              'NormalizationDataFile':shared_folder+'van_449014.nxs',   #Options:None;data_file_name
              'SampleLogVariables':{'OmegaMotorName':None,'Temperature':3.5,'MagneticField':0.0},   #Options:None;LogVariableName;number
              'UBSetup':{'a':5.0180,'b':5.0180,'c':23.3563,'alpha':90,'beta':90,'gamma':120,'u':'1.05,-0.05,0','v':'-0.95,1.05,0'},
               #Data reduction options
              'Ei':6.59,                            #Options: None;Ei_somehow_determined
              'T0':None,                            #Options: None;T0_determined_from_mantid
              'BadPulsesThreshold':None,            #Options: None;bg_pulses_threshold value
              'TimeIndepBackgroundWindow':'Default',    #Options: None;'Default';[Tib_min,Tib_max]
              'E_min':None,                         #Options: None;Emin if None the value is -0.95*Ei
              'E_max':None,                         #Options: None;Emax if None the value is 0.95*Ei
              'AdditionalDimensions':None,          #Options: None;list of triplets ("name", min, max)
               #Polarized data options
              'PolarizationState':None,             #Options:None;'SF_Px';'NSF_Px';'SF_Py';'NSF_Py';'SF_Pz';'NSF_Pz'
              'FlippingRatio':None,                 #Options:None;'14';'6.5+2.8*cos((omega+3.7)*pi/180),omega'
              'PolarizingSupermirrorDeflectionAdjustment':None, #Options:None;deflection_angle
              'EfCorrectionFunction':None,          #Options:None;'HYSPEC_default_correction';Custom_Ef_Correction_Function_Name
              }
    data_set_list.append(data_set_6p59meV_I_3p5K)
    return data_set_list
