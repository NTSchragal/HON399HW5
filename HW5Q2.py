# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 20:48:18 2019

@author: ntsch
"""

import matplotlib.pyplot as plt
from matplotlib import rcParams
import numpy as np

def Rotate(daysAdded, longitudes):
    for latitude in range(-90, 91):
        latrate = rates[latitude + 90]
        oldlong = longitudes[latitude]
        newlong = (oldlong + daysAdded * latrate) % 360
        
        longitudes.update({latitude: newlong})

longitudes = {}
for latitude in range(-90, 91):
    longitudes.update({latitude: 0})

rates = []
for latitude in range (-90, 91):
    radlat = np.pi * latitude / 180
    rates.append(14.713 - 2.396 * ((np.sin(radlat))**2) - 1.787 * ((np.sin(radlat))**4))

rcParams['figure.titlesize'] = 12

fig, axes = plt.subplots(2, 2, sharex = False, squeeze = False, figsize = (12, 10))
#axes = axes.flatten()
#fig.tight_layout()

axes[0][0].set_title("0 Days")
axes[0][0].scatter(longitudes.values(), longitudes.keys(), color = 'k', s = 3, label = "0 Days")
    
fig.suptitle("Differential Solar Rotation")

fig.subplots_adjust(top = 0.95, bottom = 0.1)

xticks = np.linspace(0, 360, num = 7)
yticks = np.linspace(-90, 90, num = 7)




#plt.xlim(-10, 360)
#plt.ylim(-90, 90)

#xticks = np.linspace(0, 360, num = 7)
#yticks = np.linspace(-90, 90, num = 7)
#plt.xticks(xticks)
#plt.yticks(yticks)
#plt.xlabel("Longitude")
#plt.ylabel("Latitude")



#Letting the sun rotate 20 days
Rotate(20, longitudes)
axes[0][1].set_title("20 Days")
axes[0][1].scatter(longitudes.values(), longitudes.keys(), color = 'r', s = 3, label = "20 Days")

#Letting the sun rotate another 30 days for a total of 50 days
Rotate(30, longitudes)
axes[1][0].set_title("50 Days")
axes[1][0].scatter(longitudes.values(), longitudes.keys(), color = 'g', s = 3, label = "50 Days")

#Letting the sun rotate another 50 days for a total of 100 days
Rotate(50, longitudes)
axes[1][1].set_title("100 Days")
axes[1][1].scatter(longitudes.values(), longitudes.keys(), color = 'b', s = 3, label = "100 Days")

#plt.legend(["0 Days", "20 Days", "50 Days", "100 Days"], bbox_to_anchor = [0.25, 0.5])


for idx in range(0, 2):
    for jdx in range(0, 2):
        axes[idx][jdx].set_xlim(-10, 360)
        axes[idx][jdx].set_ylim(-90, 90)
        axes[idx][jdx].set_xticks(xticks)
        axes[idx][jdx].set_yticks(yticks)
        axes[idx][jdx].set_xlabel("Longitude")
        axes[idx][jdx].set_ylabel("Latitude")
    #axes[idx].legend(loc = "upper right")



plt.savefig("SubplotHW5Q2Graph.png", dpi = 300)
plt.show()
    
