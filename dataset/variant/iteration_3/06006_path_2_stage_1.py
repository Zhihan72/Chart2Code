import matplotlib.pyplot as plt
import numpy as np

# Data Creation:
years = np.arange(2010, 2031)
solar_growth = [1, 2, 3, 5, 7, 10, 14, 19, 25, 30, 35, 40, 45, 48, 52, 56, 60, 65, 70, 75, 80]
wind_growth = [2, 3, 5, 8, 11, 15, 20, 25, 30, 36, 42, 49, 55, 61, 68, 75, 82, 90, 97, 104, 110]
hydro_growth = [5, 6, 7, 8, 10, 12, 15, 18, 22, 26, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80]

# Plotting:
plt.figure(figsize=(14, 8))

# Plot Solar Energy Growth
plt.plot(years, solar_growth, color='#FFA500', marker='o', linewidth=2, linestyle='-')

# Plot Wind Energy Growth
plt.plot(years, wind_growth, color='#1E90FF', marker='^', linewidth=2, linestyle='--')

# Plot Hydro Energy Growth
plt.plot(years, hydro_growth, color='#00FF00', marker='s', linewidth=2, linestyle='-.')

# Customize grid and ticks
plt.grid(True, linestyle='--', alpha=0.6)
plt.xticks(years[::2], rotation=45)
plt.yticks(np.arange(0, 121, 10))

# Adjust layout to avoid overlap
plt.tight_layout()

# Show plot
plt.show()