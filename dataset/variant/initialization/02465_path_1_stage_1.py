import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Patch

# Define the years from 2025 to 2050
years = np.arange(2025, 2051)

# Altered data representing millions of packages delivered by drones per year per continent
asia = np.array([22.0, 13.5, 4.0, 48.5, 105.0, 58.0, 0.5, 135.0, 150.0, 6.5, 1.2, 27.0, 260.0, 68.5, 9.3, 33.0, 17.5, 92.5, 170.0, 190.0, 210.0, 80.0, 40.0, 27.0, 235.0, 120.0])
europe = np.array([ 21.5, 127.0,  64.0,   4.0,  36.5, 102.0,   1.5,  91.0,  56.0,  72.5,   0.3,  49.0,  81.5,  11.0,  38.5,   2.5,   6.0,  155.5,  14.0,  114.0,  140.5,  31.0,   8.5,  26.0,  42.5,  17.5])
north_america = np.array([ 1.0,  38.5,  6.0, 158.5,  51.0, 129.0,   3.0,  66.0,  93.0, 104.0,  12.5,  66.0,   0.4,  38.5,  44.5,  74.5,   4.8,  33.0,   9.7,  11.0,  15.8, 116.0,  19.5, 143.5,  23.5,  83.5])
africa = np.array([43.0, 0.5, 11.0, 0.1, 5.3, 3.3, 6.5, 15.0, 4.2, 13.0, 38.5, 23.0, 30.0, 1.8, 20.0, 26.5, 17.5, 9.5, 54.5, 1.2, 8.0, 2.5, 0.8, 34.0, 1.8, 0.3])
south_america = np.array([97.5, 45.5, 9.3, 1.3, 24.5, 7.3, 20.5, 34.0, 14.0, 2.0, 76.0, 59.0, 5.6, 39.5, 29.0, 17.0, 110.0, 52.0, 3.0, 67.0, 86.0, 11.5, 0.5, 0.2, 4.2, 1.3])

# Create stacked area plot
fig, ax1 = plt.subplots(figsize=(14, 8))

# Apply a gradient effect by using color interpolation for each region
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']
# Stacking the areas with gradients
ax1.stackplot(years, asia, europe, north_america, africa, south_america, labels=['Asia', 'Europe', 'North America', 'Africa', 'South America'], colors=colors, alpha=0.85)

# Add title, labels, and legend
ax1.set_title("Global Drone Delivery Usage:\nTrends Across Continents (2025-2050)", fontsize=18, fontweight='bold')
ax1.set_xlabel('Year', fontsize=14)
ax1.set_ylabel('Millions of Packages Delivered', fontsize=14)
ax1.legend(loc='upper left', fontsize=12, bbox_to_anchor=(1.02, 1))
ax1.grid(True, linestyle='--', alpha=0.5)

# Enhancing x-axis with year labels
ax1.set_xticks(np.arange(2025, 2051, 5))
ax1.tick_params(axis='x', rotation=45)

# Emphasize significant milestones with annotations
ax1.annotate('Regulatory Breakthroughs in Asia', xy=(2032, 22), xytext=(2035, 60),
             arrowprops=dict(facecolor='black', shrink=0.05), fontsize=10, color='black')
ax1.annotate('North America Expansion', xy=(2040, 33), xytext=(2042, 80),
             arrowprops=dict(facecolor='black', shrink=0.05), fontsize=10, color='black')

# Secondary Y-axis for percentage growth rate
ax2 = ax1.twinx()
growth_rate = ((asia + europe + north_america + africa + south_america) / 
               (asia[0] + europe[0] + north_america[0] + africa[0] + south_america[0]) - 1) * 100
ax2.plot(years, growth_rate, 'k--', label='Global Growth Rate (%)')
ax2.set_ylabel('Growth Rate (%)', fontsize=14)
ax2.yaxis.label.set_color('black')
ax2.spines['right'].set_color('black')
ax2.tick_params(axis='y', colors='black')
ax2.legend(loc='upper right', fontsize=12)

# Display grid and adjust layout
plt.grid(which='both', linestyle=':', linewidth='0.5', color='gray')
plt.tight_layout()

# Display the plot
plt.show()