import matplotlib.pyplot as plt

energy_sources = [
    'Solar - Photovoltaic', 'Solar - Thermal', 
    'Wind - Onshore', 'Wind - Offshore', 
    'Hydropower - Conventional', 'Hydropower - Pumped', 
    'Biomass - Solid', 'Biomass - Liquid',
    'Geothermal', 'Tidal', 'Wave', 'Others'
]

percentages = [15.5, 14.5, 13, 12, 10, 10, 7, 6, 5, 3, 2, 2]

# Manually shuffled the colors list
colors = [
    '#FFEC8B', '#FFD700', 
    '#4682B4', '#87CEEB', 
    '#228B22', '#32CD32', 
    '#8B4513', '#D2691E', 
    '#6495ED', '#FF6347', 
    '#B0C4DE', '#1E90FF'
]

explode = (0.1, 0, 0.1, 0, 0.1, 0, 0, 0, 0, 0, 0, 0)

plt.figure(figsize=(12, 9))
wedges, texts, autotexts = plt.pie(
    percentages, labels=energy_sources, autopct='%1.1f%%', startangle=90,
    colors=colors, explode=explode, wedgeprops={'edgecolor': 'black', 'width': 0.3}
)

for text in texts + autotexts:
    text.set_fontsize(9)
    text.set_color('black')
for autotext in autotexts:
    autotext.set_fontweight('bold')

plt.title(
    'Detailed Global Distribution of Renewable Energy Sources in 2023\nAnalyzed by Subcategories', 
    fontsize=14, fontweight='bold', pad=20
)

plt.axis('equal')
plt.tight_layout()

plt.show()