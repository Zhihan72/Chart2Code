import numpy as np
import matplotlib.pyplot as plt

# Backstory: Monitoring the traffic trends on a popular website over different days of the week 
# and during various time slots each day.

# Days of Week
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

# Traffic data (in thousands) for different times of the day
morning_traffic = [5, 6, 7, 8, 9, 4, 3]     # 6 AM - 12 PM
afternoon_traffic = [9, 10, 11, 12, 13, 8, 7]  # 12 PM - 6 PM
evening_traffic = [15, 16, 17, 18, 19, 14, 10] # 6 PM - 12 AM
night_traffic = [3, 2, 2, 3, 4, 6, 8]       # 12 AM - 6 AM

# Creating a figure and axis
fig, ax = plt.subplots(figsize=(12, 8))

# Plotting the data
ax.plot(days, morning_traffic, label="Morning (6 AM - 12 PM)", color='skyblue', marker='o', linewidth=2)
ax.plot(days, afternoon_traffic, label="Afternoon (12 PM - 6 PM)", color='orange', marker='s', linewidth=2)
ax.plot(days, evening_traffic, label="Evening (6 PM - 12 AM)", color='green', marker='^', linewidth=2)
ax.plot(days, night_traffic, label="Night (12 AM - 6 AM)", color='purple', marker='d', linewidth=2)

# Adding labels
ax.set_xlabel('Days of the Week', fontsize=12)
ax.set_ylabel('Website Traffic (in thousands)', fontsize=12)
ax.set_title('Weekly Website Traffic Trends\nAcross Different Times of the Day', fontsize=16, fontweight='bold')

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