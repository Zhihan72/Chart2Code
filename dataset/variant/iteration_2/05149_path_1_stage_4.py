import matplotlib.pyplot as plt

energy_sources = ['GeoThermal', 'Hydro Power', 'Bio Mass', 'Solar', 'Wind Power', 'Alternative']
consumption_percentages = [10, 15, 10, 35, 25, 5]

colors = ['#ffcc99', '#66b3ff', '#ffb3e6', '#c2c2f0', '#ff9999', '#99ff99']
explode = (0, 0.1, 0, 0, 0, 0)

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