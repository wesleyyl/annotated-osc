# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 01:08:59 2023

@author: wesle
"""

import tellurium as te

r = te.loada ('''
    var S0
    var S1
    var S2
    
    S2 -> S0+S1; k0*S2 #non-essential
    S0 + S1 -> S2; k1*S0*S1 #CVODE error
    S2 -> S0+S0; k2*S2 #CVODE error
    S2 -> S0; k3*S2 #non-essential
    S0 -> S1+S1; k4*S0 #essential
    #S1 -> S1+S1; k5*S1 #AUTOCATALYTIC
    #S1 -> S1+S1; k6*S1 #AUTOCATALYTIC
    S1 + S0 -> S0; k7*S1*S0 #essential
    S2 -> S0+S1; k8*S2 #non-essential
    
    
    k0 = 3.2700256090994673
    k1 = 4.7668201424368455
    k2 = 40.06428605163637
    k3 = 24.51206058735966
    k4 = 38.165285452165776
    k5 = 20.290560927925238
    k6 = 19.264273172605787
    k7 = 17.70387918296234
    k8 = 26.822302633571915
    
    
    S0 = 1.0
    S1 = 5.0
    S2 = 9.0

''')

#m = r.simulate (0, 500, 500, ['time', 'S1'])
m = r.simulate (0, 500, 500)
r.plot()