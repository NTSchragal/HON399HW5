# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 11:33:39 2019

@author: ntsch
"""

import matplotlib.pyplot as plt
import numpy as np
import random
random.seed()

def Distance(coords):
    return np.sqrt(coords[0]**2 + coords[1]**2 + coords[2]**2)

def Step(coords):
    for i in range(0, 3):
        coords[i] += random.uniform(-1.0, 1.0)

coords = [0, 0, 0]
steps = np.linspace(0, 100, 101)
coordsList = []
coordsList.append(coords)
distances = [0]
xcoords = [0]
ycoords = [0]
zcoords = [0]
theoretical = [0]
for i in range(0, 100):
    Step(coords)
    coordsList.append(coords)
    xcoords.append(coords[0])
    ycoords.append(coords[1])
    zcoords.append(coords[2])
    distances.append(Distance(coords))
    theoretical.append(np.sqrt(3 * (i + 1))/2)

fig, ax = plt.subplots(figsize = (10, 8))
plt.title("Random Walk Simulation Results")

plt.xlabel("Steps")
plt.ylabel("Distance from start")

plt.plot(steps, distances, color = 'k')
plt.plot(steps, theoretical, color = 'y')
plt.plot(steps, xcoords, linestyle = ':', color = 'r')
plt.plot(steps, ycoords, linestyle = ':', color = 'b')
plt.plot(steps, zcoords, linestyle = ':', color = 'g')

plt.legend(["Distance from origin", "Theoretical Distance", "X-Coordinates", "Y-Coordinates", "Z-Coordinates"], bbox_to_anchor = [0.27, 1])

plt.savefig("HW4Q1Graph.png", dpi = 300)
plt.show()
