import matplotlib.pyplot as plt
import numpy as np

# Define the athletes and tests
athletes = ['Alice', 'Bob', 'Charlie', 'Diana', 'Edward']
tests = ['Endurance', 'Strength', 'Flexibility']

# Create data for the tests over six months (values are the average scores in respective tests)
endurance_scores = [50, 60, 55, 70, 65, 80]
strength_scores = [40, 50, 60, 55, 65, 75]
flexibility_scores = [30, 40, 50, 45, 55, 65]

# Month labels
months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'])

# Assign dates for training logs (x-axis)
x = np.arange(len(months))

# Create figure and subplots
fig, ax1 = plt.subplots(figsize=(14, 8))

# Plot endurance scores with new label
ax1.plot(months, endurance_scores, marker='o', markersize=6, linewidth=2, 
         linestyle='-', color='dodgerblue', label='Stamina')

# Plot strength scores with new label
ax1.plot(months, strength_scores, marker='s', markersize=6, linewidth=2, 
         linestyle='--', color='tomato', label='Power')

# Plot flexibility scores with new label
ax1.plot(months, flexibility_scores, marker='D', markersize=6, linewidth=2, 
         linestyle='-.', color='forestgreen', label='Agility')

# Title and labels
ax1.set_title("Six-Month Fitness Journey", fontsize=18, fontweight='bold', pad=20)
ax1.set_xlabel("Training Months", fontsize=14, labelpad=15)
ax1.set_ylabel("Scores on Average", fontsize=14, labelpad=15)

# Adding legend
ax1.legend(title="Test Areas", title_fontsize='13', fontsize='12', loc='upper left')

# Adding grid for readability
ax1.grid(True, linestyle='--', linewidth=0.5, alpha=0.75)

# Adding annotations for maximum scores
max_endurance = max(endurance_scores)
max_idx = endurance_scores.index(max_endurance)
ax1.annotate(f'Max: {max_endurance}', xy=(x[max_idx], max_endurance), xytext=(x[max_idx], max_endurance+10),
             arrowprops=dict(facecolor='black', shrink=0.05), fontsize=12, color='dodgerblue')

max_strength = max(strength_scores)
max_idx = strength_scores.index(max_strength)
ax1.annotate(f'Max: {max_strength}', xy=(x[max_idx], max_strength), xytext=(x[max_idx], max_strength+10),
             arrowprops=dict(facecolor='black', shrink=0.05), fontsize=12, color='tomato')

max_flexibility = max(flexibility_scores)
max_idx = flexibility_scores.index(max_flexibility)
ax1.annotate(f'Max: {max_flexibility}', xy=(x[max_idx], max_flexibility), xytext=(x[max_idx], max_flexibility+10),
             arrowprops=dict(facecolor='black', shrink=0.05), fontsize=12, color='forestgreen')

# Enhancing ticks and grid configuration
ax1.xaxis.set_ticks(np.arange(len(months)))
ax1.xaxis.set_ticklabels(months, rotation=45, ha='right', fontsize=12)
ax1.yaxis.set_major_locator(plt.MaxNLocator(integer=True))

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()