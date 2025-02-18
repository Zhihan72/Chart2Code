import matplotlib.pyplot as plt
import numpy as np
from math import pi

# Define the attributes for the radar chart
attributes = ['Military Strength', 'Economic Stability', 'Cultural Influence', 
              'Technological Innovation', 'Diplomatic Prowess']

# Define the statistics for each kingdom
eldoria_stats = [60, 65, 85, 70, 80]
lunaria_stats = [70, 60, 75, 85, 85]  # Removed Dracoria

# Prepare data and settings
data = [eldoria_stats, lunaria_stats]  # Removed Dracoria
kingdoms = ['Kingdom of Eldoria', 'Empire of Lunaria']  # Removed Dracoria
colors = ['purple', 'green']  # Removed related color

num_vars = len(attributes)

# Compute angle for each attribute
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]

# Function to create a radar chart
def create_radar_chart(ax, data, color, label):
    data += data[:1]  # Repeat the first value to close the radar chart
    ax.fill(angles, data, color=color, alpha=0.25, label=label)

# Set up the radar chart
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Create the radar chart for each kingdom
for i in range(len(kingdoms)):
    create_radar_chart(ax, data[i], colors[i], kingdoms[i])

# Configure the appearance of the radar chart
ax.set_yticklabels([])
ax.set_xticks(angles[:-1])
ax.set_xticklabels(attributes, fontsize=10, color='gray')

# Title and legend
plt.title('Attributes of Medieval Kingdoms\nComparative Analysis', size=14, weight='bold', pad=20)
ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1), fontsize=10)

# Display the plot
plt.tight_layout()
plt.show()