import matplotlib.pyplot as plt
import numpy as np

# Backstory:
# The local cycling club has been promoting cycling for fitness and environmental benefits.
# We have tracked the number of cyclists participating in weekday and weekend bike rides over a year.

# Create dataset for cyclists participating in weekday and weekend rides over a year (12 months)
months = np.arange(1, 13)  # Representing months from January to December
weekday_riders = np.array([30, 35, 40, 45, 50, 55, 60, 70, 80, 85, 90, 95])
weekend_riders = np.array([60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170])

# Create plot
fig, ax1 = plt.subplots(figsize=(12, 6))

# Plot weekday riders
ax1.plot(months, weekday_riders, marker='o', linestyle='-', color='blue', linewidth=2, label='Weekday Riders')
# Plot weekend riders
ax1.plot(months, weekend_riders, marker='s', linestyle='--', color='green', linewidth=2, label='Weekend Riders')

# Adding title and labels
ax1.set_title('Monthly Cyclist Participation in Local Cycling Club Rides\n(Weekday vs Weekend)', fontsize=16, weight='bold', pad=20)
ax1.set_xlabel('Month', fontsize=12)
ax1.set_ylabel('Number of Riders', fontsize=12)

# Setting the tick labels for the x-axis
ax1.set_xticks(months)
ax1.set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'], fontsize=10, rotation=45)

# Adding grid for better readability
ax1.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

# Adding legend to differentiate between weekday and weekend data
ax1.legend(loc='upper left', fontsize=10)

# Adding annotations for key points in the data
ax1.annotate('Summer Season Peak', xy=(8, 70), xytext=(6, 50),
             arrowprops=dict(facecolor='black', arrowstyle='->', lw=1), fontsize=10, color='darkblue')
ax1.annotate('End of Year Surge', xy=(12, 170), xytext=(10, 150),
             arrowprops=dict(facecolor='black', arrowstyle='->', lw=1), fontsize=10, color='darkgreen')

# Adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()