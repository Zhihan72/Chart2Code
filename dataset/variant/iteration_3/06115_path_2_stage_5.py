import matplotlib.pyplot as plt
import numpy as np

energy_sources = ['Windy', 'Sunshine']
energy_contribution = np.array([45, 25])

color = '#1f77b4'

fig, ax = plt.subplots(figsize=(14, 8))

bars = ax.bar(energy_sources, energy_contribution, color=color)

ax.set_xlabel('Power Sources', fontsize=14)
ax.set_ylabel('Contribution (%)', fontsize=14)

for bar, contribution in zip(bars, energy_contribution):
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width() / 2, height + 1, f'{height}%', va='bottom', ha='center', fontsize=12, color='black')

ax.set_xticks(np.arange(len(energy_sources)))
ax.set_xticklabels(energy_sources, fontsize=12)
ax.tick_params(axis='x', which='major', pad=10)

plt.tight_layout()

plt.show()