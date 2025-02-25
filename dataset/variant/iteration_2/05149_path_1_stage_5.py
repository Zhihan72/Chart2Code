import matplotlib.pyplot as plt

# Existing and new energy sources
energy_sources = [
    'GeoThermal', 'Hydro Power', 'Bio Mass', 'Solar', 'Wind Power', 
    'Alternative', 'Nuclear', 'Fossil Fuels', 'Hydrogen'
]
# Corresponding consumption percentages summing up to 100
consumption_percentages = [8, 12, 8, 28, 20, 4, 5, 10, 5]

# Update the color list to match the new energy sources
colors = ['#ffcc99', '#66b3ff', '#ffb3e6', '#c2c2f0', '#ff9999', '#99ff99', '#ff6666', '#66ff66', '#6666ff']
# Adjust explosion if desired, here keeping a single category highlighted for consistency
explode = (0, 0.1, 0, 0, 0, 0, 0, 0, 0)

fig, ax = plt.subplots(figsize=(8, 8))

ax.pie(
    consumption_percentages,
    explode=explode,
    labels=energy_sources,
    colors=colors,
    autopct='%1.1f%%',
    startangle=90,
    textprops={'fontsize': 10},
    shadow=False
)

plt.title('Eco Stats: 2023 Energy Usage\nCommunity Insights', fontsize=14, fontweight='bold', pad=15)
plt.legend(title="Alt Energy Sources", loc="upper right", bbox_to_anchor=(1, 1), markerfirst=False)

plt.tight_layout()
plt.show()