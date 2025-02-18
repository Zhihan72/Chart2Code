import matplotlib.pyplot as plt
import numpy as np

# Data
countries = ['USA', 'China', 'Germany', 'Brazil', 'India', 'UK', 'France', 'Australia', 'Canada', 'Japan']
urban_parks = np.array([1200, 3000, 900, 700, 450, 1100, 950, 800, 770, 1300])

# Sort data by number of urban parks in descending order
sorted_indices = np.argsort(-urban_parks)
sorted_countries = [countries[i] for i in sorted_indices]
sorted_urban_parks = urban_parks[sorted_indices]

# Plot
plt.figure(figsize=(14, 8))
plt.bar(sorted_countries, sorted_urban_parks, color='skyblue')

# Title and labels
plt.title('Number of Urban Parks in Various Countries (Sorted)', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Country', fontsize=14)
plt.ylabel('Number of Urban Parks', fontsize=14)

# Enhancements
plt.xticks(rotation=45, fontsize=12)
plt.yticks(fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Display the plot
plt.tight_layout()
plt.show()