import matplotlib.pyplot as plt
import numpy as np

# -------- Backstory ---------
# The "World's Most Popular Ice Cream Flavors" chart explores the popularity of various ice cream flavors across different continents. The data is hypothetical but represents a global survey conducted in 2023. Each continent's favorite flavors are highlighted in a stacked bar chart. Additionally, the growth trend of the top flavor over the last decade is presented in the sub-plot.

# Define continents and flavors
continents = ['North America', 'Europe', 'Asia', 'South America', 'Africa', 'Australia']
flavors = ['Vanilla', 'Chocolate', 'Strawberry', 'Mint', 'Cookie Dough']

# Popularity percentages for each flavor in each continent
# Data is crafted to reflect realistic hypothetical survey results
na_flavors = [35, 25, 15, 12, 13]
eu_flavors = [28, 30, 10, 20, 12]
asia_flavors = [20, 35, 25, 10, 10]
sa_flavors = [25, 20, 30, 10, 15]
africa_flavors = [15, 20, 10, 25, 30]
australia_flavors = [30, 25, 15, 10, 20]

# Compile data
flavor_data = [na_flavors, eu_flavors, asia_flavors, sa_flavors, africa_flavors, australia_flavors]

# Colors for each flavor
colors = ['#f3e5ab', '#8b4513', '#fc5a8d', '#98ff98', '#c0c0c0']

# Setup the main figure with subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))

# Main plot: Stacked bar chart showing flavor popularity by continent
bottoms = np.zeros(len(continents))
for idx, flavor in enumerate(flavors):
    ax1.bar(continents, [data[idx] for data in flavor_data], label=flavor, bottom=bottoms, color=colors[idx], edgecolor='black', alpha=0.7)
    bottoms += [data[idx] for data in flavor_data]

# Add value labels on the bars
for cont_idx, cont_data in enumerate(flavor_data):
    bottom = 0
    for flavor_idx, value in enumerate(cont_data):
        ax1.text(cont_idx, bottom + value / 2, str(value) + '%', va='center', ha='center', color='white', fontweight='bold')
        bottom += value

# Add title and labels
ax1.set_title("World's Most Popular Ice Cream Flavors by Continent (2023)", fontsize=16, fontweight='bold')
ax1.set_xlabel("Continents", fontsize=12)
ax1.set_ylabel("Popularity Percentage (%)", fontsize=12)
ax1.legend(title='Flavors', loc='upper right')

# Customize the grid for better readability
ax1.yaxis.grid(True, linestyle='--', linewidth=0.7, alpha=0.7)

# Sub-plot: Line plot showing the growth of the top flavor (Vanilla) over the last decade
years = np.arange(2013, 2024)  # Last decade
vanilla_growth = [20, 22, 23, 25, 26, 27, 29, 30, 32, 33, 34]  # Hypothetical growth data

ax2.plot(years, vanilla_growth, marker='o', linestyle='-', color='#f3e5ab', linewidth=2, markersize=6, label='Vanilla')

# Add data annotations
for i, growth in enumerate(vanilla_growth):
    ax2.text(years[i], growth + 0.5, f'{growth}%', ha='center', fontsize=10)

# Add title and labels for the subplot
ax2.set_title("Growth of Vanilla Ice Cream Popularity (2013-2023)", fontsize=14, fontweight='bold')
ax2.set_xlabel("Year", fontsize=12)
ax2.set_ylabel("Popularity Percentage (%)", fontsize=12)
ax2.legend(loc='upper left')
ax2.yaxis.grid(True, linestyle='--', linewidth=0.7, alpha=0.7)

# Adjust layout to avoid text overlap and ensure readability
fig.tight_layout()

# Display the plot
plt.show()