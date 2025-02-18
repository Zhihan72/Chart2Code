import matplotlib.pyplot as plt
import numpy as np

# Backstory:
# This scatter plot shows the relationship between the number of urban parks in various countries and the level of urbanization (percentage of the population living in urban areas).
# We aim to illustrate how different levels of urbanization influence the infrastructural and social push towards creating urban parks.

# Contextual Data
countries = ['USA', 'China', 'Germany', 'Brazil', 'India', 'UK', 'France', 'Australia', 'Canada', 'Japan']
urban_parks = np.array([1200, 3000, 900, 700, 450, 1100, 950, 800, 770, 1300])
urbanization_level = np.array([81, 64, 77, 86, 34, 84, 81, 90, 81, 91])

# Calculate average area of urban parks (hypothetical data based on urban parks count)
average_park_area = urban_parks / 10 + np.random.randint(1, 50, size=len(urban_parks))

# Create a figure with scatter plot and additional information
fig, ax = plt.subplots(figsize=(14, 8))

# Scatter plot
scatter = ax.scatter(urbanization_level, urban_parks, s=average_park_area, c=average_park_area, cmap='coolwarm', alpha=0.6, edgecolor='black')

# Title and labels
ax.set_title('Urban Parks vs. Urbanization Level in Various Countries', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Urbanization Level (%)', fontsize=14)
ax.set_ylabel('Number of Urban Parks', fontsize=14)

# Adding a color bar
cbar = fig.colorbar(scatter, ax=ax)
cbar.set_label('Average Park Area (hectares)', fontsize=12, fontweight='bold')

# Annotate each point with the country name
for i, country in enumerate(countries):
    ax.annotate(country, (urbanization_level[i], urban_parks[i]), fontsize=10, ha='right', va='bottom', color='black')

# Enhancements
ax.grid(True, linestyle='--', alpha=0.7)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
ax.set_xlim(30, 95)  # Adjust limits for better view
ax.set_ylim(400, 3200)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()