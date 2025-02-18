import matplotlib.pyplot as plt
import numpy as np

sectors = ['Residential', 'Commercial', 'Industrial', 'Agricultural', 'Healthcare', 'Education', 'Recreational']
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

# Voltage levels data
voltage_levels = np.array([
    [225, 210, 220, 219, 221, 223, 222, 227, 228, 225, 228, 227],
    [228, 230, 229, 234, 232, 239, 236, 239, 237, 236, 233, 232],
    [212, 217, 218, 223, 233, 230, 242, 243, 247, 246, 242, 238],
    [202, 207, 208, 213, 218, 222, 230, 232, 224, 219, 214, 211],
    [231, 235, 233, 235, 239, 238, 241, 243, 242, 240, 237, 236],
    [222, 223, 223, 225, 230, 229, 233, 235, 230, 229, 232, 228],
    [213, 220, 218, 223, 225, 224, 229, 228, 226, 225, 223, 220]
])

average_voltage = np.mean(voltage_levels, axis=0)

# Create a masked array to plot only the lower triangle
mask = np.triu(np.ones_like(voltage_levels, dtype=bool))  # Upper triangle mask

# Apply the mask
masked_voltage_levels = np.ma.masked_where(mask, voltage_levels)

fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(8, 12))
fig.suptitle('Futuristic City Power Monitoring\nAvg Voltage Levels by Sector and Month', fontsize=16, fontweight='bold')

# Plot the masked heatmap
heatmap = axes[0].imshow(masked_voltage_levels, cmap='cool', aspect='auto', interpolation='nearest')
cbar = fig.colorbar(heatmap, ax=axes[0])
cbar.set_label('Voltage Level (V)', fontsize=10)

axes[0].set_title('Avg Voltage Levels by Sector and Month', fontsize=12)
axes[0].set_xlabel('Month', fontsize=10)
axes[0].set_ylabel('City Sector', fontsize=10)
axes[0].set_xticks(np.arange(len(months)))
axes[0].set_xticklabels(months, fontsize=8, rotation=45)
axes[0].set_yticks(np.arange(len(sectors)))
axes[0].set_yticklabels(sectors, fontsize=8)

for i in range(len(sectors)):
    for j in range(len(months)):
        if not mask[i, j]:  # Only add text for unmasked elements
            axes[0].text(j, i, f"{voltage_levels[i, j]}", ha='center', va='center', color='black', fontsize=7)

axes[1].plot(months, average_voltage, marker='o', color='black', linewidth=2, label='Average Voltage')
axes[1].set_title('Average Voltage Trend Across Sectors', fontsize=12)
axes[1].set_xlabel('Month', fontsize=10)
axes[1].set_ylabel('Avg Voltage Level (V)', fontsize=10)
axes[1].set_xticks(np.arange(len(months)))
axes[1].set_xticklabels(months, fontsize=8, rotation=45)
axes[1].grid(True, linestyle='--', alpha=0.7)
axes[1].legend(fontsize=9)
axes[1].set_ylim(200, 250)

plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()