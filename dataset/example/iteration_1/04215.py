import matplotlib.pyplot as plt
import numpy as np

# Backstory:
# SolarFlare Technologies is a cutting-edge company focused on developing renewable energy solutions
# by harnessing solar power in various innovative ways. Over the years, they've been experimenting
# with different types of solar panels across multiple regions. The chart below depicts the average
# power output (in megawatts) of three different types of solar panels tested in four different regions.

# Define regions and solar panel types
regions = ['Desert', 'Tropical', 'Temperate', 'Arctic']
panel_types = ['Monocrystalline', 'Polycrystalline', 'Thin-Film']

# Average power output data for each panel type in different regions (in MW)
power_output = np.array([
    [70, 55, 35, 20],  # Monocrystalline
    [65, 50, 30, 18],  # Polycrystalline
    [60, 45, 28, 15]   # Thin-Film
])

# Create a meshgrid for bar positions
regions_index, panel_index = np.meshgrid(np.arange(len(regions)), np.arange(len(panel_types)), indexing='ij')
regions_index_flat = regions_index.flatten()
panel_index_flat = panel_index.flatten()
z_flat = np.zeros_like(regions_index_flat)

# Flatten the power output data for plotting
power_flat = power_output.flatten()

# Setup the figure
fig, ax = plt.subplots(figsize=(12, 8))

# Assign colors to each panel type
colors = ['#FF6347', '#4682B4', '#32CD32']

# Plot each set of bars in the chart
bar_width = 0.25  # Width of the bars
for idx, (region_idx, panel_idx, z, power, color) in enumerate(zip(regions_index_flat, panel_index_flat, z_flat, power_flat, np.repeat(colors, len(regions)))):
    x_pos = region_idx + (panel_idx - 1) * bar_width  # Modify x position to fit side-by-side
    ax.bar(x_pos, power, bar_width, color=color, edgecolor='black', label=panel_types[panel_idx] if region_idx == 0 else "")

# Set title and labels
ax.set_title("Regional Performance of Different Solar Panel Types", fontsize=14, fontweight='bold', pad=20)
ax.set_xlabel("Region", fontsize=12)
ax.set_ylabel("Average Power Output (MW)", fontsize=12)

# Customize x-axis ticks
ax.set_xticks(np.arange(len(regions)) + bar_width / 2)
ax.set_xticklabels(regions, fontsize=10)

# Adding a legend
ax.legend(title='Solar Panel Types')

# Enhance grid visibility for better readability
ax.grid(color='gray', linestyle='--', linewidth=0.5, alpha=0.6)

# Automatically adjust layout
plt.tight_layout()

# Show the plot
plt.show()