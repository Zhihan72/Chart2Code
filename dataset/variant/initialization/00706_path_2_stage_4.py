import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cm as cm

cities = ["New York", "London", "Tokyo", "Paris", "Toronto", "Sydney", "Berlin", "Singapore"]
parks_per_square_mile = np.array([3.2, 4.1, 2.8, 5.0, 3.5, 6.3, 4.5, 3.7])

# New fake data for average temperature
average_temperature = np.array([58.3, 51.8, 61.2, 52.0, 47.8, 64.4, 48.5, 81.2])

sorted_indices = np.argsort(parks_per_square_mile)
sorted_parks_per_square_mile = parks_per_square_mile[sorted_indices]

average_rainfall = np.array([49.9, 23.8, 60.4, 25.3, 32.1, 50.3, 22.7, 92.0])
sorted_average_rainfall = average_rainfall[sorted_indices]
sorted_average_temperature = average_temperature[sorted_indices]  # Sort the temperature data

positions = np.arange(len(cities))
bar_width = 0.6

fig, ax1 = plt.subplots(figsize=(14, 8))
color_map = cm.inferno(sorted_parks_per_square_mile / max(sorted_parks_per_square_mile))

bars = ax1.bar(positions, sorted_parks_per_square_mile, color=color_map, width=bar_width, alpha=0.85, edgecolor='gray', linestyle='--')

for bar, height in zip(bars, sorted_parks_per_square_mile):
    ax1.text(bar.get_x() + bar.get_width()/2, height - 0.15, f'{height:.1f}', ha='center', va='bottom', color='black', fontsize=11)

ax2 = ax1.twinx()
ax2.plot(positions, sorted_average_rainfall, color='teal', marker='s', linestyle='-', linewidth=2)

# Plotting the new dataset - average temperature
ax2.plot(positions, sorted_average_temperature, color='orange', marker='o', linestyle='--', linewidth=2)

ax1.set_xticks(positions)
ax1.set_xticklabels([])  # Keep the city labels removed
ax1.set_yticklabels([])  # Keep the left y-axis labels removed
ax2.set_yticklabels([])  # Keep the right y-axis labels removed

ax1.grid(axis='y', linestyle='-.', alpha=0.6)

plt.tight_layout()
plt.show()