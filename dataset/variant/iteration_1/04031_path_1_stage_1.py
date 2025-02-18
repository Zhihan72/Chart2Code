import matplotlib.pyplot as plt
import numpy as np

# Data
years = np.array([2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022])
smart_home_devices = np.array([50, 75, 100, 150, 220, 300, 400, 550])
industrial_devices = np.array([80, 120, 180, 280, 400, 600, 850, 1200])
healthcare_devices = np.array([20, 30, 50, 80, 110, 150, 220, 300])
automotive_devices = np.array([40, 60, 90, 130, 190, 250, 320, 450])

# Create grouped bar width and positions
bar_width = 0.2
x_pos = np.arange(len(years))

# Create subplots with 1 row and 2 columns
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5), sharex=True)

# Plot bar charts for each category on the first subplot
ax1.bar(x_pos - 1.5*bar_width, smart_home_devices, width=bar_width, label='Smart Home Devices', color='#FF5733')
ax1.bar(x_pos - 0.5*bar_width, industrial_devices, width=bar_width, label='Industrial Devices', color='#33FF57')
ax1.bar(x_pos + 0.5*bar_width, healthcare_devices, width=bar_width, label='Healthcare Devices', color='#3357FF')
ax1.bar(x_pos + 1.5*bar_width, automotive_devices, width=bar_width, label='Automotive Devices', color='#FF33FF')

# Set titles and labels for the first subplot
ax1.set_title('Growth of Internet-Connected Devices Across Sectors (2015-2022)', fontsize=16, fontweight='bold', pad=20)
ax1.set_ylabel('Number of Devices (Millions)', fontsize=13)
ax1.legend(loc='upper left', fontsize=12)
ax1.grid(axis='y', linestyle='--', alpha=0.7)

# Function to calculate the growth percentages
def calculate_growth(data):
    return [(data[i] - data[i-1]) / data[i-1] * 100 if i > 0 else 0 for i in range(len(data))]

smart_home_growth = calculate_growth(smart_home_devices)
industrial_growth = calculate_growth(industrial_devices)
healthcare_growth = calculate_growth(healthcare_devices)
automotive_growth = calculate_growth(automotive_devices)

# Plot bar chart of growth rates on the second subplot
ax2.bar(x_pos - 1.5*bar_width, smart_home_growth, width=bar_width, label='Smart Home Growth', color='#FF5733', alpha=0.7)
ax2.bar(x_pos - 0.5*bar_width, industrial_growth, width=bar_width, label='Industrial Growth', color='#33FF57', alpha=0.7)
ax2.bar(x_pos + 0.5*bar_width, healthcare_growth, width=bar_width, label='Healthcare Growth', color='#3357FF', alpha=0.7)
ax2.bar(x_pos + 1.5*bar_width, automotive_growth, width=bar_width, label='Automotive Growth', color='#FF33FF', alpha=0.7)

# Set titles and labels for the second subplot
ax2.set_title('Annual Growth Rate of Internet-Connected Devices', fontsize=16, fontweight='bold')
ax2.set_xlabel('Years', fontsize=13)
ax2.set_ylabel('Growth Rate (%)', fontsize=13)
ax2.set_xticks(x_pos)
ax2.set_xticklabels(years)
ax2.grid(axis='y', linestyle='--', alpha=0.7)
ax2.legend(loc='upper left', fontsize=12)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()