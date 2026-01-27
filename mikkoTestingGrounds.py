import numpy as np
import matplotlib.pyplot as plt



dt = 0.1
t = np.linspace(0, 10, int(10 / dt))

x = 0
y = 20

vX = 3
vY = 20

aX = 0
aY = -9.81

jX = 0
jY = 0

for i in t:

    aX = aX + jX*dt
    aY = aY + jY*dt

    vX = vX + aX*dt
    vY = vY + aY*dt

    x = x + vX*dt
    y = y + vY*dt

    print("Position:", [x, y])
    print("Velocity:", [vX, vY])
    print("Acceleration:", [aX, aY])
    print("Jerk:", [jX, jY])