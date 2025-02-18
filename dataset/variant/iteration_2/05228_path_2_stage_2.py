import matplotlib.pyplot as plt
import numpy as np

athletes = ['Alice', 'Bob', 'Charlie', 'Diana', 'Edward']
tests = ['Endurance', 'Strength', 'Flexibility']

endurance_scores = [50, 60, 55, 70, 65, 80]
strength_scores = [40, 50, 60, 55, 65, 75]
flexibility_scores = [30, 40, 50, 45, 55, 65]

months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'])
x = np.arange(len(months))

fig, ax1 = plt.subplots(figsize=(14, 8))

# Randomly altering markers, line styles, and colors
ax1.plot(months, endurance_scores, marker='x', markersize=8, linewidth=2.5, 
         linestyle='-', color='purple', label='Stamina')

ax1.plot(months, strength_scores, marker='^', markersize=8, linewidth=2.5, 
         linestyle=':', color='teal', label='Power')

ax1.plot(months, flexibility_scores, marker='v', markersize=8, linewidth=2.5, 
         linestyle='--', color='orange', label='Agility')

# Title and labels
ax1.set_title("Six-Month Fitness Journey", fontsize=18, fontweight='bold', pad=20)
ax1.set_xlabel("Training Months", fontsize=14, labelpad=15)
ax1.set_ylabel("Scores on Average", fontsize=14, labelpad=15)

# Randomly repositioned legend
ax1.legend(title="Test Areas", title_fontsize='13', fontsize='12', loc='lower right')

# Modified grid with different style
ax1.grid(True, linestyle=':', linewidth=1, alpha=0.3)

# Annotations for maximum scores
max_endurance = max(endurance_scores)
max_idx = endurance_scores.index(max_endurance)
ax1.annotate(f'Max: {max_endurance}', xy=(x[max_idx], max_endurance), xytext=(x[max_idx], max_endurance+10),
             arrowprops=dict(facecolor='black', shrink=0.05), fontsize=12, color='purple')

max_strength = max(strength_scores)
max_idx = strength_scores.index(max_strength)
ax1.annotate(f'Max: {max_strength}', xy=(x[max_idx], max_strength), xytext=(x[max_idx], max_strength+10),
             arrowprops=dict(facecolor='black', shrink=0.05), fontsize=12, color='teal')

max_flexibility = max(flexibility_scores)
max_idx = flexibility_scores.index(max_flexibility)
ax1.annotate(f'Max: {max_flexibility}', xy=(x[max_idx], max_flexibility), xytext=(x[max_idx], max_flexibility+10),
             arrowprops=dict(facecolor='black', shrink=0.05), fontsize=12, color='orange')

# Adjusting layout
plt.tight_layout()

plt.show()