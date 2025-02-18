import matplotlib.pyplot as plt

energy_sources = [
    'Solar PV', 'Solar Th',
    'Wind On', 'Wind Off',
    'Hydro Conv', 'Hydro Pump',
    'Bio Solid', 'Bio Liquid'
]

percentages = [15.5, 14.5, 13, 12, 10, 10, 7, 6]

single_color = '#4682B4'  # Consistent color for all data groups.

explode = (0.1, 0, 0.1, 0, 0.1, 0, 0, 0)

plt.figure(figsize=(12, 9))
wedges, texts, autotexts = plt.pie(
    percentages, labels=energy_sources, autopct='%1.1f%%', startangle=90,
    colors=[single_color] * len(percentages), explode=explode
)

centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

plt.axis('equal')
plt.tight_layout()

plt.show()