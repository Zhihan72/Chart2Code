import matplotlib.pyplot as plt
import numpy as np

# Leisure activities
activities = ['Dining Out', 'Movies', 'Shopping', 'Sports', 'Travel']

# Average weekly spending (in dollars) by different age groups on these activities
age_group_18_29 = [60, 40, 80, 30, 50]
age_group_30_49 = [70, 45, 90, 50, 70]
age_group_50_64 = [50, 30, 70, 40, 60]
age_group_65_plus = [35, 20, 50, 20, 40]

data = np.array([age_group_18_29, age_group_30_49, age_group_50_64, age_group_65_plus])
age_groups = ['18-29', '30-49', '50-64', '65+']

# Create a stacked bar chart
fig, ax = plt.subplots(figsize=(12, 8))

colors = ['#4CAF50', '#FF7043', '#4285F4', '#FFEB3B']

# Plotting stacked bars
cumulative_spending = np.zeros(len(activities))

for i, (spending, age_group) in enumerate(zip(data, age_groups)):
    bars = ax.bar(activities, spending, bottom=cumulative_spending, label=age_group, color=colors[i])
    cumulative_spending += spending
    
    # Adding data labels on top of each bar segment
    for bar in bars:
        yval = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_y() + yval/2, f'${yval}', ha='center', va='center', fontsize=9, color='white')

# Configure the chart
ax.set_xlabel('Leisure Activities', fontsize=12)
ax.set_ylabel('Average Weekly Spending ($)', fontsize=12)
ax.set_title('Weekly Spending on Leisure Activities by Age Groups\n(Weekends, 2023)', fontsize=16, fontweight='bold', pad=20)
ax.legend(title='Age Groups', fontsize='small', loc='upper left')

ax.yaxis.grid(True)

plt.tight_layout()

plt.show()