import numpy as np
import matplotlib.pyplot as plt

# Days of Week
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

# Traffic data (in thousands) for different times
morning_traffic = [5, 6, 7, 8, 9, 4, 3]     # 6 AM - 12 PM
afternoon_traffic = [9, 10, 11, 12, 13, 8, 7]
evening_traffic = [15, 16, 17, 18, 19, 14, 10]
night_traffic = [3, 2, 2, 3, 4, 6, 8]

# Creating a figure and axis
fig, ax = plt.subplots(figsize=(12, 8))

# Plotting the data
ax.plot(days, morning_traffic, label="Morn (6-12)", color='skyblue', marker='o', linewidth=2)
ax.plot(days, afternoon_traffic, label="Aftn (12-6)", color='orange', marker='s', linewidth=2)
ax.plot(days, evening_traffic, label="Eve (18-24)", color='green', marker='^', linewidth=2)
ax.plot(days, night_traffic, label="Nt (24-6)", color='purple', marker='d', linewidth=2)

# Adding labels
ax.set_xlabel('Days', fontsize=12)
ax.set_ylabel('Traffic (k)', fontsize=12)
ax.set_title('Weekly Traffic Trends', fontsize=16, fontweight='bold')

# Customizing ticks and grid
ax.set_xticks(range(len(days)), days)
ax.grid(True, linestyle='--', alpha=0.6)

# Rotating x-axis labels for better readability
plt.xticks(rotation=45)

# Adding a legend
ax.legend(loc='upper left', fontsize=10)

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()