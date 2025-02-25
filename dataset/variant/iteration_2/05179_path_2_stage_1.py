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

bar_width = 0.25
x_positions = np.arange(len(months))

bars_fb = ax.bar(x_positions - bar_width, facebook_data, bar_width, color='#3b5998')
bars_tw = ax.bar(x_positions, twitter_data, bar_width, color='#1DA1F2')
bars_ig = ax.bar(x_positions + bar_width, instagram_data, bar_width, color='#C13584')

for rect in bars_fb + bars_tw + bars_ig:
    height = rect.get_height()
    ax.text(rect.get_x() + rect.get_width()/2.0, height, f'{height}', ha='center', va='bottom', fontsize=9)

ax.set_xlabel('Month', fontsize=12)
ax.set_ylabel('Engagement (in thousands)', fontsize=12)
ax.set_xticks(x_positions)
ax.set_xticklabels(months, fontsize=11)

plt.tight_layout()
plt.show()