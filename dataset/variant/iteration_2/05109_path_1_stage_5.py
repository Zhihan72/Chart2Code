import matplotlib.pyplot as plt
import numpy as np

activities = ['Dining Out', 'Movies', 'Shopping', 'Sports', 'Travel']

# Manually shuffled data within each age group
age_group_18_29 = [80, 30, 50, 60, 40]  # Original: [60, 40, 80, 30, 50]
age_group_30_49 = [45, 70, 50, 90, 70]  # Original: [70, 45, 90, 50, 70]
age_group_50_64 = [70, 60, 30, 50, 40]  # Original: [50, 30, 70, 40, 60]
age_group_65_plus = [20, 50, 40, 35, 20]  # Original: [35, 20, 50, 20, 40]

data = np.array([age_group_18_29, age_group_30_49, age_group_50_64, age_group_65_plus])
age_groups = ['18-29', '30-49', '50-64', '65+']

fig, ax = plt.subplots(figsize=(12, 8))

colors = ['#3498db', '#e74c3c', '#9b59b6', '#f1c40f']

cumulative_spending = np.zeros(len(activities))
hatch_patterns = ['/', '\\', '|', '-']

for i, (spending, age_group) in enumerate(zip(data, age_groups)):
    bars = ax.bar(activities, spending, bottom=cumulative_spending, color=colors[i], hatch=hatch_patterns[i])
    cumulative_spending += spending

ax.yaxis.grid(True, linestyle='--', color='gray')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_color('orange')
ax.spines['left'].set_linewidth(0.5)

plt.tight_layout()
plt.show()