import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)

solar_energy = [30, 40, 50, 60, 70, 90, 110, 130, 160, 190, 220]
wind_energy = [20, 30, 35, 50, 65, 80, 95, 110, 125, 140, 155]

energy_data = np.vstack([solar_energy, wind_energy])

fig, ax = plt.subplots(figsize=(14, 8))

colors = ['#ffa07a', '#20b2aa']

ax.stackplot(years, energy_data, labels=['Solar Energy', 'Wind Energy'],
             colors=colors, alpha=0.85)

ax.set_title('GreenVille Renewable Energy Revolution:\nCumulative Growth of Energy Production (2010-2020)', fontsize=18, fontweight='bold', loc='center')
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Energy Production (GWh)', fontsize=14)

ax.grid(True, linestyle='--', alpha=0.7)
ax.legend(loc='upper left', title='Renewable Sources', fontsize=12, title_fontsize='13')

plt.xticks(years, rotation=45, fontsize=12)
plt.yticks(fontsize=12)
plt.tight_layout()

ax.annotate('Rapid adoption of solar energy', xy=(2014, 130), xytext=(2012, 150),
            arrowprops=dict(facecolor='black', shrink=0.05), fontsize=12)

fig, ax2 = plt.subplots(figsize=(8, 6))

total_2020_energy = np.sum(np.array([solar_energy[-1], wind_energy[-1]]))
proportions = [solar_energy[-1]/total_2020_energy, wind_energy[-1]/total_2020_energy]

ax2.bar(['Solar Energy', 'Wind Energy'], proportions, color=colors, alpha=0.85)

ax2.set_title('Proportional Contribution of Renewable Sources in 2020', fontsize=16, fontweight='bold')
ax2.set_xlabel('Renewable Source', fontsize=14)
ax2.set_ylabel('Proportion of Total Production', fontsize=14)

plt.tight_layout()
plt.show()