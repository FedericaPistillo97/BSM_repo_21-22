#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 14:29:05 2022

@author: chiaramarzi
"""

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Equlibrium values
Psa0 = 100
Psv0 = 5
Pra0 = 4
q0 = 5*1000/60   # cardiac output in ml/s 
Csa = 4
Csv = 111
Cra = 31
Poffset = 1.82

# Values of the remaing parameters in order to ensure the assigned eqiuilibrium conditions:
Kr = q0/(Pra0-Poffset)
Rsa = (Psa0-Psv0)/q0
Rsv = (Psv0-Pra0)/q0

DT = 0.1
t = np.arange(0, 100+DT, DT) # Matlab: t=[0:DT:100];
L=np.size(t)
Volume_emor = 0   # 0 for null Ii input. A value between 50 and 500 ml for the hemorrage
Emor = Volume_emor/50 # 50 seconds of hemhorrage 
A = np.zeros(int(np.around(10/DT)))
B = -Emor* np.ones(int(np.around(50/DT)))
C = np.zeros(L - int(np.around(60/DT)))
Ii = np.concatenate((A, B, C), axis=None)

Psa = np.zeros(L)
Psv = np.zeros(L)
Pra = np.zeros(L)
Psa[0] = Psa0
Psv[0] = Psv0
Pra[0] = Pra0
V = np.zeros(L-1)
q = np.zeros(L-1)

for j in range(0,L-1): # Matlab: for j = 1:L-1 
    V[j] = Cra*Pra[j] + Csa*Psa[j] + Csv*Psv[j]
    q[j] = Kr*(Pra[j]-Poffset) 
    dPsa = (q[j]-(Psa[j]-Psv[j])/Rsa)/Csa
    dPsv = ((Psa[j]-Psv[j])/Rsa-(Psv[j]-Pra[j])/Rsv+Ii[j])/Csv
    dPra = ((Psv[j]-Pra[j])/Rsv-q[j])/Cra
    Psa[j+1] = Psa[j]+DT*dPsa
    Psv[j+1]= Psv[j]+DT*dPsv
    Pra[j+1] = Pra[j]+DT*dPra

# Psa plot    
ax = sns.lineplot(x=t, y=Psa, color = 'green')
ax.set_title("Systemic arterial pressure")
ax.set(xlabel='time (s)', ylabel='Pressure (mmHg)')
ax.ticklabel_format(useOffset=False)

# Psv plot

# Pra plot

# q plot

# V plot



