import matplotlib.pyplot as plt
import numpy as np

# Define time axis (years)
years = np.arange(2040, 2051)

# Define crop growth rates for two colonies in percentage (%)
wheat_a = np.array([20, 21, 22, 22, 23, 24, 24, 25, 26, 27, 28])
corn_a = np.array([15, 16, 16, 17, 18, 18, 19, 20, 21, 22, 23])
rice_a = np.array([10, 11, 12, 12, 13, 14, 15, 15, 16, 17, 18])
wheat_b = np.array([18, 19, 20, 20, 21, 22, 23, 23, 24, 25, 26])
corn_b = np.array([14, 14, 15, 15, 16, 17, 17, 18, 19, 20, 21])
rice_b = np.array([9, 9, 10, 11, 11, 11, 12, 13, 13, 14, 15])

# Set up the plot
fig, ax = plt.subplots(figsize=(12, 8))

# Plot the data
ax.plot(years, wheat_a, color='green', linestyle='-')
ax.plot(years, corn_a, color='blue', linestyle='-')
ax.plot(years, rice_a, color='red', linestyle='-')

ax.plot(years, wheat_b, color='green', linestyle='--')
ax.plot(years, corn_b, color='blue', linestyle='--')
ax.plot(years, rice_b, color='red', linestyle='--')

# Grid
ax.grid(True, linestyle='--', alpha=0.5)

# Tight layout to prevent overlapping
plt.tight_layout()

# Show the plot
plt.show()