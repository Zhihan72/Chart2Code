import matplotlib.pyplot as plt
import numpy as np

# Data
years = np.arange(2025, 2036)
auto_vehicles = np.array([30, 50, 80, 120, 170, 220, 280, 350, 420, 500, 600])
hyperloop_pods = np.array([1, 5, 12, 30, 50, 80, 110, 150, 200, 270, 350])

# Setup the figure
fig, ax1 = plt.subplots(figsize=(14, 8))

# Plot Autonomous Vehicles
ax1.plot(years, auto_vehicles, color='teal', marker='o', linestyle='-', linewidth=2, markersize=8, label='Autonomous Vehicles')

# Plot Hyperloop Pods
ax1.plot(years, hyperloop_pods, color='purple', marker='^', linestyle='-', linewidth=2, markersize=8, label='Hyperloop Pods')

# Title and Labels
ax1.set_title('Technological Advancements in Sci-Fi Cities (2025-2035)', fontsize=18, fontweight='bold', pad=15)
ax1.set_xlabel('Year', fontsize=14)
ax1.set_ylabel('Number of Units Deployed', fontsize=14)

# Adding Legend
ax1.legend(loc='upper left', fontsize=12)

# Adding Grid
ax1.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

# Annotate key milestones
ax1.annotate('First major Hyperloop system', xy=(2033, hyperloop_pods[8]), xytext=(2030, 300),
             arrowprops=dict(facecolor='gray', arrowstyle='->'), fontsize=12, color='navy')

# Automatically adjust the layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()