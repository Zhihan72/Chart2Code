import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2040, 2061)

moon = np.array([0, 2, 5, 7, 10, 14, 18, 21, 25, 28, 30, 32, 35, 37, 40, 42, 45, 48, 50, 52, 55])
mars = np.array([0, 0, 1, 3, 6, 10, 14, 17, 20, 24, 28, 31, 34, 37, 40, 43, 46, 49, 52, 56, 60])
europa = np.array([0, 0, 0, 1, 3, 5, 8, 11, 14, 17, 20, 22, 24, 26, 30, 33, 35, 37, 40, 43, 45])
titan = np.array([0, 0, 0, 0, 1, 2, 3, 5, 7, 10, 12, 14, 15, 16, 17, 18, 19, 20, 22, 24, 25])

data = np.vstack([moon, mars, europa, titan])

colors = ['#4682B4', '#32CD32', '#DAA520', '#FF6347']

fig, ax = plt.subplots(figsize=(14, 8))

ax.stackplot(years, data, labels=['Titan', 'Europa', 'Moon', 'Mars'], colors=colors, alpha=0.85)

ax.set_title("Evolution of Human Settlements (2040-2060)", fontsize=18, fontweight='bold', pad=15)
ax.set_xlabel("Year", fontsize=14)
ax.set_ylabel("Number of Settlements", fontsize=14)
ax.legend(loc='lower right', title="Bodies", fontsize=11, title_fontsize=13)

ax.grid(False)

annotations = {2045: "First on Mars", 2050: "Moon Boom", 2055: "Start on Europa"}
for year, label in annotations.items():
    y_pos = data.sum(axis=0)[np.where(years == year)[0]][0] + 5
    ax.annotate(label, xy=(year, y_pos), xytext=(year + 1, y_pos + 10),
                arrowprops=dict(facecolor='blue', arrowstyle='->'), fontsize=11)

total_settlements = moon + mars + europa + titan
perc_moon = 100 * moon / total_settlements
perc_mars = 100 * mars / total_settlements
perc_europa = 100 * europa / total_settlements
perc_titan = 100 * titan / total_settlements

ax2 = ax.twinx()
ax2.plot(years, perc_moon, '^-.', color='#4682B4', label='Moon (%)')
ax2.plot(years, perc_mars, '^-.', color='#32CD32', label='Mars (%)')
ax2.plot(years, perc_europa, '^-.', color='#DAA520', label='Europa (%)')
ax2.plot(years, perc_titan, '^-.', color='#FF6347', label='Titan (%)')
ax2.set_ylabel("Percentage of Total (%)", fontsize=14)
ax2.set_ylim(0, 100)

ax2.legend(loc='upper left', fontsize=11, bbox_to_anchor=(0.95, 0.90), title="Proportions (%)", title_fontsize=13)

plt.tight_layout()

plt.show()