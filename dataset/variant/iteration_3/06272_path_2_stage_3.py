import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)
# Randomly altered data while preserving original structure
solar = [10, 15, 20, 32, 41, 52, 70, 85, 91, 112, 129]
wind = [48, 60, 72, 87, 99, 115, 130, 142, 153, 168, 192]
hydro = [302, 304, 311, 313, 316, 318, 321, 327, 329, 331, 334]
geothermal = [2, 5, 7, 9, 11, 13, 14, 19, 20, 22, 24]

fig, ax = plt.subplots(figsize=(12, 8))

single_color = 'steelblue'

ax.plot(years, solar, label='Solar', color=single_color, marker='o', linestyle='--')
ax.plot(years, wind, label='Wind', color=single_color, marker='s', linestyle='-.')
ax.plot(years, hydro, label='Hydro', color=single_color, marker='^', linestyle=':')
ax.plot(years, geothermal, label='Geo', color=single_color, marker='d', linestyle='-')

ax.set_title('Renewable Energy (2010-20)', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Yr', fontsize=14)
ax.set_ylabel('Energy (TWh)', fontsize=14)
ax.set_xticks(years)
ax.set_yticks(np.arange(0, 400, 50))

ax.legend(title='Sources', fontsize=12, title_fontsize=13, loc='upper left')

annotations = [
    (2016, 52, 'Sol: 52TWh'),
    (2020, 112, 'Wnd: 192TWh'),
    (2020, 334, 'Hydr: 334TWh'),
    (2020, 24, 'Geo: 24TWh')
]
for (year, output, text) in annotations:
    ax.annotate(text, xy=(year, output), xytext=(year - 2, output + 20),
                arrowprops=dict(arrowstyle='->', connectionstyle='arc3', color='gray'),
                fontsize=10, bbox=dict(boxstyle="round,pad=0.3", edgecolor='gray', facecolor='lightyellow', alpha=0.5))

ax.grid(linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()