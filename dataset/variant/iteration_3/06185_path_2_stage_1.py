import matplotlib.pyplot as plt
import numpy as np

# Day numbers (1 through 30)
days = np.arange(1, 31)

# Fictional Data
exercise_intensity = np.array([
    3, 4, 5, 6, 7, 6, 5, 6, 7, 8, 7, 6, 5, 7, 8, 7, 6, 5, 6, 7, 6, 5, 6, 7, 
    8, 7, 6, 5, 4, 3
])

heart_rate_recovery = np.array([
    20, 18, 19, 17, 16, 17, 18, 17, 16, 15, 16, 17, 18, 16, 15, 16, 17, 18, 
    17, 16, 17, 18, 17, 16, 15, 16, 17, 18, 19, 20
])

# Plotting setup
fig, ax = plt.subplots(figsize=(14, 7))

# Shuffle colors: Changed 'green' to 'red' and 'blue' to 'orange'
ax.plot(days, exercise_intensity, color='red', marker='o', linewidth=2, markersize=8, label='Exercise Intensity')

ax2 = ax.twinx()
ax2.plot(days, heart_rate_recovery, color='orange', marker='x', linestyle='--', linewidth=2, markersize=8, label='Heart Rate Recovery')

# Titles and Labels
ax.set_title('30-Day Fitness Challenge: Exercise Intensity vs. Heart Rate Recovery', fontsize=18, fontweight='bold')
ax.set_xlabel('Days', fontsize=14)
ax.set_ylabel('Exercise Intensity (arbitrary units)', fontsize=14, color='red')
ax2.set_ylabel('Heart Rate Recovery (decrease from peak, arbitrary units)', fontsize=14, color='orange')

# Grid for clarity
ax.grid(visible=True, linestyle='--', linewidth=0.5, alpha=0.7)

# Legends
lines1, labels1 = ax.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()

ax.legend(lines1 + lines2, labels1 + labels2, loc='upper left', fontsize=12)

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()