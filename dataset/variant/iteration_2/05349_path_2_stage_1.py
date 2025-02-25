import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2023, 2033)
reading = np.array([100, 110, 120, 130, 140, 150, 160, 170, 180, 190])
exercise = np.array([150, 160, 170, 180, 190, 200, 210, 220, 230, 240])
learning_new_skills = np.array([200, 210, 220, 230, 240, 250, 260, 270, 280, 290])
relaxation = np.array([120, 130, 140, 150, 160, 170, 180, 190, 200, 210])

activities = np.array([reading, exercise, learning_new_skills, relaxation])

fig, ax = plt.subplots(figsize=(14, 8))
uniform_color = '#4682B4'  # Using a single consistent color

ax.stackplot(years, activities, labels=['Reading', 'Exercise', 'Learning New Skills', 'Relaxation'],
             colors=[uniform_color, uniform_color, uniform_color, uniform_color], alpha=0.8)

ax.set_title('Projected Dedication Time for Personal Development Activities\n(2023-2032)', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Hours Spent Annually', fontsize=14)

ax.legend(title='Activities', loc='upper left', fontsize=12, bbox_to_anchor=(1.05, 1))

ax.set_xticks(np.arange(2023, 2033, 1))
ax.set_yticks(np.arange(0, 1001, 100))
ax.set_xlim(2023, 2032)
ax.set_ylim(0, 1000)

ax.grid(True, linestyle='--', alpha=0.7)

ax.plot(years, reading, marker='o', linestyle='-', color=uniform_color, label='Reading')
ax.plot(years, exercise, marker='o', linestyle='-', color=uniform_color, label='Exercise')
ax.plot(years, learning_new_skills, marker='o', linestyle='-', color=uniform_color, label='Learning New Skills')
ax.plot(years, relaxation, marker='o', linestyle='-', color=uniform_color, label='Relaxation')

plt.tight_layout()
plt.show()