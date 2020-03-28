#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 17:23:51 2020

@author: clayton

"""

from read_files import Read_files
from statistics import Statistics


import pandas as pd

#df = pd.read_csv('/home/clayton/Dropbox/Lucas/Datasets/Dados_clientes.csv',index_col=0, sep=',')



data = Read_files('Dados_clientes.csv')

df = data.read_data(data)


#print('Informações iniciais sobre o Dataset: \n\n', df)
'''
# Objeto values da classe Statistics
values = Statistics(df)

# Quantidade de indivíduos por sexo
set = values.amount_client(df.gender.value_counts())
print('\nIndivíduos divididos por sexo: \n', set)

# Encoder, neste caso, para sexo
enc = values.encoder(df['gender'])
print('\nValores do encoder para sexo: ',enc)

# Describe do dataset
desc = values.describe(df.describe())
print(desc)
'''
# Quantidade de produtos comprados por unidade
#print('Produtos disponíveis para compra: %d\n' %len(df.int_itens_comp.unique()))

# Quantidade de produtos
#print('Quantidade de produtos por udidades: %d\n' %len(df.data.order_id.unique()))

# Quantidade de clientes únicos que efetuaram compras
#print('Quantidade de clientes: %d\n' %len(df.data.customer_id.unique()))

#print(df.data.head())
# Quantidade de produtos comprados por unidade
#print('Produtos disponíveis para compra: %d\n' %len(df.int_itens_comp.unique()))

#print(values.data1.data.order_id.unique())

#values.qtd(data.customer_id.unique())

#print('Quantidade de produtos por udidades: ',len(values.qtd))
#print(values.qtd(10))