import matplotlib.pyplot as plt
import numpy as np

# Data for the analysis
happiness_score = np.array([5.0, 6.2, 6.5, 6.0, 7.0, 8.2, 7.5, 7.8, 9.0, 8.5, 7.0, 6.8, 8.0, 8.8, 9.2, 5.5])
sleep_hours = np.array([6, 7, 8, 7, 9, 10, 8, 9, 10, 8, 7, 6, 9, 10, 9, 7])
daily_steps = np.array([10, 12, 15, 11, 18, 20, 14, 19, 25, 22, 16, 12, 21, 24, 26, 13])
outdoor_hours = np.array([1, 2, 3, 2, 4, 5, 3, 4, 6, 5, 3, 2, 4, 5, 6, 2])
exercise_duration = np.array([0.5, 1.0, 1.5, 1.0, 2.0, 2.5, 1.5, 2.0, 3.0, 2.5, 1.5, 1.0, 2.0, 2.5, 3.0, 1.0])

# Change to 2x2 subplot grid
fig, axs = plt.subplots(2, 2, figsize=(14, 12))
fig.suptitle("Exploring Happiness Influences", fontsize=18, fontweight='bold')

# Scatter plot for Happiness vs. Sleep Hours
axs[0, 0].scatter(sleep_hours, happiness_score, color='purple', s=100, edgecolor='black', alpha=0.7)
axs[0, 0].set_title("Factors of Joy: Sleep Analysis", fontsize=14)
axs[0, 0].set_xlabel("Rest Periods (Hours)", fontsize=12)
axs[0, 0].set_ylabel("Well-being Metric", fontsize=12)
axs[0, 0].grid(True, linestyle='--', alpha=0.6)

# Scatter plot for Happiness vs. Daily Steps
axs[0, 1].scatter(daily_steps, happiness_score, color='purple', s=100, edgecolor='black', alpha=0.7)
axs[0, 1].set_title("Joy vs. Step Count", fontsize=14)
axs[0, 1].set_xlabel("Walking Thousands", fontsize=12)
axs[0, 1].set_ylabel("Positive Indicator", fontsize=12)
axs[0, 1].grid(True, linestyle='--', alpha=0.6)

# Scatter plot for Happiness vs. Outdoor Hours
axs[1, 0].scatter(outdoor_hours, happiness_score, color='purple', s=100, edgecolor='black', alpha=0.7)
axs[1, 0].set_title("Contentment vs. Outdoor Time", fontsize=14)
axs[1, 0].set_xlabel("Outside Duration", fontsize=12)
axs[1, 0].set_ylabel("Bliss Measure", fontsize=12)
axs[1, 0].grid(True, linestyle='--', alpha=0.6)

# Scatter plot for Happiness vs. Exercise Duration
axs[1, 1].scatter(exercise_duration, happiness_score, color='purple', s=100, edgecolor='black', alpha=0.7)
axs[1, 1].set_title("Activity Time vs. Enjoyment", fontsize=14)
axs[1, 1].set_xlabel("Fitness Hours", fontsize=12)
axs[1, 1].set_ylabel("Satisfaction Level", fontsize=12)
axs[1, 1].grid(True, linestyle='--', alpha=0.6)

fig.tight_layout(rect=[0, 0, 1, 0.95])
plt.show()