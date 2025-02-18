import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2000, 2021)

# Altered number of robots deployed in various manufacturing sectors
assembly_robots = [0, 6, 12, 18, 32, 48, 68, 86, 104, 118, 136, 148, 162, 156, 148, 128, 112, 94, 72, 36, 18]
painting_robots = [0, 3, 6, 11, 20, 32, 44, 57, 68, 76, 84, 93, 98, 100, 88, 82, 63, 51, 37, 19, 12]
welding_robots = [0, 4, 9, 14, 26, 38, 50, 73, 92, 112, 128, 144, 152, 150, 143, 126, 108, 83, 46, 23, 11]
packaging_robots = [0, 2, 5, 8, 12, 16, 24, 32, 46, 52, 70, 78, 86, 84, 76, 68, 59, 47, 34, 17, 6]

robots_data = np.vstack([assembly_robots, painting_robots, welding_robots, packaging_robots])
cumulative_data = np.cumsum(robots_data, axis=0)

colors = ['#FF4500', '#32CD32', '#DAA520', '#4682B4']

fig, ax = plt.subplots(figsize=(14, 9))

ax.fill_between(years, 0, cumulative_data[0], step='mid', hatch='/', color=colors[0], label='Assembly', alpha=0.85)
ax.fill_between(years, cumulative_data[0], cumulative_data[1], step='mid', hatch='\\', color=colors[1], label='Painting', alpha=0.85)
ax.fill_between(years, cumulative_data[1], cumulative_data[2], step='mid', hatch='-', color=colors[2], label='Welding', alpha=0.85)
ax.fill_between(years, cumulative_data[2], cumulative_data[3], step='mid', hatch='|', color=colors[3], label='Packaging', alpha=0.85)

ax.set_title("Robot Workforce in Manufacturing (2000-2020)", fontsize=18, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Robots', fontsize=14)

ax.set_xticks(np.arange(2000, 2021, 2))
ax.set_xticklabels(np.arange(2000, 2021, 2), fontsize=12, rotation=45)
ax.set_yticks(np.arange(0, 501, 50))
ax.set_yticklabels(np.arange(0, 501, 50), fontsize=12)

ax.legend(loc='lower right', fontsize=12, frameon=False)

ax.grid(True, which='both', axis='x', linestyle='-.', alpha=0.3)

important_events = [(2005, 55, 'AI Emergence'), (2015, 265, 'Peak'), (2020, 195, 'Regulation')]
for x, y, text in important_events:
    ax.annotate(text, xy=(x, y), xytext=(x+0.5, y+40), arrowprops=dict(facecolor='gray', arrowstyle='-|>'), fontsize=10, color='black')

plt.tight_layout()
plt.show()