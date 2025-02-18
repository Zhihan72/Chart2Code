import matplotlib.pyplot as plt

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
bars = ax.bar(device_categories, energy_consumption_percentages, color=single_color, edgecolor='black', width=0.6)

ax.set_ylim(0, 100)

plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()