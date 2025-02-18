import numpy as np
import matplotlib.pyplot as plt

# Backstory:
# We are analyzing the relationship between the intrinsic brightness of stars (absolute magnitude) and their surface temperature (measured in Kelvin).
# This study aims to visualize the Hertzsprung-Russell diagram, which is fundamental in understanding stellar properties and evolution.

# Data Preparation:
# Absolute Magnitude (Brightness): Higher values mean dimmer stars.
brightness = np.array([5.1, 5.4, 5.7, 6.0, 6.3, 6.5, 7.0, 7.5, 8.0, 4.2, 4.5, 4.8, 3.1, 3.3,
                       3.9, 2.7, 2.5, 1.0, -1.5, 0.8, -1.0, -2.4, -2.3])

# Surface Temperature in Kelvin
temperature = np.array([3000, 3200, 3500, 3700, 4000, 4300, 5000, 5200, 6000, 7000, 8000,
                        9000, 12000, 15000, 20000, 25000, 30000, 35000, 40000, 45000, 
                        50000, 55000, 60000])

# Define star types based on absolute magnitude
star_types = ['Supergiant' if val < 0 else 'Main Sequence' for val in brightness]

# Plotting the scatter chart
fig, ax = plt.subplots(figsize=(12, 7))

# Scatter plot of brightness vs temperature with color coding for star types
sc = ax.scatter(temperature, brightness, c=brightness, cmap='viridis', alpha=0.75, edgecolors='w', s=100)

# Adding titles and labels to the plot
ax.set_title('Hertzsprung-Russell Diagram: Stellar Classification by Brightness and Temperature', fontsize=16, fontweight='bold', wrap=True)
ax.set_xlabel('Surface Temperature (K)', fontsize=12)
ax.set_ylabel('Absolute Magnitude (Brightness)', fontsize=12)
ax.invert_yaxis()  # inverting y-axis because lower magnitudes mean brighter stars

# Adding grid lines
ax.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

# Adding a color bar and legend
cbar = plt.colorbar(sc, ax=ax)
cbar.set_label('Brightness (Absolute Magnitude)', fontsize=12)

# Add a legend showcasing star types
legend_labels = {v: f'Type {v}' for v in set(star_types)}
handles, labels = sc.legend_elements(prop="colors", alpha=0.6)
legend_labels = [legend_labels[l] for l in legend_labels]
ax.legend(handles, legend_labels, title='Star Types', loc='upper right')

# Ensuring no overlapping of text or elements
plt.tight_layout()

# Display the plot
plt.show()