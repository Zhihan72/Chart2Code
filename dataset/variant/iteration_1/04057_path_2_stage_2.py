import matplotlib.pyplot as plt
import numpy as np

# Data for the analysis
happiness_score = np.array([5.0, 6.2, 6.5, 6.0, 7.0, 8.2, 7.5, 7.8, 9.0, 8.5, 7.0, 6.8, 8.0, 8.8, 9.2, 5.5])
sleep_hours = np.array([6, 7, 8, 7, 9, 10, 8, 9, 10, 8, 7, 6, 9, 10, 9, 7])
daily_steps = np.array([10, 12, 15, 11, 18, 20, 14, 19, 25, 22, 16, 12, 21, 24, 26, 13])
outdoor_hours = np.array([1, 2, 3, 2, 4, 5, 3, 4, 6, 5, 3, 2, 4, 5, 6, 2])
exercise_duration = np.array([0.5, 1.0, 1.5, 1.0, 2.0, 2.5, 1.5, 2.0, 3.0, 2.5, 1.5, 1.0, 2.0, 2.5, 3.0, 1.0])

# Set up the figure and axes
fig, axs = plt.subplots(1, 4, figsize=(25, 6))
fig.suptitle("Factors Affecting Happiness", fontsize=18, fontweight='bold')

# Scatter plot for Happiness vs. Sleep Hours
axs[0].scatter(sleep_hours, happiness_score, color='purple', s=100, edgecolor='black', alpha=0.7)
axs[0].set_title("Happiness vs. Sleep Hours", fontsize=14)
axs[0].set_xlabel("Sleep Hours", fontsize=12)
axs[0].set_ylabel("Happiness Score", fontsize=12)
axs[0].grid(True, linestyle='--', alpha=0.6)

# Scatter plot for Happiness vs. Daily Steps
axs[1].scatter(daily_steps, happiness_score, color='purple', s=100, edgecolor='black', alpha=0.7)
axs[1].set_title("Happiness vs. Daily Steps", fontsize=14)
axs[1].set_xlabel("Daily Steps (in thousands)", fontsize=12)
axs[1].set_ylabel("Happiness Score", fontsize=12)
axs[1].grid(True, linestyle='--', alpha=0.6)

# Scatter plot for Happiness vs. Outdoor Hours
axs[2].scatter(outdoor_hours, happiness_score, color='purple', s=100, edgecolor='black', alpha=0.7)
axs[2].set_title("Happiness vs. Outdoor Hours", fontsize=14)
axs[2].set_xlabel("Outdoor Hours", fontsize=12)
axs[2].set_ylabel("Happiness Score", fontsize=12)
axs[2].grid(True, linestyle='--', alpha=0.6)

# Scatter plot for Happiness vs. Exercise Duration
axs[3].scatter(exercise_duration, happiness_score, color='purple', s=100, edgecolor='black', alpha=0.7)
axs[3].set_title("Happiness vs. Exercise Duration", fontsize=14)
axs[3].set_xlabel("Exercise Duration (hours)", fontsize=12)
axs[3].set_ylabel("Happiness Score", fontsize=12)
axs[3].grid(True, linestyle='--', alpha=0.6)

# Adjust layout to prevent overlapping
fig.tight_layout(rect=[0, 0, 1, 0.95])

# Show the plot
plt.show()