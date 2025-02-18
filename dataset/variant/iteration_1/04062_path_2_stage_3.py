import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2018, 2023)

apples_production = [120, 130, 135, 140, 150]
bananas_production = [90, 95, 100, 105, 110]

bar_height = 0.25

r1 = np.arange(len(years))
r2 = [x + bar_height for x in r1]

fig, ax = plt.subplots(figsize=(12, 7))

bars1 = ax.barh(r1, apples_production, color='yellow', height=bar_height, edgecolor='grey', label='Apples')
bars2 = ax.barh(r2, bananas_production, color='orange', height=bar_height, edgecolor='grey', label='Bananas')

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

ax.set_title("Annual Fruit Production at Green Acres Farm\n(2018-2022)", fontsize=16, fontweight='bold')
ax.set_ylabel("Year", fontsize=14)
ax.set_xlabel("Production Volume (Metric Tons)", fontsize=14)
ax.set_yticks([r + bar_height / 2 for r in range(len(years))])
ax.set_yticklabels(years)
ax.legend()

ax.grid(axis='x', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()