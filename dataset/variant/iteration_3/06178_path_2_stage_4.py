import matplotlib.pyplot as plt
import numpy as np

years = ['2018', '2019', '2020', '2021', '2022']
sources = ['Sol', 'Wnd', 'Hyd', 'Bio']

# Manually shuffled rows within energy production array but kept the structure
# (values are not changed ideally, except for shuffling within their row)
energy_production = np.array([
    [65, 50, 90, 80, 100],  # Sol list order changed
    [95, 85, 110, 80, 70],  # Wnd list order changed
    [110, 120, 100, 115, 105], # Hyd list order changed
    [45, 35, 50, 40, 30]   # Bio list order changed
])

positions = np.arange(len(years))
bar_width = 0.2

fig, ax = plt.subplots(figsize=(14, 8))

colors = ['#1E90FF', '#8B4513', '#FFD700', '#32CD32']

for i, source in enumerate(sources):
    ax.bar(positions + i*bar_width, energy_production[i], bar_width, color=colors[i])

ax.set_xlabel('Yr', fontsize=12)
ax.set_ylabel('Prod (TWh)', fontsize=12)
ax.set_title('Renewable Prod Growth (2018-22)', fontsize=14, fontweight='bold')
ax.set_xticks(positions + bar_width*1.5)
ax.set_xticklabels(years, fontsize=10)

plt.tight_layout()
plt.show()