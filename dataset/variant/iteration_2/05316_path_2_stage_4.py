import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2023)
region_a_produce = [300, 250, 200, 350, 450, 400, 550, 600, 800, 700, 850, 750, 650]
region_b_produce = [200, 300, 100, 400, 150, 500, 600, 700, 1100, 900, 950, 1000, 1050]
region_c_produce = [75, 50, 100, 125, 200, 150, 600, 300, 450, 350, 400, 500, 700]

fig, ax = plt.subplots(figsize=(14, 8))

single_color = '#1f77b4'
ax.stackplot(years, region_a_produce, region_b_produce, region_c_produce, 
             labels=['Region A', 'Region B', 'Region C'], 
             colors=[single_color, single_color, single_color], alpha=0.8)

ax.set_title('Organic Produce Growth 2010-22', fontsize=18, fontstyle='italic')
ax.set_xlabel('Year', fontsize=14, fontweight='bold')
ax.set_ylabel('Tons Delivered', fontsize=14, fontweight='bold')

ax.set_xticks(years)
ax.yaxis.grid(True, linestyle='-.', color='gray', alpha=0.7)
ax.legend(loc='upper right', title='Regions', fontsize=10, edgecolor='black')
ax.tick_params(axis='x', labelrotation=30)

plt.tight_layout()

plt.show()