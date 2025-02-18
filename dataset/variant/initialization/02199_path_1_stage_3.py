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
plt.pie(
    percentages, labels=energy_sources, autopct='%1.1f%%', startangle=90,
    colors=colors, explode=explode
)

plt.axis('equal')
plt.tight_layout()

plt.show()