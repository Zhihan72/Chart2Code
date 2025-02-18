import matplotlib.pyplot as plt
import numpy as np

activities = ['Dining Out', 'Movies', 'Shopping', 'Sports', 'Travel']

age_group_18_29 = [60, 40, 80, 30, 50]
age_group_30_49 = [70, 45, 90, 50, 70]
age_group_50_64 = [50, 30, 70, 40, 60]
age_group_65_plus = [35, 20, 50, 20, 40]

data = np.array([age_group_18_29, age_group_30_49, age_group_50_64, age_group_65_plus])
age_groups = ['18-29', '30-49', '50-64', '65+']

fig, ax = plt.subplots(figsize=(12, 8))

# New set of colors
colors = ['#3498db', '#e74c3c', '#9b59b6', '#f1c40f']

cumulative_spending = np.zeros(len(activities))
hatch_patterns = ['/', '\\', '|', '-']

for i, (spending, age_group) in enumerate(zip(data, age_groups)):
    bars = ax.bar(activities, spending, bottom=cumulative_spending, label=age_group, color=colors[i], hatch=hatch_patterns[i])
    cumulative_spending += spending

    for bar in bars:
        yval = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_y() + yval/2, f'${yval}', ha='center', va='center', fontsize=9, color='white', weight='bold')

ax.set_xlabel('Leisure Activities', fontsize=12, style='italic')
ax.set_ylabel('Avg Weekly Spending ($)', fontsize=12, fontweight='light')
ax.set_title('Weekly Spending on Leisure Activities by Age Groups\n(Weekends, 2023)', fontsize=16, fontweight='regular', pad=20)

ax.legend(title='Age Brackets', fontsize='medium', loc='lower right', frameon=False)
ax.yaxis.grid(True, linestyle='--', color='gray')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_color('orange')
ax.spines['left'].set_linewidth(0.5)

plt.tight_layout()
plt.show()