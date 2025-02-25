import numpy as np
import matplotlib.pyplot as plt

# Create modified data by removing 'Village4'
cities = ['Town1', 'District2', 'Metropolis3', 'Capital5', 'Borough6', 'Hamlet7', 'Region8', 'Locality9', 'Urban10']
populations = [50000, 150000, 300000, 600000, 850000, 1200000, 1500000, 2000000, 3000000]
park_counts = [20, 35, 50, 90, 150, 200, 250, 300, 350]

# Initialize figure and axis
fig, ax = plt.subplots(figsize=(12, 8))

# Add scatter plot
scatter = ax.scatter(populations, park_counts, s=populations, alpha=0.6, edgecolors='w', c=park_counts, cmap='viridis', label='Localities')

# Add annotations for each city
for i, city in enumerate(cities):
    ax.annotate(city, (populations[i], park_counts[i]), fontsize=10, ha='right')

# Adding a regression line
coefficients = np.polyfit(populations, park_counts, 1)
polynomial = np.poly1d(coefficients)
trendline = polynomial(populations)
ax.plot(populations, trendline, color='red', linestyle='--', linewidth=1.5, label='Approximation Line')

# Title and labels
ax.set_title('Urban Magnitude vs. Park Proliferation: An Analytical View', fontsize=14, fontweight='bold')
ax.set_xlabel('Human Aggregation Size', fontsize=12)
ax.set_ylabel('Count of Green Retreats', fontsize=12)

# Add legends and grid
ax.legend()
ax.grid(True, linestyle='--', alpha=0.7)

# Improve layout
plt.tight_layout()

# Show plot
plt.show()