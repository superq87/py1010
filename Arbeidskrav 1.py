# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 22:21:05 2024

@author: erling.mauseth
"""


KM = 10000 # Dette er en beskrivelsde av antall kjørte KM per år
FE = 5000 # Forsinring Elbil per år
FB = 7500 # Forsikring Bensinbil per år
TF = 8.38 # Trafikkforsikringsavgift: 8,38 kr/dag for både elbil og bensinbil.
DE = 0.4 # Kr/Km - Drivstoffbruk: Elbil: 0,2 kWh/km. Strømpris (antar kun hjemmelading): 2.00 kr/kWh. 
DB = 1.0 # Bensinbil: 1,0 kr/km.
BAE = 0.1 # Bomavgift: Elbil: 0,1 kr/km
BAB = 0.3 # Bomavgift: Bensinbil: 0,3 kr/km.

Kostnad_ElBil = FE + (KM*DE) + (KM*BAE) + (TF*365) 
Kostnad_Bensin = FB + (KM*DB) + (KM*BAB) + (TF*365)

print("Kostnader for Elbil per år =",Kostnad_ElBil)
print("Kostnader for Bensinbil per år =",Kostnad_Bensin)

