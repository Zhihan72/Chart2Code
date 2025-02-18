import matplotlib.pyplot as plt

energy_sources = ['Wind', 'Solar', 'Bio', 'Hydro', 'Nuc', 'Geo']
energy_percentages = [30, 40, 4, 12, 6, 8]
colors = ['#00CED1', '#1E90FF', '#FF4500', '#8B4513', '#9400D3', '#FFD700']

fig, ax = plt.subplots(figsize=(10, 7), subplot_kw=dict(aspect='equal'))

explode = (0, 0.1, 0, 0, 0, 0)
wedges, texts, autotexts = ax.pie(
    energy_percentages,
    explode=explode,
    labels=energy_sources,
    autopct='%1.1f%%',
    startangle=120,
    colors=colors,
    wedgeprops=dict(edgecolor='gray', linewidth=3, linestyle='dashdot', width=0.5)
)

plt.title("Energy Sources 2050", fontsize=16, fontweight='bold', pad=20, color='darkgreen')

plt.setp(autotexts, size=12, weight='normal', color='slategray')
plt.setp(texts, size=10, weight='light')

ax.legend(
    wedges, energy_sources,
    loc="upper center",
    bbox_to_anchor=(0.5, -0.05),
    ncol=3,
    fontsize=12
)

ax.grid(True, which='both', linestyle='--', linewidth=0.5)

plt.tight_layout()
plt.show()