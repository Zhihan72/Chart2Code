import matplotlib.pyplot as plt
import numpy as np

activities = ['Shopping', 'Sports', 'Dining Out', 'Travel', 'Movies']

age_group_18_29 = [60, 40, 80, 30, 50]
age_group_30_49 = [70, 45, 90, 50, 70]
age_group_50_64 = [50, 30, 70, 40, 60]

data = np.array([age_group_18_29, age_group_30_49, age_group_50_64])
age_groups = ['18-29', '30-49', '50-64']

bar_width = 0.5  # Adjusted for clarity in diverging chart
indices = np.arange(len(activities))

fig, ax = plt.subplots(figsize=(12, 8))

colors = ['#FF9999', '#66B3FF', '#99FF99']

for i, (spending, age_group, color) in enumerate(zip(data, age_groups, colors)):
    offset = (-1)**i * data[i] / 2  # Calculate offset to diverge from center
    ax.barh(indices, spending, left=offset, height=bar_width, label=age_group, color=color)

ax.set_yticks(indices)
ax.set_yticklabels(activities, fontsize=12)
ax.set_xlabel('Average Spending Per Week ($)', fontsize=12)
ax.set_title('Diverging Bar Chart of Expense on Fun Activities by Age Brackets\n(Year 2023)', fontsize=16, fontweight='bold', pad=20)
ax.legend(title='Ages', fontsize='small', loc='lower right')

ax.xaxis.grid(True)

plt.tight_layout()
plt.show()