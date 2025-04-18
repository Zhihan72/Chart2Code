import matplotlib.pyplot as plt
import numpy as np

study_hours = np.array([2, 4, 6, 8, 10, 12, 14, 16, 18, 20])
reading_hours = np.array([1, 1.5, 2, 2.5, 3, 3.5, 3, 2.5, 2, 1.5])
exercises_hours = np.array([0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5])

# Sort indices based on reading_hours
sorted_indices = np.argsort(reading_hours)

# Sorted data
sorted_study_hours = study_hours[sorted_indices]
sorted_reading_hours = reading_hours[sorted_indices]
sorted_exercises_hours = exercises_hours[sorted_indices]

fig, ax1 = plt.subplots(figsize=(12, 7))

bar_width = 0.35
bar_positions = np.arange(len(sorted_study_hours))

ax1.bar(bar_positions, sorted_reading_hours, bar_width, color='teal', alpha=0.6, label='Reading Hours')
ax1.bar(bar_positions + bar_width, sorted_exercises_hours, bar_width, color='darkcyan', alpha=0.6, label='Exercises Hours')

ax1.set_xticks(bar_positions + bar_width / 2)
ax1.set_xticklabels(sorted_study_hours)

ax1.set_xlabel("Study Hours")
ax1.set_ylabel("Hours")
ax1.legend()
ax1.grid(True, linestyle='--', alpha=0.6)
fig.tight_layout()

plt.show()