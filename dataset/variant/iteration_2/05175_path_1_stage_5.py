import matplotlib.pyplot as plt

energy_sources = ['Solar', 'Wind', 'Hydropower', 'Geothermal', 'Nuclear', 'Biomass', 'Fossil Fuels', 'Tidal Energy']
energy_percentages = [35, 25, 10, 5, 5, 3, 15, 2]

colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#33FFF0', '#FF9E33', '#C70039', '#900C3F']

fig, ax = plt.subplots(figsize=(10, 7), subplot_kw=dict(aspect='equal'))

# Alter exploded slices
explode = (0, 0, 0.1, 0, 0, 0, 0.1, 0)

# Alter wedge properties with different linewidths and edgecolors
wedges, texts, autotexts = ax.pie(
    energy_percentages,
    explode=explode,
    autopct='%1.1f%%',
    startangle=100,
    colors=colors,
    wedgeprops=dict(edgecolor='gray', linewidth=2, linestyle='--'),
    shadow=False  # Removing shadow for stylistic variation
)

# changing autotexts styling
plt.setp(autotexts, size=9, style='italic', color='darkblue')

# Move legend to a different position and use a border
ax.legend(
    wedges, energy_sources,
    loc="upper right",  # Changed location
    fontsize=9,
    frameon=True,  # Adding a border frame
    facecolor='lightgrey',  # Adding a background color
    edgecolor='black'
)

# Adding a grid for visual variation
ax.grid(True, linestyle=':', which='both', axis='both', color='grey')

plt.tight_layout()
plt.show()