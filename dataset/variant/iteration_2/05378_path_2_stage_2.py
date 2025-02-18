import matplotlib.pyplot as plt
import numpy as np

# Years of observation
years = np.arange(2011, 2021)

# Artificial data: Green space (in hectares) designated by different cities each year
green_space = {
    'Eco Town': np.array([40, 45, 50, 55, 60, 65, 70, 75, 80, 85]),
    'Nature Ville': np.array([30, 35, 40, 50, 55, 60, 65, 70, 75, 80]),
    'Garden Metropolis': np.array([20, 25, 35, 45, 60, 65, 70, 75, 80, 85]),
    'Oasis Hub': np.array([10, 15, 25, 35, 45, 55, 65, 75, 85, 95])
    # Removed 'Green City'
}

colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99']

plt.figure(figsize=(12, 8))
plt.stackplot(years, green_space.values(), labels=green_space.keys(), colors=colors, alpha=0.7)

plt.title('Urban Greenery Expansion Tracks\n(2011-2020)', fontsize=16, weight='bold', pad=20)
plt.xlabel('Observation Year', fontsize=14)
plt.ylabel('Green Area (ha)', fontsize=14)

plt.xticks(years, rotation=45)
plt.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)
plt.tick_params(axis='both', which='major', labelsize=12)

plt.legend(title='Participating Cities', title_fontsize=12, fontsize=10, loc='upper left')

plt.tight_layout()
plt.show()