import matplotlib.pyplot as plt
import numpy as np

children = [10, 9, 9, 11, 9, 11, 10, 10, 12, 9, 10, 8, 11, 10, 9, 11, 9, 10, 10]
teenagers = [8, 9, 7, 8, 7, 8, 9, 7, 8, 7, 8, 9, 7, 9, 8, 8, 7, 9]
young_adults = [7, 6, 6, 7, 6, 7, 6, 7, 6, 6, 6, 7, 7, 6]
adults = [6, 5, 6, 5, 6, 5, 5, 6, 6, 5, 5, 6, 5, 6, 6, 5]
seniors = [7, 6, 6, 6, 6, 7, 6, 6, 7, 6, 6, 7, 6, 6, 7]

data = [children, teenagers, young_adults, adults, seniors]
age_groups = ['Kids', 'Teens', 'Young A.', 'Adults', 'Seniors']

fig, ax = plt.subplots(figsize=(10, 7))
violin = ax.violinplot(data, vert=False, showmeans=True, showmedians=False)

colors = ['#c3e6cb', '#ffcccb', '#add8e6', '#fdd835', '#9575cd']
for patch, color in zip(violin['bodies'], colors):
    patch.set_facecolor(color)
    patch.set_edgecolor('blue')
    patch.set_alpha(0.6)

plt.title('Sleep by Age', fontsize=16, fontweight='bold')
plt.xlabel('Groups', fontsize=12)
plt.ylabel('Sleep (hrs)', fontsize=12)
plt.xticks(range(1, len(age_groups) + 1), age_groups, fontsize=10)

ax.scatter([], [], color='green', marker='^', label='Mean')
plt.legend(loc='upper left', fontsize=10)
plt.grid(visible=True, axis='x', linestyle='-.', alpha=0.7)
plt.tight_layout()
plt.show()