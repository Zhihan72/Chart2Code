import matplotlib.pyplot as plt
import numpy as np

# Backstory:
# In the distant future, humanity has established advanced agricultural colonies on Mars.
# Each colony focuses on growing a variety of crops under different simulated Earth climates.
# This script visualizes the annual growth rates of different crops in two primary colonies: 
# Colony A, which replicates a tropical climate, and Colony B, simulating a temperate climate.

# Define time axis (years)
years = np.arange(2040, 2051)

# Define crop growth rates for two colonies in percentage (%)
# Colony A (Tropical Climate) - Suitable for rapid, consistent growth
wheat_a = np.array([20, 21, 22, 22, 23, 24, 24, 25, 26, 27, 28])
corn_a = np.array([15, 16, 16, 17, 18, 18, 19, 20, 21, 22, 23])
rice_a = np.array([10, 11, 12, 12, 13, 14, 15, 15, 16, 17, 18])

# Colony B (Temperate Climate) - Moderate growth with seasonal variability
wheat_b = np.array([18, 19, 20, 20, 21, 22, 23, 23, 24, 25, 26])
corn_b = np.array([14, 14, 15, 15, 16, 17, 17, 18, 19, 20, 21])
rice_b = np.array([9, 9, 10, 11, 11, 11, 12, 13, 13, 14, 15])

# Set up the plot
fig, ax = plt.subplots(figsize=(12, 8))

# Plot the data
ax.plot(years, wheat_a, label='Wheat (Colony A)', color='green', linestyle='-')
ax.plot(years, corn_a, label='Corn (Colony A)', color='blue', linestyle='-')
ax.plot(years, rice_a, label='Rice (Colony A)', color='red', linestyle='-')

ax.plot(years, wheat_b, label='Wheat (Colony B)', color='green', linestyle='--')
ax.plot(years, corn_b, label='Corn (Colony B)', color='blue', linestyle='--')
ax.plot(years, rice_b, label='Rice (Colony B)', color='red', linestyle='--')

# Title and labels
ax.set_title("Annual Crop Growth Rates in Martian Agricultural Colonies (2040-2050)", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Growth Rate (%)', fontsize=12)

# Grid and Legend
ax.grid(True, linestyle='--', alpha=0.5)
ax.legend(title='Crops by Colony and Climate', fontsize=10, frameon=False)

# Highlighting significant milestones with annotations
ax.annotate('Introduction of Advanced Fertilizers', xy=(2045, 28), xytext=(2042, 30),
            arrowprops=dict(facecolor='black', shrink=0.05),
            fontsize=10, fontweight='bold')

# Tight layout to prevent overlapping
plt.tight_layout()

# Show the plot
plt.show()