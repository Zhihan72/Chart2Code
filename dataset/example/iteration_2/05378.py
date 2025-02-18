import matplotlib.pyplot as plt
import numpy as np

# Backstory: City Urbanization and Green Space
# In an effort to promote healthy living and sustainable urban development, various cities have been designated
# as Eco-Urbanization Zones. Each year, these cities report on the allocated green space within urban areas, showcasing
# their continuous efforts to increase urban greenery and improve the environment. The chart below presents
# the green space distribution over the last decade among five leading cities participating in this initiative.

# Years of observation
years = np.arange(2011, 2021)

# Artificial data: Green space (in hectares) designated by different cities each year
green_space = {
    'Green City': np.array([50, 55, 60, 70, 75, 80, 85, 90, 95, 100]),
    'Eco Town': np.array([40, 45, 50, 55, 60, 65, 70, 75, 80, 85]),
    'Nature Ville': np.array([30, 35, 40, 50, 55, 60, 65, 70, 75, 80]),
    'Garden Metropolis': np.array([20, 25, 35, 45, 60, 65, 70, 75, 80, 85]),
    'Oasis Hub': np.array([10, 15, 25, 35, 45, 55, 65, 75, 85, 95])
}

# Colors for each city
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99', '#cccccc']

# Create a stacked area plot
plt.figure(figsize=(12, 8))
plt.stackplot(years, green_space.values(), labels=green_space.keys(), colors=colors, alpha=0.7)

# Add title and labels
plt.title('Green Space Allocation Trends in Eco-Urbanization Zones\n(2011-2020)', fontsize=16, weight='bold', pad=20)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Green Space (in Hectares)', fontsize=14)

# Rotate x-axis labels to prevent overlap
plt.xticks(years, rotation=45)

# Customize the grid for better visibility
plt.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

# Enhance readability by adding tick params
plt.tick_params(axis='both', which='major', labelsize=12)

# Add a legend to identify the cities
plt.legend(title='Cities', title_fontsize=12, fontsize=10, loc='upper left')

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the stacked area chart
plt.show()