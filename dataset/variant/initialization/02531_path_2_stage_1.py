import matplotlib.pyplot as plt
import numpy as np

# Years and number of tourists data
years = np.arange(2030, 2040)
data = {
    'Planet A': [20, 22, 27, 35, 40, 43, 45, 50, 56, 65],
    'Planet B': [15, 18, 21, 26, 30, 32, 37, 40, 44, 50],
    'Planet C': [10, 12, 15, 19, 23, 28, 31, 35, 38, 42],
    'Planet D': [8, 10, 12, 15, 20, 24, 27, 30, 33, 38],
    'Planet E': [5, 7, 10, 12, 16, 18, 21, 25, 28, 30],
}

# Sorting data for each planet in ascending order of tourists
sorted_data = {planet: np.sort(tourists) for planet, tourists in data.items()}

# Plotting
fig, ax = plt.subplots(figsize=(12, 8))

# Bar width and offsets calculations for grouped bar chart
bar_width = 0.15
x_indexes = np.arange(len(years))
offsets = np.linspace(-0.3, 0.3, len(data))

# Plot each exoplanet's sorted data
colors = ['#FF5733', '#33FFCE', '#335BFF', '#FF33A6', '#FFD700']
for i, (planet, tourists) in enumerate(sorted_data.items()):
    ax.bar(x_indexes + offsets[i], tourists, width=bar_width, label=planet, color=colors[i], alpha=0.8)

# Customize the plot
ax.set_title('Sorted Galactic Tourism Data:\nAscending Order of Tourist Numbers per Year', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Number of Tourists (in thousands)', fontsize=14)
ax.set_xticks(x_indexes)
ax.set_xticklabels(years, rotation=45, fontsize=10)
ax.yaxis.grid(True, linestyle='--', alpha=0.7)
ax.set_axisbelow(True)

# Add legend
ax.legend(title='Exoplanets', title_fontsize='13', fontsize='11', loc='upper left')

# Adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()