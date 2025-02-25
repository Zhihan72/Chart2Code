import numpy as np
import matplotlib.pyplot as plt

# Manually shuffled data
cities = ['CityA', 'CityB', 'CityC', 'CityD', 'CityE', 'CityF', 'CityG', 'CityH', 'CityI', 'CityJ']
populations = [3000000, 50000, 2000000, 150000, 450000, 1200000, 600000, 850000, 1500000, 300000]  # population shuffled
park_counts = [20, 300, 350, 35, 75, 200, 90, 150, 250, 50]  # number of parks shuffled

# Initialize figure and axis
fig, ax = plt.subplots(figsize=(12, 8))

# Add scatter plot
scatter = ax.scatter(populations, park_counts, s=populations, alpha=0.6, edgecolors='w', c=park_counts, cmap='plasma', label='Cities')

# Add annotations for each city
for i, city in enumerate(cities):
    ax.annotate(city, (populations[i], park_counts[i]), fontsize=10, ha='right')

# Adding a regression line
coefficients = np.polyfit(populations, park_counts, 1)
polynomial = np.poly1d(coefficients)
trendline = polynomial(populations)
ax.plot(populations, trendline, color='red', linestyle='--', linewidth=1.5, label='Trendline')

# Title and labels
ax.set_title('City Size vs. Green Park Availability: A Correlation Study', fontsize=14, fontweight='bold')
ax.set_xlabel('City Population', fontsize=12)
ax.set_ylabel('Number of Green Parks', fontsize=12)

# Add legends and grid
ax.legend()
ax.grid(True, linestyle='--', alpha=0.7)

# Improve layout
plt.tight_layout()

# Show plot
plt.show()