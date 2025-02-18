import matplotlib.pyplot as plt
import numpy as np

# Data
years = np.arange(2025, 2036)
auto_vehicles = np.array([120, 80, 220, 280, 170, 30, 50, 500, 600, 420, 350])
drone_deliveries = np.array([210, 350, 160, 30, 80, 50, 450, 120, 280, 5, 15])
hyperloop_pods = np.array([150, 110, 1, 30, 350, 200, 80, 270, 50, 12, 5])

# Setup the figure and axis
fig, ax1 = plt.subplots(figsize=(14, 8))

# Plot Autonomous Vehicles with altered styles
ax1.plot(years, auto_vehicles, color='orange', marker='x', linestyle='--', linewidth=3, markersize=10, label='Auto Vehicles')

# Plot Drone Deliveries with altered styles
ax1.plot(years, drone_deliveries, color='green', marker='d', linestyle='-.', linewidth=2, markersize=8, label='Drone Deliveries')

# Plot Hyperloop Pods with altered styles
ax1.plot(years, hyperloop_pods, color='purple', marker='v', linestyle=':', linewidth=1.5, markersize=12, label='Hyperloop Pods')

# Customize grid and remove borders for randomness
ax1.grid(False)  # Disabled grid for variation

# Add legend
ax1.legend(loc='upper left')

# Show plot
plt.tight_layout()
plt.show()