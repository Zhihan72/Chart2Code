import matplotlib.pyplot as plt
import numpy as np

# Data setup
energy_sources = ['Solar', 'Wind']
energy_contribution = np.array([45, 25])

# Define colors for each source
colors = ['#FFD700', '#1f77b4']

# Create the figure and axis objects
fig, ax = plt.subplots(figsize=(14, 8))

# Creating the vertical bar chart
bars = ax.bar(energy_sources, energy_contribution, color=colors, edgecolor='black')

# Adding titles and labels
ax.set_title('Renewable Energy Mix in EcoTopia (Year 2050)', fontsize=18, fontweight='bold', pad=20)
ax.set_xlabel('Renewable Energy Sources', fontsize=14)
ax.set_ylabel('Energy Contribution (%)', fontsize=14)

# Annotating each bar with the percentage value
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