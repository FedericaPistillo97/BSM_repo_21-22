#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 10:35:28 2022

@author: chiaramarzi
"""

from matplotlib import pyplot as plt
import numpy as np
import seaborn as sns
sns.set_style("white")

def my_plot():
    # TO COMPLETE
    
# Sodium parameters  
ki_Na = # TO COMPLETE
g_Na = # TO COMPLETE
u_Na = # TO COMPLETE
ke_Na = # TO COMPLETE

# Urea parameters 
ki_U = # TO COMPLETE
g_U = # TO COMPLETE
u_U = # TO COMPLETE
ke_U = # TO COMPLETE

# Potassium parameters 
ki_K = # TO COMPLETE
g_K = # TO COMPLETE
u_K = # TO COMPLETE
ke_K = # TO COMPLETE

# Other parameters and Euler's method initialization (remember that time is in minutes)
qf0 = # TO COMPLETE # Ultradiffusion
d0 = # TO COMPLETE # dialysance
I = # TO COMPLETE  # Patient is not drinking
Vp = # TO COMPLETE   # Patient's liquid volume at the begenning of the dialysis
cd_Na = # TO COMPLETE # Na in dialysis bath
cd_U = # TO COMPLETE0 # Urea in dialysis bath
cd_K = # TO COMPLETE # K in dialysis bath

dialysis_hours = 4
dt = 0.2  #minuti
days = # TO COMPLETE
t_start = # TO COMPLETE
t_end = # TO COMPLETE
t = np.arange(t_start, t_end+dt, dt) 
L = np.size(t) 
d = np.zeros(L)
qf = np.zeros(L)

for j in np.arange(# TO COMPLETE):
    # DEFINE d and qf
    
Mi_Na = np.zeros(L)
Me_Na = np.zeros(L)
Mi_U = np.zeros(L)
Me_U = np.zeros(L)
Mi_K = np.zeros(L)
Me_K = np.zeros(L)
ci_Na = np.zeros(L)
ce_Na = np.zeros(L)
ci_U = np.zeros(L)
ce_U = np.zeros(L)
ci_K = np.zeros(L)
ce_K = np.zeros(L)
Vi = np.zeros(L)
Ve = np.zeros(L)
osmi = np.zeros(L)
osme = np.zeros(L)

# Initial conditions
Vi[0] = # TO COMPLETE
Ve[0] = # TO COMPLETE

ce_Na[0] = # TO COMPLETE
ci_Na[0] = # TO COMPLETE
Mi_Na[0] = # TO COMPLETE
Me_Na[0] = # TO COMPLETE

ce_U[0] = # TO COMPLETE
ci_U[0] = # TO COMPLETE
Mi_U[0] = # TO COMPLETE
Me_U[0] = # TO COMPLETE

ce_K[0] = # TO COMPLETE
ci_K[0] = # TO COMPLETE
Mi_K[0] = # TO COMPLETE
Me_K[0] = # TO COMPLETE

# Osmolarity
osm0= # TO COMPLETE
ceqi = # TO COMPLETE
ceqe = # TO COMPLETE
osmi[0] = # TO COMPLETE
osme[0] = # TO COMPLETE

for j in range(L-1):
    # TO COMPLETE

    
# plots
# TO COMPLETE
    