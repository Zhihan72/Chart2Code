import matplotlib.pyplot as plt
import numpy as np

# Define thematic backstory: Fairytale Forest's Annual Rainfall Distribution Over Four Seasons
# Imagine a mystical forest where fairies manage the weather. The data represents rainfall measured in millimeters.

# Seasons
seasons = ['Spring', 'Summer', 'Autumn', 'Winter']

# Generate artificial data for each location and season (in millimeters)
rainfall_data = {
    'Fairy Glen':    [160, 120, 130, 110],  # Spring, Summer, Autumn, Winter
    'Mystic Falls':  [150, 110, 140, 120],
    'Enchanted Grove': [170, 130, 150, 140],
    'Whispering Pines': [180, 140, 135, 125],
    'Twilight Meadow': [175, 125, 145, 115]
}

# Prepare data for box plot: transpose to create datasets for each season across different locations
season_data = np.array(list(rainfall_data.values()))

# Create a figure and axis
fig, ax = plt.subplots(figsize=(14, 8))

# Plotting the vertical box plots for each season
boxplots = ax.boxplot(season_data, notch=True, vert=True, patch_artist=True, labels=seasons)

# Define a color palette to represent seasons
colors = ['#a1dab4', '#41b6c4', '#2c7fb8', '#253494']

# Set colors for each box plot and adjust median line properties
for patch, color, median in zip(boxplots['boxes'], colors, boxplots['medians']):
    patch.set_facecolor(color)
    patch.set_alpha(0.7)
    patch.set_edgecolor('black')
    median.set_color('black')
    median.set_linewidth(1.5)

# Customizing the plot
ax.set_title('Annual Rainfall Distribution in Fairytale Forest\nAcross Four Seasons', fontsize=16, fontweight='bold')
ax.set_ylabel('Rainfall (mm)', fontsize=12)
ax.set_xlabel('Season', fontsize=12)

# Add a grid for the y-axis to enhance readability
ax.yaxis.grid(True, linestyle='--', color='grey', alpha=0.6)

# Adding legends to explain locations
location_labels = rainfall_data.keys()
for line, label in zip(boxplots['medians'], location_labels):
    line.set_label(label)

# Add legend
ax.legend(title='Locations', fontsize=10, loc='upper left')

# Applying tight layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()