# -*- coding: utf-8 -*-
"""
Created on Sat Apr  1 18:58:53 2023

@author: wesle
"""

import tellurium as te

r = te.loada ('''
    var S0
    var S1
    var S2
    S2 + S1 -> S1; k0*S2*S1 #CVODE Error
    S2 + S0 -> S1 + S1; k1*S2*S0 #CVODE Error
    #S2 -> S2+S2; k2*S2 #Important - AUTOCATALYTIC!!
    S1 -> S0+S2; k3*S1 #CVODE Error
    
    
    ## NEED 1 OUT OF 3 OF THE NON-ESSENTIAL REACTIONS
    S0 -> S2; k4*S0 #Non-essential
    S0 -> S2; k5*S0 #Non-essential
    S0 -> S2+S2; k6*S0 #Non-essential
    
    
    S2 + S0 -> S0; k7*S2*S0 #Important
    
    ## EACH TRUNCATED TO 2 DECIMAL PLACES
    k0 = 4.47
    k1 = 2.15
    k2 = 89.15
    k3 = 20.03
    k4 = 23.60
    k5 = 30.83
    k6 = 25.90
    k7 = 43.85
    S0 = 1.0
    S1 = 5.0
    S2 = 9.0

''')

#m = r.simulate (0, 500, 500, ['time', 'S1'])
m = r.simulate (0, 500, 500)
r.plot()
