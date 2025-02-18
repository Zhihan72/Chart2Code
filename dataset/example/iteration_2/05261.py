import matplotlib.pyplot as plt
import numpy as np

# Backstory: The chart represents a comparison of various attributes among the favorite fruits of different regions.
# The goal is to see how different fruits stack up in terms of sweetness, fiber content, vitamin C, water content, and sugar levels.

# Categories representing different attributes of fruits
categories = ['Sweetness', 'Fiber Content', 'Vitamin C', 'Water Content', 'Sugar Levels']

# Data for fruits in different regions
tropical_scores = [8, 7, 9, 6, 8]
temperate_scores = [6, 8, 7, 7, 6]
mediterranean_scores = [7, 6, 5, 8, 7]
continental_scores = [5, 6, 7, 9, 6]

# Append the first score to the end to close the radar chart
tropical_scores += tropical_scores[:1]
temperate_scores += temperate_scores[:1]
mediterranean_scores += mediterranean_scores[:1]
continental_scores += continental_scores[:1]

# Calculate the angles for each category
num_categories = len(categories)
angles = np.linspace(0, 2 * np.pi, num_categories, endpoint=False).tolist()
angles += angles[:1]  # Ensure the plot closes by repeating the first angle

# Create radar chart
fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))

# Define colors for each region
colors = ['blue', 'green', 'red', 'purple']

# Plot each region's data on the radar chart
ax.plot(angles, tropical_scores, color=colors[0], linewidth=2, linestyle='solid', label='Tropical Fruits')
ax.fill(angles, tropical_scores, color=colors[0], alpha=0.25)

ax.plot(angles, temperate_scores, color=colors[1], linewidth=2, linestyle='solid', label='Temperate Fruits')
ax.fill(angles, temperate_scores, color=colors[1], alpha=0.25)

ax.plot(angles, mediterranean_scores, color=colors[2], linewidth=2, linestyle='solid', label='Mediterranean Fruits')
ax.fill(angles, mediterranean_scores, color=colors[2], alpha=0.25)

ax.plot(angles, continental_scores, color=colors[3], linewidth=2, linestyle='solid', label='Continental Fruits')
ax.fill(angles, continental_scores, color=colors[3], alpha=0.25)

# Add category labels to each spoke
ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, fontsize=12, fontweight='bold', ha='center')

# Add y-tick labels
ax.set_yticklabels([])

# Title and legend with appropriate padding and alignment
plt.title("Fruit Attributes Comparison Across Different Regions", fontsize=16, fontweight='bold', pad=20)
plt.legend(loc='upper right', bbox_to_anchor=(1.1, 1.1), fontsize=10, title='Regions')

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()