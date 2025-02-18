import matplotlib.pyplot as plt
import numpy as np

# Manually shuffled data arrays
sleep_hours = np.array([9, 6, 10, 7, 8, 5])
coffee_cups = np.array([2, 3, 1, 3, 2, 4])
productivity_scores = np.array([85, 65, 90, 70, 80, 60])
activity_levels = np.array([0.85, 0.8, 0.95, 0.9, 0.7, 1])

fig, ax1 = plt.subplots(figsize=(12, 8))

scatter = ax1.scatter(
    sleep_hours, 
    productivity_scores, 
    c=coffee_cups, 
    cmap='plasma', 
    s=100 * activity_levels, 
    edgecolor='k', 
    alpha=0.7
)

cbar = plt.colorbar(scatter)
cbar.set_label('Cups of Coffee', fontsize=12)

ax1.set_xlabel('Hours of Sleep', fontsize=12)
ax1.set_ylabel('Productivity Score (out of 100)', fontsize=12)

ax2 = ax1.twinx()
ax2.plot(sleep_hours, activity_levels, color='green', marker='o', linestyle='-')
ax2.set_ylabel('Physical Activity Level', fontsize=12, color='green')

plt.tight_layout()
plt.show()