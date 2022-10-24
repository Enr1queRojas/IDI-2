# -*- coding: utf-8 -*-
"""
Created on Mon Aug 29 15:22:42 2022

@author: Enrique Rojas
"""
from sympy import symbols, diff
import sympy as sp


x = sp.Symbol("x")
E = 10**-4

def nr_root(function,valor_inicial):
    x = symbols("x")
    print('\n\n*** NEWTON RAPHSON METHOD IMPLEMENTATION ***')
    x0 = float(valor_inicial)
    f = function
    x1 = 0
    step = 1
    while x0 != x1:
        x1 = x0
        x0 = x0 - float((f.subs(x,x0))/(diff(f,x).subs(x,x0)))
        if ( diff(f,x).subs(x,x0) == 0):
            print("Se indetermina la division")
            break
        if x0 == x1 or step > 1000:
            exactitud = abs((0-f.subs(x,x0)).evalf())
            if exactitud<E:
                print(f"\nIteraciones: {step}, x= {x0:0.10}")
                print(f"La Exactitud:{exactitud} \nCumple el error (es menor que {E})")
                print("\n============================================")
                break
            else:
                print(f"Iteraciones: {step}, x= {x0:0.10}, La Exactitud:{exactitud} ")                
                print(f"\nIteraciones: {step}, x= {x0:0.10}")
                print(f"La Exactitud:{exactitud} \nEl error (excede,es mayor que {E}){E})")
                print("\n============================================")        
        step += 1
        
    return x0
    

    
# f1 =nr_root( x**3 - 2*x**2 - 5,3)
# f2 = nr_root(x - sp.cos(x),1)
# f3 = nr_root(x - 0.8 - 0.2*sp.sin(x),1)
# f4 = nr_root(sp.ln(x - 1) + sp.cos(x - 1),1.3)
# f5 = nr_root(sp.exp(x) - 3*x**2,1)

# f6 = nr_root(x**1/2 - 5,2.3)
# f7 = nr_root(((sp.ln(x**2+1))-(sp.exp(0.4*x)*sp.cos(sp.pi*x))),-0.24)
