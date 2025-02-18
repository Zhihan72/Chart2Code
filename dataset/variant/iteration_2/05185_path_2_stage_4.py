import matplotlib.pyplot as plt
import numpy as np

age_groups = ['Adults', 'Middle-aged', 'Teenagers', 'Young Adults', 'Seniors']
hobbies = ['Gardening', 'Traveling', 'Reading', 'Gaming', 'Painting']

data = np.array([
    [45, 60, 35, 50, 25],   # Adults
    [40, 60, 25, 15, 10],   # Middle-aged
    [35, 45, 25, 15, 10],   # Teenagers
    [30, 50, 20, 10, 5],    # Young Adults
    [35, 25, 40, 30, 40]    # Seniors
])

fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(12, 12))

bar_width = 0.15
indices = np.arange(len(hobbies))
colors = ['#ffcc99', '#c2c2f0', '#ff9999', '#66b3ff', '#99ff99']

for i in range(len(age_groups)):
    axes[0].bar(indices + i * bar_width, data[i], bar_width, label=age_groups[i], color=colors[i])

axes[0].set_title('Diverse Leisure Activities Across Age Demographics', fontsize=16, fontweight='bold')
axes[0].set_xlabel('Leisure Activities', fontsize=13)
axes[0].set_ylabel('Percentage of Participants', fontsize=13)
axes[0].set_xticks(indices + bar_width * (len(age_groups) / 2 - 0.5))
axes[0].set_xticklabels(hobbies, fontsize=12)
axes[0].legend(title='Demographic Groups', fontsize=11)
axes[0].grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

total_hobby_counts = data.sum(axis=0)
colors_pie = plt.cm.viridis(np.arange(5)/5.)
axes[1].pie(total_hobby_counts, labels=hobbies, autopct='%1.1f%%', startangle=140, colors=colors_pie,
            wedgeprops=dict(edgecolor='black'), textprops=dict(color="white"))

axes[1].set_title('Aggregate Leisure Activity Trends', fontsize=16, fontweight='bold')

plt.tight_layout()
plt.show()