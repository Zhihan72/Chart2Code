import matplotlib.pyplot as plt
import numpy as np

# Data
years = np.arange(2000, 2021)
country_a_adoption = np.array([2, 3, 4, 7, 10, 12, 15, 19, 22, 25, 30, 35, 41, 48, 55, 63, 70, 78, 86, 93, 100])
country_b_adoption = np.array([1, 1.5, 2.5, 4, 6, 8, 12, 15, 18, 22, 27, 33, 40, 48, 57, 67, 78, 90, 95, 98, 100])
country_c_adoption = np.array([0.5, 1, 1.5, 2.5, 4, 6, 9, 13, 17, 23, 30, 38, 47, 57, 68, 80, 85, 90, 94, 97, 100])

# Plotting setup
plt.figure(figsize=(12, 8))

# Plot data with new colors
plt.plot(years, country_a_adoption, color='purple', marker='o', linewidth=2, markersize=6)  # changed from 'blue' to 'purple'
plt.plot(years, country_b_adoption, color='orange', marker='s', linewidth=2, markersize=6)  # changed from 'green' to 'orange'
plt.plot(years, country_c_adoption, color='cyan', marker='^', linewidth=2, markersize=6)    # changed from 'red' to 'cyan'

# Hide axis
plt.gca().set_xticklabels([])
plt.gca().set_yticklabels([])

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Show final plot
plt.show()