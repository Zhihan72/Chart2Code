import numpy as np
import matplotlib.pyplot as plt

decades = np.arange(1980, 2031, 10)
solar_energy = [0.1, 0.5, 2, 5, 15, 25]
wind_energy = [0.3, 1, 3, 8, 20, 30]
hydro_energy = [5, 6, 8, 10, 12, 15]
geothermal_energy = [0.2, 0.4, 0.7, 1, 2, 5]

data = [solar_energy, wind_energy, hydro_energy, geothermal_energy]

# Shuffled colors for the line plots
colors = ['#CD5C5C', '#1E90FF', '#20B2AA', '#FFA07A']

fig, ax = plt.subplots(figsize=(12, 8))

for i in range(len(data)):
    ax.plot(decades, data[i], marker='o', color=colors[i], linewidth=2, linestyle='-')

ax.set_title("Growth of Renewable Energy Sources (1980-2030):\nA Decadal Analysis", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Decade', fontsize=12)
ax.set_ylabel('Percentage of Total Global Energy Consumption (%)', fontsize=12)

ax.set_xlim(1980, 2030)
ax.set_ylim(0, 35)

plt.tight_layout()
plt.show()