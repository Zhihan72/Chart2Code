import matplotlib.pyplot as plt
import numpy as np

celestial_bodies = ['Mercury', 'Venus', 'Mars', 'Jupiter', 'Saturn', 'Asteroids']
missions_data = {
    'Orbiters': [30, 40, 25, 50, 60, 10],
    'Flybys': [50, 50, 30, 40, 35, 70]
}

fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

x_pos = np.arange(len(celestial_bodies))
bar_width = 0.2
bar_depth = 0.4

consistent_color = '#FF5733'

for idx, (mission_type, percentages) in enumerate(missions_data.items()):
    x_offset = bar_width * idx
    ax.bar3d(x_pos + x_offset, idx, [0] * len(percentages), bar_width, bar_depth, percentages, color=consistent_color, alpha=0.7)

ax.set_xticks([])
ax.set_yticks([])
ax.set_zticks([])
ax.set_xlim(0, len(celestial_bodies))
ax.set_ylim(0, len(missions_data))
ax.set_zlim(0, 100)

ax.spines['left'].set_color('none')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.spines['bottom'].set_color('none')

plt.show()