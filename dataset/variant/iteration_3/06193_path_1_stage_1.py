import matplotlib.pyplot as plt

# Data Preparation
time_slots = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
upload_rates = [10, 15, 12, 20, 18, 8, 25]
download_rates = [50, 48, 52, 55, 53, 60, 58]

# Set up the figure and plot the line chart
plt.figure(figsize=(14, 8))

# Plot upload speeds
plt.plot(time_slots, upload_rates, marker='o', linestyle='-', color='blue', linewidth=2, markersize=8, label='Upload Speed (M)')

# Annotate upload speeds
for i, speed in enumerate(upload_rates):
    plt.annotate(f'{speed}', (time_slots[i], speed), textcoords="offset points", xytext=(-10, 10), ha='center', color='blue')

# Plot download speeds
plt.plot(time_slots, download_rates, marker='o', linestyle='-', color='green', linewidth=2, markersize=8, label='Download Rate (M)')

# Annotate download speeds
for i, speed in enumerate(download_rates):
    plt.annotate(f'{speed}', (time_slots[i], speed), textcoords="offset points", xytext=(-10, 10), ha='center', color='green')

# Title and labels
plt.title('Network Data Load\nSpeed Observation', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Week Days', fontsize=14)
plt.ylabel('Data Rate (Mbps)', fontsize=14)

# Applying Grid
plt.grid(True, linestyle='--', alpha=0.7)

# Customize the y-axis limits
plt.ylim(0, 70)

# Add legend to the plot
plt.legend(loc='upper left', fontsize=12)

# Improve layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()