import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2000, 2021)
residential_production = np.array([1, 1, 2, 3, 4, 5, 7, 9, 12, 15, 19, 24, 30, 37, 45, 54, 64, 75, 87, 100, 114])
commercial_production = np.array([2, 2, 3, 4, 6, 8, 11, 14, 18, 23, 29, 36, 44, 53, 63, 74, 86, 99, 113, 128, 144])
industrial_production = np.array([1, 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153, 171, 190, 210])
community_production = np.array([0, 1, 1, 2, 3, 4, 5, 7, 9, 12, 16, 21, 27, 34, 42, 51, 61, 72, 84, 97, 111])

production_data = np.vstack([residential_production, commercial_production, industrial_production, community_production])

fig, ax = plt.subplots(figsize=(14, 8))

# Changed style elements
colors = ['#CD5C5C', '#FFD700', '#4682B4', '#FF8C00']  # Changed color order
labels = ['Community', 'Industrial', 'Commercial', 'Residential']  # Changed order for variety

ax.stackplot(years, production_data, labels=labels, colors=colors, alpha=0.5)  # Changed transparency level

# Changing plot styles
ax.set_title('Solar Energy Production in Solarville (2000-2020)', fontsize=20, fontweight='normal', pad=15)
ax.set_xlabel('Year', fontsize=12, labelpad=8)
ax.set_ylabel('Energy Production (GWh)', fontsize=12, labelpad=8)

# Altered ticks and grid style
ax.set_xticks(years[::5])  # Changed spacing of x-ticks
ax.set_yticks(np.arange(0, 501, 100))  # Changed spacing of y-ticks
ax.yaxis.grid(True, linestyle=':', alpha=0.5)  # Changed grid style

# Altered legend
ax.legend(loc='lower right', fontsize=11, title='Energy Sectors', title_fontsize='11')  # Changed location and font size

ax.annotate('First Solar Setup', xy=(2000, 4), xytext=(2003, 80),
            arrowprops=dict(facecolor='gray', arrowstyle='-|>'),
            fontsize=10, color='purple', fontweight='normal')

ax.annotate('Growth Surge Noticeable', xy=(2010, 19), xytext=(2012, 180),
            arrowprops=dict(facecolor='gray', arrowstyle='-|>'),
            fontsize=10, color='green', fontweight='normal')

plt.tight_layout()
plt.show()