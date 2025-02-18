import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2040, 2061)
moon = np.array([0, 2, 5, 7, 10, 14, 18, 21, 25, 28, 30, 32, 35, 37, 40, 42, 45, 48, 50, 52, 55])
mars = np.array([0, 0, 1, 3, 6, 10, 14, 17, 20, 24, 28, 31, 34, 37, 40, 43, 46, 49, 52, 56, 60])
europa = np.array([0, 0, 0, 1, 3, 5, 8, 11, 14, 17, 20, 22, 24, 26, 30, 33, 35, 37, 40, 43, 45])
titan = np.array([0, 0, 0, 0, 1, 2, 3, 5, 7, 10, 12, 14, 15, 16, 17, 18, 19, 20, 22, 24, 25])
ceres = np.array([0, 0, 0, 0, 0, 1, 2, 4, 7, 10, 13, 15, 18, 21, 24, 26, 28, 31, 33, 35, 38])

data = np.vstack([moon, mars, europa, titan, ceres])
colors = ['#FF6347', '#4682B4', '#9ACD32', '#DA70D6', '#FFE4B5']

fig, ax = plt.subplots(figsize=(14, 8))
ax.stackplot(years, data, labels=['M0n', 'Ma®s', 'Eur0pa', 'Τιtan', 'Ĉerēs'], colors=colors, alpha=0.75)

ax.set_title("Trends in Space Colonization: 1840-1960", fontsize=16, fontweight='bold', pad=10)
ax.set_xlabel("Time Period", fontsize=12)
ax.set_ylabel("Settlement Count", fontsize=12)

ax.legend(loc='lower right', title="Locations", fontsize=9, title_fontsize=11)
ax.grid(True, linestyle='-.', alpha=0.3)
ax.spines['top'].set_linewidth(0.5)
ax.spines['right'].set_linewidth(0.5)

annotations = {2045: "Mars Landing", 2050: "Boom on Moon", 2055: "Europa Awakens"}
for year, label in annotations.items():
    y_pos = data.sum(axis=0)[np.where(years == year)[0]][0] + 8
    ax.annotate(label, xy=(year, y_pos), xytext=(year + 1, y_pos + 10),
                arrowprops=dict(facecolor='grey', arrowstyle='->'), fontsize=9)

total_settlements = moon + mars + europa + titan + ceres
perc_moon = 100 * moon / total_settlements
perc_mars = 100 * mars / total_settlements
perc_europa = 100 * europa / total_settlements
perc_titan = 100 * titan / total_settlements
perc_ceres = 100 * ceres / total_settlements

ax2 = ax.twinx()
ax2.plot(years, perc_moon, 'x-', color='#FF6347', label='Moon (%)')
ax2.plot(years, perc_mars, '*-', color='#4682B4', label='Mars (%)')
ax2.plot(years, perc_europa, 's-', color='#9ACD32', label='Europa (%)')
ax2.plot(years, perc_titan, 'd-', color='#DA70D6', label='Titan (%)')
ax2.plot(years, perc_ceres, '^-', color='#FFE4B5', label='Ceres (%)')
ax2.set_ylabel("Proportion of Total Settlements (%)", fontsize=12)
ax2.set_ylim(0, 100)
ax2.legend(loc='upper left', fontsize=9, bbox_to_anchor=(0.05, 1.15), title="Colony Share (%)", title_fontsize=11)

plt.tight_layout()
plt.show()