import matplotlib.pyplot as plt
import numpy as np

# Data
countries = ['USA', 'China', 'Germany', 'Brazil', 'India', 'UK', 'France', 'Australia', 'Canada', 'Japan', 'Russia', 'Italy']
urban_parks = np.array([1200, 3000, 900, 700, 450, 1100, 950, 800, 770, 1300, 920, 810])

# Sort data by number of urban parks in descending order
sorted_indices = np.argsort(-urban_parks)
sorted_countries = [countries[i] for i in sorted_indices]
sorted_urban_parks = urban_parks[sorted_indices]

# New set of colors for the bars
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd',
          '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf',
          '#aec7e8', '#ffbb78']

# Plot with new color scheme
plt.figure(figsize=(14, 8))
plt.bar(sorted_countries, sorted_urban_parks, color=colors, edgecolor='purple', hatch='/')

# Enhancements with manual stylistic elements
plt.xticks(rotation=30, fontsize=14)
plt.yticks(fontsize=10)
plt.grid(axis='y', linestyle='-.', alpha=0.5, color='gray')
plt.axhline(y=1000, color='r', linestyle=':', linewidth=2)
plt.legend(['Urban Parks'], loc='upper right', frameon=False)

# Display the plot
plt.tight_layout()
plt.show()