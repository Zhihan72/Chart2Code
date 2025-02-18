import matplotlib.pyplot as plt
import numpy as np

# Define sectors and months
sectors = ['Residential', 'Commercial', 'Industrial', 'Education', 'Recreational']
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

# Manually constructed data for average voltage levels (in Volts)
voltage_levels = np.array([
    [220, 215, 218, 220, 222, 224, 225, 230, 229, 228, 226, 225],  # Residential
    [230, 228, 231, 233, 235, 238, 239, 240, 238, 237, 236, 234],  # Commercial
    [210, 215, 220, 225, 230, 235, 240, 245, 248, 250, 245, 240],  # Industrial
    [220, 222, 224, 226, 228, 230, 232, 234, 233, 231, 229, 227],  # Education
    [215, 218, 220, 222, 224, 226, 228, 230, 228, 226, 224, 222]   # Recreational
])

# Calculate the average voltage level for all sectors per month
average_voltage = np.mean(voltage_levels, axis=0)

# Mask for the lower triangle
mask = np.tril(np.ones_like(voltage_levels, dtype=bool))

# Setup figure and axes for subplots
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(16, 8))
fig.suptitle('Futuristic City Power Monitoring\nAvg Voltage Levels by Sector and Month', fontsize=16, fontweight='bold')

# Plot lower triangle heatmap
heatmap = axes[0].imshow(np.ma.masked_array(voltage_levels, mask=~mask), cmap='cool', aspect='auto', interpolation='nearest')
cbar = fig.colorbar(heatmap, ax=axes[0])
cbar.set_label('Voltage Level (V)', fontsize=10)

axes[0].set_title('Avg Voltage Levels by Sector and Month', fontsize=12)
axes[0].set_xlabel('Month', fontsize=10)
axes[0].set_ylabel('City Sector', fontsize=10)
axes[0].set_xticks(np.arange(len(months)))
axes[0].set_xticklabels(months, fontsize=8, rotation=45)
axes[0].set_yticks(np.arange(len(sectors)))
axes[0].set_yticklabels(sectors, fontsize=8)

# Annotating data points only in lower triangle
for i in range(len(sectors)):
    for j in range(len(months)):
        if i >= j:  # Only print in the lower triangle
            axes[0].text(j, i, f"{voltage_levels[i, j]}", ha='center', va='center', color='black', fontsize=7)

# Plot line chart for average voltage trends
axes[1].plot(months, average_voltage, marker='o', color='blue', linewidth=2, label='Average Voltage')
axes[1].set_title('Average Voltage Trend Across Sectors', fontsize=12)
axes[1].set_xlabel('Month', fontsize=10)
axes[1].set_ylabel('Avg Voltage Level (V)', fontsize=10)
axes[1].set_xticks(np.arange(len(months)))
axes[1].set_xticklabels(months, fontsize=8, rotation=45)
axes[1].grid(True, linestyle='--', alpha=0.7)
axes[1].legend(fontsize=9)
axes[1].set_ylim(200, 250)

plt.tight_layout(rect=[0, 0.03, 1, 0.95])

# Display the plot
plt.show()