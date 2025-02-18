import matplotlib.pyplot as plt
import numpy as np

device_categories = [
    'Smart Lighting',
    'Smart Thermostats',
    'Smart Speakers',
    'Smart TVs',
    'Smart Appliances',
    'Smart Security Systems',
    'Smart Assistants',
    'Smart Plugs'
]

energy_consumption_percentages = [12, 20, 8, 25, 15, 10, 5, 5]

single_color = 'skyblue'

fig, ax = plt.subplots(figsize=(16, 10))
bars = ax.barh(device_categories, energy_consumption_percentages, color=single_color, edgecolor='black', height=0.6)

ax.set_xlim(0, 100)
ax.xaxis.grid(True, linestyle='--', alpha=0.7, color='gray')
ax.invert_yaxis()

plt.tight_layout()
plt.show()