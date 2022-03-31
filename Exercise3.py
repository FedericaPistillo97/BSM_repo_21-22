#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 10:57:41 2022

@author: chiaramarzi
"""

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

    
def myplot(t, X, t_no, X_no, outname):
    plt.figure()
    ax = sns.lineplot(x=t, y=X, color= 'red')
    ax = sns.lineplot(x=t_no, y=X_no)
    ax.set_title(outname)
    ax.set(xlabel='time (s)', ylabel=outname)
    plt.legend(['with controller', 'without controller'])
    plt.xlim(t_start,t_end)
    

# Common parameters    
q0 = (5*1000)/60 # TO COMPLETE
Psa0 = 100 # TO COMPLETE
Psv0 = 5 # TO COMPLETE
Pra0 = 4 # TO COMPLETE
Rsv = (Psv0-Pra0)/q0 # TO COMPLETE
Csa = 4 # TO COMPLETE
Csv = 111 # TO COMPLETE
Cra = 31 # TO COMPLETE
Poffset = 1.82 # TO COMPLETE

# Parameters of the simulation without controllers
Kr0 = (q0)/(Pra0-Poffset) # TO COMPLETE
Rsa0 = (Psa0-Psv0)/q0 # TO COMPLETE

# Parameters of the simulation with controllers
tauR= 15
GR= Rsa0/Psa0*1.5
tauK= 5
GK= Kr0/Psa0*10

# Time and hemorrage definition
DT= 0.1
t_start=0
t_end= 100
t= np.arange(t_start, t_end, DT)
L= np.size(t)
# Volume_emor=400
Emor= 8 # 50 seconds of hemhorrage
A= -Emor* np.ones(int(np.around(50/DT)))
B= np.zeros(L - int(np.around(50/DT)))
Ii= np.concatenate((A,B), axis=None)

# Allocation: Pressures and cardiac output without controllers
Psa_no= np.zeros(L)
Psv_no= np.zeros(L)
Pra_no= np.zeros(L)
Psa_no[0]= Psa0*1.0
Psv_no[0]= Psv0*1.0
Pra_no[0]= Pra0
q_no= np.zeros(L-1)

# Allocation: Pressures, Rsa and Kr, and cardiac output with controllers
Psa = np.zeros(L)
Psv = np.zeros(L)
Pra = np.zeros(L)
Psa[0] = Psa0*1.0
Psv[0] = Psv0*1.0
Pra[0] = Pra0
Rsa = np.zeros(L)
Rsa[0] = Rsa0
Kr = np.zeros(L)
Kr[0] = Kr0
q = np.zeros(L-1)


for j in range(L-1):
    # without controller
    q_no[j] =  Kr0*(Pra_no[j] - Poffset)
    dPsa = (q_no[j] - (Psa_no[j] - Psv_no[j])/Rsa0)/Csa
    dPsv = ((Psa_no[j] - Psv_no[j])/Rsa0 - (Psv_no[j]  - Pra_no[j])/Rsv +Ii[j])/Csv
    dPra = ((Psv_no[j]  - Pra_no[j])/Rsv - q_no[j])/Cra
    Psa_no[j+1] = Psa_no[j] + DT*dPsa
    Psv_no[j+1]= Psv_no[j] + DT*dPsv
    Pra_no[j+1] = Pra_no[j] + DT*dPra
    
    
    
    # with controllers
    q[j] =  Kr[j]*(Pra[j] - Poffset);
    #q[j] =  Kr0*(Pra[j] - Poffset);
    dPsa = (q[j] -(Psa[j]-Psv[j])/Rsa[j])/Csa
    dPsv = ((Psa[j] - Psv[j])/Rsa[j] - (Psv[j] - Pra[j])/Rsv +Ii[j])/Csv
    dPra = ((Psv[j]  - Pra[j])/Rsv - q[j])/Cra
    dRsa = (-(Rsa[j] - Rsa0) - GR * (Psa[j] - Psa0)) / tauR
    dKr = -(Kr[j]-Kr0)-GK*(Psa[j]-Psa0) / tauK
    Psa[j+1] = Psa[j] + DT*dPsa
    Psv[j+1]= Psv[j] + DT*dPsv
    Pra[j+1] = Pra[j] + DT*dPra
    Rsa[j+1] = Rsa[j] + DT*dRsa
    Kr[j+1] = Kr[j] + DT*dKr
    
V_no = Csa*Psa_no + Csv*Psv_no + Cra*Pra_no
V = Csa*Psa + Csv*Psv + Cra*Pra

# Callo myplot function with different parameters

myplot(t, Psa, t, Psa_no, 'Psa')
myplot(t, Psv, t, Psv_no, 'Psv')
myplot(t, Pra, t, Pra_no, 'Pra')
myplot(t[0:L-1], q, t[0:L-1], q_no, 'q')
myplot(t, V, t, V_no, 'V')
myplot(t, Rsa, [t[0], t[-1]], [Rsa0, Rsa0], 'Rsa')
myplot(t, Kr, [t[0], t[-1]], [Kr0, Kr0], 'K')







