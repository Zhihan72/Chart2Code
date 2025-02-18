import matplotlib.pyplot as plt
import numpy as np

team_data = {
    'Alpha Squad': [7, 8, 6, 9, 5, 7],
    'Bravo Brigade': [6, 7, 8, 6, 7, 8],
    'Charlie Crew': [9, 6, 7, 8, 6, 7],
    'Delta Division': [8, 7, 6, 7, 9, 6]
}

num_vars = 6
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]

fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Define a new set of colors to replace the original ones
colors = ['#FF6347', '#4682B4', '#32CD32', '#FFD700'] 

for idx, values in enumerate(team_data.values()):
    values += values[:1]
    ax.fill(angles, values, color=colors[idx], alpha=0.25)

ax.set_ylim(0, 10)
ax.set_xticks([])

plt.tight_layout()
plt.show()