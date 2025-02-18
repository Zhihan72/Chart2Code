import matplotlib.pyplot as plt
import numpy as np

# Data with shuffled content within each country data group
years = np.arange(2000, 2021)
country_a_adoption = np.array([22, 2, 70, 93, 35, 30, 10, 63, 25, 86, 19, 15, 4, 100, 78, 7, 41, 12, 3, 55, 48])
country_b_adoption = np.array([98, 78, 27, 33, 2.5, 1.5, 6, 67, 4, 95, 12, 8, 100, 15, 90, 1, 57, 18, 40, 22, 48])
country_c_adoption = np.array([94, 100, 90, 68, 9, 17, 47, 6, 57, 1.5, 85, 97, 0.5, 13, 1, 38, 4, 80, 23, 30, 2.5])

# Plotting setup
plt.figure(figsize=(12, 8))

# Plot data with specified colors
plt.plot(years, country_a_adoption, color='purple', marker='o', linewidth=2, markersize=6)
plt.plot(years, country_b_adoption, color='orange', marker='s', linewidth=2, markersize=6)
plt.plot(years, country_c_adoption, color='cyan', marker='^', linewidth=2, markersize=6)

# Hide axis
plt.gca().set_xticklabels([])
plt.gca().set_yticklabels([])

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Show final plot
plt.show()