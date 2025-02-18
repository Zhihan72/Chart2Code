import matplotlib.pyplot as plt
import numpy as np

sleep_hours = np.array([5, 6, 7, 8, 9, 10])
coffee_cups = np.array([4, 3, 3, 2, 2, 1])
productivity_scores = np.array([60, 65, 70, 80, 85, 90])
activity_levels = np.array([1, 0.8, 0.9, 0.7, 0.85, 0.95])

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