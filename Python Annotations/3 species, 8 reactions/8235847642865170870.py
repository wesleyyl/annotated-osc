# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 01:13:26 2023

@author: wesle
"""

import tellurium as te

r = te.loada('''
    var S0
    var S1
    var S2
    
    #S1 -> S1+S0; k0*S1 #non-essential
    S0 + S0 -> S2 + S2; k1*S0*S0 #essential
    S1 + S0 -> S1; k2*S1*S0 #CVODE error
    S1 -> S0; k3*S1 #essential
    #S0 -> S0+S0; k4*S0 #AUTOCATALYTIC & NON-ESSENTIAL
    #S1 + S2 -> S0 + S0; k5*S1*S2 #non-essential
    S2 -> S1+S1; k6*S2 #CVODE error
    S2 -> S0+S2; k7*S2 #essential
    #S2 -> S0+S2; k8*S2 #non-essential
    S2 -> S0+S0; k9*S2 #essential
    
    #TRUNCATED TO 1 DECIMAL PLACE
    #k0 = 9.5
    k1 = 33.6
    k2 = 37.7
    k3 = 11.5
    #k4 = 42.8
    #k5 = 0.6
    k6 = 20.6
    k7 = 139.4
    #k8 = 16.5
    k9 = 68.1
    
    S0 = 1.0
    S1 = 5.0
    S2 = 9.0
''')

#m = r.simulate(0, 500, 500, ['time', 'S1', 'S2'])
m = r.simulate(0, 0.5, 500)
r.plot()