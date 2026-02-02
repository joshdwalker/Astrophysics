import numpy as np
import matplotlib.pyplot as plt



dt = 0.01
t = np.linspace(0, 100, int(10 / dt))

x = 0
y = 20
z = 0

vX = 3
vY = 20
vZ = 0

aX = 0
aY = -9.81
aZ = 0

jX = 0
jY = 0
jZ = 0

xs = []
ys = []
zs = []
vXs = []
vYs = []
vZs = []
aXs = []
aYs = []
aZs = []
jXs = []
jYs = []
jZs = []

for _ in t:

    aX = aX + jX*dt
    aY = aY + jY*dt
    aZ = aZ + jZ*dt

    vX = vX + aX*dt
    vY = vY + aY*dt
    vZ = vZ + aZ*dt

    x = x + vX*dt
    y = y + vY*dt
    z = z + vZ*dt

    xs.append(x)
    ys.append(y)
    zs.append(z)

    vXs.append(vX)
    vYs.append(vY)
    vZs.append(vZ)

    aXs.append(aX)
    aYs.append(aY)
    aZs.append(aZ)

    jXs.append(jX)
    jYs.append(jY)
    jZs.append(jZ)

    if y <= 0:
        break

   
print("Position:", [xs, ys, zs])
print("new line")
print("Velocity:", [vXs, vYs, vZs])
print("new line")
print("Acceleration:", [aXs, aYs, aZs])
print("new line")
print("Jerk:", [jXs, jYs, jZs])
print("new line")


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot(xs, ys, zs)
ax.set_xlabel('X Position (m)')
ax.set_ylabel('Y Position (m)')
ax.set_zlabel('Z Position (m)')
ax.set_title('Projectile Motion Trajectory')
ax.grid(True)

plt.show()