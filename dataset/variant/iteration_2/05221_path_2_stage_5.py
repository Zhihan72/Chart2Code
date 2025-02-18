import numpy as np
import matplotlib.pyplot as plt

# Define the data
years = np.arange(2015, 2025)
tools = ["Gadget Z", "Widget Y", "Instrument X", "Device W", "App V", "Program U", "Utility T"]

active_users = np.array([
    [150, 160, 170, 180, 190, 200, 210, 220, 230, 240],
    [110, 115, 120, 125, 130, 135, 140, 145, 150, 155],
    [90,  95, 100, 105, 110, 120, 130, 140, 150, 160],
    [130, 135, 140, 145, 150, 155, 160, 165, 170, 175],
    [100, 110, 120, 130, 140, 150, 160, 170, 180, 190],
    [80, 90, 100, 110, 120, 130, 140, 150, 160, 170],
    [95, 105, 115, 125, 135, 145, 155, 165, 175, 185]
])

fig, ax = plt.subplots(figsize=(14, 7))

# Create a mask for upper triangle
mask = np.triu(np.ones_like(active_users, dtype=bool))

# Apply mask to data
data_masked = np.ma.masked_where(mask, active_users)

cax = ax.imshow(data_masked, cmap='viridis', interpolation='nearest', aspect='auto')

cbar = fig.colorbar(cax, ax=ax, orientation='vertical')
cbar.set_label('User Base (Thousand)', rotation=270, labelpad=20)

ax.set_xlabel('Timeline (Year)', fontsize=12, fontstyle='italic')
ax.set_ylabel('Software Group', fontsize=12, fontstyle='italic')

ax.set_xticks(np.arange(len(years)))
ax.set_yticks(np.arange(len(tools)))
ax.set_xticklabels(years, rotation=45, ha='right', fontsize=10)
ax.set_yticklabels(tools, fontsize=10)

ax.set_title('Digital Solution Engagement:\nDecadal Review 2015-2024', fontsize=16, fontweight='bold', pad=20)

for i in range(len(tools)):
    for j in range(len(years)):
        if not mask[i, j]:  # Only label the lower triangle
            ax.text(j, i, f'{active_users[i, j]}', ha='center', va='center', color='white', fontsize=10)

ax.grid(True, linestyle='--', linewidth=0.5)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)

plt.tight_layout()
plt.show()