# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 17:15:02 2022

@author: Enrique Rojas
"""

import numpy as np
import matplotlib.pyplot as plt

class k_means:
    
    def __init__(self,n,k):
    
        self.data = np.random.uniform(1,100,size=(n,2))
        max_lim,min_lim = round(np.max(self.data)),round(np.min(self.data))
        self.c = np.random.uniform(min_lim,max_lim,size=(k,2))
        self.step = 0
        

    def distancias(self,data,c):        
        indx_centroide = []
        for i in range(len(data)):
            distancias = []
            for j in range(len(c)):        
                dist = np.linalg.norm(data[i]-c[j],2)
                distancias = np.append(distancias,dist)       
            pos = np.argmin(distancias)
            indx_centroide = np.append(indx_centroide,pos)
        self.indx_centroide = indx_centroide
        return  self.indx_centroide

    def nuevos_centros(self,data,c,indx):
        self.n_cen =[] 
        for i in range(len(c)):
            self.old_centroide = c.copy()
            cen = np.mean(data[indx == i],axis = 0)
            self.n_cen.append(cen)
        self.n_cen = np.stack(self.n_cen,axis = 0)
        self.c = self.n_cen
        return self.c


    def adjustment(self):
        while True:
           
            indx_centroide = p.distancias(p.data,p.c)
            nuevos = p.nuevos_centros(p.data,p.c,p.indx_centroide)
            viejos = p.old_centroide
            
            if np.equal(nuevos,viejos).all():
                class_fin = np.column_stack((p.data,(p.indx_centroide+1)))
                print(f'    Iteraciones :{p.step}')
                print(f'\n    Datos Clasificados \n{class_fin}')
                plt.scatter(p.data[:,0],p.data[:,1])
                plt.scatter(nuevos[:,0],nuevos[:,1])
                plt.show()
                break
            else:
                p.step += 1
                indx_centroide = p.distancias(p.data,p.c)
                nuevos = p.nuevos_centros(p.data,p.c,p.indx_centroide)
                viejos = p.old_centroide
            
p = k_means(50,8)
p.adjustment()