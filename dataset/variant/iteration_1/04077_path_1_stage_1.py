import matplotlib.pyplot as plt
import numpy as np

# Ice cream flavors
flavors = ['Vanilla', 'Chocolate', 'Strawberry', 'Mint', 'Cookie Dough', 'Pistachio']

# Monthly revenue data for each parlor (in thousands of dollars)
parlor_data = {
    'Central Park': [12, 15, 14, 10, 16, 11],
    'Downtown': [-9, -12, -11, -8, -13, -10],
    'Suburban': [10, 11, 9, 7, 12, 8],
    'Beachfront': [-14, -16, -15, -12, -18, -14]
}

# Define colors
flavor_colors = ['#D4A017', '#3E2723', '#E91E63', '#43A047', '#795548', '#A5D6A7']

# Initialize the figure
fig, ax = plt.subplots(figsize=(14, 8))

bar_width = 0.6

# Plot bars for each parlor
for i, (parlor, revenue) in enumerate(parlor_data.items()):
    offset = i * bar_width
    ax.barh(np.arange(len(flavors)) + offset, revenue, color=flavor_colors, 
            edgecolor='black', height=bar_width, label=parlor)

# Set labels and title
ax.set_yticks(np.arange(len(flavors)) + (len(parlor_data) * bar_width) / 2 - bar_width / 2)
ax.set_yticklabels(flavors)
ax.set_xlabel('Monthly Revenue (in thousands of $)', fontsize=12)
ax.set_title('Diverging Monthly Revenue from Ice Cream Flavors', fontsize=16, fontweight='bold')

# Add legend
ax.legend(title='Parlors', fontsize=10, loc='upper left', bbox_to_anchor=(1, 1))

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()