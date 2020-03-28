#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 16:58:48 2020

@author: clayton
"""

import pandas as pd


#======================================================================================

"""
	Function that loads all data sets for model construction

	Args:
        One csv file

    	Returns:
        One Pandas Dataframe
 """

class Read_files(object): 
    
    
    
    def __init__(self, val1):
        self.val1 = val1
        
        
    def read_data(self, file):
       self.file = file
       df = pd.read_csv(file, sep=',',index_col=0)
       print(df)
        
     
#======================================================================================
