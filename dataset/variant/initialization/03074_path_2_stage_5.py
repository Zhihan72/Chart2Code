import matplotlib.pyplot as plt

energy_sources = ['Solar', 'Wind', 'Hydro', 'Bio', 'Geo', 'Ocean', 'Nuclear', 'Coal', 'Natural Gas']
energy_share = [30, 20, 15, 10, 5, 5, 5, 5, 5]
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A6', '#FFFF33', '#33FFF3', '#808080', '#654321', '#00FF00']
explode = (0.1, 0, 0, 0, 0, 0, 0, 0, 0)

fig, ax = plt.subplots(figsize=(10, 7))
wedges, texts, autotexts = ax.pie(
    energy_share, labels=energy_sources, autopct='%0.2f%%',
    startangle=110, colors=colors, explode=explode, shadow=False,
    textprops=dict(color='blue'), wedgeprops=dict(linestyle='--')
)

plt.setp(autotexts, size=9, weight='medium')
plt.setp(texts, size=11)

ax.set_title(
    "Projected Energy Mix for 2050", 
    fontsize=18, fontweight='normal', pad=15
)
ax.legend(
    wedges, energy_sources, title="Energy Sources", loc="upper right", 
    bbox_to_anchor=(0.8, 0.1, 1, 0.2)
)

ax.grid(True, linestyle=':', linewidth=0.5)
ax.spines['bottom'].set_linestyle('-.')  # Adding a border with different style

plt.tight_layout()
plt.show()