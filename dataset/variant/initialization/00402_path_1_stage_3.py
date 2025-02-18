import matplotlib.pyplot as plt

energy_sources = ['Wind', 'Hydropower', 'Solar', 'Geothermal', 'Biomass']
percentages = [25, 18, 35, 10, 12]

# New set of colors for the chart
colors = ['#FF6384', '#36A2EB', '#FFCE56', '#4BC0C0', '#9966FF']

fig, ax = plt.subplots(figsize=(8, 8))

wedges, texts, autotexts = ax.pie(
    percentages,
    labels=energy_sources,
    autopct='%1.1f%%',
    startangle=200,
    colors=colors,
    pctdistance=0.75,
    wedgeprops=dict(width=0.3, edgecolor='w'),
    explode=[0.1 if energy == 'Solar' else 0 for energy in energy_sources],
    shadow=True
)

plt.setp(autotexts, size=10, weight='bold', color='darkblue')
plt.setp(texts, size=12)

ax.axis('equal')

plt.title("Renewable Sources' Power Shift:\nExploring Global Impact\nvia Green Technologies (2023)",
          pad=20, fontsize=14, fontweight='bold', color='darkgreen', ha='center')

ax.legend(wedges, energy_sources, title="Eco Power Types", loc='center left',
          bbox_to_anchor=(1, 0, 0.5, 1), fontsize='medium', frameon=False)

plt.tight_layout()

plt.show()