# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 15:14:02 2023

@author: wesle
"""

import tellurium as te

r = te.loada ('''
    var S0
    var S1
    var S2
    
    
    S0 + S2 -> S1; k0*S0*S2
    S2 -> S0+S2; k1*S2
    S2 + S0 -> S1; k2*S2*S0
    #S2 -> S2+S2; k3*S2 #AUTOCAT
    #S2 -> S2+S2; k4*S2 #AUTOCAT
    S1 + S2 -> S1; k5*S1*S2
    S0 + S1 -> S0; k6*S0*S1
    S2 -> S2+S1; k7*S2
    #S0 -> S0+S0; k8*S0 #AUTOCAT
    S0 + S0 -> S1 + S2; k9*S0*S0
    
    k0 = 57.0545508864937
    k1 = 11.563831291931283
    k2 = 1.962041922589867
    k3 = 61.72532037715531
    k4 = 52.32635916514403
    k5 = 3.6007916160551225
    k6 = 21.57195694430852
    k7 = 32.42863561479251
    k8 = 14.96009402154863
    k9 = 0.8627736211939456
    S0 = 1.0
    S1 = 5.0
    S2 = 9.0

''')

#m = r.simulate(0, 500, 500, ['time', 'S1'])
m = r.simulate(0, 10, 500)
r.plot()