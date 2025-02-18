import matplotlib.pyplot as plt

days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

# Altered data values within each time period
morning_traffic = [7, 3, 8, 9, 5, 6, 4]
afternoon_traffic = [12, 11, 10, 13, 8, 9, 7]
evening_traffic = [18, 17, 15, 14, 16, 19, 10]
night_traffic = [6, 4, 3, 8, 2, 3, 2]

fig, ax = plt.subplots(figsize=(12, 8))

# Plotting the shuffled data colors
ax.plot(days, morning_traffic, color='green', marker='o', linewidth=2)
ax.plot(days, afternoon_traffic, color='purple', marker='s', linewidth=2)
ax.plot(days, evening_traffic, color='skyblue', marker='^', linewidth=2)
ax.plot(days, night_traffic, color='orange', marker='d', linewidth=2)

# Adding labels
ax.set_xlabel('Days', fontsize=12)
ax.set_ylabel('Traffic (k)', fontsize=12)
ax.set_title('Web Traffic Trends', fontsize=16, fontweight='bold')

# Rotating x-axis labels
plt.xticks(rotation=45)

plt.tight_layout()

plt.show()