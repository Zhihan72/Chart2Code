import matplotlib.pyplot as plt
import numpy as np

# Data
years = np.arange(2025, 2036)
auto_vehicles = np.array([30, 50, 80, 120, 170, 220, 280, 350, 420, 500, 600])
drone_deliveries = np.array([5, 15, 30, 50, 80, 120, 160, 210, 280, 350, 450])
hyperloop_pods = np.array([1, 5, 12, 30, 50, 80, 110, 150, 200, 270, 350])

# Setup the figure and subplots
fig, ax1 = plt.subplots(figsize=(14, 8))

# Apply a single color for all plots, e.g., 'teal'
color = 'teal'

# Plot Autonomous Vehicles
ax1.plot(years, auto_vehicles, color=color, marker='o', linestyle='-', linewidth=2, markersize=8)

# Plot Drone Deliveries
ax1.plot(years, drone_deliveries, color=color, marker='s', linestyle='-', linewidth=2, markersize=8)

# Plot Hyperloop Pods
ax1.plot(years, hyperloop_pods, color=color, marker='^', linestyle='-', linewidth=2, markersize=8)

# Adding Grid
ax1.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

# Automatically adjust the layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()