import matplotlib.pyplot as plt
import numpy as np

# Backstory: Population dynamics in a fictitious continent, Elvarna, over three decades.
# We are analyzing the population growth in six major cities over the years.

# Data: Population in millions over three decades for six cities in Elvarna
cities = ['Lunaris', 'Selene', 'Aurora', 'Eldoria', 'Nyx', 'Solara']
years = ['1990', '2000', '2010', '2020']

# Population data for each city across the years
population_data = {
    'Lunaris': [1.2, 1.5, 1.7, 2.0],
    'Selene': [0.8, 1.0, 1.3, 1.8],
    'Aurora': [1.7, 2.0, 2.2, 2.5],
    'Eldoria': [0.9, 1.1, 1.4, 1.6],
    'Nyx': [1.1, 1.3, 1.6, 2.1],
    'Solara': [1.4, 1.6, 1.9, 2.3]
}

# Colors for each city
colors = ['darkblue', 'teal', 'purple', 'darkgreen', 'red', 'gold']

# Create the plot
fig, ax = plt.subplots(figsize=(14, 8))
bar_width = 0.15  # Width of the bars

# Generate the bar positions for each city
bar_positions = np.arange(len(years))

# Plotting data for each city as groups
for i, city in enumerate(cities):
    ax.bar(
        bar_positions + i * bar_width,
        population_data[city], 
        width=bar_width,
        color=colors[i],
        edgecolor='black',
        label=city,
        alpha=0.8
    )

# Annotation for the data
for i, city in enumerate(cities):
    for j, pop in enumerate(population_data[city]):
        ax.text(
            bar_positions[j] + i * bar_width,
            pop + 0.05,
            f'{pop:.1f}',
            ha='center',
            va='bottom',
            fontsize=10,
            fontweight='bold',
            color='black'
        )

# Titles and Labels
ax.set_title('Population Growth in Major Cities of Elvarna (1990-2020)', fontsize=18, fontweight='bold', pad=20)
ax.set_xlabel('Years', fontsize=14)
ax.set_ylabel('Population (in millions)', fontsize=14)
ax.set_xticks(bar_positions + bar_width * (len(cities) - 1) / 2)
ax.set_xticklabels(years, fontsize=12)
ax.legend(title='Cities', title_fontsize='13', fontsize=11, loc='upper left', bbox_to_anchor=(1, 1))

# Customize the grid
ax.grid(True, linestyle='--', alpha=0.6)

# Make layout adjustments to avoid overlap
plt.tight_layout()

# Display the plot
plt.show()