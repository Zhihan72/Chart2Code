import numpy as np
import matplotlib.pyplot as plt

# Define the years and software tools
years = np.arange(2015, 2025)
software_tools = ["Tool A", "Tool B", "Tool C", "Tool D", "Tool E"]

# Define synthetic data for the number of active users (thousands)
active_users = np.array([
    [150, 160, 170, 180, 190, 200, 210, 220, 230, 240],  # Tool A
    [110, 115, 120, 125, 130, 135, 140, 145, 150, 155],  # Tool B
    [90,  95, 100, 105, 110, 120, 130, 140, 150, 160],   # Tool C
    [130, 135, 140, 145, 150, 155, 160, 165, 170, 175],  # Tool D
    [100, 110, 120, 130, 140, 150, 160, 170, 180, 190]   # Tool E
])

fig, ax = plt.subplots(figsize=(14, 7))

# Plot the heatmap
cax = ax.imshow(active_users, cmap='viridis', interpolation='nearest', aspect='auto')

# Add a color bar
cbar = fig.colorbar(cax, ax=ax, orientation='vertical')
cbar.set_label('Active Users (in Thousands)', rotation=270, labelpad=20)

# Set axis labels
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Software Tool', fontsize=12)

# Set x and y ticks
ax.set_xticks(np.arange(len(years)))
ax.set_yticks(np.arange(len(software_tools)))
ax.set_xticklabels(years, rotation=45, ha='right', fontsize=10)
ax.set_yticklabels(software_tools, fontsize=10)

# Title
ax.set_title('Software Tool Usage Trends:\nA Decade Evaluation (2015-2024)', fontsize=16, fontweight='bold', pad=20)

# Annotate each cell with the data value
for i in range(len(software_tools)):
    for j in range(len(years)):
        ax.text(j, i, f'{active_users[i, j]}', ha='center', va='center', color='white', fontsize=10)

# Additional customization: set grid and layout
ax.grid(False)
plt.tight_layout()

# Display the plot
plt.show()