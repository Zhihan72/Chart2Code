import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2018, 2023)

apples_production = [120, 130, 135, 140, 150]
bananas_production = [90, 95, 100, 105, 110]

bar_height = 0.3

r1 = np.arange(len(years))
r2 = [x + bar_height for x in r1]

fig, ax = plt.subplots(figsize=(12, 7))

bars1 = ax.barh(r1, apples_production, color='limegreen', height=bar_height, edgecolor='blue', label='Apples', hatch='/')
bars2 = ax.barh(r2, bananas_production, color='c', height=bar_height, edgecolor='purple', label='Bananas', hatch='\\')

def add_labels(bars, ax):
    for bar in bars:
        width = bar.get_width()
        ax.annotate(f'{width}',
                    xy=(width, bar.get_y() + bar.get_height() / 2),
                    xytext=(5, 0),
                    textcoords="offset points",
                    ha='left', va='center', fontsize=10, color='red')

add_labels(bars1, ax)
add_labels(bars2, ax)

ax.set_title("Crop Yield Figures at Blue Valley Ranch\n(2018-2022)", fontsize=16, fontweight='bold', color='darkred')
ax.set_ylabel("Timeline", fontsize=14, color='darkgreen')
ax.set_xlabel("Yield Volume (Metric Tons)", fontsize=14, color='darkblue')
ax.set_yticks([r + bar_height / 2 for r in range(len(years))])
ax.set_yticklabels(['2018', '2019', '2020', '2021', '2022'])
ax.legend(frameon=False)

ax.grid(axis='x', linestyle='-.', alpha=0.5)

plt.tight_layout()
plt.show()