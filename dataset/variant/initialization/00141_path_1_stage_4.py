import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)
vegetables = np.array([4, 3, 5, 7, 2, 18, 15, 9, 22, 11, 13])  # Randomly shuffled
grains = np.array([8, 10, 9, 5, 6, 14, 13, 11, 12, 7, 15])    # Randomly shuffled
proteins = np.array([10, 4, 19, 7, 6, 16, 5, 3, 12, 14, 9])   # Randomly shuffled
population_growth = np.array([124, 102, 106, 110, 108, 100, 121, 104, 113, 118, 115])  # Randomly shuffled

fig, ax1 = plt.subplots(figsize=(12, 8))

ax1.stackplot(years, vegetables, grains, proteins,
              labels=['Veg', 'Grain', 'Prot'],
              colors=['#32CD32', '#FFD700', '#FF69B4'], alpha=0.85)

ax1.set_title('Diet Change: 2010-20', fontsize=16, fontweight='bold', color='darkgreen')
ax1.set_xlabel('Year', fontsize=12, color='navy')
ax1.set_ylabel('Consumption (MT)', fontsize=12, color='maroon')
ax1.grid(True, linestyle='-.', alpha=0.7)
ax1.set_xticks(years)
ax1.set_xticklabels(years, rotation=45)
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)

ax2 = ax1.twinx()
ax2.plot(years, population_growth, color='navy', linestyle='--', marker='s', label='Pop (M)')
ax2.set_ylabel('Pop (M)', fontsize=12, color='navy')
ax2.tick_params(axis='y', labelcolor='navy')

lines, labels = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines + lines2, labels + labels2, loc='upper right', fontsize=10, bbox_to_anchor=(0.9, 1.0))

ax1.annotate('Shift', xy=(2015, 20), xytext=(2016, 30),
             arrowprops=dict(facecolor='red', arrowstyle='->'), fontsize=10)

plt.tight_layout()
plt.show()