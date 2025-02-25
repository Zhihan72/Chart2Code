import matplotlib.pyplot as plt

energy_sources = ['Solar', 'Wind', 'Hydro', 'Geo', 'Nuc', 'Bio']
energy_percentages = [40, 30, 12, 8, 6, 4]
colors = ['#1E90FF', '#00CED1', '#8B4513', '#FFD700', '#9400D3', '#FF4500']

fig, ax = plt.subplots(figsize=(10, 7), subplot_kw=dict(aspect='equal'))

explode = (0.1, 0, 0, 0, 0, 0)
wedges, texts, autotexts = ax.pie(
    energy_percentages,
    explode=explode,
    labels=energy_sources,
    autopct='%1.1f%%',
    startangle=140,
    colors=colors,
    wedgeprops=dict(edgecolor='black', linewidth=1.5, width=0.3),
    shadow=True
)

plt.title("Energy Sources 2050", fontsize=14, fontweight='bold', pad=20)

plt.setp(autotexts, size=10, weight='bold', color='black')
plt.setp(texts, size=10, weight='bold')

ax.legend(
    wedges, energy_sources,
    title="Sources",
    loc="center left",
    bbox_to_anchor=(1, 0, 0.5, 1),
    fontsize=10
)

plt.tight_layout()
plt.show()