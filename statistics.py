 #!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 16:58:48 2020

@author: clayton
"""
from sklearn.preprocessing import LabelEncoder


class Statistics(object):


    # Após criado as classes, passo os parâmetros para a função construtor
    def __init__(self, val1):
       self.val1 = val1
       

    # Com os parametros já definidos na função construtor, agora só criar os métodos para o objeto.
    def amount_client(self, valor_cli):
        self.valor_cli = valor_cli
        return valor_cli
        
    # Função de encoder para para características não numéricas
    def encoder(self, val_encoder, enc = LabelEncoder()):
        self.val_encoder = val_encoder
        return enc.fit_transform(val_encoder)


    # Função estatística dos dados do dataset
    def describe(self, val_desc):
        self.val_desc = val_desc
        return val_desc



####################################################################################


def Categoria_filho(self):
    df = pd.read_csv(self.file, sep=',', index_col=0)
    print('Informações sobre a categoria filho: \n\n', df)
    print('\n Quantidade por catogoria filho: \n', df.child_category_name.value_counts().plot(kind='bar'))

def Categoria_pai(self):
    df = pd.read_csv(self.file, sep=',', index_col=0)
    print('Informações sobre a categoria pai: \n\n', df)
    print('\n Quantidade por catogoria pai: \n', df.parent_category_name.value_counts().plot(kind='bar'))

def Produtos(self):
    df = pd.read_csv(self.file, sep=',', index_col=0)
    print('Informações sobre os produtos: \n\n', df)
    a = df.groupby(by='product_name')['customer_id'].count()
    print('\n Quantidade de da categoria filho mais vendida: \n',a.sort_values(ascending=False).plot(kind='barh',subplots=True))
    print('Os produtos mais vendidos: \n\n')
    print('\n mais vendidos: \n',product_name.value_counts().plot(kind='barh'))


