import matplotlib.pyplot as plt
import numpy as np

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'Sept', 'October', 'November', 'December']
engagement_data = {
    'Bookface': [38, 30, 25, 32, 28, 37, 40, 23, 35, 30, 35, 28],  # Manually shuffled
    'Twister': [22, 20, 26, 20, 25, 28, 24, 17, 19, 15, 18, 22],  # Manually shuffled
    'Gramsta': [38, 45, 47, 40, 33, 42, 48, 39, 45, 35, 50, 40]  # Manually shuffled
}

facebook_data = np.array(engagement_data['Bookface'])
twitter_data = np.array(engagement_data['Twister'])
instagram_data = np.array(engagement_data['Gramsta'])

fig, ax = plt.subplots(figsize=(14, 8))
bar_height = 0.25
y_positions = np.arange(len(months))

bars_fb = ax.barh(y_positions - bar_height, facebook_data, bar_height, label='Bookface', color='darkorange')
bars_tw = ax.barh(y_positions, twitter_data, bar_height, label='Twister', color='steelblue')
bars_ig = ax.barh(y_positions + bar_height, instagram_data, bar_height, label='Gramsta', color='forestgreen')

for rect in bars_fb + bars_tw + bars_ig:
    width = rect.get_width()
    ax.text(width, rect.get_y() + rect.get_height()/2.0, f'{width}', ha='left', va='center', fontsize=12)

ax.set_title('21st-century Social Network Engagements', fontsize=16, pad=20, weight='bold')
ax.set_ylabel('Months of the Year', fontsize=12)
ax.set_xlabel('Engagement Rate (thousands)', fontsize=12)
ax.set_yticks(y_positions)
ax.set_yticklabels(months, fontsize=11)

ax.legend(title='Network', fontsize=11, loc='upper left')
ax.xaxis.grid(True, linestyle='-', linewidth=0.5, alpha=0.5)

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()
plt.show()