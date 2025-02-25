import matplotlib.pyplot as plt
import numpy as np

age_groups = ['Teens', 'Youngsters', 'Young Inhabitants', 'Grown-ups', 'Midlifers', 'Elders']
hobbies = ['Literature', 'Video Games', 'Wanderlust', 'Artistry', 'Floral Design']

data = np.array([
    [15, 25, 30, 5, 10],   # Teens
    [30, 50, 20, 10, 5],   # Youngsters
    [40, 60, 25, 15, 10],  # Young Inhabitants
    [50, 40, 30, 20, 15],  # Grown-ups
    [45, 30, 40, 25, 20],  # Midlifers
    [35, 25, 40, 30, 40]   # Elders
])

fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(18, 9))

total_hobby_counts = data.sum(axis=0)
colors_pie = plt.cm.viridis(np.arange(5)/5.)
axes[0].pie(total_hobby_counts, labels=hobbies, autopct='%1.1f%%', startangle=140, colors=colors_pie,
            wedgeprops=dict(edgecolor=None), textprops=dict(color="white"))

axes[0].set_title('Overall Leisure Trends', fontsize=16, fontweight='bold')

bar_width = 0.35
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0']

for i, hobby in enumerate(hobbies):
    positive_values = [data[j, i] if j < len(data) / 2 else 0 for j in range(len(data))]
    negative_values = [-data[j, i] if j >= len(data) / 2 else 0 for j in range(len(data))]

    axes[1].barh(i, np.sum(positive_values), color=colors[i], left=0, align='center')
    axes[1].barh(i, np.sum(negative_values), color=colors[i], left=0, align='center')

axes[1].set_yticks(np.arange(len(hobbies)))
axes[1].set_yticklabels(hobbies, fontsize=12)
axes[1].set_xlabel('Engagement Percentage', fontsize=13)
axes[1].set_title('Activity Choices by Age (Diverging)', fontsize=16, fontweight='bold')
axes[1].axvline(0, color='black', linewidth=0.8)

plt.tight_layout()
plt.show()