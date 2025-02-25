import matplotlib.pyplot as plt
import numpy as np

age_groups = ['Teenagers', 'Young Adults', 'Adults', 'Middle-aged', 'Seniors']
hobbies = ['Reading', 'Gaming', 'Traveling', 'Painting', 'Gardening']

data = np.array([
    [35, 45, 25, 15, 10],   # Teenagers
    [30, 50, 20, 10, 5],    # Young Adults
    [45, 30, 40, 25, 20],   # Adults
    [40, 60, 25, 15, 10],   # Middle-aged
    [35, 25, 40, 30, 40]    # Seniors
])

fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(12, 12))

bar_width = 0.15
indices = np.arange(len(hobbies))
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0']

for i in range(len(age_groups)):
    axes[0].bar(indices + i * bar_width, data[i], bar_width, label=age_groups[i], color=colors[i])

axes[0].set_title('Hobby Preferences Among Different Age Groups', fontsize=16, fontweight='bold')
axes[0].set_xlabel('Hobbies', fontsize=13)
axes[0].set_ylabel('Percentage of People Involved', fontsize=13)
axes[0].set_xticks(indices + bar_width * (len(age_groups) / 2 - 0.5))
axes[0].set_xticklabels(hobbies, fontsize=12)
axes[0].legend(title='Age Groups', fontsize=11)
axes[0].grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

# Calculate total hobby counts
total_hobby_counts = data.sum(axis=0)
# Set colors for the pie chart using a colormap
colors_pie = plt.cm.viridis(np.arange(5)/5.)
# Create a pie chart in the second subplot
axes[1].pie(total_hobby_counts, labels=hobbies, autopct='%1.1f%%', startangle=140, colors=colors_pie,
            wedgeprops=dict(edgecolor='black'), textprops=dict(color="white"))

axes[1].set_title('Overall Hobby Preferences', fontsize=16, fontweight='bold')

plt.tight_layout()
plt.show()