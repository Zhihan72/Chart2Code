import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cm as cm

cities = ["New York", "London", "Tokyo", "Paris", "Toronto", "Sydney", "Berlin", "Singapore"]
parks_per_square_mile = np.array([3.2, 4.1, 2.8, 5.0, 3.5, 6.3, 4.5, 3.7])

sorted_indices = np.argsort(parks_per_square_mile)
sorted_parks_per_square_mile = parks_per_square_mile[sorted_indices]

average_rainfall = np.array([49.9, 23.8, 60.4, 25.3, 32.1, 50.3, 22.7, 92.0])
sorted_average_rainfall = average_rainfall[sorted_indices]

positions = np.arange(len(cities))
bar_width = 0.6

fig, ax1 = plt.subplots(figsize=(14, 8))
color_map = cm.viridis(sorted_parks_per_square_mile / max(sorted_parks_per_square_mile))

bars = ax1.bar(positions, sorted_parks_per_square_mile, color=color_map, width=bar_width, alpha=0.9, edgecolor='black')

for bar, height in zip(bars, sorted_parks_per_square_mile):
    ax1.text(bar.get_x() + bar.get_width()/2, height - 0.1, f'{height:.1f}', ha='center', va='bottom', color='white', fontsize=10)

ax2 = ax1.twinx()
ax2.plot(positions, sorted_average_rainfall, color='orange', marker='o', linewidth=2.5)

ax1.set_xticks(positions)
ax1.set_xticklabels([])  # Remove city labels
ax1.set_yticklabels([])  # Remove left axis labels
ax2.set_yticklabels([])  # Remove right axis labels

ax1.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()