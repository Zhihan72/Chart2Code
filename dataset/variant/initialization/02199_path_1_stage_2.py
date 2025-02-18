import matplotlib.pyplot as plt

energy_sources = [
    'Solar PV', 'Solar Th', 
    'Wind On', 'Wind Off', 
    'Hydro Conv', 'Hydro Pump', 
    'Bio Solid', 'Bio Liquid',
    'Geothermal', 'Tidal', 'Wave', 'Other'
]

percentages = [15.5, 14.5, 13, 12, 10, 10, 7, 6, 5, 3, 2, 2]

colors = [
    '#FFD700', '#FFEC8B', # Solar
    '#87CEEB', '#4682B4', # Wind
    '#32CD32', '#228B22', # Hydropower
    '#D2691E', '#8B4513', # Biomass
    '#FF6347', '#6495ED', # Geothermal, Tidal
    '#1E90FF', '#B0C4DE'  # Wave, Others
]

explode = (0.1, 0, 0.1, 0, 0.1, 0, 0, 0, 0, 0, 0, 0)

plt.figure(figsize=(12, 9))
plt.pie(
    percentages, labels=energy_sources, autopct='%1.1f%%', startangle=90,
    colors=colors, explode=explode
)

# Removed title, legend, and border by omitting wedgeprops.

plt.axis('equal')  # Ensures the pie is drawn as a circle.
plt.tight_layout()

plt.show()