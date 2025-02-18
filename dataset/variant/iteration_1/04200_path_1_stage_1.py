import matplotlib.pyplot as plt
import numpy as np

# Data: Altered runs scored by three players in different matches
match_conditions = ['Day Match', 'Night Match', 'Day-Night Match']
player_a_scores = [65, 50, 75]
player_b_scores = [70, 60, 80]
player_c_scores = [60, 55, 45]

# Create an artificial dataset for scatter plot with altered scores
matches = np.array(['Match 1', 'Match 2', 'Match 3'])
player_a_runs = np.array([65, 50, 75])
player_b_runs = np.array([70, 60, 80])
player_c_runs = np.array([60, 55, 45])
match_types = ['Day', 'Night', 'Day-Night']

# Auxiliary data for visual effects
background_score = [20, 20, 20]

# Plot configuration
fig, ax = plt.subplots(figsize=(10, 6))

# Scatter plots for individual players with altered scores
scatter_a = ax.scatter(matches, player_a_runs, color='b', label='Player A', s=100, edgecolor='black')
scatter_b = ax.scatter(matches, player_b_runs, color='g', label='Player B', s=100, edgecolor='black')
scatter_c = ax.scatter(matches, player_c_runs, color='r', label='Player C', s=100, edgecolor='black')

# Plot line to show a base performance level
ax.plot(matches, background_score, linestyle='--', color='grey', label='Base Performance', linewidth=2)

# Annotate points with match type
for i, txt in enumerate(match_types):
    ax.annotate(txt, (matches[i], player_a_runs[i]), textcoords="offset points", xytext=(0, 10), ha='center', fontsize=9, color='blue')
    ax.annotate(txt, (matches[i], player_b_runs[i]), textcoords="offset points", xytext=(0, 10), ha='center', fontsize=9, color='green')
    ax.annotate(txt, (matches[i], player_c_runs[i]), textcoords="offset points", xytext=(0, 10), ha='center', fontsize=9, color='red')

# Add large circles for average runs with recalculated averages
avg_runs = np.mean([player_a_runs, player_b_runs, player_c_runs], axis=0)
scatter_avg = ax.scatter(matches, avg_runs, color='orange', label='Average Runs', s=200, edgecolor='brown', alpha=0.5)

# Enhancing the plot with titles and labels
ax.set_title("Cricket Match Performance Analysis\nPlayer runs across different match types", fontsize=14, fontweight='bold')
ax.set_xlabel('Matches', fontsize=12)
ax.set_ylabel('Runs Scored', fontsize=12)
ax.set_xticks(matches)
ax.set_xticklabels(matches, rotation=45)

# Adding a legend to distinguish between players
ax.legend(loc='upper left', fontsize=10)

# Add a grid for better readability
ax.grid(True, linestyle='--', alpha=0.6)

# Automatically adjust layout
plt.tight_layout()

# Display the plot
plt.show()