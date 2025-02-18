import matplotlib.pyplot as plt
import numpy as np

# Data setup
energy_sources = ['Solar', 'Wind']  # Removed "Hydro", "Geothermal", "Biomass"
energy_contribution = np.array([45, 25])  # Updated accordingly

# Additional details
emission_reduction = [90, 80]  # Updated accordingly

# Define colors for each source
colors = ['#FFD700', '#1f77b4']  # Updated accordingly

# Create the figure and axis objects
fig, ax = plt.subplots(figsize=(14, 8))

# Creating the horizontal bar chart
bars = ax.barh(energy_sources, energy_contribution, color=colors, edgecolor='black')

# Adding a secondary axis for emission reduction
ax2 = ax.twinx()
ax2.plot(energy_sources, emission_reduction, 'o-', color='black', linewidth=2, markersize=10, label='Emission Reduction')

# Adding titles and labels
ax.set_title('Renewable Energy Mix and Emission Reduction\nin EcoTopia (Year 2050)', fontsize=18, fontweight='bold', pad=20)
ax.set_xlabel('Energy Contribution (%)', fontsize=14)
ax.set_ylabel('Renewable Energy Sources', fontsize=14)
ax2.set_ylabel('Emission Reduction (%)', fontsize=14)

# Annotating each bar with the percentage value
for bar, contribution in zip(bars, energy_contribution):
    width = bar.get_width()
    ax.text(width + 1, bar.get_y() + bar.get_height() / 2, f'{width}%', va='center', ha='left', fontsize=12, color='black')

# Customizing the y-axis
ax.set_yticks(np.arange(len(energy_sources)))
ax.set_yticklabels(energy_sources, fontsize=12)
ax.tick_params(axis='y', which='major', pad=10)

# Extending the range of the secondary y-axis to fit the emission reduction percentages better
ax2.set_ylim(0, 100)
ax2.set_yticks(np.arange(0, 110, 10))

# Adding legend
ax.legend(['Energy Contribution'], loc='lower right', fontsize=12)
ax2.legend(loc='upper right', fontsize=12)

# Adding grid to the primary x-axis
ax.xaxis.grid(True, linestyle='--', linewidth=0.7, alpha=0.6)

# Automatically adjust the layout to prevent overlapping
plt.tight_layout()

# Display the plot
plt.show()