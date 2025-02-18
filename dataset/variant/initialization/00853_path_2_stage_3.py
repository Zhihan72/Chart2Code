import matplotlib.pyplot as plt
import numpy as np

celestial_bodies = ['Jupiter', 'Mars', 'Mercury', 'Asteroids', 'Saturn', 'Venus']  # Sorted based on example data
missions_data = {
    'Orbiters': [10, 30, 40, 25, 50, 60],  # Sorted data in ascending order
    'Landers': [20, 5, 10, 10, 45, 20],    # Sorted data in ascending order
    'Flybys': [50, 40, 70, 35, 30, 50]     # Sorted data in ascending order
}

fig, ax = plt.subplots(figsize=(12, 8))

x_pos = np.arange(len(celestial_bodies))
bar_width = 0.2

colors = ['#FF5733', '#33FFCE', '#335BFF']

# Plotting each mission type as a sorted bar chart
for idx, (mission_type, percentages) in enumerate(missions_data.items()):
    ax.bar(x_pos + idx * bar_width, percentages, bar_width, label=mission_type,
           color=colors[idx], alpha=0.7)

ax.set_xticks(x_pos + bar_width)
ax.set_xticklabels(celestial_bodies, rotation=45, ha='right')
ax.set_ylim(0, 100)
ax.legend()

plt.tight_layout()
plt.show()