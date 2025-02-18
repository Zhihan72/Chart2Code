import matplotlib.pyplot as plt
import numpy as np

# Define the years for the x-axis
years = np.arange(2020, 2031)

# Data for renewable energy production in Europe (excluding solar)
wind_energy = [200, 215, 230, 260, 300, 350, 410, 490, 590, 710, 860]
hydro_energy = [180, 182, 185, 190, 195, 200, 205, 210, 215, 220, 225]

# Data for non-renewable energy production (excluding nuclear)
fossil_energy = [1200, 1180, 1160, 1120, 1100, 1050, 1000, 950, 900, 850, 800]

# Create a figure with a grid layout for multiple subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6), gridspec_kw={'width_ratios': [2, 1]})

# First plot: Line chart of renewable energy production (excluding solar)
ax1.plot(years, wind_energy, marker='s', linestyle='--', color='skyblue', linewidth=2)
ax1.plot(years, hydro_energy, marker='^', linestyle='-.', color='green', linewidth=2)

ax1.grid(True, linestyle='--', alpha=0.5)

# Second plot: Bar chart for energy mix comparison (excluding nuclear)
width = 0.4  # width of the bars

# Plot the fossil energy data
ax2.bar(years - width / 2, fossil_energy, width, color='gray', alpha=0.7)

ax2.grid(True, linestyle='--', alpha=0.5)

# Remove textual elements
ax1.tick_params(labelsize=10)
ax2.tick_params(labelsize=10)

# Adjust layout for better readability
plt.tight_layout()

# Display the final plot
plt.show()