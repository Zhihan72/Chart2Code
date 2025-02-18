import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2020)
corn_yield = np.array([6.8, 5.7, 5.5, 6.3, 5.8, 6.1, 5.2, 6.0, 5.9, 6.5])
soybean_yield = np.array([3.5, 2.9, 2.6, 3.0, 2.4, 3.1, 2.1, 3.3, 2.8, 2.5])

fig, ax1 = plt.subplots(figsize=(14, 8))

ax1.plot(years, corn_yield, color='blue', linestyle='-.', marker='^', linewidth=2, markersize=10, label='Bountiful Corn')
ax1.plot(years, soybean_yield, color='purple', linestyle='-', marker='d', linewidth=2, markersize=10, label='Soybean Surprise')

annotations = {
    2015: ('Dry Spell', (0, 40)),
    2018: ('Top Yield Year', (0, -40))
}

for year, (text, offset) in annotations.items():
    index = np.where(years == year)[0][0]
    ax1.annotate(
        text, 
        (years[index], corn_yield[index]), 
        xytext=offset, 
        textcoords='offset points', 
        arrowprops=dict(arrowstyle='->', color='darkblue'),
        ha='center', fontsize=10, color='darkgreen'
    )

ax1.set_title("Ten-Year Harvest Insights: Corn and Soybean\n(2010-2019)", fontsize=16, fontweight='bold', pad=20)
ax1.set_xlabel("Calendar Year", fontsize=14)
ax1.set_ylabel("Production (Metric Tons)", fontsize=14)

lines = ax1.get_lines()
labels = [l.get_label() for l in lines]
ax1.legend(lines, labels, loc='lower right', fontsize=12)

ax1.grid(True, linestyle='-.', alpha=0.5)

plt.tight_layout()
plt.show()