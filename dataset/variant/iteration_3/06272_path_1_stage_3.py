import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)
solar = [10, 14, 21, 30, 38, 50, 68, 80, 92, 110, 130]
wind = [50, 58, 70, 85, 97, 110, 128, 140, 155, 170, 190]
hydro = [300, 305, 310, 312, 315, 320, 322, 325, 328, 330, 332]

fig, ax = plt.subplots(figsize=(12, 8))

# Shuffle the colors assigned to each data group or type
ax.plot(years, solar, label='Solar', color='deepskyblue', marker='p', linestyle='-.')
ax.plot(years, wind, label='Wind', color='orange', marker='x', linestyle='--')
ax.plot(years, hydro, label='Hydro', color='royalblue', marker='h', linestyle='-')

ax.set_title('Renewable Energy Production Trends (2010-2020)', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Energy Produced (TWh)', fontsize=14)
ax.set_xticks(years)
ax.set_yticks(np.arange(0, 400, 50))

ax.legend(title='Energy Sources', fontsize=12, title_fontsize=13, loc='lower right')

annotations = [
    (2016, 50, 'Solar: 50 TWh'),
    (2020, 110, 'Wind: 190 TWh'),
    (2020, 332, 'Hydro: 332 TWh')
]

for (year, output, text) in annotations:
    ax.annotate(text, xy=(year, output), xytext=(year - 2, output + 20),
                arrowprops=dict(arrowstyle='->', connectionstyle='arc3', color='gray'),
                fontsize=10, bbox=dict(boxstyle="round,pad=0.3", edgecolor='gray', facecolor='lightyellow', alpha=0.5))

ax.grid(linestyle=':', alpha=0.5)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()
plt.show()