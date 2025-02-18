import matplotlib.pyplot as plt
import numpy as np

# Data for age groups
children = [9, 9, 10, 11, 10, 9, 10, 11, 12, 9, 10, 11, 8, 9, 10, 11, 10, 9, 10]
teenagers = [7, 8, 9, 7, 8, 7, 8, 9, 7, 8, 9, 7, 8, 9, 8, 8, 7, 9]
young_adults = [6, 6, 7, 6, 7, 6, 6, 7, 7, 6, 7, 6, 6, 7]
adults = [5, 6, 5, 6, 5, 6, 5, 6, 5, 6, 5, 6, 6, 5, 6, 5]
seniors = [6, 6, 7, 6, 6, 7, 6, 7, 6, 6, 7, 6, 7, 6, 6]

data = [children, teenagers, young_adults, adults, seniors]
age_groups = ['Kids', 'Teens', 'Y.Adults', 'Adults', 'Seniors']

fig, ax = plt.subplots(figsize=(10, 7))

violin = ax.violinplot(data, showmeans=False, showmedians=True)

colors = ['#9575cd', '#add8e6', '#fdd835', '#c3e6cb', '#ffcccb']
for patch, color in zip(violin['bodies'], colors):
    patch.set_facecolor(color)
    patch.set_edgecolor('black')
    patch.set_alpha(0.7)

plt.ylabel('Groups', fontsize=12)
plt.xlabel('Sleep (hrs)', fontsize=12)
plt.yticks(range(1, len(age_groups) + 1), age_groups, fontsize=10)

for i, group in enumerate(data):
    mean_val = np.mean(group)
    plt.text(mean_val + 0.1, i + 1, f'M: {mean_val:.1f}h', verticalalignment='center', fontsize=9, color='darkblue')

plt.tight_layout()

plt.show()