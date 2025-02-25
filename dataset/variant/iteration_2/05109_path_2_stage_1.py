import matplotlib.pyplot as plt
import numpy as np

# Categories of leisure activities
activities = ['Dining Out', 'Movies', 'Shopping', 'Sports', 'Travel']

# Average weekly spending (in dollars) by different age groups on these activities
age_group_18_29 = [60, 40, 80, 30, 50]
age_group_30_49 = [70, 45, 90, 50, 70]
age_group_50_64 = [50, 30, 70, 40, 60]
age_group_65_plus = [35, 20, 50, 20, 40]

data = np.array([age_group_18_29, age_group_30_49, age_group_50_64, age_group_65_plus])
age_groups = ['18-29', '30-49', '50-64', '65+']

bar_width = 0.2
indices = np.arange(len(activities))

fig, ax = plt.subplots(figsize=(12, 8))

# Use a single color for all data groups
single_color = '#4CAF50'

for i, (spending, age_group) in enumerate(zip(data, age_groups)):
    bars = ax.bar(indices + i * bar_width, spending, width=bar_width, label=age_group, color=single_color)
    
    for bar in bars:
        yval = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, yval + 2, f'${yval}', ha='center', va='bottom', fontsize=9)

ax.set_xlabel('Leisure Activities', fontsize=12)
ax.set_ylabel('Average Weekly Spending ($)', fontsize=12)
ax.set_title('Weekly Spending on Leisure Activities by Age Groups\n(Weekends, 2023)', fontsize=16, fontweight='bold', pad=20)
ax.set_xticks(indices + bar_width * 1.5)
ax.set_xticklabels(activities)
ax.legend(title='Age Groups', fontsize='small', loc='upper left')

ax.yaxis.grid(True)

plt.tight_layout()
plt.show()