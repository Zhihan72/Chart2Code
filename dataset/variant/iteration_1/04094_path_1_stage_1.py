import matplotlib.pyplot as plt

days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

# Traffic data in thousands
morning_traffic = [5, 6, 7, 8, 9, 4, 3]  # 6 AM - 12 PM
afternoon_traffic = [9, 10, 11, 12, 13, 8, 7]  # 12 PM - 6 PM
evening_traffic = [15, 16, 17, 18, 19, 14, 10]  # 6 PM - 12 AM
night_traffic = [3, 2, 2, 3, 4, 6, 8]  # 12 AM - 6 AM

fig, ax = plt.subplots(figsize=(12, 8))

# Plotting the data
ax.plot(days, morning_traffic, label="Morning (6-12)", color='skyblue', marker='o', linewidth=2)
ax.plot(days, afternoon_traffic, label="Afternoon (12-6)", color='orange', marker='s', linewidth=2)
ax.plot(days, evening_traffic, label="Evening (6-12)", color='green', marker='^', linewidth=2)
ax.plot(days, night_traffic, label="Night (12-6)", color='purple', marker='d', linewidth=2)

# Adding labels
ax.set_xlabel('Days', fontsize=12)
ax.set_ylabel('Traffic (k)', fontsize=12)
ax.set_title('Web Traffic Trends', fontsize=16, fontweight='bold')

# Customizing ticks and grid
ax.set_xticks(range(len(days)))
ax.grid(True, linestyle='--', alpha=0.6)

# Rotating x-axis labels
plt.xticks(rotation=45)

# Adding a legend
ax.legend(loc='upper left', fontsize=10)

plt.tight_layout()

plt.show()