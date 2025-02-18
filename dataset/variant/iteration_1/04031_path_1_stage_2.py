import matplotlib.pyplot as plt
import numpy as np

years = np.array([2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022])
smart_home_devices = np.array([50, 75, 100, 150, 220, 300, 400, 550])
industrial_devices = np.array([80, 120, 180, 280, 400, 600, 850, 1200])
healthcare_devices = np.array([20, 30, 50, 80, 110, 150, 220, 300])
automotive_devices = np.array([40, 60, 90, 130, 190, 250, 320, 450])

bar_width = 0.2
x_pos = np.arange(len(years))

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5), sharex=True)

ax1.bar(x_pos - 1.5*bar_width, smart_home_devices, width=bar_width, label='Smart Home Devices', hatch='/', color='#FF5733')
ax1.bar(x_pos - 0.5*bar_width, industrial_devices, width=bar_width, label='Industrial Devices', hatch='\\', color='#33FF57')
ax1.bar(x_pos + 0.5*bar_width, healthcare_devices, width=bar_width, label='Healthcare Devices', hatch='x', color='#3357FF')
ax1.bar(x_pos + 1.5*bar_width, automotive_devices, width=bar_width, label='Automotive Devices', hatch='-', color='#FF33FF')

ax1.set_title('Growth of Internet-Connected Devices (2015-2022)', fontsize=16, fontweight='bold', pad=20)
ax1.set_ylabel('Devices (Millions)', fontsize=13)
ax1.legend(loc='upper right', fontsize=10, frameon=False)
ax1.grid(False)

def calculate_growth(data):
    return [(data[i] - data[i-1]) / data[i-1] * 100 if i > 0 else 0 for i in range(len(data))]

smart_home_growth = calculate_growth(smart_home_devices)
industrial_growth = calculate_growth(industrial_devices)
healthcare_growth = calculate_growth(healthcare_devices)
automotive_growth = calculate_growth(automotive_devices)

ax2.bar(x_pos - 1.5*bar_width, smart_home_growth, width=bar_width, label='Smart Home Growth', color='#FF5733', linestyle=':', linewidth=2)
ax2.bar(x_pos - 0.5*bar_width, industrial_growth, width=bar_width, label='Industrial Growth', color='#33FF57', linestyle='--', linewidth=2)
ax2.bar(x_pos + 0.5*bar_width, healthcare_growth, width=bar_width, label='Healthcare Growth', color='#3357FF', linestyle='-.', linewidth=2)
ax2.bar(x_pos + 1.5*bar_width, automotive_growth, width=bar_width, label='Automotive Growth', color='#FF33FF', linestyle='-', linewidth=2)

ax2.set_title('Annual Growth Rate of Devices', fontsize=16, fontweight='bold')
ax2.set_xlabel('Years', fontsize=13)
ax2.set_ylabel('Growth Rate (%)', fontsize=13)
ax2.set_xticks(x_pos)
ax2.set_xticklabels(years)
ax2.grid(True, which='both', axis='y')

plt.tight_layout()
plt.show()