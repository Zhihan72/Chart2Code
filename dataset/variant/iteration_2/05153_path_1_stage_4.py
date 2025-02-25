import matplotlib.pyplot as plt
import numpy as np

decades = np.array(['1980s', '1990s', '2000s', '2010s', '2020s'])

vhs_usage = [80, 40, 30, 10, 5]
dvd_usage = [10, 50, 85, 30, 5]
bluray_usage = [5, 15, 45, 75, 50]
digital_usage = [0, 5, 15, 70, 85]

fig, ax = plt.subplots(figsize=(14, 8))

ax.plot(decades, vhs_usage, marker='o', linestyle='-', linewidth=2, color='#33FF5E')
ax.plot(decades, dvd_usage, marker='^', linestyle='--', linewidth=2, color='#FF33B8')
ax.plot(decades, bluray_usage, marker='s', linestyle=':', linewidth=2, color='#3375FF')
ax.plot(decades, digital_usage, marker='D', linestyle='-.', linewidth=2, color='#FF5733')

ax.set_title("Era of Shifting Media: Digital Ascendant", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Time Periods', fontsize=12, fontweight='bold')
ax.set_ylabel('Adoption Rate (%)', fontsize=12, fontweight='bold')

ax.annotate('Tape Peak', xy=('1980s', 80), xytext=('1990s', 70),
            arrowprops=dict(facecolor='black', shrink=0.05), fontsize=10, fontweight='bold', color='darkred')
ax.annotate('Stream Supremacy', xy=('2020s', 85), xytext=('2010s', 65),
            arrowprops=dict(facecolor='black', shrink=0.05), fontsize=10, fontweight='bold', color='navy')

highlight_decades = ['2000s', '2010s']
for decade in highlight_decades:
    ax.axvline(decade, color='grey', linestyle='--', linewidth=1, alpha=0.5)

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(False)

plt.tight_layout()
plt.show()