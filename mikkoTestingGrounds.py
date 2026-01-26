import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(1,100,100)  # sec
dt = 1 # sec

x = 0 # m
y = 0 # m 

vX = 3 # m/s
vY = 20 # m/s

aY = -9.81 # m/s^2
aX = 0 # m/s^2

for t in t:

    y = y + vY*dt + 0.5*aY*(dt^2)
    vY = vY + aY*dt
    print(y)
    print(vY)
