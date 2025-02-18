import matplotlib.pyplot as plt
import numpy as np

study_hours = np.array([2, 4, 6, 8, 10, 12, 14, 16, 18, 20])
reading_hours = np.array([1, 1.5, 2, 2.5, 3, 3.5, 3, 2.5, 2, 1.5])
exercises_hours = np.array([0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5])

# Rearrange arrays to remove the dependency on random functionality
shuffled_reading_hours = reading_hours[[3, 0, 6, 9, 4, 1, 8, 7, 2, 5]]
shuffled_exercises_hours = exercises_hours[[5, 8, 2, 0, 6, 7, 4, 1, 9, 3]]

fig, ax1 = plt.subplots(figsize=(12, 7))

bar_width = 0.35
bar_positions = np.arange(len(study_hours))

ax1.bar(bar_positions, shuffled_reading_hours, bar_width, color='teal', alpha=0.6)
ax1.bar(bar_positions + bar_width, shuffled_exercises_hours, bar_width, color='darkcyan', alpha=0.6)

ax1.set_xticks(bar_positions + bar_width / 2)
ax1.set_xticklabels(study_hours)

ax1.set_xlabel("Study Hours")
ax1.set_ylabel("Hours")

fig.tight_layout()

plt.show()