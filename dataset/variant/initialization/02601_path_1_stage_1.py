import matplotlib.pyplot as plt
import numpy as np

celestial_bodies = ['Mars', 'Venus', 'Jupiter', 'Saturn', 'Mercury', 'Moon', 'Comets']
missions_count = [55, 40, 15, 12, 8, 65, 10]
colors = ['#FF5733', '#FFBD33', '#75FF33', '#33FF57', '#33FFF5', '#335BFF', '#AF33FF']

fig, ax = plt.subplots(figsize=(12, 7))

# Plot the horizontal bar chart
bars = ax.barh(celestial_bodies, missions_count, color=colors, edgecolor='black')

# Annotate each bar with the mission count
for bar, count in zip(bars, missions_count):
    xval = bar.get_width()
    ax.text(xval + 2, bar.get_y() + bar.get_height()/2, str(count), va='center', fontsize=10, fontweight='bold', color='black')

ax.set_title('Exploratory Missions Across the Solar System\nEarth\'s Focus on Celestial Bodies as of 2023', fontsize=16, fontweight='bold')
ax.set_xlabel('Number of Missions', fontsize=12, labelpad=10)
ax.set_ylabel('Celestial Bodies', fontsize=12, labelpad=10)

# Configure limits and grid
ax.set_xlim(0, 70)
ax.grid(True, which='both', axis='x', linestyle='--', linewidth=0.7, alpha=0.7)

plt.tight_layout()
plt.show()