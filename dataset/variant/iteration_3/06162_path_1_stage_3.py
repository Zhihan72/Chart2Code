import matplotlib.pyplot as plt
import numpy as np

# Data setup
years = np.arange(2040, 2061)
moon = np.array([0, 2, 5, 7, 10, 14, 18, 21, 25, 28, 30, 32, 35, 37, 40, 42, 45, 48, 50, 52, 55])
mars = np.array([0, 0, 1, 3, 6, 10, 14, 17, 20, 24, 28, 31, 34, 37, 40, 43, 46, 49, 52, 56, 60])
europa = np.array([0, 0, 0, 1, 3, 5, 8, 11, 14, 17, 20, 22, 24, 26, 30, 33, 35, 37, 40, 43, 45])
titan = np.array([0, 0, 0, 0, 1, 2, 3, 5, 7, 10, 12, 14, 15, 16, 17, 18, 19, 20, 22, 24, 25])
ceres = np.array([0, 0, 0, 0, 0, 1, 2, 4, 7, 10, 13, 15, 18, 21, 24, 26, 28, 31, 33, 35, 38])

data = np.vstack([moon, mars, europa, titan, ceres])
# New color palette
colors = ['#FF6347', '#4682B4', '#9ACD32', '#DA70D6', '#FFE4B5']  # Tomato, SteelBlue, YellowGreen, Orchid, Moccasin

# Plotting
fig, ax = plt.subplots(figsize=(14, 8))
ax.stackplot(years, data, labels=['Moon', 'Mars', 'Europa', 'Titan', 'Ceres'], colors=colors, alpha=0.75)

# Titles and labels
ax.set_title("Evolution of Human Settlements Across Celestial Bodies (2040-2060)", fontsize=16, fontweight='bold', pad=10)
ax.set_xlabel("Year", fontsize=12)
ax.set_ylabel("Number of Settlements", fontsize=12)

# Legend, grid, and spines
ax.legend(loc='lower right', title="Bodies", fontsize=9, title_fontsize=11)
ax.grid(True, linestyle='-.', alpha=0.3)
ax.spines['top'].set_linewidth(0.5)
ax.spines['right'].set_linewidth(0.5)

# Annotations
annotations = {2045: "First Mars Settlement", 2050: "Moon Growth", 2055: "Europa Starts"}
for year, label in annotations.items():
    y_pos = data.sum(axis=0)[np.where(years == year)[0]][0] + 8
    ax.annotate(label, xy=(year, y_pos), xytext=(year + 1, y_pos + 10),
                arrowprops=dict(facecolor='grey', arrowstyle='->'), fontsize=9)

# Percentage calculations and second y-axis
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
ax2.set_ylabel("Percentage of Total Settlements (%)", fontsize=12)
ax2.set_ylim(0, 100)
ax2.legend(loc='upper left', fontsize=9, bbox_to_anchor=(0.05, 1.15), title="Settlement (%)", title_fontsize=11)

plt.tight_layout()
plt.show()