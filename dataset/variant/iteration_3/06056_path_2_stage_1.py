import matplotlib.pyplot as plt
import numpy as np

# The goal is to investigate the distribution of sleep duration (in hours) across various age groups.

# Randomly altered data within each group
children = [10, 9, 9, 11, 9, 11, 10, 10, 12, 9, 10, 8, 11, 10, 9, 11, 9, 10, 10]
teenagers = [8, 9, 7, 8, 7, 8, 9, 7, 8, 7, 8, 9, 7, 9, 8, 8, 7, 9]
young_adults = [7, 6, 6, 7, 6, 7, 6, 7, 6, 6, 6, 7, 7, 6]
adults = [6, 5, 6, 5, 6, 5, 5, 6, 6, 5, 5, 6, 5, 6, 6, 5]
seniors = [7, 6, 6, 6, 6, 7, 6, 6, 7, 6, 6, 7, 6, 6, 7]

data = [children, teenagers, young_adults, adults, seniors]
age_groups = ['Children (6-12)', 'Teenagers (13-19)', 'Young Adults (20-35)', 'Adults (36-55)', 'Seniors (56+)']

fig, ax = plt.subplots(figsize=(10, 7))
violin = ax.violinplot(data, showmeans=False, showmedians=True)

colors = ['#add8e6', '#ffcccb', '#c3e6cb', '#fdd835', '#9575cd']
for patch, color in zip(violin['bodies'], colors):
    patch.set_facecolor(color)
    patch.set_edgecolor('black')
    patch.set_alpha(0.7)

plt.title('Analysis of Sleep Patterns Across Different Age Groups', fontsize=16, fontweight='bold')
plt.ylabel('Age Groups', fontsize=12)
plt.xlabel('Sleep Duration (hours)', fontsize=12)
plt.yticks(range(1, len(age_groups) + 1), age_groups, fontsize=10)

for i, group in enumerate(data):
    mean_val = np.mean(group)
    plt.text(mean_val + 0.1, i + 1, f'Mean: {mean_val:.1f}h', verticalalignment='center', fontsize=9, color='darkblue')

ax.scatter([], [], color='red', label='Median')
plt.legend(loc='upper right', fontsize=10)
plt.grid(visible=True, axis='x', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()