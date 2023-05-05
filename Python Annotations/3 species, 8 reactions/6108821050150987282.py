# -*- coding: utf-8 -*-
"""
Created on Thu May  4 17:21:37 2023

@author: wesle
"""

import tellurium as te

r = te.loada ('''
    var S0
    var S1
    var S2
    S2 + S1 -> S0; k0*S2*S1
    #S1 -> S1+S1; k1*S1 #AUTOCAT
    S0 + S1 -> S0; k2*S0*S1
    S2 -> S1+S1; k3*S2
    S0 -> S2; k4*S0
    S2 + S0 -> S1; k5*S2*S0
    S0 -> S2+S2; k6*S0
    S1 + S2 -> S2; k7*S1*S2
    S2 + S1 -> S2; k8*S2*S1
    k0 = 19.647087300546065
    k1 = 43.21629736472226
    k2 = 22.840154884218205
    k3 = 42.73154854869749
    k4 = 28.204598901217977
    k5 = 28.43866583998443
    k6 = 22.012541768254987
    k7 = 6.352619827373057
    k8 = 62.598740220605556
    S0 = 1.0
    S1 = 5.0
    S2 = 9.0

''')

#m = r.simulate (0, 500, 500, ['time', 'S1'])
m = r.simulate (0, 500, 500)
r.plot()