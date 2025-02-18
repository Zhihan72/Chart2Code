import matplotlib.pyplot as plt

# Yield data
tomatoes_yield = [45, 50, 55, 47, 52, 60, 58, 54, 49, 53]
lettuce_yield = [30, 28, 32, 25, 31, 29, 27, 30, 28, 35]
carrots_yield = [40, 42, 45, 38, 47, 44, 39, 41, 43, 40]

# Combine data for plotting
data = [tomatoes_yield, lettuce_yield, carrots_yield]

# Initialize figure and axis
fig, ax = plt.subplots(figsize=(12, 8))

# Create a vertical box plot for a single group
box = ax.boxplot([item for sublist in data for item in sublist], vert=True, patch_artist=True,
                 flierprops=dict(marker='o', color='red', alpha=0.5),
                 notch=True)

# Set color for the single box
box['boxes'][0].set_facecolor('lightgrey')

# Adjust layout
plt.tight_layout()

# Show plot
plt.show()