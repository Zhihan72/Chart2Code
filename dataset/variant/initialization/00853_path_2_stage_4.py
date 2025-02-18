import matplotlib.pyplot as plt
import numpy as np

celestial_bodies = ['Jupiter', 'Mars', 'Mercury', 'Asteroids', 'Saturn', 'Venus']
missions_data = {
    'Orbiters': [10, 30, 40, 25, 50, 60],
    'Landers': [20, 5, 10, 10, 45, 20],
    'Flybys': [50, 40, 70, 35, 30, 50]
}

fig, ax = plt.subplots(figsize=(12, 8))

x_pos = np.arange(len(celestial_bodies))
bar_width = 0.2

# Using a single consistent color across all data groups
single_color = '#FF5733'

# Plotting each mission type with the single color
for idx, (mission_type, percentages) in enumerate(missions_data.items()):
    ax.bar(x_pos + idx * bar_width, percentages, bar_width, label=mission_type,
           color=single_color, alpha=0.7)

ax.set_xticks(x_pos + bar_width)
ax.set_xticklabels(celestial_bodies, rotation=45, ha='right')
ax.set_ylim(0, 100)
ax.legend()

plt.tight_layout()
plt.show()