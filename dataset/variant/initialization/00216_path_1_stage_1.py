import matplotlib.pyplot as plt
import numpy as np

# Define the years for the x-axis
years = np.arange(2020, 2031)

# Original data for renewable energy production in Europe
solar_energy = [150, 170, 190, 220, 260, 310, 370, 440, 530, 640, 770]
wind_energy = [200, 215, 230, 260, 300, 350, 410, 490, 590, 710, 860]
hydro_energy = [180, 182, 185, 190, 195, 200, 205, 210, 215, 220, 225]

# Additional data for non-renewable energy production (in GWh) in Europe
fossil_energy = [1200, 1180, 1160, 1120, 1100, 1050, 1000, 950, 900, 850, 800]
nuclear_energy = [450, 445, 440, 435, 430, 425, 420, 415, 410, 405, 400]

# Create a figure with a grid layout for multiple subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6), gridspec_kw={'width_ratios': [2, 1]})

# First plot: Line chart of renewable energy production
ax1.plot(years, solar_energy, marker='o', linestyle='-', color='gold', linewidth=2)
ax1.plot(years, wind_energy, marker='s', linestyle='--', color='skyblue', linewidth=2)
ax1.plot(years, hydro_energy, marker='^', linestyle='-.', color='green', linewidth=2)

ax1.grid(True, linestyle='--', alpha=0.5)

# Second plot: Stacked bar chart for energy mix comparison
width = 0.4  # width of the bars

# Plot the data
ax2.bar(years - width / 2, fossil_energy, width, color='gray', alpha=0.7)
ax2.bar(years - width / 2, nuclear_energy, width, bottom=fossil_energy, color='darkblue', alpha=0.7)

ax2.grid(True, linestyle='--', alpha=0.5)

# Remove textual elements
ax1.tick_params(labelsize=10)
ax2.tick_params(labelsize=10)

# Adjust layout for better readability
plt.tight_layout()

# Display the final plot
plt.show()