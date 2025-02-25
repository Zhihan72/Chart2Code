import matplotlib.pyplot as plt
import numpy as np

# Years from the start of the mission
years = np.arange(0, 11)  # 0 to 10 years

# Distance traveled by each spacecraft (in million kilometers)
voyager_1 = np.array([0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 55])
voyager_2 = np.array([0, 0.5, 2, 4, 7, 11, 16, 22, 29, 37, 46])
new_horizons = np.array([0, 1.2, 2.8, 5.1, 8.0, 11.0, 14.5, 18.5, 23.0, 28.0, 33.5])
juno = np.array([0, 0.8, 2.3, 4.5, 7.6, 11.2, 15.5, 20.2, 25.6, 31.5, 38.1])
cassini = np.array([0, 0.9, 2.5, 5.0, 8.5, 12.8, 17.4, 22.5, 28.3, 34.7, 41.8])

# Create a figure and axis
fig, ax = plt.subplots(figsize=(12, 8))

# Plot the data for each spacecraft
ax.plot(years, voyager_1, marker='o', linestyle='-', linewidth=2)
ax.plot(years, voyager_2, marker='^', linestyle='--', linewidth=2)
ax.plot(years, new_horizons, marker='s', linestyle='-.', linewidth=2)
ax.plot(years, juno, marker='D', linestyle=':', linewidth=2)
ax.plot(years, cassini, marker='x', linestyle='-', linewidth=2)

# Include a grid for better readability
ax.grid(True, linestyle='--', alpha=0.7)

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()