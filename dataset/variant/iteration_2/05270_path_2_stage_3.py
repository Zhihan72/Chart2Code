import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)

solar_energy = [30, 40, 50, 60, 70, 90, 110, 130, 160, 190, 220]
wind_energy = [20, 30, 35, 50, 65, 80, 95, 110, 125, 140, 155]

energy_data = np.vstack([solar_energy, wind_energy])

fig, ax = plt.subplots(figsize=(14, 8))

colors = ['#ffa07a', '#20b2aa']

ax.stackplot(years, energy_data, colors=colors, alpha=0.85)

ax.set_title('EcoCity Clean Energy Ascendancy:\nLayered Growth of Power Supply (2010-2020)', fontsize=18, fontweight='bold', loc='center')
ax.set_xlabel('Production Year', fontsize=14)
ax.set_ylabel('Energy Output (Gigawatt-hours)', fontsize=14)

plt.xticks(years, rotation=45, fontsize=12)
plt.yticks(fontsize=12)
plt.tight_layout()

ax.annotate('Notable uptake of solar energy tech', xy=(2014, 130), xytext=(2012, 150),
            arrowprops=dict(facecolor='black', shrink=0.05), fontsize=12)

fig, ax2 = plt.subplots(figsize=(8, 6))

total_2020_energy = np.sum(np.array([solar_energy[-1], wind_energy[-1]]))
proportions = [solar_energy[-1]/total_2020_energy, wind_energy[-1]/total_2020_energy]

ax2.bar(['Sunsational Energy', 'Zephyr Power'], proportions, color=colors, alpha=0.85)

ax2.set_title('Energy Champions of 2020', fontsize=16, fontweight='bold')
ax2.set_xlabel('Eco-Friendly Source', fontsize=14)
ax2.set_ylabel('Portion of Energy Yield', fontsize=14)

plt.tight_layout()
plt.show()