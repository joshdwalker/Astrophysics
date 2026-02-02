import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# Settings
# -----------------------------
G = 6.67430e-11      # gravitational constant
dt = 10.0            # seconds per step (you will tune this)
steps = 20000
softening = 1e6      # meters (prevents singularities)

# -----------------------------
# Bodies (you can add more)
# Each body: mass (kg), position (m), velocity (m/s)
# Example: Sun-Earth-Moon-ish setup (rough, for learning)
# -----------------------------
m = np.array([
    1.9885e30,   # Sun
    5.972e24,    # Earth
    7.342e22,    # Moon
], dtype=float)

r = np.array([
    [0.0, 0.0],               # Sun at origin
    [1.496e11, 0.0],          # Earth at ~1 AU
    [1.496e11 + 3.844e8, 0.0] # Moon offset from Earth
], dtype=float)

v = np.array([
    [0.0, 0.0],     # Sun
    [0.0, 29780.0], # Earth orbital speed ~29.78 km/s
    [0.0, 29780.0 + 1022.0]  # Moon adds ~1.022 km/s
], dtype=float)

# -----------------------------
# Helper: compute accelerations from gravity
# -----------------------------
def gravity_accels(r, m, G, softening):
    """
    r: (N,2) positions
    m: (N,) masses
    returns a: (N,2) accelerations
    """
    N = r.shape[0]
    a = np.zeros_like(r)

    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            dr = r[j] - r[i]                    # vector from i to j
            dist2 = np.dot(dr, dr) + softening**2
            inv_dist3 = 1.0 / (dist2 * np.sqrt(dist2))
            a[i] += G * m[j] * dr * inv_dist3   # acceleration on i due to j

    return a

# -----------------------------
# Storage for plotting (track a few bodies)
# -----------------------------
track_idx = [0, 1, 2]  # which bodies to plot
paths = {i: {"x": [], "y": []} for i in track_idx}

# -----------------------------
# Integrate (Leapfrog / velocity Verlet-ish)
# Much more stable than plain Euler for gravity
# -----------------------------
a = gravity_accels(r, m, G, softening)

for k in range(steps):
    # half-step velocity
    v += 0.5 * a * dt

    # full-step position
    r += v * dt

    # new accel
    a = gravity_accels(r, m, G, softening)

    # half-step velocity
    v += 0.5 * a * dt

    # record
    for i in track_idx:
        paths[i]["x"].append(r[i, 0])
        paths[i]["y"].append(r[i, 1])

# -----------------------------
# Plot
# -----------------------------
plt.figure()
for i in track_idx:
    plt.plot(np.array(paths[i]["x"]) / 1e9, np.array(paths[i]["y"]) / 1e9, label=f"body {i}")
plt.gca().set_aspect('equal', adjustable='box')
plt.xlabel("x (Gm)")  # gigameters
plt.ylabel("y (Gm)")
plt.title("2D N-body gravity simulation")
plt.grid(True)
plt.legend()
plt.show()
