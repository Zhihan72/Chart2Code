import matplotlib.pyplot as plt
import numpy as np

weeks = np.array(range(1, 53))

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

total_readings = mystery_readings + fantasy_readings + science_fiction_readings

sorted_indices = np.argsort(total_readings)
sorted_weeks = weeks[sorted_indices]
sorted_readings = total_readings[sorted_indices]

fig, ax = plt.subplots(figsize=(14, 8))

colors = ['#e377c2', '#2ca02c', '#1f77b4']  # Shuffled colors
marker_styles = ['o', 's', '^']  # Different marker styles

ax.plot(sorted_weeks, sorted_readings, color=colors[0], marker=marker_styles[0], linestyle='-', linewidth=2, markersize=8, label='Total Readings')

ax.set_title('Weekly Reading Challenge (Sorted by Total Books Read)', fontsize=16, fontweight='bold')
ax.set_xlabel('Week Number (Sorted)', fontsize=14)
ax.set_ylabel('Total Number of Books Read', fontsize=14)
ax.legend(title='Total Books Read', loc='lower right')  # Changed legend location

ax.set_xticks(sorted_weeks[::4])
ax.set_xticklabels([f'Week {i}' for i in sorted_weeks[::4]], rotation=45)
ax.grid(axis='x', linestyle=':', alpha=0.5)  # Different grid style
ax.spines['top'].set_visible(False)  # Adjusted border visibility
ax.spines['right'].set_visible(False)

plt.tight_layout()
plt.show()