import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2000, 2021)

residential_production = np.array([1, 1, 2, 3, 4, 5, 7, 9, 12, 15, 19, 24, 30, 37, 45, 54, 64, 75, 87, 100, 114])
commercial_production = np.array([2, 2, 3, 4, 6, 8, 11, 14, 18, 23, 29, 36, 44, 53, 63, 74, 86, 99, 113, 128, 144])
industrial_production = np.array([1, 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153, 171, 190, 210])
agricultural_production = np.array([0, 1, 1, 2, 3, 5, 6, 8, 10, 13, 16, 20, 25, 30, 36, 43, 50, 58, 67, 77, 88])

production_data = np.vstack([residential_production, commercial_production, industrial_production, agricultural_production])

fig, ax = plt.subplots(figsize=(14, 8))

colors = ['#FFD700', '#FF8C00', '#CD5C5C', '#8A2BE2']
labels = ['Residential', 'Commercial', 'Industrial', 'Agricultural']

ax.stackplot(years, production_data, labels=labels, colors=colors, alpha=0.7)

ax.set_title('Solar Energy Production Growth in Solarville (2000-2020)', fontsize=18, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=14, labelpad=10)
ax.set_ylabel('Energy Production (GWh)', fontsize=14, labelpad=10)
ax.set_xticks(years[::2])
ax.set_yticks(np.arange(0, 551, 50))
ax.yaxis.grid(True, linestyle='--', alpha=0.7)

ax.legend(loc='upper left', fontsize=12, title='Sectors', title_fontsize='12')

ax.annotate('First Solar Panels Installed', xy=(2000, 4), xytext=(2003, 100),
            arrowprops=dict(facecolor='black', arrowstyle='->'),
            fontsize=12, color='blue', fontweight='bold')

ax.annotate('Residential Growth Surge', xy=(2010, 19), xytext=(2014, 240),
            arrowprops=dict(facecolor='black', arrowstyle='->'),
            fontsize=12, color='red', fontweight='bold')

plt.tight_layout()
plt.show()