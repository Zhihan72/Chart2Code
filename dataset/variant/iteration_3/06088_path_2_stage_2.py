import matplotlib.pyplot as plt
import numpy as np

# Seasons with randomly altered labels
seasons = ['Cold Breeze', 'Falling Leaves', 'Fresh Green', 'Hot Sun']

# Generate artificial data for each location and season (in millimeters)
rainfall_data = {
    'Meadow of Twilight': [175, 125, 145, 115],
    'Falls of Mist': [150, 110, 140, 120],
    'Pines Whisper': [180, 140, 135, 125],
    'Glen of Fae': [160, 120, 130, 110],
    'Grove of Enchant': [170, 130, 150, 140]
}

# Prepare data for box plot
season_data = np.array(list(rainfall_data.values()))

# Create a figure and axis
fig, ax = plt.subplots(figsize=(14, 8))

# Plotting the vertical box plots for each season
boxplots = ax.boxplot(season_data, notch=False, vert=True, patch_artist=True, labels=seasons)

# Define a color palette to represent seasons
colors = ['#253494', '#41b6c4', '#a1dab4', '#2c7fb8']

# Set colors for each box plot and adjust median line properties
for patch, color, median in zip(boxplots['boxes'], colors, boxplots['medians']):
    patch.set_facecolor(color)
    patch.set_alpha(0.9)
    patch.set_edgecolor('grey')
    median.set_color('darkred')
    median.set_linewidth(2)

# Customizing the plot
ax.set_title('Rainfall Variations of Enchanted Realms\nAcross the Mysterious Seasons', fontsize=18, fontweight='bold')
ax.set_ylabel('Rainfall (mm)', fontsize=14)
ax.set_xlabel('Seasons', fontsize=14)

# Modify the grid to be visible only on the x-axis
ax.xaxis.grid(True, linestyle='-.', color='blue', alpha=0.5)

# Adding legends to explain locations
location_labels = rainfall_data.keys()
for line, label in zip(boxplots['medians'], location_labels):
    line.set_label(label)

# Add legend with a different location
ax.legend(title='Mystical Locations', fontsize=11, loc='upper right')

# Applying tight layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()