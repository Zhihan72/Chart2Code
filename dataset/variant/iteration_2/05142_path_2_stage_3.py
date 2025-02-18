import matplotlib.pyplot as plt
import numpy as np

regions = ['North America', 'Europe', 'Asia', 'South America', 'Africa']
q1_sales = [140, 55, 98, 120, 75]
q2_sales = [160, 45, 65, 150, 110]
q3_sales = [185, 130, 120, 165, 85]
q4_sales = [90, 60, 140, 130, 180]

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10), gridspec_kw={'height_ratios': [3, 1]})

bar_width = 0.2
bar_positions = np.arange(len(regions))

ax1.bar(bar_positions - 1.5 * bar_width, q1_sales, width=bar_width, color='#FF4500', edgecolor='blue', linestyle='-', linewidth=1)
ax1.bar(bar_positions - 0.5 * bar_width, q2_sales, width=bar_width, color='#FFE4B5', edgecolor='green', linestyle='--', linewidth=2)
ax1.bar(bar_positions + 0.5 * bar_width, q3_sales, width=bar_width, color='#32CD32', edgecolor='red', linestyle='-.', linewidth=3)
ax1.bar(bar_positions + 1.5 * bar_width, q4_sales, width=bar_width, color='#1E90FF', edgecolor='purple', linestyle=':', linewidth=4)

ax1.xaxis.grid(True, linestyle=':', alpha=0.5)

overall_sales = np.array(q1_sales) + np.array(q2_sales) + np.array(q3_sales) + np.array(q4_sales)

ax2.barh(regions, overall_sales, color='#8A2BE2', edgecolor='orange', linestyle='-', linewidth=1.5, alpha=0.9)

for i in range(len(overall_sales)):
    ax2.text(overall_sales[i] + 5, i, f'{overall_sales[i]}K', va='center', ha='left', fontsize=12, color='black', fontweight='bold')

plt.tight_layout()

plt.show()