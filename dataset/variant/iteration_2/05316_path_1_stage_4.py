import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2023)

region_a_produce = [200, 250, 300, 350, 400, 450, 550, 600, 650, 700, 750, 800, 850]
region_c_produce = [50, 75, 100, 125, 150, 200, 300, 350, 400, 450, 500, 600, 700]

fig, ax = plt.subplots(figsize=(14, 8))

ax.stackplot(years, region_a_produce, region_c_produce, 
             labels=['Sector Y', 'Area Z'], 
             colors=['#f7a8b8', '#ffe082'], alpha=0.6)

ax.set_title('The Growth in Organic Harvest Distribution\n2010-2022', fontsize=20, fontweight='bold', color='darkblue')
ax.set_xlabel('Year', fontsize=15, fontstyle='italic')
ax.set_ylabel('Metric Tons of Organic Produce', fontsize=15, fontstyle='italic')

ax.set_xticks(years)
ax.yaxis.grid(False)
ax.xaxis.grid(True, linestyle='-.', alpha=0.3)
ax.legend(loc='lower right', title='Province Groups', fontsize=13, frameon=False)
ax.tick_params(axis='x', labelrotation=30)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()
plt.show()