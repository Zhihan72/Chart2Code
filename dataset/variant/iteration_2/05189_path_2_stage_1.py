import matplotlib.pyplot as plt
import numpy as np

# Dataset for cyclists
months = np.arange(1, 13)  # Representing months from January to December
weekday_riders = np.array([30, 35, 40, 45, 50, 55, 60, 70, 80, 85, 90, 95])
weekend_riders = np.array([60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170])

# Create plot
fig, ax1 = plt.subplots(figsize=(12, 6))

# Plot weekday riders
ax1.plot(months, weekday_riders, marker='o', linestyle='-', color='blue', linewidth=2)
# Plot weekend riders
ax1.plot(months, weekend_riders, marker='s', linestyle='--', color='green', linewidth=2)

# Add title and labels
ax1.set_title('Monthly Cyclist Participation in Local Cycling Club Rides\n(Weekday vs Weekend)', fontsize=16, weight='bold', pad=20)
ax1.set_xlabel('Month', fontsize=12)
ax1.set_ylabel('Number of Riders', fontsize=12)

# Set the tick labels for the x-axis
ax1.set_xticks(months)
ax1.set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'], fontsize=10, rotation=45)

# Remove grid, legend, and annotations

# Show the plot
plt.show()