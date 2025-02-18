import matplotlib.pyplot as plt
import numpy as np

# Define growth (in centimeters) of different house plants under different light conditions
sunlight = np.array([2, 4, 6, 8, 10, 12, 14, 16, 18, 20])
succulent_growth = np.array([2, 3, 5, 8, 10, 12, 14, 16, 17.5, 18])
fern_growth = np.array([1, 2, 3, 4, 5.5, 6.5, 7, 7.5, 8, 8.5])
pothos_growth = np.array([1, 2, 4, 7, 11, 16, 20, 23, 25, 27])
cactus_growth = np.array([2, 4, 6, 7, 8, 10, 11, 11.5, 12, 12.5])

# Sizes for different subspecies, emphasizing their growth stages
sizes = np.array([50, 70, 90, 110, 130, 150, 170, 190, 210, 230])

# Create a scatter plot for plant growth under sunlight
plt.figure(figsize=(14, 8))

plt.scatter(sunlight, succulent_growth, s=sizes, c='green', alpha=0.6, edgecolor='k', label='Lush')
plt.scatter(sunlight, fern_growth, s=sizes, c='orange', alpha=0.6, edgecolor='k', label='Frond')
plt.scatter(sunlight, pothos_growth, s=sizes, c='blue', alpha=0.6, edgecolor='k', label='Vine')
plt.scatter(sunlight, cactus_growth, s=sizes, c='red', alpha=0.6, edgecolor='k', label='Spine')

# Titles and labels
plt.title('Sun Power on Greenery Rise\nTracked by Days', fontsize=16, fontweight='bold')
plt.xlabel('Luminosity Hours', fontsize=12)
plt.ylabel('Height Climb (cm)', fontsize=12)

# Customizing the legend
plt.legend(title="Species", loc='upper left', fontsize=10)

# Adding grid
plt.grid(True, linestyle='--', alpha=0.7)

# Adding a tight layout to avoid text overlapping
plt.tight_layout()

# Display the plot
plt.show()