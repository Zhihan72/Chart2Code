import matplotlib.pyplot as plt
import numpy as np

years = ['2020', '2021', '2022', '2023']
solar_energy = [200, 250, 300, 350]
wind_energy = [150, 180, 220, 260]

colors = ['#ffd700', '#87ceeb']
fig, ax = plt.subplots(figsize=(10, 6))

bar_width = 0.3
index = np.arange(len(years))

ax.bar(index, solar_energy, color=colors[0], width=bar_width, align='center')
ax.bar(index + bar_width, wind_energy, color=colors[1], width=bar_width, align='center')

ax.set_xticks(index + 0.5 * bar_width)
ax.set_xticklabels(years)

ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Energy Generation (GWh)', fontsize=12)

plt.tight_layout()
plt.show()