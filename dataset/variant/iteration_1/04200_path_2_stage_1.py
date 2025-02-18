import matplotlib.pyplot as plt
import numpy as np

# Data: Runs scored by three players in different matches
matches = np.array(['Match 1', 'Match 2', 'Match 3'])
player_a_runs = np.array([50, 75, 65])
player_b_runs = np.array([60, 80, 70])
player_c_runs = np.array([45, 55, 60])
match_types = ['Day', 'Night', 'Day-Night']
background_score = [20, 20, 20]

fig, ax = plt.subplots(figsize=(10, 6))

# Apply consistent color across all groups: using a medium blue
consistent_color = 'mediumblue'

# Scatter plots for players
scatter_a = ax.scatter(matches, player_a_runs, color=consistent_color, label='Player A', s=100, edgecolor='black')
scatter_b = ax.scatter(matches, player_b_runs, color=consistent_color, label='Player B', s=100, edgecolor='black')
scatter_c = ax.scatter(matches, player_c_runs, color=consistent_color, label='Player C', s=100, edgecolor='black')

# Plotting the base performance line
ax.plot(matches, background_score, linestyle='--', color='grey', label='Base Performance', linewidth=2)

# Annotating points
for i, txt in enumerate(match_types):
    ax.annotate(txt, (matches[i], player_a_runs[i]), textcoords="offset points", xytext=(0, 10), ha='center', fontsize=9, color=consistent_color)
    ax.annotate(txt, (matches[i], player_b_runs[i]), textcoords="offset points", xytext=(0, 10), ha='center', fontsize=9, color=consistent_color)
    ax.annotate(txt, (matches[i], player_c_runs[i]), textcoords="offset points", xytext=(0, 10), ha='center', fontsize=9, color=consistent_color)

# Average runs with consistent color for visibility
avg_runs = np.mean([player_a_runs, player_b_runs, player_c_runs], axis=0)
scatter_avg = ax.scatter(matches, avg_runs, color=consistent_color, label='Average Runs', s=200, edgecolor='brown', alpha=0.5)

ax.set_title("Cricket Match Performance Analysis\nPlayer runs across different match types", fontsize=14, fontweight='bold')
ax.set_xlabel('Matches', fontsize=12)
ax.set_ylabel('Runs Scored', fontsize=12)
ax.set_xticks(matches)
ax.set_xticklabels(matches, rotation=45)

ax.legend(loc='upper left', fontsize=10)
ax.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()