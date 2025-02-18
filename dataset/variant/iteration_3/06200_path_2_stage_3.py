import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2015, 2026)
ev_sales = [450, 200, 1100, 700, 100, 2000, 200, 4300, 3500, 2700, 1500]

# Calculate CO2 reduction based on altered ev_sales
co2_reduction = np.array(ev_sales) * 0.15

fig, ax1 = plt.subplots(figsize=(14, 8))

# Plot horizontal bar chart
bars = ax1.barh(years, ev_sales, color='#4CAF50')

for bar, sales in zip(bars, ev_sales):
    xval = bar.get_width()
    ax1.text(xval + 100, bar.get_y() + bar.get_height() / 2, f'{sales}', va='center', ha='left', fontsize=10, color='black')

ax1.set_ylabel('Year', fontsize=12)
ax1.set_xlabel('Number of EVs Sold', fontsize=12)
ax1.set_title('Techville Electric Vehicle Adoption and CO2 Reduction (2015-2025)', fontsize=16, fontweight='bold', pad=20)
ax1.set_yticks(years)
ax1.set_yticklabels(years)

ax2 = ax1.twiny()
ax2.plot(co2_reduction, years, color='blue', linestyle='--', marker='o', linewidth=2, markersize=8)
ax2.set_xlabel('CO2 Reduction (in tons)', fontsize=12, color='blue')
ax2.tick_params(axis='x', labelcolor='blue')

for i, reduction in enumerate(co2_reduction):
    ax2.text(reduction + 10, years[i], f'{reduction:.1f}', va='center', ha='left', fontsize=10, color='blue')

plt.tight_layout()
plt.show()