# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 01:04:11 2023

@author: wesle
"""

import tellurium as te

r = te.loada ('''
    var S0
    var S1
    var S2
    S0 + S2 -> S1 + S1; k0*S0*S2
    S0 + S1 -> S1; k1*S0*S1
    S1 + S0 -> S2; k2*S1*S0
    S1 -> S1+S1; k3*S1 #AUTOCATALYTIC
    S2 + S1 -> S0 + S0; k4*S2*S1
    S2 -> S0; k5*S2
    S2 -> S0; k6*S2
    k0 = 3.5509839611691976
    k1 = 18.135124560900387
    k2 = 39.700476024268525
    k3 = 41.002393505831286
    k4 = 1.730970302823081
    k5 = 7.990774900446527
    k6 = 16.324501545518793
    S0 = 1.0
    S1 = 5.0
    S2 = 9.0

''')

#m = r.simulate (0, 500, 500, ['time', 'S1'])
m = r.simulate (0, 1000, 1000)
r.plot()