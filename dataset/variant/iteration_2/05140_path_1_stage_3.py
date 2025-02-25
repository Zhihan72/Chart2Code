import matplotlib.pyplot as plt

# Data for the box plot
apple_yield = [30, 35, 40, 32, 33, 36, 38, 37, 34, 31]
orange_yield = [25, 28, 22, 26, 29, 24, 21, 27, 23, 26]
pear_yield = [15, 17, 13, 18, 16, 14, 19, 12, 16, 15]
cherry_yield = [10, 13, 9, 11, 14, 8, 7, 10, 12, 13]

data = [apple_yield, orange_yield, pear_yield, cherry_yield]

# Create the figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Create the horizontal box plot
boxplot = ax.boxplot(data, vert=False, patch_artist=True, widths=0.6, notch=True)

# Set colors for boxes
colors = ['#FFD700', '#FF69B4', '#FF6347', '#90EE90']
for patch, color in zip(boxplot['boxes'], colors):
    patch.set_facecolor(color)

# Customize whiskers, caps, and medians
for whisker in boxplot['whiskers']:
    whisker.set(color='#8B8B8B', linewidth=1.5, linestyle='--')

for cap in boxplot['caps']:
    cap.set(color='#8B8B8B', linewidth=1.5)

for median in boxplot['medians']:
    median.set(color='black', linewidth=2)

# Add grids
ax.xaxis.grid(True, linestyle='--', alpha=0.7)
ax.set_axisbelow(True)

# Adjust the layout
plt.tight_layout()

# Display the chart
plt.show()