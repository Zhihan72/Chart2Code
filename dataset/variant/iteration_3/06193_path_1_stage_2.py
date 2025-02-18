import matplotlib.pyplot as plt

# Data Preparation
time_slots = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
upload_rates = [10, 15, 12, 20, 18, 8, 25]
download_rates = [50, 48, 52, 55, 53, 60, 58]

# Set up the figure and plot the line chart
plt.figure(figsize=(14, 8))

# Plot upload speeds
plt.plot(time_slots, upload_rates, marker='o', color='blue', linewidth=2, markersize=8)

# Plot download speeds
plt.plot(time_slots, download_rates, marker='o', color='green', linewidth=2, markersize=8)

# Title and labels
plt.title('Network Data Load\nSpeed Observation', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Week Days', fontsize=14)
plt.ylabel('Data Rate (Mbps)', fontsize=14)

# Customize the y-axis limits
plt.ylim(0, 70)

# Remove spines from the plot
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)

# Improve layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()