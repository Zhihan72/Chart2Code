import matplotlib.pyplot as plt

energy_sources = ['Wind', 'Biomass', 'Solar', 'Nuclear', 'Hydro', 'Coal', 'Geothermal']
contributions = [20, 10, 30, 10, 15, 5, 10]
colors = ['#ffb3e6', '#ffcc00', '#99ff99', '#ccccff', '#66b3ff', '#ffcc99', '#ff6666']

fig, ax = plt.subplots(figsize=(10, 8))

wedges, texts, autotexts = ax.pie(
    contributions,
    labels=energy_sources,
    colors=colors,
    autopct='%1.1f%%',
    startangle=90,
    wedgeprops=dict(width=0.3, edgecolor='gray', linestyle='--', linewidth=1.5),
    explode=[0 if x != 'Nuclear' else 0.1 for x in energy_sources],
    shadow=False,
    textprops={'fontsize': 10, 'family': 'serif'}
)

ax.axis('equal')

plt.setp(autotexts, size=10, weight='bold', color='blue')
plt.setp(texts, size=10, style='italic')

# Title and legend have been randomly modified
plt.title(
    "Power Resource Distribution (Randomized)",
    fontsize=14, weight='bold', color='darkgreen', pad=15
)

ax.legend(
    wedges, energy_sources,
    title="Power Types",
    loc="upper right",
    fontsize=9,
    frameon=False
)

plt.tight_layout()

plt.show()