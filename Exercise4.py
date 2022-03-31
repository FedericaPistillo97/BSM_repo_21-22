#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 14:44:47 2022

@author: chiaramarzi
"""

# Complete the libraries importation
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

def my_plot(x, y, color, title, xlabel, ylabel):
    plt.figure()
    sns.lineplot(x = x, y = y, color = color)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    

# Compliances values from Table III of Albanese et al., 2016
Cl = 0.00127
Ct = 0.00238
Cb = 0.0131
CA = 0.2
Ccw = 0.2445
# Unstressed volumes from Table III of Albanese et al., 2016
Vul = 34.4/1000 #ml to L
Vut = 6.63/1000
Vub = 18.7/1000
VuA = 1263/1000
# Resistances values from Table III of Albanese et al., 2016
Rml = 1.021
Rlt = 0.3369
Rtb = 0.3063
RbA = 0.0817
dt = 0.0002
t_start= 0
t_end= 20
t= np.arange(t_start, t_end+dt, dt)
L=np.size(t)

# Simulation of 20 seconds

# State variables
P1 = np.zeros(L+1)
P2 = np.zeros(L+1)
P3 = np.zeros(L+1)
P4 = np.zeros(L+1)
P5 = np.zeros(L+1)

# Auxiliary variables
Pl = np.zeros(L)
Ppl = np.zeros(L)
Pt = np.zeros(L)
Pb = np.zeros(L)
PA = np.zeros(L)

# Volumes
Vl = np.zeros(L)
Vt = np.zeros(L)
Vb = np.zeros(L)
VA = np.zeros(L)
VD = np.zeros(L)

# Natural breath definition
T = 5 # period of the natural breath
Amus= 3
Pmus= Amus*(np.cos(2*np.pi/T*t)-1)
Pm= np.zeros(L)

# Initial conditions
Ppl[0] = -5
P5[0] = Ppl[0] - Pmus[0]
VA[0] = 2.3 - VuA
P4[0] = VA[0]/CA

for j in range(L):
    Pl[j] = P1[j]
    Ppl[j] = P5[j] + Pmus[j]   
    Pt[j] = P2[j] + Ppl[j]
    Pb[j] = P3[j] + Ppl[j]
    PA[j] = P4[j] + Ppl[j]
    
      
    Vl[j] = Cl*Pl[j] + Vul
    Vt[j] = Ct*(Pt[j] - Ppl[j]) + Vut
    Vb[j] = Cb*(Pb[j] - Ppl[j]) + Vub
    VA[j] = CA*(PA[j] - Ppl[j]) + VuA
    VD[j] = Vl[j] + Vt[j] + Vb[j]
    
    dP1 = 1/Cl* ( (Pm[j] - Pl[j])/Rml - (Pl[j] - Pt[j])/Rlt )
    dP2 = 1/Ct* ( (Pl[j] - Pt[j])/Rlt - (Pt[j] - Pb[j])/Rtb )
    dP3 = 1/Cb* ( (Pt[j] - Pb[j])/Rtb - (Pb[j] - PA[j])/RbA )
    dP4 = 1/CA* (Pb[j] - PA[j])/RbA
    dP5 = 1/Ccw* (Pl[j] - Pt[j])/Rlt
    
    P1[j+1] = P1[j] + dP1*dt
    P2[j+1] = P2[j] + dP2*dt
    P3[j+1] = P3[j] + dP3*dt
    P4[j+1] = P4[j] + dP4*dt
    P5[j+1] = P5[j] + dP5*dt
               
# Pressures plots
f, ax = plt.subplots(2, 2, figsize=(10,10))
sns.lineplot(x=t, y=Pmus, ax=ax[0][0])
ax[0][0].set_title("Muscle pressure")
ax[0][0].set(xlabel='time (s)', ylabel="$cmH_2O$")
sns.lineplot(x=t, y=Ppl, ax=ax[0][1])
ax[0][1].set_title('pleural pressure')
ax[0][1].set(xlabel='time (s)', ylabel="$cmH_2O$")
sns.lineplot(x=t, y=PA, ax=ax[1][0])
ax[1][0].set_title('alveolar pressure')
ax[1][0].set(xlabel='time (s)', ylabel="$cmH_2O$")
# Volumes plots
f, ax = plt.subplots(2, 2, figsize=(10,10))
ax1, ax2, ax3, ax4 = ax.flatten()
sns.lineplot(x=t, y=VA+VD, ax=ax1)
ax1.set_title('total volume')
ax1.set(xlabel='time (s)', ylabel='L')
sns.lineplot(x=t, y=VA, ax=ax2)
ax2.set_title('alveolar volume')
ax2.set(xlabel='time (s)', ylabel='L')
sns.lineplot(x=t, y=VD, ax=ax3)
ax3.set_title('dead volume')
ax3.set(xlabel='time (s)', ylabel='L')


# Alveolar ventilation  (at equilibrium)
Vent = (np.max(VA[int(np.round(5/dt,0)):-1]) - np.min(VA[int(np.round(5/dt,0)):-1]))*60/T # to exclude the first part of the signal
print("Ventiliation:", Vent)
