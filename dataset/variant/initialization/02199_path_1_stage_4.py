import matplotlib.pyplot as plt

energy_sources = [
    'Solar PV', 'Solar Th',
    'Wind On', 'Wind Off',
    'Hydro Conv', 'Hydro Pump',
    'Bio Solid', 'Bio Liquid'
]

percentages = [15.5, 14.5, 13, 12, 10, 10, 7, 6]

colors = [
    '#FFD700', '#FFEC8B', # Solar
    '#87CEEB', '#4682B4', # Wind
    '#32CD32', '#228B22', # Hydropower
    '#D2691E', '#8B4513'  # Biomass
]

explode = (0.1, 0, 0.1, 0, 0.1, 0, 0, 0)

plt.figure(figsize=(12, 9))
wedges, texts, autotexts = plt.pie(
    percentages, labels=energy_sources, autopct='%1.1f%%', startangle=90,
    colors=colors, explode=explode
)

# Draw a circle at the center for a donut shape
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.tight_layout()

plt.show()