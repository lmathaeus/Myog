#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 17:23:51 2020

@author: clayton
"""
import sys
import matplotlib.pyplot as plt
#import datetime
import read_files as rf

# Essa é a forma de leitura do conjunto de dados copleto
df = rf.load_dataset(sys.argv[1])

#print(df.head())

