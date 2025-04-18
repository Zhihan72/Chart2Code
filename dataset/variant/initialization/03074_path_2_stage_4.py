import matplotlib.pyplot as plt

# Additional data series are incorporated
energy_sources = ['Solar', 'Wind', 'Hydro', 'Bio', 'Geo', 'Ocean', 'Nuclear', 'Coal', 'Natural Gas']
energy_share = [30, 20, 15, 10, 5, 5, 5, 5, 5]
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A6', '#FFFF33', '#33FFF3', '#808080', '#654321', '#00FF00']
explode = (0.1, 0, 0, 0, 0, 0, 0, 0, 0)

fig, ax = plt.subplots(figsize=(10, 7))
wedges, texts, autotexts = ax.pie(
    energy_share, labels=energy_sources, autopct='%1.1f%%',
    startangle=140, colors=colors, explode=explode, shadow=True,
    textprops=dict(color='black'), wedgeprops=dict(width=0.3)
)

plt.setp(autotexts, size=10, weight="bold")
plt.setp(texts, size=12)

ax.set_title(
    "Global Energy Mix 2050", 
    fontsize=16, fontweight='bold', pad=20
)
ax.legend(
    wedges, energy_sources, title="Sources", loc="center left", 
    bbox_to_anchor=(1, 0, 0.5, 1)
)

plt.tight_layout()
plt.show()