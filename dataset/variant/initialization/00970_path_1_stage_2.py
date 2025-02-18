import matplotlib.pyplot as plt
import numpy as np

# Yield data
tomatoes_yield = [45, 50, 55, 47, 52, 60, 58, 54, 49, 53]
lettuce_yield = [30, 28, 32, 25, 31, 29, 27, 30, 28, 35]
carrots_yield = [40, 42, 45, 38, 47, 44, 39, 41, 43, 40]
cucumbers_yield = [20, 22, 19, 23, 21, 18, 24, 22, 20, 25]

# Combine data for plotting
data = [tomatoes_yield, lettuce_yield, carrots_yield, cucumbers_yield]

# Initialize figure and axis
fig, ax = plt.subplots(figsize=(12, 8))

# Create a horizontal box plot
box = ax.boxplot(data, vert=False, patch_artist=True,
                 labels=["Lettuce", "Cucumbers", "Tomatoes", "Carrots"], 
                 flierprops=dict(marker='o', color='red', alpha=0.5),
                 boxprops=dict(color='darkblue', linewidth=1.5),
                 whiskerprops=dict(color='blue', linestyle='--'),
                 capprops=dict(color='blue'),
                 medianprops=dict(color='orange', linewidth=2),
                 notch=True)

# Set shuffled colors for each box
shuffled_colors = ['orange', 'lightcoral', 'lightgreen', 'skyblue']
for patch, color in zip(box['boxes'], shuffled_colors):
    patch.set_facecolor(color)

# Add grid and labels
ax.grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.7)
ax.set_title("Comparison of Vegetable Types\nin City Farming", fontsize=16, weight='bold', pad=20)
ax.set_xlabel("Amount (kg)", fontsize=14)
ax.set_ylabel("Produce Category", fontsize=14)

# Annotate
ax.annotate('Variation Peak\nin Output', xy=(55, 1), xytext=(60, 1.5),
            arrowprops=dict(facecolor='black', shrink=0.05), fontsize=10)

# Adjust layout
plt.tight_layout()

# Show plot
plt.show()