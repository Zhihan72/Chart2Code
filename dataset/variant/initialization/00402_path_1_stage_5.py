import matplotlib.pyplot as plt

energy_sources = ['Wind', 'Hydropower', 'Solar', 'Geothermal', 'Biomass']
percentages = [25, 18, 35, 10, 12]

colors = ['#FF6384', '#36A2EB', '#FFCE56', '#4BC0C0', '#9966FF']

fig, ax = plt.subplots(figsize=(8, 8))

wedges, texts, autotexts = ax.pie(
    percentages,
    labels=energy_sources,
    autopct='%1.1f%%',
    startangle=200,
    colors=colors
)

plt.setp(autotexts, size=10, weight='bold', color='darkblue')
plt.setp(texts, size=12)

ax.axis('equal')

plt.title("Renewable Sources' Power Shift:\nExploring Global Impact\nvia Green Technologies (2023)",
          pad=20, fontsize=14, fontweight='bold', color='darkgreen', ha='center')

plt.tight_layout()

plt.show()