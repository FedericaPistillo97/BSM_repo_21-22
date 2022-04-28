#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 15:28:35 2022
@author: chiaramarzi
"""

from matplotlib import pyplot as plt
import numpy as np
import seaborn as sns
sns.set_style("white")

# Inputs
Q = #TO CPMPLETE
Mco2 = #TO CPMPLETE
PIco2 = #TO CPMPLETE

# Parameters
Vlung = #TO CPMPLETE #pulmonary volume 
VD = #TO CPMPLETE #ventilation of the dead space	
Kco2 = #TO CPMPLETE #dissociation constant for CO2 in blood
Vtiss = #TO CPMPLETE #tissue volume 	
alphaco2 = #TO CPMPLETE #dissociation constant for CO2 in tissue
V0 = #TO CPMPLETE #basal value of ventilation	
Gp = #TO CPMPLETE #gain of the peripheral chemoreceptor control
Gc = #TO CPMPLETE #gain of the central chemoreceptor control
taup = #TO CPMPLETE #time constant of the peripheral chemoreceptor
tauc = #TO CPMPLETE #time constant of the central chemoreceptor
thetap = #TO CPMPLETE #set point of the peripheral and central controls
thetac = #TO CPMPLETE #set point of the peripheral and central controls
Tp = #TO CPMPLETE # valore normale 6.1; #pure delay of the peripheral control
Tc = #TO CPMPLETE # valore normale 7.1 #pure delay of the central control

# Basal condition at equilibrium
Paco2_0 = #TO CPMPLETE
Pvco2_0 = #TO CPMPLETE

# Time definition
tmax = 1000
dt = 0.1
t_start = 0
t = #TO CPMPLETE
L = np.size(t) 

# Space allocation
Paco2 = np.zeros(L)
Pvco2 = np.zeros(L)
DVp = np.zeros(L)
DVc = np.zeros(L)
V = np.zeros(L)

# Initial conditions in case of pure delays
start_index = #TO CPMPLETE
#Paco2, Pvco2, V TO CPMPLETE

# Integration with the Euler's method
for j in np.arange(start_index,L-1):
    #TO CPMPLETE
    
# Plots
#TO CPMPLETE