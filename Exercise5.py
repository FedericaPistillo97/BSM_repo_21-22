#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 08:23:54 2022

@author: chiaramarzi
"""

from matplotlib import pyplot as plt
import numpy as np
import seaborn as sns
sns.set_style("white")

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
Vul = 34.4/1000 # ml to L
Vut = 6.63/1000
Vub = 18.7/1000
VuA = 1263/1000
# Resistances values from Table III of Albanese et al., 2016
Rml = 1.021
Rlt = 0.3369
Rtb = 0.3063
RbA = 0.0817
dt = 0.0002 

# Simulation of 20 seconds
t_start = 0
t_end = 20
t = np.arange(t_start, t_end+dt, dt) 
L = np.size(t) 

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
dV = np.zeros(L)
dVa = np.zeros(L)
dVd = np.zeros(L)
Vl = np.zeros(L)
Vt = np.zeros(L)
Vb = np.zeros(L)
VA = np.zeros(L)
VD = np.zeros(L)

# breath definition
T = 5 # period of the natural breath
ventilation = "actual natural" # TO COMPLETE
if ventilation == "natural":
    print("Natural breath")
    Amus=3
    Pmus=Amus*(np.cos(2*np.pi/T*t)-1)
    Pm=np.zeros(L)
    # TO COMPLETE
elif ventilation == "natural with increased amplitude":
    print("natural breath with increased amplitude")
    Amus=3*2
    Pmus= Amus*(np.cos(2*np.pi/T*t)-1)  
    Pm = np.zeros(L)
    # TO COMPLETE
elif ventilation == "natural with increased frequency":
    print("natural breath with increased frequency")
    Amus = 3
    T = 5/2
    Pmus= Amus*(np.cos(2*np.pi/T*t)-1)  
    Pm = np.zeros(L)
    # TO COMPLETE
elif ventilation == "artificial":
    print("Artificial ventilation")
    Am = -3
    Pm= Am*(np.cos(2*np.pi/T*t)-1)  
    Pmus = np.zeros(L)
    # TO COMPLETE
elif ventilation == "mixed":
    print("Mixed ventilation")
    Amus = 1
    fi = 0.5*np.pi
    Pmus = (Amus*np.cos(2*np.pi/T*t+fi)-Amus)
    Am = -3
    Pm = Am*(np.cos(2*np.pi/T*t)-1)
    # TO COMPLETE
elif ventilation == "actual natural":
    print("Actual natural ventilation")
    Pm = np.zeros(L)
    Amus = -6
    TI = 0.4 * T
    TE = T - TI
    tau = TE/5
    tti = np.arange(0, TI, dt) 
    PmusI = -Amus/TI/TE*tti*tti + Amus*T/TI/TE*tti 
    tte=np.arange(TI, T, dt) 
    PmusE =Amus/(1-np.exp(-TE/tau))*(np.exp(-(tte-TI)/tau)-np.exp(-(TE/tau)))
    Pmustot = np.concatenate((PmusI, PmusE), axis=None) # one cycle
    Pmus = np.concatenate((Pmustot, Pmustot, Pmustot, Pmustot, Pmustot[0]), axis=None)
    # TO COMPLETE
else:
    print("The options are: natural; natural with increased amplitude; natural with increased frequency; artificial; mixed; actual natural")
    

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
    
    dV[j] = (Pm[j] - Pl[j])/Rml   
    dVa[j] = (Pb[j] - PA[j])/RbA
    dVd[j] = dV[j] - dVa[j]    
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
my_plot(t, Pmus, 'red', 'Muscle pressure', 'time (s)', "$cmH_2O$")
my_plot(t, Pm, 'cyan', 'Mouth pressure', 'time (s)', "$cmH_2O$")
my_plot(t, Ppl, 'green', 'Pleural pressure', 'time (s)', "$cmH_2O$")
my_plot(t, PA, 'black', 'Alveolar pressure', 'time (s)', "$cmH_2O$")
my_plot(t, Pt, 'yellow', 'Tracheal pressure', 'time (s)', "$cmH_2O$")
my_plot(t, Pb, 'orange', 'Bronchial pressure', 'time (s)', "$cmH_2O$")

# Volumes plots
my_plot(t, VA+VD, 'magenta', 'Total volume', 'time (s)', "L")
my_plot(t, VA, 'blue', 'Alveolar volume', 'time (s)', "L")
my_plot(t, VD, 'gray', 'Dead volume', 'time (s)', "L")

# Alveolar ventilation  (at equilibrium)
Vent = (np.max(VA[int(np.round(5/dt,0)):-1]) - np.min(VA[int(np.round(5/dt,0)):-1]))*60/T # to exclude the first part of the signal wich is transitional
print("Ventiliation:", Vent)