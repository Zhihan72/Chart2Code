import matplotlib.pyplot as plt
import numpy as np

# Backstory: We are visualizing the adoption rates of different renewable energy sources over the past decade.

# Define the data for the bar chart
years = ['2012', '2014', '2016', '2018', '2020', '2022']
energy_sources = ['Solar', 'Wind', 'Hydro', 'Geothermal', 'Bioenergy']

# Adoption data in percentage (rows: years, columns: energy sources)
adoption_data = np.array([
    [5, 10, 30, 5, 3],   # 2012
    [10, 15, 35, 6, 5],  # 2014
    [20, 30, 40, 7, 7],  # 2016
    [30, 40, 45, 8, 10], # 2018
    [40, 50, 50, 9, 12], # 2020
    [50, 60, 55, 10, 15] # 2022
])

# Prepare the figure
fig, ax = plt.subplots(figsize=(14, 8))

# Plot each energy source's adoption data
bar_width = 0.15  # Width of the bars
x = np.arange(len(years))

for idx, source in enumerate(energy_sources):
    ax.bar(x + idx * bar_width, adoption_data[:, idx], width=bar_width, label=source)

# Set axis labels and title
ax.set_xlabel('Years', fontsize=12, labelpad=10)
ax.set_ylabel('Adoption Rate (%)', fontsize=12, labelpad=10)
ax.set_title('Adoption Rates of Renewable Energy Sources (2012-2022)', fontsize=16, fontweight='bold', pad=20)

# Set x-ticks positions and labels
ax.set_xticks(x + bar_width * (len(energy_sources) - 1) / 2)
ax.set_xticklabels(years)

# Add legend and grid
ax.legend(title='Energy Source', fontsize=10, title_fontsize=12)
ax.grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.7)

# Annotate bars with their respective values
for idx, source in enumerate(energy_sources):
    for i in range(len(years)):
        ax.text(x[i] + idx * bar_width, adoption_data[i, idx] + 1, str(adoption_data[i, idx]), ha='center', va='bottom')

# Adjust layout to prevent overlap and ensure clarity
plt.tight_layout()

# Display the plot
plt.show()