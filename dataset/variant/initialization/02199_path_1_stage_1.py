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
wedges, texts, autotexts = plt.pie(
    percentages, labels=energy_sources, autopct='%1.1f%%', startangle=90,
    colors=colors, explode=explode, wedgeprops={'edgecolor': 'black'}, shadow=True
)

for text in texts + autotexts:
    text.set_fontsize(9)
    text.set_color('black')
for autotext in autotexts:
    autotext.set_fontweight('bold')

plt.title('Renewable Energy Distribution - 2023', fontsize=14, fontweight='bold', pad=20)

plt.legend(
    wedges, energy_sources, title="Sources", loc='upper right', bbox_to_anchor=(1.2, 1),
    fontsize=10, title_fontsize='11'
)

plt.axis('equal')
plt.tight_layout(rect=[0, 0, 0.9, 1])

plt.show()