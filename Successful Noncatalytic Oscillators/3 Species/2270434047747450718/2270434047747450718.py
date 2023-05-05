# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 21:55:49 2023

@author: wesle
"""

"""
Oscillator Variations:
    - comment out 1, 2, 3, 4, 5
    - comment out 1, 2, 4, 6
    - comment out 1, 3, 4, 5, 6
    - comment out 1, 2, 4, 5, 6, 8 (USE THIS VERSION)
    - comment out 1, 2, 3, 6
    - comment out 1, 2, 3, 4, 6, 8
    - comment out 1, 3, 4, 5, 7, 8
    - comment out 1, 3, 5, 7, 8
    

"""


import tellurium as te

r = te.loada ('''
    var S0
    var S1
    var S2
    
    
    S0 -> S1+S1; k0*S0 #CVODE error
    #S1 -> S1+S2; k1*S1 #non-essential 1
    S2 + S1 -> S1; k2*S2*S1 #CVODE error
    S2 -> S0+S2; k3*S2 #essential
    S0 + S0 -> S2 + S2; k4*S0*S0 #essential
    #S1 + S0 -> S1; k5*S1*S0 #non-essential 2
    S1 + S0 -> S1; k6*S1*S0 #non-essential 3
    #S2 -> S0+S2; k7*S2 #non-essential 4
    #S1 + S0 -> S1; k8*S1*S0 #non-essential 5
    #S1 -> S0; k9*S1 #non-essential 6
    S1 -> S0; k10*S1 #non-essential 7
    #S2 -> S0+S0; k11*S2 #essential 8
    
    
    
    #TRUNCATED TO 1 DECIMAL PLACE
    k0 = 14.6
    #k1 = 18.2
    k2 = 2.9
    k3 = 100.6
    k4 = 69.8
    #k5 = 62.2
    k6 = 10.9
    #k7 = 18.5
    #k8 = 7.2
    #k9 = 7.4
    k10 = 5.4
    #k11 = 34.5
    
    
    S0 = 1.0
    S1 = 5.0
    S2 = 9.0

''')

#m = r.simulate(0, 500, 500, ['time', 'S1'])
m = r.simulate(5, 100, 1000)
r.plot()