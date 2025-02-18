import matplotlib.pyplot as plt

# Define regions and data
regions = ['N. America', 'Europe']
wheat_na = [3.2, 3.5, 3.6, 4.0, 4.2, 3.9, 4.1, 3.8, 4.0, 3.7]
wheat_eu = [5.5, 5.4, 5.6, 5.7, 5.8, 5.5, 5.6, 5.4, 5.7, 5.5]
data_wheat = [wheat_na, wheat_eu]

fig, ax = plt.subplots(figsize=(6, 8))

# Plot Wheat Yields
box_wheat = ax.boxplot(data_wheat, vert=True, patch_artist=True, labels=regions, notch=True)

# New colors for each region's box
colors = ['#66CCFF', '#99FF66']

for patch, color in zip(box_wheat['boxes'], colors):
    patch.set_facecolor(color)

# Set labels
ax.set_ylabel('Yield (t/ha)', fontsize=12)
ax.set_xlabel('Regions', fontsize=12)

plt.tight_layout()
plt.show()