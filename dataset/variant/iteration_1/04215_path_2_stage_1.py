import matplotlib.pyplot as plt
import numpy as np

# Define regions and solar panel types
regions = ['Desert', 'Tropical', 'Temperate', 'Arctic']
panel_types = ['Monocrystalline', 'Polycrystalline', 'Thin-Film']

# Average power output data for each panel type in different regions (in MW)
power_output = np.array([
    [70, 55, 35, 20],  # Monocrystalline
    [65, 50, 30, 18],  # Polycrystalline
    [60, 45, 28, 15]   # Thin-Film
])

# Setup the figure
fig, ax = plt.subplots(figsize=(12, 8))

# Assign colors to each panel type
colors = ['#FF6347', '#4682B4', '#32CD32']

bar_width = 0.25  # Width of the bars
y_pos = np.arange(len(regions))

# Plot horizontal bars
for idx, (panel_idx, color) in enumerate(zip(range(len(panel_types)), colors)):
    ax.barh(y_pos + (panel_idx - 1) * bar_width, power_output[panel_idx], bar_width, color=color, edgecolor='black', label=panel_types[panel_idx])

# Set title and labels
ax.set_title("Regional Performance of Different Solar Panel Types", fontsize=14, fontweight='bold', pad=20)
ax.set_ylabel("Region", fontsize=12)
ax.set_xlabel("Average Power Output (MW)", fontsize=12)

# Customize y-axis ticks
ax.set_yticks(y_pos)
ax.set_yticklabels(regions, fontsize=10)

# Adding a legend
ax.legend(title='Solar Panel Types')

# Enhance grid visibility for better readability
ax.grid(color='gray', linestyle='--', linewidth=0.5, alpha=0.6)

# Automatically adjust layout
plt.tight_layout()

# Show the plot
plt.show()