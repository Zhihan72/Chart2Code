import numpy as np
import matplotlib.pyplot as plt

languages_spoken = np.array([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 7, 8, 9, 10])
satisfaction_level = np.array([4, 5, 5, 6, 6, 7, 7, 7, 8, 8, 9, 9, 9, 9, 10])

unique_languages = np.unique(languages_spoken)
avg_satisfaction = [satisfaction_level[languages_spoken == lang].mean() for lang in unique_languages]

fig, ax = plt.subplots(figsize=(8, 6))

# Randomly changed bar color, marker, and linestyle
colors = ['gold', 'mediumpurple', 'mediumseagreen', 'tomato', 'cornflowerblue']
markers = ['^', 's', 'o', 'D', '*']
linestyles = ['-', ':', '-.', '--', '-']

# Shuffling assuming this order is 'random'
color_choice = colors[1]
marker_choice = markers[2]
linestyle_choice = linestyles[3]

ax.barh(unique_languages, avg_satisfaction, color=color_choice, alpha=0.8, edgecolor='k')  # Changed color
ax.plot(avg_satisfaction, unique_languages, linestyle=linestyle_choice, marker=marker_choice, color='black')  # Added line plot

ax.set_yticks(np.arange(1, 11, 1))
ax.set_xticks(np.arange(1, 11, 1))

# Randomly choosing to disable grid for a stylistic change
# ax.grid(True, linestyle='--', alpha=0.7)  # it's commented out for a random change

# Adding a legend with altered style
ax.legend(['Bar Representation'], loc='lower right', fontsize=10, shadow=True)

ax.set_xlabel('Average Satisfaction Level', fontsize=12, fontweight='bold')
ax.set_ylabel('Languages Spoken', fontsize=12, fontweight='bold')

# Add a border with a random style
for spine in ax.spines.values():
    spine.set_edgecolor('green')
    spine.set_linestyle(':')  # Dashed border

plt.tight_layout()
plt.show()