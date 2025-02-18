import matplotlib.pyplot as plt
import numpy as np

age_groups = ['Teens (13-19)', 'Young Adults (20-29)', 'Adults (30-39)', 'Middle-aged (40-49)', 'Seniors (50+)']
social_media = [3.2, 2.8, 2.1, 1.5, 0.8]
gaming = [2.4, 1.9, 1.3, 0.8, 0.6]
productivity = [1.2, 1.5, 1.8, 2.3, 1.9]
entertainment = [2.1, 2.4, 2.0, 1.5, 1.2]

def sort_data(data, labels):
    return zip(*sorted(zip(labels, data), key=lambda x: x[1], reverse=True))

sorted_age_groups, sorted_social_media = sort_data(social_media, age_groups)
_, sorted_gaming = sort_data(gaming, age_groups)
_, sorted_productivity = sort_data(productivity, age_groups)
_, sorted_entertainment = sort_data(entertainment, age_groups)

fig, ax = plt.subplots(2, 2, figsize=(14, 10))
ax = ax.flatten()

ax[0].barh(sorted_age_groups, sorted_social_media, color='cornflowerblue', linestyle='solid')
ax[1].barh(sorted_age_groups, sorted_gaming, color='crimson', linestyle='dotted')
ax[2].barh(sorted_age_groups, sorted_productivity, color='seagreen', linestyle='dashed')
ax[3].barh(sorted_age_groups, sorted_entertainment, color='goldenrod', linestyle='dashdot')

titles = ['Social Media Usage', 'Gaming Time', 'Productivity Tasks', 'Entertainment Hours']
for i, axis in enumerate(ax):
    axis.set_title(titles[i], fontsize=12)
    axis.invert_yaxis()
    axis.grid(axis='x', linestyle=':', linewidth=0.5, alpha=0.9)
    axis.spines['top'].set_visible(False)
    axis.spines['right'].set_visible(False)

ax[0].legend(['Social Media'])
ax[1].legend(['Gaming'])
ax[2].legend(['Productivity'])
ax[3].legend(['Entertainment'])

plt.tight_layout()
plt.show()