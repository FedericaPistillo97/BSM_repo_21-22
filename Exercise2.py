#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 13:13:06 2022

@author: chiaramarzi
"""

import matplotlib.pyplot as plt
import numpy as np
from numpy.linalg import eig, solve # To compute eigenvectors and eigenvalues
import seaborn as sns
from scipy.linalg import expm


q0 = # TO COMPLETE  # cardiac in ml/s
Psa0 = 100
Psv0 = 5
Pra0 = 4
Csa = 4
Csv = 111
Cra = 31

# Computation of remaining parameters at equilibrium
Kr = # TO COMPLETE
Rsa = # TO COMPLETE
Rsv = # TO COMPLETE

### Exponential function of A
A_00 = # TO COMPLETE
A_01 = # TO COMPLETE
A_02 = # TO COMPLETE
A_10 = # TO COMPLETE
A_11 = # TO COMPLETE
A_12 = # TO COMPLETE
A_20 = # TO COMPLETE
A_21 = # TO COMPLETE
A_22 = # TO COMPLETE
A = np.array([[A_00, A_01, A_02], [A_10, A_11, A_12], [A_20, A_21, A_22]]) # Check A type and shape, by using type(A) and np.shape(A)
X0 = np.array([Psa0*1.5, Psv0, Pra0]) # Check X0 type and shape, by using type(X0) and np.shape(X0)
DT = # TO COMPLETE
t_start = 0
t_end = 50
t = np.arange(t_start, t_end, DT) 
L = np.size(t)
X_exp = np.zeros((3,L))
for j in range(L):
    X_exp[:,j] = # TO COMPLETE
    
### Eigenvectors and eigenvalues of A
w,v = # TO COMPLETE
lambda1 = # TO COMPLETE
lambda2 = # TO COMPLETE
lambda3 = # TO COMPLETE
alpha = # TO COMPLETE
X_eig = # TO COMPLETE

# Euler's method    
Ii = np.zeros(L) 
Psa = np.zeros(L)
Psv = np.zeros(L)
Pra = np.zeros(L)
q = np.zeros(L-1)
Psa[0] = # TO COMPLETE
Psv[0] = # TO COMPLETE
Pra[0] = # TO COMPLETE


for j in range(0,L-1): 
    q[j] =  # TO COMPLETE
    dPsa = # TO COMPLETE
    dPsv = # TO COMPLETE
    dPra = # TO COMPLETE
    Psa[j+1] = # TO COMPLETE
    Psv[j+1]= # TO COMPLETE
    Pra[j+1] = # TO COMPLETE
    
    
ax = plt.figure()
ax = sns.lineplot(x=t, y=Psa)
ax = sns.lineplot(x=t, y=X_exp[0,:], color='red')
ax = sns.lineplot(x=t, y=X_eig[0,:], color='cyan', linestyle='dashed')
ax.set_title("Systemic arterial pressure")
ax.set(xlabel='time (s)', ylabel='Pressure (mmHg)')
plt.legend(['Euler','Exponential', 'Eigenvectors'])
plt.xlim(t_start,t_end)

ax = plt.figure()
ax = sns.lineplot(x=t, y=Psv)
ax = sns.lineplot(x=t, y=X_exp[1,:], color='red')
ax = sns.lineplot(x=t, y=X_eig[1,:], color='cyan', linestyle='dashed')
ax.set_title("Systemic venous pressure")
ax.set(xlabel='time (s)', ylabel='Pressure (mmHg)')
plt.legend(['Euler','Exponential', 'Eigenvectors'])
plt.xlim(t_start,t_end)

ax = plt.figure()
ax = sns.lineplot(x=t, y=Pra)
ax = sns.lineplot(x=t, y=X_exp[2,:], color='red')
ax = sns.lineplot(x=t, y=X_eig[2,:], color='cyan', linestyle='dashed')
ax.set_title("Right atrial pressure")
ax.set(xlabel='time (s)', ylabel='Pressure (mmHg)')
plt.legend(['Euler','Exponential', 'Eigenvectors'])
plt.xlim(t_start,t_end)