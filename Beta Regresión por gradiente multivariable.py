# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 22:51:14 2022

@author: Enrique Rojas
"""

import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd

import numpy as np
import pandas as pd

df = pd.read_excel('tareaRGD.xlsx')

X = df[['x1','x2','x3']].to_numpy()

y =  df['y'].to_numpy()
n = X.shape[0]
step_max = 1000
E = 10**-5

def rgl_gradiente(a,b,eta):
    
    eta= eta
    step = 0 
    
    while True:
        step += 1
        error = 0
        for i in range(n):
            for j in range(X.shape[1]):
                E_a= np.average((a*X[i][j]+b-y[i])*X[i][j])
                E_b= np.average(a*X[i][j]+b-y[i])
        gradiente = np.array(E_a,E_b)
        a,b =[a,b]-eta* gradiente
        error = E_a**2+E_b**2
        print(error)
        if (E > error or step == step_max):
            
            return a,b,eta,error,step
                
            
print(rgl_gradiente(1,1.5,0.00025))       
