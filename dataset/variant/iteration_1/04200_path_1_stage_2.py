import matplotlib.pyplot as plt
import numpy as np

matches = np.array(['Match 1', 'Match 2', 'Match 3'])
player_a_runs = np.array([65, 50, 75])
player_b_runs = np.array([70, 60, 80])
player_c_runs = np.array([60, 55, 45])
background_score = [20, 20, 20]
match_types = ['Day', 'Night', 'Day-Night']
avg_runs = np.mean([player_a_runs, player_b_runs, player_c_runs], axis=0)

fig, ax = plt.subplots(figsize=(10, 6))

scatter_a = ax.scatter(matches, player_a_runs, color='cyan', label='Player A', s=80, marker='o', edgecolor='black')
scatter_b = ax.scatter(matches, player_b_runs, color='lime', label='Player B', s=80, marker='^', edgecolor='purple')
scatter_c = ax.scatter(matches, player_c_runs, color='magenta', label='Player C', s=80, marker='s', edgecolor='gray')

ax.plot(matches, background_score, linestyle='-', color='brown', label='Base Performance', linewidth=2.5)

for i, txt in enumerate(match_types):
    ax.annotate(txt, (matches[i], player_a_runs[i]), textcoords="offset points", xytext=(0, 10), ha='center', fontsize=9, color='cyan')
    ax.annotate(txt, (matches[i], player_b_runs[i]), textcoords="offset points", xytext=(0, 10), ha='center', fontsize=9, color='lime')
    ax.annotate(txt, (matches[i], player_c_runs[i]), textcoords="offset points", xytext=(0, 10), ha='center', fontsize=9, color='magenta')

scatter_avg = ax.scatter(matches, avg_runs, color='gold', label='Average Runs', s=200, edgecolor='black', alpha=0.5)

ax.set_title("Cricket Match Performance Analysis\nPlayer runs across different match types", fontsize=14, fontweight='bold')
ax.set_xlabel('Matches', fontsize=12)
ax.set_ylabel('Runs Scored', fontsize=12)
ax.set_xticks(matches)
ax.set_xticklabels(matches, rotation=30)

ax.legend(loc='lower right', fontsize=10)
ax.grid(False)

plt.tight_layout()
plt.show()