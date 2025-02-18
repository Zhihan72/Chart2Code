import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2000, 2021)
sedans = [9.5, 9.2, 8.9, 8.7, 8.5, 8.3, 8.0, 7.8, 7.6, 7.4, 7.2, 7.0, 6.8, 6.5, 6.3, 6.1, 5.9, 5.7, 5.5, 5.3, 5.0]
suvs = [14.0, 13.8, 13.5, 13.2, 12.8, 12.5, 12.2, 11.8, 11.5, 11.2, 10.8, 10.5, 10.2, 9.8, 9.5, 9.2, 8.9, 8.6, 8.3, 8.0, 7.7]
evs = [18.0, 17.5, 17.0, 16.5, 16.0, 15.5, 15.0, 14.5, 14.0, 13.5, 13.0, 12.5, 12.0, 11.5, 11.0, 10.5, 10.0, 9.5, 9.0, 8.5, 8.0]
hybrids = [6.0, 5.8, 5.6, 5.5, 5.3, 5.1, 5.0, 4.8, 4.7, 4.5, 4.3, 4.2, 4.0, 3.9, 3.8, 3.6, 3.5, 3.4, 3.2, 3.1, 3.0]

data = [sedans, suvs, evs, hybrids]
labels = ['Sedans', 'SUVs', 'EVs', 'Hybrids']

fig, ax = plt.subplots(figsize=(14, 9))

# Use a single color for all box plot elements
single_color = 'lightblue'
box = ax.boxplot(data, vert=False, patch_artist=True, notch=True,
                 boxprops=dict(facecolor=single_color, color='navy'),
                 whiskerprops=dict(color='navy'),
                 capprops=dict(color='navy'),
                 medianprops=dict(color='darkorange', linewidth=2),
                 flierprops=dict(markerfacecolor='red', marker='o', markersize=8, linestyle='none'))

means = [np.mean(cat) for cat in data]
ax.scatter(means, range(1, len(labels) + 1), color='blue', marker='D', label='Mean Value')

ax.set_title("Fuel Efficiency Evolution in Vehicles\n(2000-2020)", fontsize=16, fontweight='bold')
ax.set_xlabel("Fuel Consumption (Liters per 100km)", fontsize=12)
ax.set_yticks(ticks=[1, 2, 3, 4])
ax.set_yticklabels(labels, fontsize=11)
ax.grid(axis='x', linestyle='--', alpha=0.7)
ax.legend(loc='upper right')

for i, cat in enumerate(data, start=1):
    min_val, max_val = min(cat), max(cat)
    ax.annotate(f'Min: {min_val}', xy=(min_val, i), xytext=(min_val-1.5, i+0.1),
                arrowprops=dict(facecolor='green', shrink=0.05), fontsize=9, color='green')
    ax.annotate(f'Max: {max_val}', xy=(max_val, i), xytext=(max_val+0.5, i-0.1),
                arrowprops=dict(facecolor='red', shrink=0.05), fontsize=9, color='red')

plt.tight_layout()
plt.show()