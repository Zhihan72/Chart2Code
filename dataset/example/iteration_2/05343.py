import matplotlib.pyplot as plt
import numpy as np

# Decades from 1800 to 1880
decades = np.array([1800, 1820, 1840, 1860, 1880])

# Captured territories (in square miles) by different pirate fleets
black_beard_fleet = np.array([500, 1200, 2300, 1800, 700])
red_beard_fleet = np.array([300, 700, 1100, 1300, 500])
storm_riders_fleet = np.array([0, 300, 800, 1100, 1200])
shadow_reapers_fleet = np.array([100, 600, 1000, 1300, 1800])

# Create the line chart
plt.figure(figsize=(12, 8))

# Plot the black beard fleet line
plt.plot(decades, black_beard_fleet, marker='o', linestyle='-', linewidth=2, color='black', label='Black Beard Fleet')

# Plot the red beard fleet line
plt.plot(decades, red_beard_fleet, marker='s', linestyle='--', linewidth=2, color='red', label='Red Beard Fleet')

# Plot the storm riders fleet line
plt.plot(decades, storm_riders_fleet, marker='^', linestyle='-', linewidth=2, color='blue', label='Storm Riders Fleet')

# Plot the shadow reapers fleet line
plt.plot(decades, shadow_reapers_fleet, marker='d', linestyle='--', linewidth=2, color='purple', label='Shadow Reapers Fleet')

# Customize axes labels and title
plt.xlabel('Decade', fontsize=12)
plt.ylabel('Captured Territories (sq. miles)', fontsize=12)
plt.title('Rise and Fall of Pirate Fleets (1800-1880)', fontsize=16, fontweight='bold', pad=20)

# Add gridlines to the plot for better readability
plt.grid(True, linestyle='--', alpha=0.6)

# Add legend to distinguish between different fleets
plt.legend(loc='upper left', fontsize=12)

# Automatically adjust the layout for better text visibility
plt.tight_layout()

# Display the plot
plt.show()