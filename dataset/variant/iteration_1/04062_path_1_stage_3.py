import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2018, 2023)

apples_production = [135, 150, 120, 140, 130]  # Values shuffled
bananas_production = [100, 90, 110, 95, 105]   # Values shuffled
oranges_production = [125, 130, 115, 110, 120] # Values shuffled

bar_height = 0.25

r1 = np.arange(len(years))
r2 = [x + bar_height for x in r1]
r3 = [x + bar_height for x in r2]

fig, ax = plt.subplots(figsize=(12, 7))

# Plot horizontal bars
bars1 = ax.barh(r1, apples_production, color='orange', height=bar_height, edgecolor='grey', label='Apples')
bars2 = ax.barh(r2, bananas_production, color='red', height=bar_height, edgecolor='grey', label='Bananas')
bars3 = ax.barh(r3, oranges_production, color='yellow', height=bar_height, edgecolor='grey', label='Oranges')

def add_labels(bars, ax):
    for bar in bars:
        width = bar.get_width()
        ax.annotate(f'{width}', 
                    xy=(width, bar.get_y() + bar.get_height() / 2),
                    xytext=(3, 0),
                    textcoords="offset points",
                    ha='left', va='center', fontsize=11)

add_labels(bars1, ax)
add_labels(bars2, ax)
add_labels(bars3, ax)

ax.set_title("Annual Fruit Production at Green Acres Farm\n(2018-2022)", fontsize=16, fontweight='bold')
ax.set_ylabel("Year", fontsize=14)
ax.set_xlabel("Production Volume (Metric Tons)", fontsize=14)
ax.set_yticks([r + bar_height for r in range(len(years))])
ax.set_yticklabels(years)
ax.legend()
ax.grid(axis='x', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()