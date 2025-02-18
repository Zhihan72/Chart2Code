import matplotlib.pyplot as plt
import numpy as np

# Data
regions = ['North', 'South', 'East', 'West']
juice_sales = [1200, 1500, 1400, 1300]
soda_sales = [1800, 1600, 1700, 1500]
energy_sales = [900, 1100, 1050, 950]

# Sort data by juice sales
sorted_indices = np.argsort(juice_sales)
regions_sorted = [regions[i] for i in sorted_indices]
juice_sorted = [juice_sales[i] for i in sorted_indices]
soda_sorted = [soda_sales[i] for i in sorted_indices]
energy_sorted = [energy_sales[i] for i in sorted_indices]

x = np.arange(len(regions))
width = 0.25

fig, ax1 = plt.subplots(figsize=(10, 8))

# Plot data
bars1 = ax1.bar(x - width, juice_sorted, width, color='#ff9999', label='Juice')
bars2 = ax1.bar(x, soda_sorted, width, color='#66b3ff', label='Soda')
bars3 = ax1.bar(x + width, energy_sorted, width, color='#99ff99', label='Energy')

ax1.set_title('Monthly Beverage Sales by Region', fontsize=16, fontweight='bold')
ax1.set_xlabel('Region', fontsize=13)
ax1.set_ylabel('Sales (liters)', fontsize=13)
ax1.set_xticks(x)
ax1.set_xticklabels(regions_sorted, fontsize=12)

ax1.legend()

def add_labels(ax, bars):
    for bar in bars:
        yval = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2.0, yval + 30, int(yval), va='center', ha='center', fontsize=11, fontweight='bold', color='black')

add_labels(ax1, bars1)
add_labels(ax1, bars2)
add_labels(ax1, bars3)

plt.tight_layout()
plt.show()