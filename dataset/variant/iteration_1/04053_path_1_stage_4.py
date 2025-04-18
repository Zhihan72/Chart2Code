import numpy as np
import matplotlib.pyplot as plt

years = np.linspace(1, 12, 12)
orbital_radius_planet_a = np.sin(years / 2) * 0.5 + 1
orbital_radius_planet_b = np.sin((years - 1) / 2) * 0.4 + 1.5
orbital_radius_planet_c = np.sin((years - 2) / 2) * 0.3 + 2
orbital_radius_planet_d = np.cos(years / 2) * 0.6 + 2.5
orbital_radius_planet_e = np.sin((years + 1) / 3) * 0.7 + 0.8

fig, ax = plt.subplots(figsize=(12, 7))

ax.plot(years, orbital_radius_planet_a, linestyle='--', marker='D', color='green', label='Astro A')
ax.plot(years, orbital_radius_planet_b, linestyle=':', marker='^', color='red', label='Celestial B')
ax.plot(years, orbital_radius_planet_c, linestyle='-.', marker='v', color='yellow', label='Sphere C')
ax.plot(years, orbital_radius_planet_d, linestyle='-', marker='*', color='brown', label='World D')
ax.plot(years, orbital_radius_planet_e, linestyle='-', marker='h', color='pink', label='Body E')

ax.set_title("Time Travel of Various Spheres: A-E", fontsize=16, pad=20)
ax.set_xlabel("Chronological Span", fontsize=13)
ax.set_ylabel("Radial Distance (AU)", fontsize=13)
ax.legend(loc='best', fontsize=12)
ax.grid(False)
fig.patch.set_facecolor('#e0e0e0')
ax.spines['top'].set_linewidth(1.5)
ax.spines['right'].set_linewidth(1.5)
ax.spines['left'].set_linewidth(1.5)
ax.spines['bottom'].set_linewidth(1.5)
plt.tight_layout()
plt.show()