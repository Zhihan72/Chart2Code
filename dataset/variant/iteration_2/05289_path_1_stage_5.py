import matplotlib.pyplot as plt
import numpy as np

weeks = np.array(range(1, 53))

mystery_readings = np.array([
    25, 28, 30, 32, 29, 25, 27, 32, 35, 30, 28, 26, 33, 35, 28, 30, 32, 36, 38, 40, 
    32, 28, 30, 29, 27, 35, 38, 40, 45, 42, 40, 38, 35, 40, 42, 45, 48, 50, 45, 42, 
    40, 38, 35, 30, 32, 34, 36, 38, 35, 30, 28, 25
])

# Removed fantasy_readings from the calculation
# Removed science_fiction_readings entirely

total_readings = mystery_readings  # Only using mystery_readings

sorted_indices = np.argsort(total_readings)
sorted_weeks = weeks[sorted_indices]
sorted_readings = total_readings[sorted_indices]

fig, ax = plt.subplots(figsize=(14, 8))

colors = ['#e377c2']
marker_styles = ['o']

ax.plot(sorted_weeks, sorted_readings, color=colors[0], marker=marker_styles[0], linestyle='-', linewidth=2, markersize=8, label='Mystery Readings')

ax.set_title('Reading Trend by Week', fontsize=16, fontweight='bold')
ax.set_xlabel('Week', fontsize=14)
ax.set_ylabel('Books', fontsize=14)
ax.legend(title='Legend', loc='lower right')

ax.set_xticks(sorted_weeks[::4])
ax.set_xticklabels([f'Wk {i}' for i in sorted_weeks[::4]], rotation=45)
ax.grid(axis='x', linestyle=':', alpha=0.5)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()
plt.show()