import matplotlib.pyplot as plt
import numpy as np

# Activity names including a new activity
activities = ['Social Surfing', 'Digital Play', 'Online Courses', 'Binge Watching', 'E-book Surf', 'Virtual Meet']

# Expanded data to include the hybrid period
average_hours_lockdown = np.array([15, 10, 25, 30, 5, 20])
average_hours_prelockdown = np.array([5, 8, 10, 15, 3, 6])
average_hours_hybrid = np.array([10, 9, 20, 22, 4, 15])  # New made-up data for hybrid era

fig, ax = plt.subplots(figsize=(12, 9))

# Adjust bar height and indices for three groups
bar_height = 0.25
index = np.arange(len(activities))

# Plot the bars
bar1 = ax.barh(index, average_hours_lockdown, bar_height, label='Lockdown Era', color='teal', edgecolor='gray')
bar2 = ax.barh(index + bar_height, average_hours_prelockdown, bar_height, label='Pre-lockdown', color='cornflowerblue', edgecolor='gray')
bar3 = ax.barh(index + 2 * bar_height, average_hours_hybrid, bar_height, label='Hybrid Era', color='lightgreen', edgecolor='gray')

# Set chart elements
ax.set_title('Average Weekly Screen Use by Middle Schoolers\nDuring Various Periods', fontsize=15, fontweight='bold')
ax.set_xlabel('Hours per Week', fontsize=12)
ax.set_ylabel('Forms of Activity', fontsize=12)
ax.set_yticks(index + bar_height)
ax.set_yticklabels(activities, fontsize=10, rotation=0, va='center')
ax.legend(fontsize=10)

# Annotating bars with values
for bar_group in [bar1, bar2, bar3]:
    for bar in bar_group:
        width = bar.get_width()
        ax.text(width + 0.5, bar.get_y() + bar.get_height() / 2, f'{width}', va='center', ha='left', fontsize=10)

ax.grid(axis='x', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()