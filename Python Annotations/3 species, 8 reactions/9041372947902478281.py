# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 21:00:07 2023

@author: wesle
"""

import tellurium as te

r = te.loada ('''
    var S0
    var S1
    var S2
    
    
    #S0 -> S1+S2; k0*S0 #non-essential
    S1 -> S1+S0; k1*S1 #CVODE error
    #S0 + S1 -> S2 + S2; k2*S0*S1 #non-essential
    S1 + S2 -> S1; k3*S1*S2 #CVODE error 
    #S2 -> S2+S2; k4*S2 #essential - AUTOCAT!
    S2 + S0 -> S1 + S1; k5*S2*S0 #CVODE error
    S1 + S0 -> S2; k6*S1*S0 #essential
    S0 + S2 -> S2; k7*S0*S2 #essential
    #S0 + S0 -> S0; k8*S0*S0 #non-essential
    #S0 + S1 -> S1; k9*S0*S1 #non-essential
    #S0 + S2 -> S0; k10*S0*S2 #non-essential
    S2 + S0 -> S0; k11*S2*S0 #non-essential DUPLICATE
    S0 + S2 -> S0; k12*S0*S2 #non-essential DUPLICATE
    #S0 + S2 -> S0; k13*S0*S2 #non-essential DUPLICATE
    #S0 + S2 -> S0; k14*S0*S2 #non-essential DUPLICATE
    S1 -> S0+S2; k15*S1 #non-essential
    
    
    #k0 = 21.227901797576774
    k1 = 27.929662407640407
    #k2 = 6.246524718586304
    k3 = 3.2704908664672176
    k4 = 93.62898101746234
    k5 = 13.960309400490441
    k6 = 25.757652525550572
    k7 = 22.70845184345882
    #k8 = 71.07835794659513
    #k9 = 10.951512079669206
    #k10 = 10.848840528822949
    k11 = 71.84774049157912
    k12 = 40.23820335919722
    #k13 = 40.38704243077628
    #k14 = 23.866018276990474
    k15 = 14.667726603954245
    
    
    S0 = 1.0
    S1 = 5.0
    S2 = 9.0

''')

#m = r.simulate(0, 500, 500, ['time', 'S1'])
m = r.simulate(0, 0.5, 500)
r.plot()