import matplotlib.pyplot as plt
import numpy as np

regions = ['North America', 'Europe', 'Asia', 'South America', 'Africa']
q1_sales = [140, 55, 98, 120, 75]
q2_sales = [160, 45, 65, 150, 110]
q3_sales = [185, 130, 120, 165, 85]
q4_sales = [90, 60, 140, 130, 180]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6), gridspec_kw={'width_ratios': [2.5, 1]})

bar_width = 0.2
bar_positions = np.arange(len(regions))
consistent_color = '#FF4500'  # Single color for all data groups
edge_color = 'black'  # Single edge color for all data groups

ax1.bar(bar_positions - 1.5 * bar_width, q1_sales, width=bar_width, color=consistent_color, edgecolor=edge_color, linestyle='-', linewidth=1)
ax1.bar(bar_positions - 0.5 * bar_width, q2_sales, width=bar_width, color=consistent_color, edgecolor=edge_color, linestyle='-', linewidth=1)
ax1.bar(bar_positions + 0.5 * bar_width, q3_sales, width=bar_width, color=consistent_color, edgecolor=edge_color, linestyle='-', linewidth=1)
ax1.bar(bar_positions + 1.5 * bar_width, q4_sales, width=bar_width, color=consistent_color, edgecolor=edge_color, linestyle='-', linewidth=1)

ax1.xaxis.grid(True, linestyle=':', alpha=0.5)

overall_sales = np.array(q1_sales) + np.array(q2_sales) + np.array(q3_sales) + np.array(q4_sales)

ax2.barh(regions, overall_sales, color=consistent_color, edgecolor=edge_color, linestyle='-', linewidth=1.5, alpha=0.9)

for i in range(len(overall_sales)):
    ax2.text(overall_sales[i] + 5, i, f'{overall_sales[i]}K', va='center', ha='left', fontsize=12, color='black', fontweight='bold')

plt.tight_layout()

plt.show()