import matplotlib.pyplot as plt
import numpy as np

energy_data = np.array([
    [200, 150, 100, 50],  # Europe
    [300, 200, 250, 30],  # Asia
    [250, 220, 180, 40],  # North America
    [120, 100, 300, 20],  # South America
    [180, 90, 70, 10]     # Africa
])

regions = ['Europe', 'Asia', 'North America', 'South America', 'Africa']
single_color = '#66b3ff'

fig, ax = plt.subplots(figsize=(12, 8))
neg_positions = -np.cumsum(energy_data[:, :2], axis=1)
pos_positions = np.cumsum(energy_data[:, 2:], axis=1)
bar_width = 0.4

for i in range(2):
    ax.barh(regions, energy_data[:, i], color=single_color, height=bar_width, left=neg_positions[:, i])

for i in range(2, 4):
    ax.barh(regions, energy_data[:, i], color=single_color, height=bar_width, left=pos_positions[:, i-2]-energy_data[:, i])

ax.set_yticks(np.arange(len(regions)))
ax.set_yticklabels(regions)
ax.axvline(0, color='black', linewidth=0.8)
ax.set_xlabel('Energy Generation (GWh)')

plt.tight_layout()
plt.show()