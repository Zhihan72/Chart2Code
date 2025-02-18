import matplotlib.pyplot as plt
import numpy as np

# **Backstory: Monthly Revenues of Different Ice Cream Flavors at Ice Cream Parlors**
# This visualization presents monthly revenue data for different ice cream flavors at multiple parlors.
# It's intended to offer insights into flavor popularity and seasonal trends across locations.

# Define the ice cream flavors and parlors
flavors = ['Vanilla', 'Chocolate', 'Strawberry', 'Mint', 'Cookie Dough', 'Pistachio']
parlors = ['Central Park', 'Downtown', 'Suburban', 'Beachfront']

# Monthly revenue data for each parlor (in thousands of dollars)
revenue_data = {
    'Central Park': [12, 15, 14, 10, 16, 11],
    'Downtown': [9, 12, 11, 8, 13, 10],
    'Suburban': [10, 11, 9, 7, 12, 8],
    'Beachfront': [14, 16, 15, 12, 18, 14]
}

# Define colors
flavor_colors = ['#D4A017', '#3E2723', '#E91E63', '#43A047', '#795548', '#A5D6A7']

# Initialize the figure with multiple subplots
fig, ax = plt.subplots(figsize=(14, 8))

# Width of a single bar
bar_width = 0.18

# Plot bars for each parlor
for i, parlor in enumerate(parlors):
    # Calculate positions for each set of bars
    positions = np.arange(len(flavors)) + i * bar_width
    ax.bar(positions, revenue_data[parlor], width=bar_width, color=flavor_colors, label=parlor, edgecolor='black')

# Set labels and title
ax.set_xlabel('Ice Cream Flavors', fontsize=12)
ax.set_ylabel('Monthly Revenue (in thousands of $)', fontsize=12)
ax.set_title('Monthly Revenue from Ice Cream Flavors Across Different Parlors', fontsize=16, fontweight='bold', pad=15)

# Set x-ticks to be in the middle of grouped bars
ax.set_xticks(np.arange(len(flavors)) + bar_width * 1.5)
ax.set_xticklabels(flavors, rotation=45, ha='right')

# Add grid for easier visualization
ax.yaxis.grid(True, linestyle='--', alpha=0.7)

# Add data labels on top of each bar
for i, parlor in enumerate(parlors):
    positions = np.arange(len(flavors)) + i * bar_width
    for j, value in enumerate(revenue_data[parlor]):
        ax.text(positions[j], value + 0.3, str(value), ha='center', va='bottom', fontsize=10, color='black')

# Add legend
ax.legend(title='Parlors', fontsize=10, loc='upper left', bbox_to_anchor=(1, 1))

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()