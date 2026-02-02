import numpy as np
import matplotlib.pyplot as plt

dt = 0.01
t = np.linspace(0, 100, int(10 / dt))

x = 0
y = 0
z = 20 

vX = 3
vY = 0
vZ = 20

aX = 0
aY = 0
aZ = -9.81

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

    aX = aX + jX * dt
    aY = aY + jY * dt
    aZ = aZ + jZ * dt

    vX = vX + aX * dt
    vY = vY + aY * dt
    vZ = vZ + aZ * dt

    x = x + vX * dt
    y = y + vY * dt
    z = z + vZ * dt

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

    if z <= 0:
        break

print("Final position:", (xs[-1], ys[-1], zs[-1]))
print("Final velocity:", (vXs[-1], vYs[-1], vZs[-1]))

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot(xs, ys, zs)
ax.set_xlabel('X Position (m)')
ax.set_ylabel('Y Position (m)')
ax.set_zlabel('Z Position (m)')
ax.set_title('Projectile Motion Trajectory')
ax.grid(True)

plt.show()
