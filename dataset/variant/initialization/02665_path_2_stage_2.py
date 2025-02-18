import matplotlib.pyplot as plt
import numpy as np

marketplaces = ['ShopNow', 'MegaMart', 'QuickCart', 'EasyShop', 'BuyFast']
delivery_times = [
    [2, 3, 5, 2, 3, 4, 5, 2, 3, 6, 2, 3, 4],
    [4, 3, 5, 6, 4, 7, 3, 6, 4, 5, 7, 6, 8, 20],
    [1, 2, 2, 1, 3, 2, 1, 2, 3, 1, 1, 2],
    [3, 5, 4, 6, 5, 3, 4, 5, 6, 4, 5, 7, 3, 4],
    [6, 8, 7, 9, 8, 10, 7, 6, 7, 11, 12, 10]
]
average_delivery_times = [np.mean(times) for times in delivery_times]

# New set of colors for box plots
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']

fig, ax = plt.subplots(figsize=(12, 8))
bplot = ax.boxplot(delivery_times, vert=False, patch_artist=True, 
                   notch=False,
                   boxprops=dict(facecolor='lightgray', color='gray'),
                   whiskerprops=dict(color='darkgray'),
                   capprops=dict(color='lightgreen'),
                   medianprops=dict(color='purple', linewidth=2),
                   flierprops=dict(marker='x', color='orange', markersize=5))

# Customize box colors with new colors
for patch, color in zip(bplot['boxes'], colors):
    patch.set_facecolor(color)

# Overlay a line plot for average delivery times
ax.plot(average_delivery_times, range(1, len(marketplaces) + 1), 
        linestyle='--', marker='s', color='indigo', linewidth=1, markersize=6, 
        label='Average Delivery Time')

ax.yaxis.grid(True, linestyle=':', linewidth=0.5, alpha=0.9)
ax.set_yticklabels(marketplaces, fontsize=12)
ax.set_title('Delivery Times Distribution Across Marketplaces', 
             fontsize=14, fontweight='semibold')
ax.set_xlabel('Delivery Time (Days)', fontsize=11)

# Add a legend
handles = [plt.Line2D([0], [0], color=c, lw=4) for c in colors] + [plt.Line2D([0], [0], color='indigo', lw=1, marker='s')]
legend_labels = ['ShopNow', 'MegaMart', 'QuickCart', 'EasyShop', 'BuyFast', 'Average']
ax.legend(handles, legend_labels, loc='lower left', title='Platforms', fontsize=9)

plt.tight_layout()
plt.show()