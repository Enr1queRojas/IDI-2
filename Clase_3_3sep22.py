# -*- coding: utf-8 -*-
"""
Created on Sat Sep  3 11:23:41 2022

@author: Enrique Rojas
"""


import sympy as sp


x,y = sp.symbols('x'), sp.symbols('y')
x0,y0= [1.0,1.0]
F = sp.Matrix([x+2*y**2, 2*x**2 - y -5])
J_inv = F.jacobian([x,y]).inv()

www = J_inv.subs([(x,5),(y,3)])

