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

ax.barh(y_positions - bar_height, facebook_data, bar_height, color='#3b5998', label='Facebook')
ax.barh(y_positions, twitter_data, bar_height, color='#1DA1F2', label='Twitter')
ax.barh(y_positions + bar_height, instagram_data, bar_height, color='#C13584', label='Instagram')

ax.set_yticks(y_positions)
ax.set_yticklabels(months, fontsize=11)
ax.invert_yaxis()  # Optional: invert to maintain Jan at the top, Dec at the bottom
ax.set_xlabel('Engagement')

plt.tight_layout()
plt.show()