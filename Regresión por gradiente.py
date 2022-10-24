# -*- coding: utf-8 -*-
"""
Created on Sat Sep 24 12:03:40 2022

@author: Enrique Rojas
"""
import numpy as np 
import matplotlib.pyplot as plt


step_max = 10000
E = 10**-5

def rgl_gradiente(a,b,eta):
    
    eta= eta
    x = np.arange(0,10)
    y = x+3*np.random.uniform(0,1)
    step = 0 
    E_a= np.average((a*x+b-y)*x)
    E_b= np.average(a*x+b-y)
    while True:
        step += 1
        error = 0
        gradiente = np.array(E_a,E_b)
        a,b =[a,b]-eta* gradiente
        E_a= np.average((a*x+b-y)*x)
        E_b= (np.average(a*x+b-y))        
        error += (E_a-E_b)**2
        if (E > error or step == step_max):
            plt.plot(x,y, 'yo',(a*x+b))
            return a,b,eta,error,step
                
            
print(rgl_gradiente(1,1.5,0.0025))       

