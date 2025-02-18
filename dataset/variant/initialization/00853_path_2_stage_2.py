import matplotlib.pyplot as plt
import numpy as np

celestial_bodies = ['Mercury', 'Venus', 'Mars', 'Jupiter', 'Saturn', 'Asteroids']
missions_data = {
    'Orbiters': [40, 60, 30, 10, 50, 25],  # Shuffled data
    'Landers': [10, 20, 5, 20, 45, 10],    # Shuffled data
    'Flybys': [70, 50, 40, 50, 30, 35]     # Shuffled data
}

fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

x_pos = np.arange(len(celestial_bodies))
y_pos = np.arange(len(missions_data))

bar_width = 0.2
bar_depth = 0.4

colors = ['#FF5733', '#33FFCE', '#335BFF']

for idx, (mission_type, percentages) in enumerate(missions_data.items()):
    x_offset = bar_width * idx
    ax.bar3d(x_pos + x_offset, idx, [0] * len(percentages), bar_width, bar_depth, percentages,
             color=colors[idx], alpha=0.7)

ax.set_zlim(0, 100)

plt.show()