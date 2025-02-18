import matplotlib.pyplot as plt
import numpy as np

# Years from 2023 to 2032
years = np.arange(2023, 2033)

# Projected hours dedication for each activity (arbitrary units)
reading = np.array([100, 110, 120, 130, 140, 150, 160, 170, 180, 190])
learning_new_skills = np.array([200, 210, 220, 230, 240, 250, 260, 270, 280, 290])
relaxation = np.array([120, 130, 140, 150, 160, 170, 180, 190, 200, 210])

# Stack the data for area plotting
activities = np.array([reading, learning_new_skills, relaxation])

# Create the stacked area chart
fig, ax = plt.subplots(figsize=(14, 8))
ax.stackplot(years, activities, labels=['Reading', 'Learning New Skills', 'Relaxation'],
             colors=['#FF6347', '#9ACD32', '#DAA520'], alpha=0.8)

# Title and axis labels
ax.set_title('Projected Dedication Time for Personal Development Activities\n(2023-2032)', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Hours Spent Annually', fontsize=14)

# Add legend
ax.legend(title='Activities', loc='upper left', fontsize=12, bbox_to_anchor=(1.05, 1))

# Configure x and y ticks
ax.set_xticks(np.arange(2023, 2033, 1))
ax.set_yticks(np.arange(0, 1001, 100))
ax.set_xlim(2023, 2032)
ax.set_ylim(0, 1000)

# Add gridlines for better readability
ax.grid(True, linestyle='--', alpha=0.7)

# Add individual activity trends line plot (overlapping)
ax.plot(years, reading, marker='o', linestyle='-', color='#FF6347', label='Reading')
ax.plot(years, learning_new_skills, marker='o', linestyle='-', color='#9ACD32', label='Learning New Skills')
ax.plot(years, relaxation, marker='o', linestyle='-', color='#DAA520', label='Relaxation')

# Enhance layout to avoid overlapping elements
plt.tight_layout()

# Show plot
plt.show()