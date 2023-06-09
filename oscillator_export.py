# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import tellurium as te
import os
import tempfile


r = te.loada('''
    var S0
    var S1
    var S2
    
    
    S1 -> S1+S0; k1*S1 #CVODE error
    S1 + S2 -> S1; k3*S1*S2 #CVODE error 
    S2 -> S2+S2; k4*S2 #essential
    S2 + S0 -> S1 + S1; k5*S2*S0 #CVODE error
    S1 + S0 -> S2; k6*S1*S0 #essential
    S0 + S2 -> S2; k7*S0*S2 #essential
    S2 + S0 -> S0; k11*S2*S0 #non-essential DUPLICATE
    S0 + S2 -> S0; k12*S0*S2 #non-essential DUPLICATE
    S1 -> S0+S2; k15*S1 #non-essential
    
    
    k1 = 27.929662407640407
    k3 = 3.2704908664672176
    k4 = 93.62898101746234
    k5 = 13.960309400490441
    k6 = 25.757652525550572
    k7 = 22.70845184345882
    k11 = 71.84774049157912
    k12 = 40.23820335919722
    k15 = 14.667726603954245
    
    
    S0 = 1.0
    S1 = 5.0
    S2 = 9.0
''')

#m = r.simulate(0, 500, 500, ['time', 'S1', 'S2'])
m = r.simulate(0, 20, 500)
r.plot()


#temp_dir = tempfile.mkdtemp()
temp_dir = os.path.dirname(os.path.abspath( __file__ ))
file_path = os.path.join(temp_dir, 'oscillator.xml')
r.exportToSBML(file_path)