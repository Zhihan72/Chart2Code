import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2015, 2026)

north_america = [100, 150, 230, 330, 450, 580, 730, 890, 1070, 1260, 1460]
europe = [80, 120, 200, 290, 410, 550, 720, 900, 1100, 1310, 1530]
asia = [60, 90, 170, 270, 390, 530, 690, 870, 1070, 1290, 1520]
other_regions = [20, 35, 60, 95, 140, 200, 280, 380, 500, 640, 800]

data = np.vstack([north_america, europe, asia, other_regions])

fig, ax = plt.subplots(figsize=(12, 8))

# Updated the color palette for the stacked area plot
ax.stackplot(years, data, labels=['North America', 'Europe', 'Asia', 'Other Regions'],
             colors=['#e41a1c', '#377eb8', '#4daf4a', '#984ea3'], alpha=0.8)

ax.set_title('Growth of Electric Vehicle Adoption by Region\nfrom 2015 to 2025', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Number of Electric Vehicles (in thousands)', fontsize=12)

ax.legend(loc='upper left', title='Regions', fontsize=10, bbox_to_anchor=(1, 1))

ax.grid(axis='y', linestyle='--', alpha=0.7)

plt.xticks(years, rotation=45)

plt.tight_layout()

plt.show()