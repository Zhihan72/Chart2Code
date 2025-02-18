import matplotlib.pyplot as plt
import numpy as np

age_groups = ['Teens', '20s', '30s', '40s', '50+']
hobbies = ['Read', 'Grdn', 'Game', 'Cook', 'Exr']

# Manually shuffled some data values among age groups
data = {
    'Teens':       [20,  8, 30, 15, 10],  # values shuffled
    '20s':         [15, 35, 10, 20, 30],  # values shuffled
    '30s':         [12, 20, 45, 25, 15],  # values shuffled
    '40s':         [25, 12, 50, 30, 20],  # values shuffled
    '50+':         [30, 30, 15, 35, 25]   # values shuffled
}

fig, ax = plt.subplots(figsize=(14, 8))
bar_width = 0.15
indices = np.arange(len(hobbies))

colors = ['#33FFBD', '#FF5733', '#9D33FF', '#FFC300', '#3375FF']

for i, (age_group, color) in enumerate(zip(age_groups, colors)):
    offset = i * bar_width
    ax.bar(indices + offset, data[age_group], width=bar_width, color=color)

ax.set_xlabel('Hobbies', fontsize=14)
ax.set_ylabel('Hours', fontsize=14)
ax.set_title('Leisure Time in Sept 2023', fontsize=16, weight='bold')
ax.set_xticks(indices + bar_width * 2)
ax.set_xticklabels(hobbies, fontsize=12)

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

for i, (age_group, color) in enumerate(zip(age_groups, colors)):
    for j, value in enumerate(data[age_group]):
        ax.text(j + i * bar_width, value + 0.5, str(value),
                ha='center', va='bottom', fontsize=10, color=color, fontweight='bold')

plt.tight_layout()
plt.show()