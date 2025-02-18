import matplotlib.pyplot as plt
import numpy as np

# Backstory: Tracking the Population Growth in Several Fictional Cities Over a Decade
# The chart will depict the population trends of five different fictional cities from 2010 to 2020.

# Years from 2010 to 2020
years = np.arange(2010, 2021)

# Population data for each fictional city (in thousands)
city_a = [150, 155, 160, 165, 170, 175, 180, 185, 190, 195, 200]
city_b = [100, 105, 110, 120, 130, 140, 150, 160, 155, 150, 145]
city_c = [80, 82, 85, 88, 90, 92, 95, 98, 105, 110, 120]
city_d = [200, 205, 215, 230, 240, 245, 260, 270, 275, 280, 290]
city_e = [60, 65, 70, 80, 90, 95, 100, 110, 120, 130, 140]

# Create the plot
fig, ax = plt.subplots(figsize=(14, 8))

# Plot line charts for each city
ax.plot(years, city_a, marker='o', linestyle='-', linewidth=2, label='City A', color='#1f77b4')
ax.plot(years, city_b, marker='s', linestyle='--', linewidth=2, label='City B', color='#ff7f0e')
ax.plot(years, city_c, marker='^', linestyle='-.', linewidth=2, label='City C', color='#2ca02c')
ax.plot(years, city_d, marker='d', linestyle=':', linewidth=2, label='City D', color='#d62728')
ax.plot(years, city_e, marker='x', linestyle='-', linewidth=2, label='City E', color='#9467bd')

# Title and labels
ax.set_title('Population Growth in Fictional Cities (2010-2020)', fontsize=18, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=15)
ax.set_ylabel('Population (in thousands)', fontsize=15)

# Customize y-ticks
ax.set_yticks(range(50, 301, 25))

# Customize x-ticks
ax.set_xticks(years)
ax.tick_params(axis='x', rotation=45)

# Add grid 
ax.grid(True, linestyle='--', alpha=0.6)

# Add legend
ax.legend(title='Fictional Cities', fontsize=12, loc='upper left')

# Automatically adjust layout
plt.tight_layout()

# Show plot
plt.show()