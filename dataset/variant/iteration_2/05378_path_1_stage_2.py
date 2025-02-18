import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2011, 2021)

# Removed 'Oasis Hub' from the data table
green_space = {
    'Green City': np.array([50, 55, 60, 70, 75, 80, 85, 90, 95, 100]),
    'Eco Town': np.array([40, 45, 50, 55, 60, 65, 70, 75, 80, 85]),
    'Nature Ville': np.array([30, 35, 40, 50, 55, 60, 65, 70, 75, 80]),
    'Garden Metropolis': np.array([20, 25, 35, 45, 60, 65, 70, 75, 80, 85])
}

# Adjusted the colors array to match the number of cities
colors = ['#66b3ff', '#ffcc99', '#cccccc', '#99ff99']

plt.figure(figsize=(12, 8))
plt.stackplot(years, green_space.values(), labels=green_space.keys(), colors=colors, alpha=0.7)

plt.title('Green Space Allocation Trends in Eco-Urbanization Zones\n(2011-2020)', fontsize=16, weight='bold', pad=20)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Green Space (in Hectares)', fontsize=14)
plt.xticks(years, rotation=45)
plt.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)
plt.tick_params(axis='both', which='major', labelsize=12)
plt.legend(title='Cities', title_fontsize=12, fontsize=10, loc='upper left')
plt.tight_layout()
plt.show()