import numpy as np
import matplotlib.pyplot as plt

years = np.linspace(1, 12, 12)
orbital_radius_planet_a = np.sin(years / 2) * 0.5 + 1
orbital_radius_planet_b = np.sin((years - 1) / 2) * 0.4 + 1.5
orbital_radius_planet_c = np.sin((years - 2) / 2) * 0.3 + 2
orbital_radius_planet_d = np.cos(years / 2) * 0.6 + 2.5
orbital_radius_planet_e = np.sin((years + 1) / 3) * 0.7 + 0.8

fig, ax = plt.subplots(figsize=(12, 7))

ax.plot(years, orbital_radius_planet_a, linestyle='-', marker='o', color='blue', label='Planet A')
ax.plot(years, orbital_radius_planet_b, linestyle='-', marker='s', color='red', label='Planet B')
ax.plot(years, orbital_radius_planet_c, linestyle='-', marker='^', color='green', label='Planet C')
ax.plot(years, orbital_radius_planet_d, linestyle='-', marker='x', color='purple', label='Planet D')
ax.plot(years, orbital_radius_planet_e, linestyle='-', marker='d', color='orange', label='Planet E')

ax.set_title("Simulated Orbits of Planets A, B, C, D, and E over Time", fontsize=16, pad=20)
ax.set_xlabel("Years", fontsize=13)
ax.set_ylabel("Orbital Radius (AU)", fontsize=13)
ax.legend(loc='upper right', fontsize=12)
ax.grid(True, linestyle='--', alpha=0.6)
fig.patch.set_facecolor('#f0f0f0')
plt.tight_layout()
plt.show()