import matplotlib.pyplot as plt
import numpy as np

age_groups = ['Teens', '20s', '30s', '40s', '50+']
hobbies = ['Read', 'Grdn', 'Game', 'Cook', 'Exr']

data = {
    'Teens':       [20,  8, 30, 15, 10],
    '20s':         [15, 35, 10, 20, 30],
    '30s':         [12, 20, 45, 25, 15],
    '40s':         [25, 12, 50, 30, 20],
    '50+':         [30, 30, 15, 35, 25]
}

fig, ax = plt.subplots(figsize=(14, 8))
indices = np.arange(len(hobbies))
colors = ['#33FFBD', '#FF5733', '#9D33FF', '#FFC300', '#3375FF']

# Initialize a bottom data set to keep track of where the current stack starts
bottom = np.zeros(len(hobbies))

# Plot stacked bar chart
for age_group, color in zip(age_groups, colors):
    ax.bar(indices, data[age_group], width=0.5, label=age_group, color=color, bottom=bottom)
    bottom += np.array(data[age_group])

ax.set_xlabel('Hobbies', fontsize=14)
ax.set_ylabel('Hours', fontsize=14)
ax.set_title('Leisure Time in Sept 2023', fontsize=16, weight='bold')
ax.set_xticks(indices)
ax.set_xticklabels(hobbies, fontsize=12)

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

ax.legend(title='Age Groups')

plt.tight_layout()
plt.show()