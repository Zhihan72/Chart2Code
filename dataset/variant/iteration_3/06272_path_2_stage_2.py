import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)
solar = [10, 14, 21, 30, 38, 50, 68, 80, 92, 110, 130]
wind = [50, 58, 70, 85, 97, 110, 128, 140, 155, 170, 190]
hydro = [300, 305, 310, 312, 315, 320, 322, 325, 328, 330, 332]
geothermal = [3, 4, 6, 8, 10, 12, 15, 18, 19, 21, 23]

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
    (2016, 50, 'Sol: 50TWh'),
    (2020, 110, 'Wnd: 190TWh'),
    (2020, 332, 'Hydr: 332TWh'),
    (2020, 23, 'Geo: 23TWh')
]
for (year, output, text) in annotations:
    ax.annotate(text, xy=(year, output), xytext=(year - 2, output + 20),
                arrowprops=dict(arrowstyle='->', connectionstyle='arc3', color='gray'),
                fontsize=10, bbox=dict(boxstyle="round,pad=0.3", edgecolor='gray', facecolor='lightyellow', alpha=0.5))

ax.grid(linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()