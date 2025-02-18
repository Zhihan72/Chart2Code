import matplotlib.pyplot as plt

energy_sources = [
    'Solar - Photovoltaic', 'Wind - Onshore', 
    'Solar - Thermal', 'Wind - Offshore', 
    'Hydropower - Conventional', 'Hydropower - Pumped', 
    'Biomass - Solid', 'Biomass - Liquid',
    'Geothermal', 'Wave', 'Tidal', 'Others'
]

percentages = [15.5, 13, 14.5, 12, 10, 10, 7, 6, 5, 2, 3, 2]

colors = [
    '#FFEC8B', '#4682B4', 
    '#FFD700', '#87CEEB', 
    '#228B22', '#32CD32', 
    '#8B4513', '#D2691E', 
    '#6495ED', '#B0C4DE', 
    '#FF6347', '#1E90FF'
]

explode = (0.1, 0.1, 0, 0, 0.1, 0, 0, 0, 0, 0, 0, 0)

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