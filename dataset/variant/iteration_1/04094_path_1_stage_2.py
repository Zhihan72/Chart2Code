import matplotlib.pyplot as plt

days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

morning_traffic = [5, 6, 7, 8, 9, 4, 3]
afternoon_traffic = [9, 10, 11, 12, 13, 8, 7]
evening_traffic = [15, 16, 17, 18, 19, 14, 10]
night_traffic = [3, 2, 2, 3, 4, 6, 8]

fig, ax = plt.subplots(figsize=(12, 8))

# Plotting the data
ax.plot(days, morning_traffic, color='skyblue', marker='o', linewidth=2)
ax.plot(days, afternoon_traffic, color='orange', marker='s', linewidth=2)
ax.plot(days, evening_traffic, color='green', marker='^', linewidth=2)
ax.plot(days, night_traffic, color='purple', marker='d', linewidth=2)

# Adding labels
ax.set_xlabel('Days', fontsize=12)
ax.set_ylabel('Traffic (k)', fontsize=12)
ax.set_title('Web Traffic Trends', fontsize=16, fontweight='bold')

# Rotating x-axis labels
plt.xticks(rotation=45)

plt.tight_layout()

plt.show()