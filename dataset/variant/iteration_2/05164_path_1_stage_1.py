import matplotlib.pyplot as plt
import numpy as np

sectors = ['Neural Computing', 'Cyber Defense', 'Quantum AI', 'Clean Energy', 'Interstellar Tech']

expenditure_data = [
    [100, 120, 130, 125, 140, 150, 135, 145, 155, 160],
    [75, 85, 80, 90, 110, 120, 115, 105, 100, 95],
    [200, 220, 210, 230, 240, 250, 245, 255, 260, 275],
    [50, 55, 60, 65, 70, 75, 80, 85, 90, 95],
    [180, 190, 200, 195, 185, 210, 220, 225, 230, 235]
]

years = np.arange(2013, 2023)

fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(18, 8))

ax1 = axes[0]
bp = ax1.boxplot(expenditure_data, vert=False, patch_artist=True, showmeans=True, notch=True,
                 boxprops=dict(facecolor="#ffcccb", color="#8b0000", linewidth=1.2),
                 medianprops=dict(color="#0000cd", linewidth=1.5),
                 meanprops=dict(marker='D', markeredgecolor='black', markerfacecolor='lime'),
                 whiskerprops=dict(color="#8b0000"), capprops=dict(color="#8b0000"))

ax1.set_yticklabels(sectors, fontsize=11)
ax1.set_title("10-Year Analysis of R&D Investment Trends by Sector", fontsize=14, fontweight='bold', pad=20)
ax1.set_xlabel("Investment (Millions USD)", fontsize=12)
ax1.set_ylabel("Industry Sectors", fontsize=12)
ax1.xaxis.grid(True, linestyle='--', alpha=0.7)

ax2 = axes[1]
growth_rates = [
    [10, 5, 20, 15, 10, 15, 5, 10, 15, 20],
    [8, 12, 5, 10, 20, 15, 10, 5, 8, 12],
    [15, 10, 20, 15, 20, 10, 15, 20, 10, 15],
    [5, 8, 12, 15, 5, 8, 10, 12, 15, 10],
    [12, 10, 5, 20, 15, 10, 20, 15, 10, 12]
]
for idx, sector_growth in enumerate(growth_rates):
    ax2.scatter(years, sector_growth, label=sectors[idx], s=100, alpha=0.7, edgecolors='w')

ax2.set_title("Comparative Study of Sector-wise R&D Growth (2013-2022)", fontsize=14, fontweight='bold', pad=20)
ax2.set_xlabel("Timeline (Year)", fontsize=12)
ax2.set_ylabel("Growth (%)", fontsize=12)
ax2.legend(title='Industries', fontsize=9, title_fontsize=10)
ax2.yaxis.grid(True, linestyle='--', alpha=0.7)
ax2.set_xticks(years)
ax2.set_xticklabels([str(yr) for yr in years], rotation=45, ha='right')

plt.tight_layout()
plt.show()