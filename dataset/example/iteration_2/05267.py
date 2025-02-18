import matplotlib.pyplot as plt
import numpy as np

# Defining tree species and their fictional distributions
tree_species = ['Oak', 'Pine', 'Maple', 'Birch', 'Redwood', 'Willow', 'Sequoia']
sunlight_hours = np.array([4, 6, 5, 8, 2, 9, 3])  # Sunlight exposure (hours/day)
moisture_levels = np.array([800, 600, 700, 500, 1200, 400, 1300])  # Moisture levels (mm/year)
prevalence = np.array([200, 250, 180, 300, 220, 270, 320])  # Tree prevalence (size of scatter)

# Create a scatter plot
plt.figure(figsize=(12, 8))
scatter = plt.scatter(sunlight_hours, moisture_levels, s=prevalence, c=prevalence, cmap='viridis', edgecolor='black', alpha=0.8)

# Titles and labels
plt.title('Tree Distribution in the Forest of Eldoria', fontsize=16, fontweight='bold')
plt.xlabel('Average Sunlight Exposure (Hours/Day)', fontsize=12, fontweight='bold')
plt.ylabel('Average Moisture Levels (mm/Year)', fontsize=12, fontweight='bold')

# Add a color bar
color_bar = plt.colorbar(scatter)
color_bar.set_label('Tree Prevalence (Arbitrary Units)', rotation=270, labelpad=20)

# Annotations for each type of tree
for i, species in enumerate(tree_species):
    plt.annotate(species, (sunlight_hours[i], moisture_levels[i]), 
                 textcoords="offset points", xytext=(0,10), ha='center', fontsize=9, color='black')

# Grid for better readability
plt.grid(True, linestyle='--', alpha=0.6)

# Automatically adjust the layout
plt.tight_layout()

# Display the plot
plt.show()