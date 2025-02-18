import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2000, 2021)

# Number of robots deployed in various manufacturing sectors
assembly_robots = [0, 5, 10, 20, 35, 50, 70, 85, 100, 120, 140, 150, 155, 160, 150, 130, 110, 90, 60, 30, 15]
painting_robots = [0, 2, 5, 10, 18, 30, 45, 55, 65, 75, 85, 90, 95, 98, 92, 80, 65, 55, 35, 20, 10]
welding_robots = [0, 3, 8, 15, 25, 40, 55, 70, 90, 110, 130, 145, 150, 155, 145, 125, 105, 80, 50, 25, 10]
packaging_robots = [0, 1, 3, 6, 10, 15, 22, 30, 42, 54, 68, 75, 80, 85, 80, 70, 55, 45, 30, 15, 5]

robots_data = np.vstack([assembly_robots, painting_robots, welding_robots, packaging_robots])
cumulative_data = np.cumsum(robots_data, axis=0)

# Changed colors order
colors = ['#4682B4', '#DAA520', '#FF4500', '#32CD32']

fig, ax = plt.subplots(figsize=(14, 9))

# Plot the area chart using `fill_between`
ax.fill_between(years, 0, cumulative_data[0], color=colors[0], label='Assembly', alpha=0.85)
ax.fill_between(years, cumulative_data[0], cumulative_data[1], color=colors[1], label='Painting', alpha=0.85)
ax.fill_between(years, cumulative_data[1], cumulative_data[2], color=colors[2], label='Welding', alpha=0.85)
ax.fill_between(years, cumulative_data[2], cumulative_data[3], color=colors[3], label='Packaging', alpha=0.85)

# Labels and Title
ax.set_title("Robot Workforce in Manufacturing (2000-2020)", fontsize=18, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Robots', fontsize=14)

ax.set_xticks(np.arange(2000, 2021, 2))
ax.set_xticklabels(np.arange(2000, 2021, 2), fontsize=12, rotation=45)
ax.set_yticks(np.arange(0, 501, 50))
ax.set_yticklabels(np.arange(0, 501, 50), fontsize=12)

ax.legend(loc='upper left', fontsize=12)

ax.grid(True, which='both', axis='y', linestyle='--', alpha=0.6)

important_events = [(2005, 50, 'AI Emergence'), (2015, 240, 'Peak'), (2020, 185, 'Regulation')]
for x, y, text in important_events:
    ax.annotate(text, xy=(x, y), xytext=(x+0.5, y+40), arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, color='black')

plt.tight_layout()
plt.show()