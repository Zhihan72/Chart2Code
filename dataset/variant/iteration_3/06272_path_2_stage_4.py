import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)
solar = [10, 15, 20, 32, 41, 52, 70, 85, 91, 112, 129]
wind = [48, 60, 72, 87, 99, 115, 130, 142, 153, 168, 192]
hydro = [302, 304, 311, 313, 316, 318, 321, 327, 329, 331, 334]
geothermal = [2, 5, 7, 9, 11, 13, 14, 19, 20, 22, 24]

fig, ax = plt.subplots(figsize=(12, 8))

# Changed colors, marker types and line styles
ax.plot(years, solar, label='Solar', color='forestgreen', marker='x', linestyle='-')
ax.plot(years, wind, label='Wind', color='firebrick', marker='p', linestyle='--')
ax.plot(years, hydro, label='Hydro', color='navy', marker='h', linestyle='-')
ax.plot(years, geothermal, label='Geo', color='purple', marker='*', linestyle=':')

# Changed title, font weight and position
ax.set_title('Renewable Energy Production: 2010-2020', fontsize=18, fontweight='light', pad=25)
ax.set_xlabel('Year', fontsize=16)
ax.set_ylabel('Energy (TWh)', fontsize=16)
ax.set_xticks(years[::2]) # Display every second year
ax.set_yticks(np.arange(0, 400, 50))

# Altered legend style
ax.legend(title='Energy Sources', fontsize=11, title_fontsize=12, loc='lower right', frameon=False)

# Removed fancy annotation styling
annotations = [
    (2016, 52, 'Solar: 52TWh'),
    (2020, 112, 'Wind: 192TWh'),
    (2020, 334, 'Hydro: 334TWh'),
    (2020, 24, 'Geo: 24TWh')
]
for (year, output, text) in annotations:
    ax.annotate(text, xy=(year, output), xytext=(year - 2, output + 20),
                arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=.2', color='gray'),
                fontsize=10)

# Added grid and border custom styling
ax.grid(linestyle='-', linewidth=0.5, color='gray', alpha=0.3)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()
plt.show()