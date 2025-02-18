import matplotlib.pyplot as plt
import numpy as np

# Exoplanet data
exoplanets = ['Xeno 1', 'Nexus 2', 'Terra Nova', 'Zypher', 'Cosmo Prime',
              'Artemis', 'Elysium', 'Solaria', 'Arcadia', 'Veridian']

# Distances from Earth (in light-years)
distances = np.array([4.2, 8.6, 15.3, 20.7, 22.5, 28.4, 30.1, 35.0, 38.7, 40.0])

# Estimated sizes (in Earth Masses)
sizes = np.array([0.9, 1.1, 1.3, 2.0, 1.8, 1.0, 2.5, 0.8, 1.6, 1.4])

# Habitability scores (on a scale of 0 to 1)
habitability_scores = np.array([0.8, 0.6, 0.9, 0.4, 0.5, 0.7, 0.3, 0.2, 0.6, 0.1])

# Bubble sizes (scaling factor for better visualization)
bubble_sizes = sizes * 150

# Create a 3D scatter plot
fig = plt.figure(figsize=(14, 9))
ax = fig.add_subplot(111, projection='3d')

# Plotting the data with a single color
scatter = ax.scatter(distances, sizes, habitability_scores, s=bubble_sizes, 
                     c='royalblue', alpha=0.85)

# Setting labels and title
ax.set_title('Exoplanet Exploration: Evaluating Promising Targets in the Universe', fontsize=16, pad=30)
ax.set_xlabel('Distance from Earth (light-years)', fontsize=12, labelpad=10)
ax.set_ylabel('Estimated Size (Earth Masses)', fontsize=12, labelpad=10)
ax.set_zlabel('Habitability Score', fontsize=12, labelpad=10)

# Annotating each exoplanet with its name
for i, planet in enumerate(exoplanets):
    ax.text(distances[i], sizes[i], habitability_scores[i] + 0.03, planet, fontsize=9, color='navy', ha='center')

# Automatically adjust layout
plt.tight_layout()

# Display the plot
plt.show()