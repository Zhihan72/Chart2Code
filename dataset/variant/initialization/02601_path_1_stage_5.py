import matplotlib.pyplot as plt
import numpy as np

# Data series
celestial_bodies = ['Jupiter', 'Mars', 'Venus', 'Moon', 'Mercury', 'Saturn', 'Comets']
missions_count = [15, 55, 40, 65, 8, 12, 10]
additional_bodies = ['Asteroids', 'Neptune', 'Europa']
additional_missions_count = [4, 20, 9]

# Combine both data series
all_bodies = celestial_bodies + additional_bodies
all_missions_count = missions_count + additional_missions_count

# Altered colors list for randomness
colors = ['#33FF57', '#FF5733', '#335BFF', '#AF33FF', '#75FF33', '#FFBD33', '#33FFF5', '#900C3F', '#C70039', '#FFC300']

fig, ax = plt.subplots(figsize=(12, 7))
bars = ax.barh(all_bodies, all_missions_count, color=colors, edgecolor='gray', linestyle='dotted')

for bar, count in zip(bars, all_missions_count):
    xval = bar.get_width()
    ax.text(xval + 2, bar.get_y() + bar.get_height()/2, str(count), va='center', fontsize=9, fontweight='normal', color='blue')

ax.set_title('Space Exploration and Surveys', fontsize=14, fontweight='normal', style='italic')
ax.set_xlabel('Number of Missions', fontsize=11, labelpad=8)
ax.set_ylabel('Targets', fontsize=11, labelpad=8)

ax.set_xlim(0, 70)
ax.grid(True, which='major', axis='x', linestyle='-', linewidth=0.5, alpha=0.5)

plt.tight_layout()
plt.show()