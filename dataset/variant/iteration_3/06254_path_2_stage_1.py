import matplotlib.pyplot as plt
import numpy as np

# Cities (for simplicity, indexed as 1, 2, 3, ..., 10)
cities = np.arange(1, 11)

# Urban green spaces per capita in square meters
green_space_per_capita = np.array([15, 30, 25, 40, 50, 32, 22, 60, 45, 35])

# Average happiness index (scale from 1 to 10)
happiness_index = np.array([6.0, 7.5, 7.0, 8.0, 9.0, 7.2, 6.5, 9.5, 8.2, 7.8])

# Create scatter plot
plt.figure(figsize=(12, 7))
plt.scatter(green_space_per_capita, happiness_index, color='royalblue', edgecolors='black', s=150, alpha=0.7)

# Annotations for each city
for i, city in enumerate(cities):
    plt.annotate(f'City {city}', 
                 (green_space_per_capita[i], happiness_index[i]),
                 textcoords="offset points",
                 xytext=(5,5),
                 ha='center', fontsize=10, color='black')

# Titles and labels
plt.title("Correlation Between Urban Green Space and Happiness Index\n Analysis of Various Global Cities", fontsize=16, fontweight='bold')
plt.xlabel("Urban Green Space per Capita (sqm)", fontsize=13)
plt.ylabel("Average Happiness Index (scale 1-10)", fontsize=13)

# Grid configuration to improve readability
plt.grid(True, linestyle='--', alpha=0.6)

# Add trend line (linear regression)
m, b = np.polyfit(green_space_per_capita, happiness_index, 1)
plt.plot(green_space_per_capita, m * green_space_per_capita + b, color='crimson', linestyle='--', linewidth=2, label='Trend Line')

# Add legend
plt.legend(loc='lower right')

# Automatically adjust layout to prevent text overlapping
plt.tight_layout()

# Display the plot
plt.show()