import matplotlib
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

xs = []
ys = []
vXs = []
vYs = []
aXs = []
aYs = []
jXs = []
jYs = []

for _ in t:

    aX = aX + jX*dt
    aY = aY + jY*dt

    vX = vX + aX*dt
    vY = vY + aY*dt

    x = x + vX*dt
    y = y + vY*dt

    xs.append(x)
    ys.append(y)
    vXs.append(vX)
    vYs.append(vY)
    aXs.append(aX)
    aYs.append(aY)
    jXs.append(jX)
    jYs.append(jY)

   
print("Position:", [xs, ys])
print("new line")
print("Velocity:", [vXs, vYs])
print("new line")
print("Acceleration:", [aXs, aYs])
print("new line")
print("Jerk:", [jXs, jYs])
print("new line")

plot = matplotlib.pyplot.plot(xs, ys, 'bo')