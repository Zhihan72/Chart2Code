import matplotlib.pyplot as plt

energy_sources = ['Hydropower', 'Wind', 'Solar', 'Ocean', 'Geothermal']
energy_share = [20, 25, 30, 5, 5]

# Manually shuffled colors for each data group
colors = ['#FFD700', '#00FA9A', '#8B4513', '#87CEEB', '#4682B4']

explode = (0.05, 0, 0.1, 0, 0)

fig, ax = plt.subplots(figsize=(10, 7))
wedges, texts, autotexts = ax.pie(
    energy_share, labels=energy_sources, autopct='%1.1f%%',
    startangle=120, colors=colors, explode=explode, shadow=False,
    textprops=dict(color='blue'), wedgeprops=dict(width=0.35, edgecolor='grey')
)

plt.setp(autotexts, size=9, weight="normal")
plt.setp(texts, size=11)

ax.set_title(
    "Future Green Energy Distribution in 2050:\nMoving Towards Sustainability", 
    fontsize=14, fontweight='normal', pad=15
)

ax.grid(visible=True, linestyle='--', color='grey')

plt.tight_layout()
plt.show()