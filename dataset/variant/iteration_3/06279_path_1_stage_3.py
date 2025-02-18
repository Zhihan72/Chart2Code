import matplotlib.pyplot as plt
import numpy as np

categories = ['Storyline', 'Graphics', 'Audio', 'Replay Value', 'Difficulty', 'Controls', 'Community']
action_game = [8, 9, 7, 6, 8, 9, 7]
adventure_game = [9, 8, 9, 7, 5, 8, 8]
role_playing_game = [10, 8, 8, 9, 7, 8, 9]
shooter_game = [7, 9, 8, 7, 6, 9, 8]
sports_game = [6, 7, 8, 8, 6, 7, 5]

# Adding the first rating value to close the loop for each genre
action_game += action_game[:1]
adventure_game += adventure_game[:1]
role_playing_game += role_playing_game[:1]
shooter_game += shooter_game[:1]
sports_game += sports_game[:1]

num_vars = len(categories)
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]  # Closing the circle by adding the first value to the end

# Create the plot with polar coordinates
fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))

plt.ylim(0, 11)  # Set the radius limits

# Define the styles for each genre
genres = {
    'Action': ('#1f77b4', 'solid', 'o'),
    'Adventure': ('#ff7f0e', '--', '^'),
    'Role-Playing': ('#2ca02c', 'dashdot', 's'),
    'Shooter': ('#d62728', ':', 'D'),
    'Sports': ('#9467bd', (0, (3, 1, 1, 1)), 'P')
}

# Dataset for each genre
datasets = [action_game, adventure_game, role_playing_game, shooter_game, sports_game]

# Iterate over datasets and their corresponding genre styles
for data, (color, linestyle, marker) in zip(datasets, genres.values()):
    ax.plot(angles, data, color=color, linewidth=2, linestyle=linestyle, marker=marker, markersize=6)
    ax.fill(angles, data, color=color, alpha=0.4)

# Set the labels for categories (ax.set_xticks)
ax.set_xticks(angles[:-1])  # Remove the last angle since it's a duplicate
ax.set_xticklabels(categories, fontsize=12, ha='center')

# Remove y-axis labels and ticks
ax.set_yticklabels([])
ax.set_yticks([])

# Hide the polar spine and grid
ax.spines['polar'].set_visible(False)
ax.grid(False)

# Adjust layout and display the plot
plt.tight_layout()
plt.show()