# spgMantid
Python scripts for creation of spaghetti-style plots of Mantid inelastic data and related utilities. 


There are two main utilities in this repo, the first is to make spaghetti plots and the second is to generate a detailed balance background based on the temperature dependence of these measurements. Both are not tested.

The general workflow is the following:

1) Define your datasets correctly in the "define_data.py" file, you should follow the syntax of the example file but change it to your needs. Make a folder for where merged files will be stored, be sure to change the "shared_folder", "raw_data_folder" and "mde_folder" values in "define_data.py". This is where reduced data is saved, if you want to change the workspaces after generating them you will either need to delete the workspace manually in the Mantid workspace manager using DeleteWorkspace('ws'), or reset your iPython console. You will also need to delete the saved mde file. 
2) Define any slices that you may want to plot aside from the spaghetti plots in "define_slices.py". Not technically necessary. 
3) Follow the example scripts to generate your plots. Reduction will be done at this point. 

Report any bugs to Tom Halloran at thallor1@jhu.edu (after trying to solve them for yourself 😃)
