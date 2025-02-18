import matplotlib.pyplot as plt
import numpy as np

# Define the categories for the video game genres
categories = ['Storyline', 'Graphics', 'Audio', 'Replay Value', 'Difficulty', 'Controls', 'Community']

# Ratings of different gaming genres
action_game = [8, 9, 7, 6, 8, 9, 7]
adventure_game = [9, 8, 9, 7, 5, 8, 8]
role_playing_game = [10, 8, 8, 9, 7, 8, 9]
shooter_game = [7, 9, 8, 7, 6, 9, 8]
sports_game = [6, 7, 8, 8, 6, 7, 5]

# Close the loop for radar chart
action_game += action_game[:1]
adventure_game += adventure_game[:1]
role_playing_game += role_playing_game[:1]
shooter_game += shooter_game[:1]
sports_game += sports_game[:1]

# Number of variables
num_vars = len(categories)

# Compute angles for each category
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]

# Initialize the radar chart
fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))

# Plot settings for better visualization
plt.yticks([2, 4, 6, 8, 10], ['2', '4', '6', '8', '10'], color='grey', size=8)
plt.ylim(0, 11)

# Plot data for each genre with distinctive colors and styles
genres = {
    'Action': ('#1f77b4', 'solid', 'o'),
    'Adventure': ('#ff7f0e', '--', '^'),
    'Role-Playing': ('#2ca02c', 'dashdot', 's'),
    'Shooter': ('#d62728', ':', 'D'),
    'Sports': ('#9467bd', (0, (3, 1, 1, 1)), 'P')
}

datasets = [action_game, adventure_game, role_playing_game, shooter_game, sports_game]

for data, (label, style) in zip(datasets, genres.items()):
    color, linestyle, marker = style
    ax.plot(angles, data, color=color, linewidth=2, linestyle=linestyle, marker=marker, markersize=6, label=label)
    ax.fill(angles, data, color=color, alpha=0.25)

# Add title and labels
plt.title('2023 Video Game Genre Evaluations\nRatings Based on Different Aspects', size=16, color='purple', weight='bold', loc='center', pad=30)
ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, color='black', size=11)
ax.set_yticklabels([])

# Add legend
plt.legend(loc='upper right', bbox_to_anchor=(1.2, 1.0), title='Game Genres')

# Adjust the layout
plt.tight_layout()

# Show the plot
plt.show()