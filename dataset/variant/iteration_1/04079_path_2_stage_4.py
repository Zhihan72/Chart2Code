import matplotlib.pyplot as plt

energy_sources = ['Solar', 'Wind', 'Hydro', 'Geothermal', 'Biomass', 'Nuclear', 'Coal']
contributions = [30, 20, 15, 10, 10, 10, 5]
colors = ['#99ff99', '#ffb3e6', '#ff6666', '#66b3ff', '#ffcc00', '#ccccff', '#ffcc99']

fig, ax = plt.subplots(figsize=(10, 8))

# Draw a donut chart (ring pie chart)
wedges, texts, autotexts = ax.pie(
    contributions,
    labels=energy_sources,
    colors=colors,
    autopct='%1.1f%%',
    startangle=90,
    wedgeprops=dict(width=0.3, edgecolor='gray', linestyle='--', linewidth=1.5),
    explode=[0.1 if x == 'Solar' else 0 for x in energy_sources],
    shadow=False,
    textprops={'fontsize': 10, 'family': 'serif'}
)

# Set aspect ratio to equal for a circular pie chart
ax.axis('equal')

plt.setp(autotexts, size=10, weight='bold', color='blue')
plt.setp(texts, size=10, style='italic')

plt.title(
    "Energy Contribution (2023)",
    fontsize=14, weight='bold', color='darkgreen', pad=15
)

ax.legend(
    wedges, energy_sources,
    title="Sources",
    loc="upper right",
    fontsize=9,
    frameon=False
)

plt.tight_layout()

plt.show()