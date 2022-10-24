# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 12:09:50 2022

@author: Enrique Rojas
"""


import numpy as np
import pandas as pd


#%%

# Carga y normalizacion de la base de datos

"""
Tomemos como entradas el monto solicitado (normalizado), la carga que implica al
salario el pago de la mensualidad y la antigüedad laboral al contratar 
(normalizada).
"""
data = np.array((pd.read_excel('PercMultAplicado.xlsx').replace("SI",1)).replace("NO",0))
monto_norm, pago_salario, antigüedad = data[:,1] /30000, data[:,2]/data[:,5], data[:,6]/180
data = np.float64(np.array([monto_norm,pago_salario,antigüedad,data[:,-1] ]).T)

#%%

# Separamos la base de datos en 70-30 de relación entrenamiento-prueba

training = data[:700]
test = data[700:]

#%%

# Hiperparámetros

alpha = 0.025
a =  1

#%%

# Arquitectura del perceptrón

"Entradas"
N = 3
"Patrones de aprendizaje"
Q = len(training)
"Neuronas" 
L = len(training)
"Salidas conocidas"
M = 1

#%%

# Valores del perceptron

# Valores de entrada y salida
x = training[:,:3]
d = training[:,-1]
y = np.zeros([Q,M])

# Inicializacion aleatorea de los pesos
W_h = np.random.uniform(-1,1,(L,N))
W_o = np.random.uniform(-1,1,(M,L))
step = 0

#%%

#Entrenamiento del modelo (ajuste de los pesos)

while(True):


#Forward

    for i in range(Q):
        net_h = W_h @ x[i].transpose()
        y_h = np.reshape(1/(1+np.exp(-a*net_h)),(L,1))
        net_o = W_o @ y_h
        y = 1 / (1 + np.exp(-a*net_o) )
    
#Backward

        d_o = ( np.reshape(d[i],(M,1)) - y)  *  y * (1 - y)
        d_h = y_h * (1 - y_h) * ( np.transpose(W_o) @ d_o )
        W_h +=  alpha * d_h  @ np.reshape(x[i],(1,N))       
        W_o +=  alpha * d_o  @ y_h.transpose() 
        step += 1
        
    if  np.linalg.norm(d_o) < 10**-8: 
        break   

#%%
# Testing

Q_t = len(test)
y_test = np.zeros([Q_t,M])
x_test = test[:,:N]
d_test = test[:,-1]
res = []
for i in range(Q_t):
    net_h = W_h @ x_test[i].transpose()
    y_h = np.reshape(1/(1+np.exp(-a*net_h)),(L,1))
    net_o = W_o @ y_h
    y_test = 1 / (1 + np.exp(-a*net_o) )
    res = np.append(res,np.round(y_test))

res = np.reshape(res,(Q_t,M))    

#%%
# Validacion 

validation = []

for i in range(len(d_test)):
    if d_test[i] == res[i]:
        v = 1
        validation.append(v)
    else:
        v = 0
        validation.append(v)

accuracy = 100*np.round(sum(validation)/len(d_test),4)       

#%%



print(f'\n<--------------------------->\n|-  Accuracy: {accuracy}%\n|-  Error {d_o} \n|-  Iteraciones:{step}\n<--------------------------->')