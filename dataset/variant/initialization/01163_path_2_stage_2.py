import matplotlib.pyplot as plt
import numpy as np

sedans = [9.5, 9.2, 8.9, 8.7, 8.5, 8.3, 8.0, 7.8, 7.6, 7.4, 7.2, 7.0, 6.8, 6.5, 6.3, 6.1, 5.9, 5.7, 5.5, 5.3, 5.0]

fig, ax = plt.subplots(figsize=(7, 9))

# Use a single color for the box plot
single_color = 'lightblue'
box = ax.boxplot(sedans, vert=True, patch_artist=True, notch=True,
                 boxprops=dict(facecolor=single_color, color='navy'),
                 whiskerprops=dict(color='navy'),
                 capprops=dict(color='navy'),
                 medianprops=dict(color='darkorange', linewidth=2),
                 flierprops=dict(markerfacecolor='red', marker='o', markersize=8, linestyle='none'))

mean = np.mean(sedans)
ax.scatter(1, mean, color='blue', marker='D', label='Mean Value')

ax.set_title("Fuel Efficiency of Sedans\n(2000-2020)", fontsize=16, fontweight='bold')
ax.set_ylabel("Fuel Consumption (Liters per 100km)", fontsize=12)
ax.set_xticks(ticks=[1])
ax.set_xticklabels(['Sedans'], fontsize=11)
ax.grid(axis='y', linestyle='--', alpha=0.7)
ax.legend(loc='upper right')

min_val, max_val = min(sedans), max(sedans)
ax.annotate(f'Min: {min_val}', xy=(1, min_val), xytext=(1.2, min_val-0.5),
            arrowprops=dict(facecolor='green', shrink=0.05), fontsize=9, color='green')
ax.annotate(f'Max: {max_val}', xy=(1, max_val), xytext=(1.2, max_val+0.5),
            arrowprops=dict(facecolor='red', shrink=0.05), fontsize=9, color='red')

plt.tight_layout()
plt.show()