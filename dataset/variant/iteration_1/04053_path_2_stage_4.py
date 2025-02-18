import numpy as np
import matplotlib.pyplot as plt

years = np.linspace(1, 12, 12)
orbital_radius_a = np.sin(years / 2) * 0.5 + 1
orbital_radius_b = np.sin((years - 1) / 2) * 0.4 + 1.5
orbital_radius_c = np.sin((years - 2) / 2) * 0.3 + 2
orbital_radius_d = np.cos(years / 3) * 0.6 + 1.1
orbital_radius_e = np.cos((years - 1) / 4) * 0.2 + 2.5

fig, ax = plt.subplots(figsize=(12, 7))

ax.plot(years, orbital_radius_a, linestyle='-', marker='o', color='#FF5733')
ax.plot(years, orbital_radius_b, linestyle='-', marker='s', color='#33FF57')
ax.plot(years, orbital_radius_c, linestyle='-', marker='^', color='#3357FF')
ax.plot(years, orbital_radius_d, linestyle='-', marker='D', color='#FF33A1')
ax.plot(years, orbital_radius_e, linestyle='-', marker='x', color='#33FFF5')

ax.set_title("Orbits of Planets", fontsize=16, pad=20)
ax.set_xlabel("Years", fontsize=13)
ax.set_ylabel("Radius (AU)", fontsize=13)

plt.tight_layout()
plt.show()