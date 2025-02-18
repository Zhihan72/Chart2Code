import matplotlib.pyplot as plt
import numpy as np

players = ['Thunderfoot', 'Speedy', 'Wall', 'Sniper', 'Maestro']
skills = ['Dribbling', 'Shooting', 'Passing', 'Stamina', 'Defense']

performance_data = [
    [6, 9, 7, 6, 5], 
    [9, 5, 6, 8, 5], 
    [5, 6, 7, 7, 9], 
    [7, 10, 5, 5, 6],
    [8, 7, 9, 6, 6]   
]

performance_data = [player + [player[0]] for player in performance_data]

num_vars = len(skills)
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]

fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

marker_styles = ['o', 's', 'D', '^', '*']
line_styles = ['-', '--', '-.', ':', '-']

for i, player_data in enumerate(performance_data):
    ax.plot(angles, player_data, marker=marker_styles[i % len(marker_styles)], linestyle=line_styles[i % len(line_styles)], label=players[i], alpha=0.6)

ax.set_xticks(angles[:-1])
ax.set_xticklabels(skills)

ax.grid(color='black', linestyle='-.', linewidth=0.3)

ax.legend(loc='upper right', bbox_to_anchor=(1.1, 1.1))

plt.tight_layout()
plt.show()