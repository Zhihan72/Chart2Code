import matplotlib.pyplot as plt
import numpy as np

matches = np.array(['Match 1', 'Match 2', 'Match 3'])
player_a_runs = np.array([50, 75, 65])
player_b_runs = np.array([60, 80, 70])
player_c_runs = np.array([45, 55, 60])
background_score = [20, 20, 20]

fig, ax = plt.subplots(figsize=(10, 6))

consistent_color = 'mediumblue'

ax.scatter(matches, player_a_runs, color=consistent_color, s=100, edgecolor='black')
ax.scatter(matches, player_b_runs, color=consistent_color, s=100, edgecolor='black')
ax.scatter(matches, player_c_runs, color=consistent_color, s=100, edgecolor='black')
ax.plot(matches, background_score, linestyle='--', color='grey', linewidth=2)

avg_runs = np.mean([player_a_runs, player_b_runs, player_c_runs], axis=0)
ax.scatter(matches, avg_runs, color=consistent_color, s=200, edgecolor='brown', alpha=0.5)

ax.set_xticks(matches)
ax.set_xticklabels(matches, rotation=45)

ax.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()