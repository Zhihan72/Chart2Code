import matplotlib.pyplot as plt

energy_sources = ['Solar', 'Wind', 'Hydropower', 'Geothermal', 'Nuclear', 'Biomass', 'Fossil Fuels', 'Tidal Energy']
energy_percentages = [35, 25, 10, 5, 5, 3, 15, 2]

# New set of colors for the pie chart
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#33FFF0', '#FF9E33', '#C70039', '#900C3F']

fig, ax = plt.subplots(figsize=(10, 7), subplot_kw=dict(aspect='equal'))

explode = (0.1, 0, 0, 0, 0, 0, 0, 0)
wedges, texts, autotexts = ax.pie(
    energy_percentages,
    explode=explode,
    autopct='%1.1f%%',
    startangle=140,
    colors=colors,
    wedgeprops=dict(edgecolor='black', linewidth=1.5, width=0.3),
    shadow=True
)

plt.setp(autotexts, size=10, weight='bold', color='black')

ax.legend(
    wedges, energy_sources,
    loc="center left",
    bbox_to_anchor=(1, 0, 0.5, 1),
    fontsize=10
)

plt.tight_layout()
plt.show()