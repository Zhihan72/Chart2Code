import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

study_hours = np.array([2, 4, 6, 8, 10, 12, 14, 16, 18, 20])
exam_scores = np.array([55, 60, 65, 68, 72, 78, 80, 84, 88, 93])
reading_hours = np.array([1, 1.5, 2, 2.5, 3, 3.5, 3, 2.5, 2, 1.5])
exercises_hours = np.array([0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5])

# Define the shuffled list of colors for different data groups
color_options = ['lightcoral', 'skyblue', 'lightgreen', 'darkblue']
shuffled_colors = ['skyblue', 'darkblue', 'lightcoral', 'lightgreen']

fig, ax1 = plt.subplots(figsize=(12, 7))

# Color assignment changes based on shuffled_colors
ax1.scatter(study_hours, exam_scores, color=shuffled_colors[0], edgecolor='black', s=100, alpha=0.7)
X_Y_Spline = make_interp_spline(study_hours, exam_scores, k=3)
X_ = np.linspace(study_hours.min(), study_hours.max(), 500)
Y_ = X_Y_Spline(X_)
ax1.plot(X_, Y_, color=shuffled_colors[1], linewidth=2.5)

ax1.set_xlabel('Weekly Study Hours', fontsize=12)
ax1.set_ylabel('Mathematics Exam Score', fontsize=12, color=shuffled_colors[0])
ax1.set_xlim(0, 22)
ax1.set_ylim(50, 100)
ax1.set_title('Study Habits Analysis\nImpact of Study Hours and Methods on Exam Performance', fontsize=14, fontweight='bold')

ax2 = ax1.twinx()
bar_width = 0.35
bar_positions = study_hours - bar_width/2
ax2.bar(bar_positions, reading_hours, bar_width, color=shuffled_colors[2], alpha=0.6)
ax2.bar(bar_positions + bar_width, exercises_hours, bar_width, color=shuffled_colors[3], alpha=0.6)

ax2.set_ylabel('Average Weekly Activity Hours', fontsize=12, color=shuffled_colors[3])
ax2.set_ylim(0, 6)

plt.show()