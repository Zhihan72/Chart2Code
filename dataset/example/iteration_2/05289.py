import matplotlib.pyplot as plt
import numpy as np

# Backstory:
# In a small town, a local library runs weekly reading challenges with different genres each month.
# We analyze the data on how well different genres performed over weekly reading challenges in 2022.

# Data Construction:
# Weeks of the year for simplicity (12 genres, one per month)
weeks = np.array(range(1, 53))

# Reading engagement data (Books read per week) for different genres (fictional data)
mystery_readings = np.array([25, 28, 30, 32, 29, 25, 27, 32, 35, 30, 28, 26, 33, 35, 28, 30, 32, 36, 38, 40, 32, 28, 30, 29, 27, 35, 38, 40, 45, 42, 40, 38, 35, 40, 42, 45, 48, 50, 45, 42, 40, 38, 35, 30, 32, 34, 36, 38, 35, 30, 28, 25])
fantasy_readings = np.array([18, 20, 22, 25, 23, 22, 24, 26, 29, 27, 25, 23, 20, 22, 25, 27, 28, 26, 24, 22, 20, 19, 21, 23, 25, 26, 28, 29, 27, 25, 23, 22, 24, 26, 27, 28, 30, 32, 29, 27, 25, 23, 20, 21, 23, 25, 26, 28, 29, 27, 26, 24])
science_fiction_readings = np.array([30, 28, 29, 31, 33, 32, 30, 29, 31, 35, 37, 34, 32, 30, 29, 28, 27, 29, 30, 32, 34, 36, 31, 30, 28, 27, 26, 29, 32, 34, 33, 31, 29, 30, 32, 33, 35, 36, 34, 32, 30, 29, 28, 30, 32, 31, 30, 28, 27, 25, 26, 24])

# Plot Data:
fig, ax = plt.subplots(figsize=(14, 8))

# Plot weekly reading data for different genres using bar charts
ax.bar(weeks - 0.3, mystery_readings, width=0.3, label='Mystery', color='#1f77b4')
ax.bar(weeks, fantasy_readings, width=0.3, label='Fantasy', color='#ff7f0e')
ax.bar(weeks + 0.3, science_fiction_readings, width=0.3, label='Science Fiction', color='#2ca02c')

# Setting up the title and labels
ax.set_title('Weekly Reading Challenge Participation in 2022', fontsize=16, fontweight='bold')
ax.set_xlabel('Week of the Year', fontsize=14)
ax.set_ylabel('Number of Books Read', fontsize=14)
ax.legend(title='Genres', loc='upper right')

# Applying custom ticks
ax.set_xticks(weeks[::4])
ax.set_xticklabels([f'Week {i}' for i in weeks[::4]], rotation=45)
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Automatically adjust layout for better visibility
plt.tight_layout()

# Display the chart
plt.show()