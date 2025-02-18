import matplotlib.pyplot as plt
import numpy as np

# Define the years for the x-axis
years = np.arange(2000, 2021)

# Data on deforestation in million hectares
deforestation = np.array([15, 14.8, 14.5, 14.1, 13.8, 13.6, 13.5, 13.2, 13.0, 12.8, 12.5, 12.5, 12.3, 12.0, 11.8, 11.5, 11.3, 11.0, 10.8, 10.5, 10.3])

# Data on reforestation in million hectares
reforestation = np.array([1, 1.2, 1.5, 1.8, 2.0, 2.3, 2.6, 3.0, 3.3, 3.7, 4.1, 4.5, 5.0, 5.5, 6.0, 6.5, 7.1, 7.6, 8.2, 8.8, 9.5])

# Total forest coverage remaining (initial value considered 100 million hectares and reducing due to net deforestation)
initial_forest_coverage = 100
net_deforestation = deforestation - reforestation
forest_coverage = initial_forest_coverage - np.cumsum(net_deforestation)

# Stacking the data for area's chart representation 
data_stack = np.vstack([deforestation, reforestation])

# Creating the figure and the subplot
fig, ax = plt.subplots(figsize=(12, 8))

# Plotting the stacked area chart with shuffled colors
ax.stackplot(years, data_stack, labels=['Deforestation', 'Reforestation'], colors=['#228B22', '#8B0000'], alpha=0.7)

# Adding a secondary axis to display forest coverage
ax2 = ax.twinx()
ax2.plot(years, forest_coverage, label='Total Forest Coverage', color='navy', linestyle='-', linewidth=2)

# Title and labels
ax.set_title("Global Forest Coverage and Reforestation Efforts (2000-2020)", fontsize=18, fontweight='bold')
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Area (Million Hectares)', fontsize=14)
ax2.set_ylabel('Global Forest Coverage (Million Hectares)', fontsize=14, color='navy')

# X-axis ticks and grid
ax.set_xticks(years)
ax.set_xticklabels(years, rotation=45, ha='right')
ax.grid(visible=True, which='major', linestyle='--', linewidth=0.5, color='grey', alpha=0.7)
ax.minorticks_on()
ax.grid(visible=True, which='minor', linestyle=':', linewidth=0.5, color='grey', alpha=0.5)

# Adding legends
ax.legend(loc='upper left', title='Forest Data')
ax2.legend(loc='upper right')

# Annotating significant points
ax.annotate('Intensified Global Efforts', xy=(2010, 3.7), xytext=(2005, 10),
            arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=12, backgroundcolor='w')

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()