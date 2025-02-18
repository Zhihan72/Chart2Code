import matplotlib.pyplot as plt
import numpy as np

# Years of interest
years = np.arange(2012, 2023)

# Mode of transport percentages over the years
public_transport = np.array([30, 32, 34, 35, 36, 38, 40, 42, 45, 48, 50])
cycling = np.array([5, 6, 7, 9, 11, 13, 15, 17, 20, 22, 25])
walking = np.array([10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
electric_vehicles = np.array([2, 3, 4, 5, 6, 8, 10, 12, 15, 18, 20])
conventional_vehicles = np.array([53, 48, 43, 38, 33, 26, 19, 12, 2, 1, 0])

# Compute the total sustainable transport usage
sustainable_transport = cycling + walking + electric_vehicles

# Set up the plot
fig, ax = plt.subplots(figsize=(14, 9))

# Stack the bar chart
ax.bar(years, public_transport, color='#4d88ff')
ax.bar(years, cycling, bottom=public_transport, color='#ff9933')
ax.bar(years, walking, bottom=public_transport + cycling, color='#66c266')
ax.bar(years, electric_vehicles, bottom=public_transport + cycling + walking, color='#cc66ff')
ax.bar(years, conventional_vehicles, bottom=public_transport + cycling + walking + electric_vehicles, color='#ff6666')

# Overlay a line plot for sustainable transport
ax.plot(years, sustainable_transport, color='gold', linewidth=2.5, marker='o', markersize=8)

# Remove y-axis grid lines for clarity
ax.grid(axis='y', linestyle='--', alpha=0.5)

# Adjust layout to prevent overlap
plt.tight_layout()

# Show plot
plt.show()