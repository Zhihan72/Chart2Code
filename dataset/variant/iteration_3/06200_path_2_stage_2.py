import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2015, 2026)
ev_sales = [450, 200, 1100, 700, 100, 2000, 200, 4300, 3500, 2700, 1500]

# Calculate CO2 reduction based on altered ev_sales
co2_reduction = np.array(ev_sales) * 0.15

fig, ax1 = plt.subplots(figsize=(14, 8))

bars = ax1.bar(years, ev_sales, color='#4CAF50')

for bar in bars:
    yval = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width() / 2, yval + 100, f'{yval}', ha='center', va='bottom', fontsize=10, color='black')

ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Number of EVs Sold', fontsize=12)
ax1.set_title('Techville Electric Vehicle Adoption and CO2 Reduction (2015-2025)', fontsize=16, fontweight='bold', pad=20)
ax1.set_xticks(years)
ax1.set_xticklabels(years, rotation=45, ha='right')

ax2 = ax1.twinx()
ax2.plot(years, co2_reduction, color='blue', linestyle='--', marker='o', linewidth=2, markersize=8)
ax2.set_ylabel('CO2 Reduction (in tons)', fontsize=12, color='blue')
ax2.tick_params(axis='y', labelcolor='blue')

for i, reduction in enumerate(co2_reduction):
    ax2.text(years[i], reduction + 10, f'{reduction:.1f}', ha='center', va='bottom', fontsize=10, color='blue')

plt.tight_layout()
plt.show()