import matplotlib.pyplot as plt
import numpy as np

# Define the months and categories of IoT devices
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
devices = ['Smart Meters', 'Security Cameras', 'Connected Vehicles', 'Smart Home Devices']

# Monthly Internet Traffic Volume data in Gigabytes (GB) for each category over the months
smart_meters_traffic = [50, 55, 60, 65, 75, 85, 95, 105, 110, 120, 125, 130]
security_cameras_traffic = [200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310]
connected_vehicles_traffic = [150, 160, 170, 175, 180, 185, 190, 195, 200, 210, 220, 230]
smart_home_traffic = [100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210]

# Set up the plot
fig, ax = plt.subplots(figsize=(14, 8))

# Stack the data for plotting the area chart
traffic_data = np.vstack([smart_meters_traffic, security_cameras_traffic, connected_vehicles_traffic, smart_home_traffic])

# Create the stacked area plot
ax.stackplot(months, traffic_data, labels=devices, colors=['#ADD8E6', '#FFB6C1', '#90EE90', '#FFFFE0'], alpha=0.8)

# Customize the chart
ax.set_title("Internet Traffic Volume Across Various IoT Devices in Smart City (2024)", fontsize=18, fontweight='bold', pad=20)
ax.set_xlabel("Month", fontsize=14, labelpad=12)
ax.set_ylabel("Internet Traffic Volume (GB)", fontsize=14, labelpad=12)

# Rotate x-axis labels to avoid overlap
plt.xticks(rotation=45)

# Add a legend
ax.legend(loc='upper left', fontsize=12, title="IoT Devices", title_fontsize='14')

# Annotate significant traffic volume increase
ax.annotate('Traffic Spike', xy=('Aug', 270), xytext=('Jun', 400),
            arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=12, ha='center')

# Add a grid to enhance readability
ax.grid(True, linestyle='--', alpha=0.7)

# Automatically adjust layout to prevent overlap and improve aesthetics
plt.tight_layout()

# Display the plot
plt.show()