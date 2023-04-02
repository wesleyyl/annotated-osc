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
    
    S0 + S0 -> S2 + S2; k1*S0*S0 #essential
    S1 + S0 -> S1; k2*S1*S0 #CVODE error
    S1 -> S0; k3*S1 #essential
    S2 -> S1+S1; k6*S2 #CVODE error
    S2 -> S0+S2; k7*S2 #essential
    S2 -> S0+S0; k9*S2 #essential
    
    #TRUNCATED TO 1 DECIMAL PLACE
    k1 = 33.6
    k2 = 37.7
    k3 = 11.5
    k6 = 20.6
    k7 = 139.4
    k9 = 68.1
    
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