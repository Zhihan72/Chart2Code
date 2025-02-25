import matplotlib.pyplot as plt
import numpy as np

# Altered activity names
activities = ['Social Surfing', 'Digital Play', 'Online Courses', 'Binge Watching', 'E-book Surf', 'Virtual Meet']
average_hours_lockdown = np.array([15, 10, 25, 30, 5, 20])
average_hours_prelockdown = np.array([5, 8, 10, 15, 3, 6])

fig, ax = plt.subplots(figsize=(12, 7))

bar_height = 0.35
index = np.arange(len(activities))

# Use the same color for both data groups
bar1 = ax.barh(index, average_hours_lockdown, bar_height, label='Lockdown Era', color='teal', edgecolor='gray')
bar2 = ax.barh(index + bar_height, average_hours_prelockdown, bar_height, label='Pre-lockdown', color='teal', edgecolor='gray')

# Randomly altered textual elements
ax.set_title('Average Weekly Screen Use by Middle Schoolers\nDuring the Pandemic Times', fontsize=15, fontweight='bold')
ax.set_xlabel('Hours per Week', fontsize=12)
ax.set_ylabel('Forms of Activity', fontsize=12)
ax.set_yticks(index + bar_height / 2)
ax.set_yticklabels(activities, fontsize=10, rotation=0, va='center')
ax.legend(fontsize=10)

for bar_group in [bar1, bar2]:
    for bar in bar_group:
        width = bar.get_width()
        ax.text(width + 0.5, bar.get_y() + bar.get_height() / 2, f'{width}', va='center', ha='left', fontsize=10)

ax.grid(axis='x', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()