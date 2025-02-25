import matplotlib.pyplot as plt

# Define regions
regions = ['North America', 'Europe', 'Asia']

# Data representing wheat yields (in tons per hectare) for 2022
wheat_na = [3.2, 3.5, 3.6, 4.0, 4.2, 3.9, 4.1, 3.8, 4.0, 3.7]
wheat_eu = [5.5, 5.4, 5.6, 5.7, 5.8, 5.5, 5.6, 5.4, 5.7, 5.5]
wheat_as = [3.8, 3.9, 4.0, 4.1, 4.2, 4.0, 4.1, 3.9, 4.0, 4.1]

# Organize the data for the box plot
data_wheat = [wheat_na, wheat_eu, wheat_as]

# Create subplot
fig, ax = plt.subplots(figsize=(6, 8))

# Plot Wheat Yields
box_wheat = ax.boxplot(data_wheat, vert=True, patch_artist=True, labels=regions, notch=True)
for patch in box_wheat['boxes']:
    patch.set_facecolor('#FF9999')
ax.set_title('Wheat Yields in 2022', fontsize=14, fontweight='bold')
ax.set_ylabel('Yield (tons per hectare)', fontsize=12)
ax.set_xlabel('Regions', fontsize=12)
ax.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)
ax.set_axisbelow(True)

# Common title (adjusted for single plot)
fig.suptitle('Climate Change Impact on Wheat Yields in 2022', fontsize=16, fontweight='bold', y=0.98)

# Adjust layout
plt.tight_layout(rect=[0, 0, 1, 0.95])

# Show plot
plt.show()