import matplotlib.pyplot as plt
import numpy as np

# Backstory: Analysis of Monthly Social Media Engagement for a Tech Blog across Different Platforms in 2023

# Data: Monthly social media engagement (likes, shares, comments) in thousands
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
platforms = ['Facebook', 'Twitter', 'Instagram']

# Engagement data for each platform
# Format: [likes, shares, comments] in thousands
engagement_data = {
    'Facebook': [35, 28, 23, 25, 30, 35, 40, 38, 37, 32, 30, 28],
    'Twitter': [20, 18, 15, 17, 19, 22, 25, 28, 26, 24, 22, 20],
    'Instagram': [40, 35, 33, 39, 42, 45, 50, 48, 47, 45, 40, 38]
}

# Create numpy arrays for the data
facebook_data = np.array(engagement_data['Facebook'])
twitter_data = np.array(engagement_data['Twitter'])
instagram_data = np.array(engagement_data['Instagram'])

# Setting up the figure and axis
fig, ax = plt.subplots(figsize=(14, 8))

# Define bar width and positions
bar_width = 0.25
x_positions = np.arange(len(months))

# Plot bars for each platform
bars_fb = ax.bar(x_positions - bar_width, facebook_data, bar_width, label='Facebook', color='#3b5998')
bars_tw = ax.bar(x_positions, twitter_data, bar_width, label='Twitter', color='#1DA1F2')
bars_ig = ax.bar(x_positions + bar_width, instagram_data, bar_width, label='Instagram', color='#C13584')

# Annotate each bar with the values
for rect in bars_fb + bars_tw + bars_ig:
    height = rect.get_height()
    ax.text(rect.get_x() + rect.get_width()/2.0, height, f'{height}', ha='center', va='bottom', fontsize=9)

# Set the title and labels
ax.set_title('Monthly Social Media Engagement for Tech Innovators Blog (2023)', fontsize=16, pad=20, weight='bold')
ax.set_xlabel('Month', fontsize=12)
ax.set_ylabel('Engagement (in thousands)', fontsize=12)
ax.set_xticks(x_positions)
ax.set_xticklabels(months, fontsize=11)

# Add a legend
ax.legend(title='Platform', fontsize=11)

# Add grid lines for better readability
ax.yaxis.grid(True, linestyle='--', alpha=0.7)

# Automatically adjust layout to prevent label overlap
plt.tight_layout()

# Display the plot
plt.show()