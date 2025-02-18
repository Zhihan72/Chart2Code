import numpy as np
import matplotlib.pyplot as plt
from math import pi

# Define the training centers and parameters
centers = ['DragonForce', 'TigerClaw', 'EagleStrike', 'PantherHeart', 'WolfPack', 'PhoenixFlame']
parameters = ['Strength Training', 'Agility Training', 'Self-defense', 'Endurance', 'Flexibility']

# Constructing data for each training center
data = np.array([
    [90, 80, 85, 70, 95],  # DragonForce
    [88, 75, 80, 85, 90],  # TigerClaw
    [85, 85, 90, 80, 82],  # EagleStrike
    [80, 90, 78, 70, 88],  # PantherHeart
    [95, 85, 80, 78, 92],  # WolfPack
    [82, 88, 87, 76, 90]   # PhoenixFlame - New data series added
])

# Number of parameters
num_vars = len(parameters)

# Compute angle for each parameter
angles = np.linspace(0, 2 * pi, num_vars, endpoint=False).tolist()
angles += angles[:1]  # close the circle

# Initialize the radar chart
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Function to draw each training center in the radar plot
def plot_center(data, color, label):
    values = data.tolist()
    values += values[:1]
    ax.plot(angles, values, linewidth=2, linestyle='solid', color=color, label=label)
    ax.fill(angles, values, color=color, alpha=0.25)

# Set colors for each center
colors = ['b', 'g', 'r', 'c', 'm', 'y']  # Added 'y' for the new center

# Plot each training center
for idx, center_data in enumerate(data):
    plot_center(center_data, colors[idx], centers[idx])

# Add parameter labels
plt.xticks(angles[:-1], parameters, color='grey', size=10)

# Add values grid
plt.yticks([20, 40, 60, 80, 100], ["20", "40", "60", "80", "100"], color="grey", size=8)
plt.ylim(0, 100)

# Add a title
plt.title('Evaluation of Martial Arts Training Centers in Fictitious City', size=14, color='darkred', weight='bold', position=(0.5, 1.1))

# Add legend
plt.legend(loc='upper right', bbox_to_anchor=(1.1, 1.1), title='Training Centers')

# Automatically adjust layout to avoid overlap
plt.tight_layout()

# Display the radar chart
plt.show()