# -*- coding: utf-8 -*-
"""
Created on Sat Apr  1 19:43:02 2023

@author: wesle
"""

import tellurium as te

r = te.loada ('''
    var S0
    var S1
    var S2
    S2 + S2 -> S0 + S0; k0*S2*S2
    S1 -> S1+S2; k1*S1
    S0 + S0 -> S2; k2*S0*S0
    #S1 -> S1+S1; k3*S1 #AUTOCATALYTIC
    S0 + S1 -> S2; k4*S0*S1
    S2 -> S1+S0; k5*S2
    k0 = 4.37305717305256
    k1 = 4.412803350435261
    k2 = 28.141111243128545
    k3 = 40.63493054188901
    k4 = 25.13686142202299
    k5 = 1.2112313147755178
    S0 = 1.0
    S1 = 5.0
    S2 = 9.0

''')

#m = r.simulate (0, 500, 500, ['time', 'S1'])
m = r.simulate (0, 500, 500)
r.plot()