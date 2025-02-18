import matplotlib.pyplot as plt
import numpy as np

study_hours = np.array([2, 4, 6, 8, 10, 12, 14, 16, 18, 20])
reading_hours = np.array([1, 1.5, 2, 2.5, 3, 3.5, 3, 2.5, 2, 1.5])
exercises_hours = np.array([0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5])

# Shuffled list of colors for different data groups
shuffled_colors = ['skyblue', 'lightcoral', 'darkblue', 'lightgreen']

fig, ax1 = plt.subplots(figsize=(12, 7))

# Horizontal bars for reading_hours and exercises_hours
bar_height = 0.35
bar_positions = study_hours - bar_height/2
ax1.barh(bar_positions, reading_hours, bar_height, color=shuffled_colors[1], alpha=0.6, label='Reading')
ax1.barh(bar_positions + bar_height, exercises_hours, bar_height, color=shuffled_colors[3], alpha=0.6, label='Exercises')

ax1.set_xlabel('Average Weekly Activity Hours', fontsize=12, color=shuffled_colors[3])
ax1.set_ylabel('Weekly Study Hours', fontsize=12)
ax1.set_xlim(0, 6)
ax1.set_ylim(0, 22)
ax1.set_title('Study Habits Analysis\nImpact of Study Hours and Methods', fontsize=14, fontweight='bold')

ax1.legend()

plt.show()