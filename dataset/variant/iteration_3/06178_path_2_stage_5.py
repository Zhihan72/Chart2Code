import matplotlib.pyplot as plt
import numpy as np

years = ['2018', '2019', '2020', '2021', '2022']
sources = ['Sol', 'Wnd', 'Hyd', 'Bio']

energy_production = np.array([
    [65, 50, 90, 80, 100], 
    [95, 85, 110, 80, 70], 
    [110, 120, 100, 115, 105], 
    [45, 35, 50, 40, 30]
])

positions = np.arange(len(years))
bar_height = 0.2

fig, ax = plt.subplots(figsize=(14, 8))

colors = ['#1E90FF', '#8B4513', '#FFD700', '#32CD32']

for i, source in enumerate(sources):
    ax.barh(positions + i*bar_height, energy_production[i], bar_height, color=colors[i])

ax.set_ylabel('Yr', fontsize=12)
ax.set_xlabel('Prod (TWh)', fontsize=12)
ax.set_title('Renewable Prod Growth (2018-22)', fontsize=14, fontweight='bold')
ax.set_yticks(positions + bar_height*1.5)
ax.set_yticklabels(years, fontsize=10)

plt.tight_layout()
plt.show()