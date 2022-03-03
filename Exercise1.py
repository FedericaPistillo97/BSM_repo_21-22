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
Psv0 = 
Pra0 = 
q0 =   # cardiac output in ml/s 
Csa = 4
Csv = 
Cra = 
Poffset = 

# Values of the remaing parameters in order to ensure the assigned eqiuilibrium conditions:
Kr = 
Rsa = 
Rsv = 

DT = 0.1
t = np.arange(0, 100+DT, DT) # Matlab: t=[0:DT:100];
L=np.size(t)
Volume_emor =     # 0 for null Ii input. A value between 50 and 500 ml for the hemorrage
Emor = Volume_emor/50 # 50 seconds of hemhorrage 
A = np.zeros(int(np.around(10/DT)))
B = -Emor* np.ones(int(np.around(50/DT)))
C = np.zeros(L - int(np.around(60/DT)))
Ii = np.concatenate((A, B, C), axis=None)

Psa = np.zeros(L)
Psv = np.zeros(L)
Pra = np.zeros(L)
Psa[0] = 
Psv[0] = 
Pra[0] = 
V = np.zeros(L-1)
q = np.zeros(L-1)

for j in range(0,L-1): # Matlab: for j = 1:L-1 
    V[j] = 
    q[j] =  
    dPsa = 
    dPsv = 
    dPra = 
    Psa[j+1] = 
    Psv[j+1]= 
    Pra[j+1] = 

# Psa plot    
ax = sns.lineplot(x=t, y=Psa, color = 'green')
ax.set_title("Systemic arterial pressure")
ax.set(xlabel='time (s)', ylabel='Pressure (mmHg)')
ax.ticklabel_format(useOffset=False)

# Psv plot

# Pra plot

# q plot

# V plot



