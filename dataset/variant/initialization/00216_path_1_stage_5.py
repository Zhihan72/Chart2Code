import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2020, 2031)
wind_energy = [200, 215, 230, 260, 300, 350, 410, 490, 590, 710, 860]
hydro_energy = [180, 182, 185, 190, 195, 200, 205, 210, 215, 220, 225]
fossil_energy = [1200, 1180, 1160, 1120, 1100, 1050, 1000, 950, 900, 850, 800]

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 10))

# Grouped bar chart for wind and hydro energy
width = 0.3
ax1.bar(years - width, wind_energy, width, color='skyblue', alpha=0.7)
ax1.bar(years, hydro_energy, width, color='green', alpha=0.7)

# Grouped bar chart for fossil energy
ax2.bar(years, fossil_energy, width, color='gray', alpha=0.7)

ax1.tick_params(labelsize=10)
ax2.tick_params(labelsize=10)

plt.tight_layout()
plt.show()