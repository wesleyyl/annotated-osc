# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import tellurium as te

r = te.loada('''
    var S0
    var S1
    var S2
    var S3
    #S2 + S0 -> S1 + S3; k0*S2*S0 #non-essential
    S3 -> S2+S1; k1*S3 #essential
    S3 + S0 -> S3; k2*S3*S0 #CVODE error
    S1 + S2 -> S2; k3*S1*S2 #CVODE error
    S1 -> S0+S0; k4*S1 #essential
    S1 -> S3+S3; k5*S1 #CVODE error
    S2 -> S1+S0; k6*S2 #essential
    S1 -> S0+S0; k7*S1 #essential
    S0 + S2 -> S1 + S3; k8*S0*S2 #essential
    S0 + S2 -> S3 + S1; k9*S0*S2 #non-essential
    #S0 -> S1; k10*S0 #non-essential
    #S0 -> S1+S1; k11*S0 #non-essential
    
    
    #TRUNCATED TO 2 DECIMAL PLACES
    k0 = 14.62
    k1 = 30.59
    k2 = 2.84
    k3 = 35.00
    k4 = 35.54
    k5 = 8.36
    k6 = 31.62
    k7 = 25.73
    k8 = 36.42
    k9 = 25.73
    #k10 = 18.83
    #k11 = 45.51
    
    S0 = 1.0
    S1 = 5.0
    S2 = 9.0
    S3 = 3.0
''')

#m = r.simulate(0, 500, 500, ['time', 'S1', 'S2'])
m = r.simulate(0, 20, 500)
r.plot()


