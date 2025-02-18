import matplotlib.pyplot as plt
import numpy as np

device_categories = ['Smart Thermostats', 'Smart Tvs', 'Smart Spkers', 'Smar Lighting', 'Smrt Appliances']
energy_consumption_percentages = [20, 25, 30, 10, 15]

cmap = plt.get_cmap('coolwarm')
colors = [cmap(0.4), cmap(1.0), cmap(0.6), cmap(0.2), cmap(0.8)]

fig, ax = plt.subplots(figsize=(14, 8))
bars = ax.bar(device_categories, energy_consumption_percentages, color=colors)

ax.set_xlabel('Smart Devices', fontsize=12, fontweight='bold')
ax.set_ylabel('Energy Consumption (%)', fontsize=12, fontweight='bold')
ax.set_title('Consuming Tech Energy:\nPercentage of Device Involvement Smart Homes (2023)', fontsize=16, fontweight='bold', loc='left', pad=20)

for bar in bars:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, height + 0.5,
            f'{height}%', ha='center', va='bottom', fontsize=11, fontweight='bold', color='darkred')

ax.set_ylim(0, 100)

plt.tight_layout()
plt.show()