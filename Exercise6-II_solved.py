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

def my_plot(t, y_i, y_e, solute):
    f, ax = plt.subplots(1, 2, figsize=(10,10))
    sns.lineplot(x=t/60, y=y_i, ax=ax[0])
    ax[0].set(xlabel='time (hours)')
    ax[0].set_title("intracellular " + solute)
    sns.lineplot(x=t/60, y=y_e, ax=ax[1], color='red')
    ax[1].set(xlabel='time (hours)')
    ax[1].set_title("extracellular " + solute)
    
# Sodium parameters  
ki_Na = 1.5
g_Na = 0.02
u_Na = 0.107
ke_Na = g_Na * ki_Na

# Urea parameters 
ki_U = 0.77
g_U = 1
u_U = 0.075
ke_U = g_U * ki_U

# Potassium parameters 
ki_K = 1.5
g_K = 28.2
u_K = 0.045
ke_K = g_K * ki_K

# Other parameters and Euler's method initialization (remember that time is in minutes)
qf0 = 2/(4*60) # Ultradiffusion
d0 = 0.241 # dialysance
I = 2/(48*60)  # Patient is now drinking
Vp = 0.58 * 70   # Patient's liquid volume at the beginning of the dialysis
cd_Na = 140 # Na in dialysis bath
cd_U = 0 # Urea in dialysis bath
cd_K = 2 # K in dialysis bath

dialysis_hours = 4
dt = 0.2  #minuti
days = 12
t_start = 0
t_end = days*24*60
t = np.arange(t_start, t_end+dt, dt) 
L = np.size(t) 
d = np.zeros(L)
qf = np.zeros(L)

for j in np.arange(2, days+2, 2):
    d[int(j*24*60/dt - 4*60/dt):int(j*24*60/dt)] = d0
    qf[int(j*24*60/dt - 4*60/dt):int(j*24*60/dt)] = qf0
    
    
    
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
Vi[0] = 5 * Vp / 8
Ve[0] = 3 * Vp / 8 

ce_Na[0] = 140
ci_Na[0] = ce_Na[0]*g_Na+u_Na/ki_Na
Mi_Na[0] = ci_Na[0]*Vi[0]
Me_Na[0] = ce_Na[0]*Ve[0]

ce_U[0] = 0
ci_U[0] = ce_U[0]*g_U+u_U/ki_U
Mi_U[0] = ci_U[0]*Vi[0]
Me_U[0] = ce_U[0]*Ve[0]

ce_K[0] = 4
ci_K[0] = ce_K[0]*g_K+u_K/ki_K
Mi_K[0] = ci_K[0]*Vi[0]
Me_K[0] = ce_K[0]*Ve[0]

# Osmolarity
osm0= 280  
kf = 0.1
ceqi = (osm0 - 0.93*(ci_Na[0] + ci_K[0] + ci_U[0])) /0.93
ceqe = (osm0 - 0.93*(ce_Na[0] + ce_K[0] + ce_U[0])) /0.93
osmi[0] = 0.93*(ci_Na[0] + ci_K[0] + ci_U[0] + ceqi)
osme[0] = 0.93*(ce_Na[0] + ce_K[0] + ce_U[0] + ceqe)

for j in range(L-1):
    dVi = kf*(osmi[j] - osme[j])
    dVe = I - qf[j] - kf*(osmi[j] - osme[j])
    Vi[j+1]= Vi[j] + dt*dVi
    Ve[j+1]= Ve[j] + dt*dVe
    
    dMi_Na = - ki_Na*Mi_Na[j]/Vi[j] + ke_Na*Me_Na[j]/Ve[j] +u_Na
    dMe_Na =   ki_Na*Mi_Na[j]/Vi[j] - ke_Na*Me_Na[j]/Ve[j] -d[j]*(Me_Na[j]/Ve[j] -cd_Na)-qf[j]*ce_Na[j]
    Mi_Na[j+1] = Mi_Na[j] + dt*dMi_Na
    Me_Na[j+1] = Me_Na[j] + dt*dMe_Na
    ci_Na[j+1] = Mi_Na[j+1]/Vi[j+1]
    ce_Na[j+1] = Me_Na[j+1]/Ve[j+1]
    
    dMi_U = - ki_U*Mi_U[j]/Vi[j] + ke_U*Me_U[j]/Ve[j] +u_U
    dMe_U =   ki_U*Mi_U[j]/Vi[j] - ke_U*Me_U[j]/Ve[j] -d[j]*(Me_U[j]/Ve[j] -cd_U)-qf[j]*ce_U[j]
    Mi_U[j+1] = Mi_U[j] + dt*dMi_U
    Me_U[j+1] = Me_U[j] + dt*dMe_U
    ci_U[j+1] = Mi_U[j+1]/Vi[j+1]
    ce_U[j+1] = Me_U[j+1]/Ve[j+1]
    
    dMi_K = - ki_K*Mi_K[j]/Vi [j]+ ke_K*Me_K[j]/Ve[j] +u_K
    dMe_K =   ki_K*Mi_K[j]/Vi[j] - ke_K*Me_K[j]/Ve[j] -d[j]*(Me_K[j]/Ve[j] -cd_K)-qf[j]*ce_K[j]
    Mi_K[j+1] = Mi_K[j] + dt*dMi_K
    Me_K[j+1] = Me_K[j] + dt*dMe_K
    ci_K[j+1] = Mi_K[j+1]/Vi[j+1]
    ce_K[j+1] = Me_K[j+1]/Ve[j+1]
    
    osmi[j+1] = 0.93*(ci_Na[j+1] + ci_K[j+1] + ci_U[j+1] + ceqi)
    osme[j+1] = 0.93*(ce_Na[j+1] + ce_K[j+1] + ce_U[j+1] + ceqe)


    
# plots
my_plot(t, ci_Na, ce_Na, "sodium")
my_plot(t, ci_U, ce_U, "urea")
my_plot(t, ci_K, ce_K, "potassium")

ax = plt.figure()
ax = sns.lineplot(x=t/60, y=Vi)
ax = sns.lineplot(x=t/60, y=Ve, color='red')
plt.legend(['Vi', 'Ve'])