import matplotlib.pyplot as plt
import numpy as np

# Planetary bodies
planets = ['Mercury', 'Venus', 'Earth', 'Moon', 'Mars', 'Europa', 'Titan']

# Artificial water content data (in percentage)
water_content_data = [
    [0.1, 0.1, 0.2, 0.2, 0.1],
    [0.0, 0.0, 0.1, 0.1, 0.0],
    [70.0, 68.0, 72.0, 71.0, 69.0],
    [0.1, 0.2, 0.1, 0.3, 0.2],
    [2.0, 2.1, 2.2, 2.0, 2.1],
    [52.5, 53.0, 52.0, 53.5, 52.3],
    [40.0, 41.0, 40.5, 41.5, 40.3]
]

# Create a figure and axis
fig, ax = plt.subplots(figsize=(12, 8))

# Plot the horizontal box plot
box = ax.boxplot(water_content_data, patch_artist=True, notch=False, vert=False, labels=planets)

# Customize box colors
colors = ['#FFA07A', '#FF4500', '#1E90FF', '#FFD700', '#FF6347', '#98FB98', '#BA55D3']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

# Adding median line color
plt.setp(box['medians'], color='black')

# Set title and labels
ax.set_title("Astrobiology Research: Soil Water Content Evaluation\nAcross Various Planetary Bodies in the Solar System", 
             fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Water Content (%)", fontsize=12)
ax.set_ylabel("Planetary Bodies", fontsize=12)

# Enhance gridlines for readability
ax.grid(True, linestyle='--', alpha=0.5, which='both', linewidth=0.7)

# Annotate with additional information
for i, (planet, data) in enumerate(zip(planets, water_content_data)):
    max_val = max(data)
    ax.text(max_val + 3, i + 1, f'Max: {max_val:.1f}%', va='center', fontsize=10, color=colors[i])

# Automatically adjust layout
plt.tight_layout()

# Show the plot
plt.show()