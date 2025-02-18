import matplotlib.pyplot as plt
import numpy as np

# Original team data is modified according to the task description
team_data = {
    'Alpha Squad': [8, 7, 6, 9, 5, 7],    # Swapped a couple of values
    'Bravo Brigade': [8, 7, 6, 8, 6, 7],  # Reordered the values
    'Charlie Crew': [7, 9, 6, 7, 8, 6],   # Altered placement
    'Delta Division': [7, 8, 9, 6, 6, 7]  # Repositioned to create variation
}

num_vars = 6
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]

fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Pre-defined set of colors to replace the original ones
colors = ['#FF6347', '#4682B4', '#32CD32', '#FFD700']

for idx, values in enumerate(team_data.values()):
    values += values[:1]
    ax.fill(angles, values, color=colors[idx], alpha=0.25)

ax.set_ylim(0, 10)
ax.set_xticks([])

plt.tight_layout()
plt.show()