import matplotlib.pyplot as plt
import numpy as np

# Leisure activities
activities = ['Dining Out', 'Movies', 'Shopping', 'Sports', 'Travel']

# Average weekly spending by different age groups
age_group_18_29 = [60, 40, 80, 30, 50]
age_group_30_49 = [70, 45, 90, 50, 70]
age_group_50_64 = [50, 30, 70, 40, 60]
age_group_65_plus = [35, 20, 50, 20, 40]

data = np.array([age_group_18_29, age_group_30_49, age_group_50_64, age_group_65_plus])
age_groups = ['18-29', '30-49', '50-64', '65+']

fig, ax = plt.subplots(figsize=(12, 8))

colors = ['#4CAF50', '#FF7043', '#4285F4', '#FFEB3B']

# Plotting stacked bars
cumulative_spending = np.zeros(len(activities))

# Altered the chart to utilize different line styles between segments
hatch_patterns = ['/', '\\', '|', '-']

for i, (spending, age_group) in enumerate(zip(data, age_groups)):
    bars = ax.bar(activities, spending, bottom=cumulative_spending, label=age_group, color=colors[i], hatch=hatch_patterns[i])
    cumulative_spending += spending

    # Added data labels on top of each bar segment with different marker styles
    for bar in bars:
        yval = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_y() + yval/2, f'${yval}', ha='center', va='center', fontsize=9, color='white', weight='bold')

# Configuring the chart's stylistic elements
ax.set_xlabel('Leisure Activities', fontsize=12, style='italic')
ax.set_ylabel('Avg Weekly Spending ($)', fontsize=12, fontweight='light')
ax.set_title('Weekly Spending on Leisure Activities by Age Groups\n(Weekends, 2023)', fontsize=16, fontweight='regular', pad=20)

# Altered legend style and position
ax.legend(title='Age Brackets', fontsize='medium', loc='lower right', frameon=False)

# Introduced different grid styles
ax.yaxis.grid(True, linestyle='--', color='gray')

# Changed line width for borders
ax.spines['top'].set_visible(False)
ax.spines['right'].set_color('orange')
ax.spines['left'].set_linewidth(0.5)

plt.tight_layout()

plt.show()