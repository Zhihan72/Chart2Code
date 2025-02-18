import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2020, 2031)
wind_energy = [200, 215, 230, 260, 300, 350, 410, 490, 590, 710, 860]
hydro_energy = [180, 182, 185, 190, 195, 200, 205, 210, 215, 220, 225]
fossil_energy = [1200, 1180, 1160, 1120, 1100, 1050, 1000, 950, 900, 850, 800]

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 10))

ax1.plot(years, wind_energy, marker='s', linestyle='--', color='skyblue', linewidth=2)
ax1.plot(years, hydro_energy, marker='^', linestyle='-.', color='green', linewidth=2)
ax1.grid(True, linestyle='--', alpha=0.5)

width = 0.4
ax2.bar(years - width / 2, fossil_energy, width, color='gray', alpha=0.7)
ax2.grid(True, linestyle='--', alpha=0.5)

ax1.tick_params(labelsize=10)
ax2.tick_params(labelsize=10)

plt.tight_layout()
plt.show()