import numpy as np
import matplotlib.pyplot as plt
from math import pi

# Define the categories for ice cream shop attributes
categories = ['Flavor Variety', 'Affordability', 'Customer Service', 'Ambience', 'Quality']
N = len(categories)

# Define the scores for each ice cream shop
shopA_scores = [8, 6, 9, 7, 8]
shopB_scores = [7, 8, 8, 6, 9]
shopC_scores = [9, 7, 7, 8, 7]
shopD_scores = [6, 9, 8, 7, 8]

# Calculate angles for the radar chart, including closing point to complete the loop
angles = np.linspace(0, 2 * pi, N, endpoint=False).tolist()
angles += angles[:1]

# Extend data for each shop to close the radar plot loop
shopA_scores += shopA_scores[:1]
shopB_scores += shopB_scores[:1]
shopC_scores += shopC_scores[:1]
shopD_scores += shopD_scores[:1]

# Function to plot each shop on the radar chart
def plot_radar(ax, data, label, color):
    ax.fill(angles, data, color=color, alpha=0.25)
    ax.plot(angles, data, color=color, linewidth=2, label=label)

# Initialize the radar chart
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Plot each shop using different colors
plot_radar(ax, shopA_scores, 'Ice Cream Delight', '#1f77b4')
plot_radar(ax, shopB_scores, 'Frozen Paradise', '#ff7f0e')
plot_radar(ax, shopC_scores, 'Sweet Treat Haven', '#2ca02c')
plot_radar(ax, shopD_scores, 'Chill & Thrill', '#d62728')

# Add category labels
plt.xticks(angles[:-1], categories, color='grey', size=10)

# Set radial limits
ax.set_ylim(0, 10)

# Title and Legend
plt.title("Battle of the Ice Cream Shops:\nA Comprehensive Attribute Comparison", size=15, color='black', y=1.1)
plt.legend(loc='upper right', bbox_to_anchor=(1.15, 1.15), fontsize=10, frameon=False, title="Shops")

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()