import matplotlib.pyplot as plt
import numpy as np

# Data setup
energy_sources = ['Windy', 'Sunshine']
energy_contribution = np.array([45, 25])

# Set a single consistent color for all bars
color = '#1f77b4'

# Create the figure and axis objects
fig, ax = plt.subplots(figsize=(14, 8))

# Creating the vertical bar chart with a consistent color
bars = ax.bar(energy_sources, energy_contribution, color=color, edgecolor='black')

# Adding titles and labels
ax.set_title('Future Power Split in GreenVille (Year 2050)', fontsize=18, fontweight='bold', pad=20)
ax.set_xlabel('Power Sources', fontsize=14)
ax.set_ylabel('Contribution (%)', fontsize=14)

# Annotating each bar
for bar, contribution in zip(bars, energy_contribution):
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width() / 2, height + 1, f'{height}%', va='bottom', ha='center', fontsize=12, color='black')

# Customizing the x-axis
ax.set_xticks(np.arange(len(energy_sources)))
ax.set_xticklabels(energy_sources, fontsize=12)
ax.tick_params(axis='x', which='major', pad=10)

# Adding grid to the y-axis
ax.yaxis.grid(True, linestyle='--', linewidth=0.7, alpha=0.6)

# Automatically adjust the layout to prevent overlapping
plt.tight_layout()

# Display the plot
plt.show()