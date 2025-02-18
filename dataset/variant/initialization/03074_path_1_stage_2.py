import matplotlib.pyplot as plt

energy_sources = ['Hydropower', 'Biomass', 'Wind', 'Solar', 'Ocean', 'Geothermal']
energy_share = [20, 15, 25, 30, 5, 5]
colors = ['#00FA9A', '#8B4513', '#87CEEB', '#FFD700', '#4682B4', '#FF6347']
explode = (0.1, 0, 0, 0, 0, 0)

fig, ax = plt.subplots(figsize=(10, 7))
wedges, texts, autotexts = ax.pie(
    energy_share, labels=energy_sources, autopct='%1.1f%%',
    startangle=140, colors=colors, explode=explode, shadow=True,
    textprops=dict(color='black'), wedgeprops=dict(width=0.3)
)

plt.setp(autotexts, size=10, weight="bold")
plt.setp(texts, size=12)

ax.set_title(
    "Future Green Energy Distribution in 2050:\nTowards Sustainability", 
    fontsize=16, fontweight='bold', pad=20
)
ax.legend(
    wedges, energy_sources, title="Power Categories", loc="center left", 
    bbox_to_anchor=(1, 0, 0.5, 1)
)

plt.tight_layout()
plt.show()