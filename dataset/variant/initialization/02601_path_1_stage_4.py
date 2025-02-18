import matplotlib.pyplot as plt
import numpy as np

# Existing data series
celestial_bodies = ['Jupiter', 'Mars', 'Venus', 'Moon', 'Mercury', 'Saturn', 'Comets']
missions_count = [15, 55, 40, 65, 8, 12, 10]
# Additional data series
additional_bodies = ['Asteroids', 'Neptune', 'Europa']
additional_missions_count = [4, 20, 9]

# Combine both data series
all_bodies = celestial_bodies + additional_bodies
all_missions_count = missions_count + additional_missions_count

# Manually shuffled colors list, extended for new categories
colors = ['#FF5733', '#33FF57', '#AF33FF', '#335BFF', '#33FFF5', '#75FF33', '#FFBD33', '#C70039', '#900C3F', '#FFC300']

fig, ax = plt.subplots(figsize=(12, 7))
bars = ax.barh(all_bodies, all_missions_count, color=colors, edgecolor='black')

for bar, count in zip(bars, all_missions_count):
    xval = bar.get_width()
    ax.text(xval + 2, bar.get_y() + bar.get_height()/2, str(count), va='center', fontsize=10, fontweight='bold', color='black')

ax.set_title('Space Exploration and Celestial Surveys in the Cosmos', fontsize=16, fontweight='bold')
ax.set_xlabel('Missions Launched', fontsize=12, labelpad=10)
ax.set_ylabel('Planetary Targets', fontsize=12, labelpad=10)

ax.set_xlim(0, 70)
ax.grid(True, which='both', axis='x', linestyle='--', linewidth=0.7, alpha=0.7)

plt.tight_layout()
plt.show()