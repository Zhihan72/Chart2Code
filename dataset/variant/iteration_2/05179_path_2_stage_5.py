import matplotlib.pyplot as plt
import numpy as np

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

engagement_data = {
    'Facebook': [32, 35, 30, 37, 38, 40, 28, 23, 25, 30, 28, 35],  # Randomly altered
    'Twitter': [22, 25, 18, 20, 24, 19, 28, 17, 22, 20, 26, 15],  # Randomly altered
    'Instagram': [47, 50, 40, 35, 42, 39, 38, 33, 45, 40, 48, 45]  # Randomly altered
}

facebook_data = np.array(engagement_data['Facebook'])
twitter_data = np.array(engagement_data['Twitter'])
instagram_data = np.array(engagement_data['Instagram'])

fig, ax = plt.subplots(figsize=(14, 8))

bar_height = 0.25
y_positions = np.arange(len(months))

ax.barh(y_positions - bar_height, facebook_data, bar_height, color='#FF5733', label='Facebook')
ax.barh(y_positions, twitter_data, bar_height, color='#33FF57', label='Twitter')
ax.barh(y_positions + bar_height, instagram_data, bar_height, color='#3357FF', label='Instagram')

ax.set_yticks(y_positions)
ax.set_yticklabels(months, fontsize=11)
ax.invert_yaxis()
ax.set_xlabel('Engagement')

plt.tight_layout()
plt.show()