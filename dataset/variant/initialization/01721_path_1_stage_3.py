import matplotlib.pyplot as plt
import numpy as np

players = ['Thunderfoot', 'Speedy', 'Wall', 'Sniper', 'Maestro']
skills = ['Dribbling', 'Shooting', 'Passing', 'Stamina', 'Defense']

performance_data_shuffled = [
    [9, 6, 7, 6, 5],  # Thunderfoot
    [6, 5, 9, 5, 8],  # Speedy
    [6, 9, 7, 7, 5],  # Wall
    [7, 6, 5, 10, 5], # Sniper
    [8, 9, 6, 7, 6]   # Maestro
]

performance_data = [np.array(player + [player[0]]) for player in performance_data_shuffled]
num_vars = len(skills)

angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]

fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

styles = ['-', '--', '-.', ':']
markers = ['o', 's', 'D', '^', 'v']
colors = ['blue', 'green', 'red', 'purple', 'orange']

for index, player_data in enumerate(performance_data):
    linestyle = styles[index % len(styles)]
    marker = markers[index % len(markers)]
    color = colors[index % len(colors)]
    ax.plot(angles, player_data, linewidth=2, color=color, linestyle=linestyle, marker=marker)
    ax.fill(angles, player_data, color=color, alpha=0.25)

ax.set_ylim(0, 10)
ax.set_yticks(range(1, 10))
ax.yaxis.grid(True, color='gray', linestyle='--', linewidth=0.3)
ax.xaxis.grid(True, color='black', linestyle='-.', linewidth=0.5)

ax.set_xticks(angles[:-1])
ax.set_xticklabels(skills, fontsize=12, color='navy')

plt.title("Performance Metrics of Star Players\nin Fantasy Football", size=15, color='darkred', y=1.08)
ax.legend(players, loc='upper left', fontsize=9)

plt.tight_layout()
plt.show()