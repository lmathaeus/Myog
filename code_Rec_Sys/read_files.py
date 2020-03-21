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

def load_dataset(file_name):
    data = pd.read_csv(open(file_name),sep= ',', index_col=0)
    
    return data	
     
#======================================================================================
