import matplotlib.pyplot as plt
import numpy as np

players = ['Thunderfoot', 'Speedy', 'Wall', 'Sniper', 'Maestro']
skills = ['Dribbling', 'Shooting', 'Passing', 'Stamina', 'Defense']

# Shuffling the content of each player's performance data while maintaining structure
performance_data_shuffled = [
    [9, 6, 7, 6, 5],  # Thunderfoot (shuffled)
    [6, 5, 9, 5, 8],  # Speedy (shuffled)
    [6, 9, 7, 7, 5],  # Wall (shuffled)
    [7, 6, 5, 10, 5], # Sniper (shuffled)
    [8, 9, 6, 7, 6]   # Maestro (shuffled)
]

performance_data = [np.array(player + [player[0]]) for player in performance_data_shuffled]
num_vars = len(skills)

angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]

fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

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