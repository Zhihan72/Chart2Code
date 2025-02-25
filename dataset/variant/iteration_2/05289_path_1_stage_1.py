import matplotlib.pyplot as plt
import numpy as np

# Weeks of the year for simplicity (12 genres, one per month)
weeks = np.array(range(1, 53))

# Reading engagement data (Books read per week) for different genres (fictional data)
mystery_readings = np.array([
    25, 28, 30, 32, 29, 25, 27, 32, 35, 30, 28, 26, 33, 35, 28, 30, 32, 36, 38, 40, 
    32, 28, 30, 29, 27, 35, 38, 40, 45, 42, 40, 38, 35, 40, 42, 45, 48, 50, 45, 42, 
    40, 38, 35, 30, 32, 34, 36, 38, 35, 30, 28, 25
])
fantasy_readings = np.array([
    18, 20, 22, 25, 23, 22, 24, 26, 29, 27, 25, 23, 20, 22, 25, 27, 28, 26, 24, 22, 
    20, 19, 21, 23, 25, 26, 28, 29, 27, 25, 23, 22, 24, 26, 27, 28, 30, 32, 29, 27, 
    25, 23, 20, 21, 23, 25, 26, 28, 29, 27, 26, 24
])
science_fiction_readings = np.array([
    30, 28, 29, 31, 33, 32, 30, 29, 31, 35, 37, 34, 32, 30, 29, 28, 27, 29, 30, 32, 
    34, 36, 31, 30, 28, 27, 26, 29, 32, 34, 33, 31, 29, 30, 32, 33, 35, 36, 34, 32, 
    30, 29, 28, 30, 32, 31, 30, 28, 27, 25, 26, 24
])

# Total readings per week across all genres
total_readings = mystery_readings + fantasy_readings + science_fiction_readings

# Sorting weeks based on total readings
sorted_indices = np.argsort(total_readings)
sorted_weeks = weeks[sorted_indices]
sorted_readings = total_readings[sorted_indices]

# Plot Data:
fig, ax = plt.subplots(figsize=(14, 8))

# Plot sorted total reading data using a bar chart
ax.bar(sorted_weeks, sorted_readings, color='#1f77b4', label='Total Readings')

# Setting up the title and labels
ax.set_title('Weekly Reading Challenge (Sorted by Total Books Read)', fontsize=16, fontweight='bold')
ax.set_xlabel('Week Number (Sorted)', fontsize=14)
ax.set_ylabel('Total Number of Books Read', fontsize=14)
ax.legend(title='Total Books Read', loc='upper right')

ax.set_xticks(sorted_weeks[::4])
ax.set_xticklabels([f'Week {i}' for i in sorted_weeks[::4]], rotation=45)
ax.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()