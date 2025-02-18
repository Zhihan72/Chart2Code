import matplotlib.pyplot as plt
import numpy as np

# Define the data for the bar chart
years = ['2012', '2014', '2016', '2018', '2020', '2022']
energy_sources = ['Solar', 'Wind', 'Hydro', 'Bioenergy']

# Adoption data in percentage (rows: years, columns: energy sources)
adoption_data = np.array([
    [5, 10, 30, 3],   
    [10, 15, 35, 5],  
    [20, 30, 40, 7],  
    [30, 40, 45, 10], 
    [40, 50, 50, 12], 
    [50, 60, 55, 15]  
])

# Shuffled colors
colors = ['#ff7f0e', '#2ca02c', '#9467bd', '#1f77b4']

# Prepare the figure
fig, ax = plt.subplots(figsize=(14, 8))

# Plot each energy source's adoption data with altered styles
bar_width = 0.15
x = np.arange(len(years))
marker_styles = ['o', 's', '^', 'D']  # Added marker styles for visual variety

for idx, source in enumerate(energy_sources):
    ax.bar(x + idx * bar_width, adoption_data[:, idx], width=bar_width, label=source, color=colors[idx])

# Set labels and title
ax.set_xlabel('Years', fontsize=14)
ax.set_ylabel('Adoption Rate (%)', fontsize=14)
ax.set_title('Renewable Energy Adoption Rates (2012-2022)', fontsize=18, fontweight='bold')

# Set x-ticks positions and labels
ax.set_xticks(x + bar_width * (len(energy_sources) - 1) / 2)
ax.set_xticklabels(years)

# Add legend with altered styles
ax.legend(title='Source', fontsize=11, title_fontsize=13, loc='upper left')

# Configure the grid with new line style
ax.grid(True, which='both', linestyle='-', linewidth=0.7, alpha=0.5)

# Annotate bars with values
for idx, source in enumerate(energy_sources):
    for i in range(len(years)):
        ax.text(x[i] + idx * bar_width, adoption_data[i, idx] + 1, str(adoption_data[i, idx]), 
                ha='center', va='bottom', fontstyle='italic')  # Added italic fontstyle for annotations

# Adjust layout
plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)

# Display the plot
plt.show()