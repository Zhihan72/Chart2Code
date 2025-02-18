import matplotlib.pyplot as plt
import numpy as np

years = ['2018', '2019', '2020', '2021', '2022']
sources = ['Sol', 'Wnd', 'Hyd', 'Bio']

energy_production = np.array([
    [50, 65, 80, 90, 100],
    [70, 80, 85, 95, 110],
    [100, 105, 110, 115, 120],
    [30, 35, 40, 45, 50]
])

positions = np.arange(len(years))
bar_width = 0.2

fig, ax = plt.subplots(figsize=(14, 8))

colors = ['#1E90FF', '#8B4513', '#FFD700', '#32CD32']

for i, source in enumerate(sources):
    ax.bar(positions + i*bar_width, energy_production[i], bar_width, label=source, color=colors[i])

ax.set_xlabel('Yr', fontsize=12)
ax.set_ylabel('Prod (TWh)', fontsize=12)
ax.set_title('Renewable Prod Growth (2018-22)', fontsize=14, fontweight='bold')
ax.set_xticks(positions + bar_width*1.5)
ax.set_xticklabels(years, fontsize=10)
ax.legend(title='Source', fontsize=10, title_fontsize=12)

ax.yaxis.grid(True)
ax.xaxis.grid(False)

plt.tight_layout()
plt.show()