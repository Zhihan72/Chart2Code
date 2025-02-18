import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2015, 2026)

# Data for each region
north_america = [100, 150, 230, 330, 450, 580, 730, 890, 1070, 1260, 1460]
europe = [80, 120, 200, 290, 410, 550, 720, 900, 1100, 1310, 1530]
asia = [60, 90, 170, 270, 390, 530, 690, 870, 1070, 1290, 1520]
other_regions = [20, 35, 60, 95, 140, 200, 280, 380, 500, 640, 800]

data = np.vstack([north_america, europe, asia, other_regions])

fig, ax = plt.subplots(figsize=(12, 8))

# Stylistic changes to the stacked plot with shuffled labels
ax.stackplot(years, data, labels=['North America', 'Asia', 'Europe', 'Other Regions'],
             colors=['#2ca02c', '#d62728', '#ff7f0e', '#1f77b4'], alpha=0.85, edgecolor='gray', linewidth=1.5)

# Changed textual elements
ax.set_title('EV Adoption Growth by Areas\nfrom 2015 to 2025', fontsize=18, fontweight='bold', pad=25)
ax.set_xlabel('Year', fontsize=13, style='italic')
ax.set_ylabel('EVs Count (thousands)', fontsize=13, style='italic')

ax.legend(loc='upper left', fontsize=11, shadow=True, fancybox=True)
ax.grid(axis='y', linestyle=':', linewidth=1, alpha=0.6)
plt.xticks(years, rotation=30)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
plt.tight_layout()

plt.show()