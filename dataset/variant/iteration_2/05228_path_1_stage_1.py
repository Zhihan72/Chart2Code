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

# Plot endurance scores with adjusted marker type
ax1.plot(months, endurance_scores, marker='x', markersize=7, linewidth=1, 
         linestyle='-', color='dodgerblue', label='Endurance')

# Plot strength scores with adjusted line style
ax1.plot(months, strength_scores, marker='s', markersize=6, linewidth=2, 
         linestyle='-', color='tomato', label='Strength')

# Plot flexibility scores with adjusted linewidth
ax1.plot(months, flexibility_scores, marker='D', markersize=6, linewidth=1, 
         linestyle=':', color='forestgreen', label='Flexibility')

# Titles and labels
ax1.set_title("Performance Tracking Comparison Over Six Months", fontsize=18, fontweight='normal', pad=20)
ax1.set_xlabel("Months", fontsize=14, labelpad=15)
ax1.set_ylabel("Scores", fontsize=14, labelpad=15)

# Adjusted legend location and visibility
ax1.legend(title="Test Types", title_fontsize='13', fontsize='12', loc='lower right')

# Adjusted grid style
ax1.grid(True, linestyle='-', linewidth=0.8, alpha=0.5)

# Removed annotations for a cleaner look

# Enhanced ticks configuration
ax1.xaxis.set_ticks(np.arange(len(months)))
ax1.xaxis.set_ticklabels(months, rotation=45, ha='right', fontsize=12)
ax1.yaxis.set_major_locator(plt.MaxNLocator(integer=True))

plt.tight_layout()
plt.show()