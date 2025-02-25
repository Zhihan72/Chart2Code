import matplotlib.pyplot as plt
import numpy as np

# Original data
age_groups = ['Teens (13-19)', 'Young Adults (20-29)', 'Adults (30-39)', 'Middle-aged (40-49)', 'Seniors (50+)']
social_media = [3.2, 2.8, 2.1, 1.5, 0.8]
gaming = [2.4, 1.9, 1.3, 0.8, 0.6]
productivity = [1.2, 1.5, 1.8, 2.3, 1.9]
entertainment = [2.1, 2.4, 2.0, 1.5, 1.2]

# Function to sort data and labels
def sort_data(data, labels):
    return zip(*sorted(zip(labels, data), key=lambda x: x[1], reverse=True))

sorted_age_groups, sorted_social_media = sort_data(social_media, age_groups)
_, sorted_gaming = sort_data(gaming, age_groups)
_, sorted_productivity = sort_data(productivity, age_groups)
_, sorted_entertainment = sort_data(entertainment, age_groups)

fig, ax = plt.subplots(2, 2, figsize=(14, 10))
ax = ax.flatten()

# Create sorted bar charts
ax[0].barh(sorted_age_groups, sorted_social_media, color='royalblue')
ax[1].barh(sorted_age_groups, sorted_gaming, color='tomato')
ax[2].barh(sorted_age_groups, sorted_productivity, color='forestgreen')
ax[3].barh(sorted_age_groups, sorted_entertainment, color='gold')

# Titles for the subplots
titles = ['Social Media', 'Gaming', 'Productivity', 'Entertainment']
for i in range(4):
    ax[i].set_title(titles[i])
    ax[i].invert_yaxis()  # Invert y-axis to have the highest values on top
    ax[i].grid(axis='x', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()