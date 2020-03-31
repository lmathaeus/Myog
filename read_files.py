#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 16:58:48 2020

@author: clayton
"""

import pandas as pd

# ======================================================================================

"""
	Function that loads all data sets for model construction

	Args:
        One csv file

    	Returns:
        One Pandas Dataframe
 """


class Read_files:

    def __init__(self, file):
        self.file = file



    def read_cliente(self):
        df = pd.read_csv(self.file, sep=',', index_col=0)
        samples = df.head()
        print('Informações iniciais sobre o Dataset: \n\n', df)
        print('\n Quantidade por sexo: \n', df.gender.value_counts())

    def read_product(self):
        df = pd.read_csv(self.file, sep=',', index_col=0)
        samples = df.head()
        print('Informações iniciais sobre o produto: \n\n', df)
        print('\n Quantidade por produto: \n', df.product_name.value_counts())


# ======================================================================================
