import matplotlib.pyplot as plt
import numpy as np

players = ['Thunderfoot', 'Speedy', 'Wall', 'Sniper', 'Maestro']
skills = ['Dribbling', 'Shooting', 'Passing', 'Stamina', 'Defense']

performance_data = [
    [6, 9, 7, 6, 5],  # Thunderfoot
    [9, 5, 6, 8, 5],  # Speedy
    [5, 6, 7, 7, 9],  # Wall
    [7, 10, 5, 5, 6], # Sniper
    [8, 7, 9, 6, 6]   # Maestro
]

performance_data = [np.array(player + [player[0]]) for player in performance_data]
num_vars = len(skills)

angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]

fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Use a single consistent color across all data groups
consistent_color = 'blue'
for player_data in performance_data:
    ax.plot(angles, player_data, linewidth=2, color=consistent_color, linestyle='-', marker='o')
    ax.fill(angles, player_data, color=consistent_color, alpha=0.25)

ax.set_yticklabels([])
ax.set_xticks(angles[:-1])
ax.set_xticklabels(skills, fontsize=12, color='navy')

plt.title("Performance Metrics of Star Players\nin Fantasy Football", size=15, color='darkred', y=1.08)
ax.legend(players, loc='upper right', bbox_to_anchor=(1.2, 1.2), fontsize=10)

ax.grid(color='grey', linestyle='--', linewidth=0.5)
plt.tight_layout()

plt.show()