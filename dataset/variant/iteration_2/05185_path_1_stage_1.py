import matplotlib.pyplot as plt
import numpy as np

# Define Age Groups and Hobbies
age_groups = ['Youngsters', 'Young Inhabitants', 'Grown-ups', 'Midlifers', 'Elders']
hobbies = ['Literature', 'Video Games', 'Wanderlust', 'Artistry', 'Floral Design']

# Data representing the percentage of each age group involved in each hobby
data = np.array([
    [30, 50, 20, 10, 5],   # Youngsters
    [40, 60, 25, 15, 10],  # Young Inhabitants
    [50, 40, 30, 20, 15],  # Grown-ups
    [45, 30, 40, 25, 20],  # Midlifers
    [35, 25, 40, 30, 40]   # Elders
])

# Create subplots
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(18, 9))

bar_width = 0.15
indices = np.arange(len(hobbies))

colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0']

for i in range(len(age_groups)):
    axes[0].bar(indices + i * bar_width, data[i], bar_width, label=age_groups[i], color=colors[i])

axes[0].set_title('Activity Choices by Age', fontsize=16, fontweight='bold')
axes[0].set_xlabel('Leisure Activities', fontsize=13)
axes[0].set_ylabel('Engagement Percentage', fontsize=13)
axes[0].set_xticks(indices + bar_width * (len(age_groups) / 2 - 0.5))
axes[0].set_xticklabels(hobbies, fontsize=12)
axes[0].legend(title='Demographics', fontsize=11)
axes[0].grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

total_hobby_counts = data.sum(axis=0)
colors_pie = plt.cm.viridis(np.arange(5)/5.)
axes[1].pie(total_hobby_counts, labels=hobbies, autopct='%1.1f%%', startangle=140, colors=colors_pie,
            wedgeprops=dict(edgecolor='black'), textprops=dict(color="white"))

axes[1].set_title('Overall Leisure Trends', fontsize=16, fontweight='bold')

plt.tight_layout()

plt.show()