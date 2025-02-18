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

# Add the first skill score to the end to close the radar chart
performance_data = [player + [player[0]] for player in performance_data]

num_vars = len(skills)
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]

fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

for player_data in performance_data:
    ax.fill(angles, player_data, alpha=0.25)  # Fill the area for radar chart

ax.set_yticklabels([])
ax.set_xticks(angles[:-1])
ax.set_xticklabels(['' for _ in skills])  # Empty labels for cleaner look

ax.grid(color='grey', linestyle='--', linewidth=0.5)

plt.tight_layout()
plt.show()