import matplotlib.pyplot as plt
import numpy as np

# Data:
years = np.array([2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022])
smart_home_devices = np.array([50, 75, 100, 150, 220, 300, 400, 550])
industrial_devices = np.array([80, 120, 180, 280, 400, 600, 850, 1200])
healthcare_devices = np.array([20, 30, 50, 80, 110, 150, 220, 300])
automotive_devices = np.array([40, 60, 90, 130, 190, 250, 320, 450])
wearable_devices = np.array([10, 15, 25, 40, 60, 90, 130, 180])
entertainment_devices = np.array([30, 45, 70, 100, 140, 200, 270, 360])

# Create grouped bar width and positions
bar_width = 0.15
x_pos = np.arange(len(years))

fig, ax1 = plt.subplots(figsize=(14, 6))

# Plot bar charts for each category
ax1.bar(x_pos - 2.5*bar_width, smart_home_devices, width=bar_width, label='Gadgetry Devices', color='#FF5733')
ax1.bar(x_pos - 1.5*bar_width, industrial_devices, width=bar_width, label='Factory Devices', color='#33FF57')
ax1.bar(x_pos - 0.5*bar_width, healthcare_devices, width=bar_width, label='Health Gadgets', color='#3357FF')
ax1.bar(x_pos + 0.5*bar_width, automotive_devices, width=bar_width, label='Vehicle Gear', color='#FF33FF')
ax1.bar(x_pos + 1.5*bar_width, wearable_devices, width=bar_width, label='Wearable Devices', color='#FFD700')
ax1.bar(x_pos + 2.5*bar_width, entertainment_devices, width=bar_width, label='Entertainment Devices', color='#00FFFF')

# Set titles and labels
ax1.set_title('Device Connectivity Growth (2015-2022)', fontsize=16, fontweight='bold', pad=20)
ax1.set_ylabel('Devices Count (in Millions)', fontsize=13)
ax1.set_xlabel('Timeframe', fontsize=13)
ax1.set_xticks(x_pos)
ax1.set_xticklabels(years)
ax1.legend(loc='upper left', fontsize=12)
ax1.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()