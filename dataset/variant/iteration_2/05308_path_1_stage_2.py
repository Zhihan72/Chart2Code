import numpy as np
import matplotlib.pyplot as plt

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

# Manually altered data groups
smart_thermostat = [2.3, 2.1, 3.0, 2.4, 3.5, 4.0, 3.8, 4.2, 4.1, 3.4, 3.2, 3.7]
smart_lighting = [1.2, 1.5, 1.3, 2.0, 1.7, 2.4, 2.2, 2.5, 1.6, 2.3, 1.8, 2.1]
smart_refrigerator = [1.8, 1.5, 1.6, 1.9, 1.7, 2.4, 2.1, 2.5, 2.8, 3.0, 2.7, 3.2]
smart_security = [3.2, 3.0, 3.5, 3.3, 3.6, 4.0, 3.8, 4.2, 4.1, 4.3, 4.4, 4.1]

data_usage = np.array([
    smart_thermostat,
    smart_lighting,
    smart_refrigerator,
    smart_security
])

device_labels = ['Smart Thermostat', 'Smart Lighting', 'Smart Refrigerator', 'Smart Security']

fig, ax = plt.subplots(figsize=(14, 8))

for idx, label in enumerate(device_labels):
    ax.plot(months, data_usage[idx], marker='o', linestyle='-', linewidth=2, label=label, color='royalblue')

ax.set_title('Monthly Internet Data Usage Trends in a Smart Home (in GB)', fontsize=16, fontweight='bold', pad=10)
ax.set_xlabel('Month', fontsize=12)
ax.set_ylabel('Data Usage (GB)', fontsize=12)
ax.grid(True, linestyle='--', alpha=0.5)
ax.legend(title='Smart Devices', fontsize=10, title_fontsize=12, loc='upper left', bbox_to_anchor=(1, 1))

plt.tight_layout()
plt.show()