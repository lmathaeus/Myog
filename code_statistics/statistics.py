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



