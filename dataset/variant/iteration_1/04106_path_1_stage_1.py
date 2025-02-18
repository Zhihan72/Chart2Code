import matplotlib.pyplot as plt
import numpy as np

age_groups = ['Teens', '20s', '30s', '40s', '50+']
hobbies = ['Reading', 'Gardening', 'Gaming', 'Cooking', 'Exercising']

data = {
    'Teens':       [12,  8, 50, 10, 15],
    '20s':         [15, 12, 45, 20, 20],
    '30s':         [20, 20, 30, 25, 30],
    '40s':         [25, 30, 15, 30, 25],
    '50+':         [30, 35, 10, 35, 20]
}

fig, ax = plt.subplots(figsize=(14, 8))
bar_width = 0.15
indices = np.arange(len(hobbies))

# Previously: ['#FF5733', '#33FFBD', '#3375FF', '#9D33FF', '#FFC300']
colors = ['#33FFBD', '#FF5733', '#9D33FF', '#FFC300', '#3375FF']

for i, (age_group, color) in enumerate(zip(age_groups, colors)):
    offset = i * bar_width
    ax.bar(indices + offset, data[age_group], width=bar_width, label=age_group, color=color)

ax.set_xlabel('Hobbies', fontsize=14)
ax.set_ylabel('Time Spent (hours)', fontsize=14)
ax.set_title('Leisure Time Distribution:\nHow Different Age Groups Spend Their Hours in September 2023', fontsize=16, weight='bold')
ax.set_xticks(indices + bar_width*2)
ax.set_xticklabels(hobbies, fontsize=12)
ax.legend(title='Age Groups', loc='upper right')

for i, (age_group, color) in enumerate(zip(age_groups, colors)):
    for j, value in enumerate(data[age_group]):
        ax.text(j + i * bar_width, value + 0.5, str(value),
                ha='center', va='bottom', fontsize=10, color=color, fontweight='bold')

ax.yaxis.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()