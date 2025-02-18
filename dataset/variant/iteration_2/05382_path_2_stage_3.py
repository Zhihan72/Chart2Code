import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2000, 2021)

residential_production = np.array([1, 1, 2, 3, 4, 5, 7, 9, 12, 15, 19, 24, 30, 37, 45, 54, 64, 75, 87, 100, 114])
commercial_production = np.array([2, 2, 3, 4, 6, 8, 11, 14, 18, 23, 29, 36, 44, 53, 63, 74, 86, 99, 113, 128, 144])
industrial_production = np.array([1, 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153, 171, 190, 210])
agricultural_production = np.array([0, 1, 1, 2, 3, 5, 6, 8, 10, 13, 16, 20, 25, 30, 36, 43, 50, 58, 67, 77, 88])

production_data = np.vstack([residential_production, commercial_production, industrial_production, agricultural_production])

fig, ax = plt.subplots(figsize=(12, 7))

# Altered colors and added hatches
colors = ['#8A2BE2', '#FFD700', '#FF8C00', '#CD5C5C']
hatches = ['/', '\\', '|', '-']
labels = ['Home', 'Business', 'Factory', 'Farm']

# Randomly chosen edge color to augment stackplot
ax.stackplot(years, production_data, labels=labels, colors=colors, linewidth=2.5, edgecolor='gray', alpha=0.7)

ax.set_title('Growth of SunPower in Lightville (2000-2020)', fontsize=16, fontweight='medium', pad=15)
ax.set_xlabel('Year', fontsize=12, labelpad=8)
ax.set_ylabel('Output Volume (GWh)', fontsize=12, labelpad=8)
ax.set_xticks(years[::2])
ax.set_yticks(np.arange(0, 551, 50))
ax.yaxis.grid(True, linestyle='-.', linewidth=0.75)

# Changed legend style
ax.legend(loc='upper left', fontsize=10, title='Categories', title_fontsize='11', facecolor='lightgrey', edgecolor='black')

# Removed existing annotations for stylistic change; added new annotations
ax.annotate('Solar Milestone', xy=(2005, 10), xytext=(2007, 150),
            arrowprops=dict(facecolor='darkblue', arrowstyle='->'),
            fontsize=10, color='green', fontweight='bold')

plt.tight_layout()
plt.show()