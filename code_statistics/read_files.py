#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 16:58:48 2020

@author: clayton
"""

import pandas as pd
from datetime import date, datetime
from sklearn.preprocessing import LabelEncoder


#======================================================================================

"""
	Function that loads all data sets for model construction

	Args:
        One csv file

    	Returns:
        One Pandas Dataframe
 """

class Read_files:
    """ Apresenta informações sobre o conjunto de dados Clientes """
    
    
    def __init__(self, file):
        self.file = file

    # Função que trás informações básicas sobre os clientes
    def read_cliente(self):
        df =  pd.read_csv(self.file, sep=',',index_col=0)

        # Transforma o campo birthday no formato date
        born = pd.to_datetime(df.birthdate)
        ano, mes = born.dt.year, born.dt.month
        today = datetime.today()
        idade = (today.year - ano) - (today.month < mes)

        # Rermove dados faltantes
        df["gender"].fillna(df["gender"], inplace=True)
        df['type'].fillna(df['type'], inplace=True)

        # Encoder
        enc = LabelEncoder()
        sexo = enc.fit_transform(df['gender'])
        pessoa = enc.fit_transform(df['type'])

        # Criando uma nova coluna contendo esses valores
        df['sexo'] = sexo
        df['pessoa'] = pessoa
        df['idade'] = idade
        df = df.drop(['birthdate'], axis=1)

        # Eliminando outliears campo idade
        df.loc[(df["idade"] < 15), "idade"] = 15
        df.loc[(df["idade"] > 75), "idade"] = 75

        df.to_csv('../data/ClientsData.csv')
        return df



#======================================================================================
