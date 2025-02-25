import matplotlib.pyplot as plt
import numpy as np

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

engagement_data = {
    'Facebook': [35, 28, 23, 25, 30, 35, 40, 38, 37, 32, 30, 28],
    'Twitter': [20, 18, 15, 17, 19, 22, 25, 28, 26, 24, 22, 20],
    'Instagram': [40, 35, 33, 39, 42, 45, 50, 48, 47, 45, 40, 38]
}

facebook_data = np.array(engagement_data['Facebook'])
twitter_data = np.array(engagement_data['Twitter'])
instagram_data = np.array(engagement_data['Instagram'])

fig, ax = plt.subplots(figsize=(14, 8))

bar_height = 0.25
y_positions = np.arange(len(months))

# Updated color scheme
ax.barh(y_positions - bar_height, facebook_data, bar_height, color='#FF5733', label='Facebook')  # Changed color
ax.barh(y_positions, twitter_data, bar_height, color='#33FF57', label='Twitter')  # Changed color
ax.barh(y_positions + bar_height, instagram_data, bar_height, color='#3357FF', label='Instagram')  # Changed color

ax.set_yticks(y_positions)
ax.set_yticklabels(months, fontsize=11)
ax.invert_yaxis()
ax.set_xlabel('Engagement')

plt.tight_layout()
plt.show()