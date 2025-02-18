import matplotlib.pyplot as plt
import numpy as np

device_categories = ['Smrt Appliances', 'Smart Tvs', 'Smar Lighting', 'Smart Spkers', 'Smart Thermostats']
energy_consumption_percentages = [15, 25, 10, 30, 20]

cmap = plt.get_cmap('coolwarm')
colors = [cmap(0.8), cmap(1.0), cmap(0.2), cmap(0.6), cmap(0.4)]

fig, ax = plt.subplots(figsize=(14, 8))
bars = ax.barh(device_categories, energy_consumption_percentages, color=colors, height=0.6)

ax.set_xlabel('Engy Consumpt (%)', fontsize=12, fontweight='bold')
ax.set_ylabel('Szmart Devices', fontsize=12, fontweight='bold')
ax.set_title('Consuming Tech Energy:\nPerctage of Device Involvement Smart Homes (2023)', fontsize=16, fontweight='bold', loc='left', pad=20)

for bar in bars:
    width = bar.get_width()
    ax.text(width + 0.5, bar.get_y() + bar.get_height()/2,
            f'{width}%', va='center', ha='left', fontsize=11, fontweight='bold', color='darkred')

ax.set_xlim(0, 100)
ax.invert_yaxis()

plt.tight_layout()
plt.show()