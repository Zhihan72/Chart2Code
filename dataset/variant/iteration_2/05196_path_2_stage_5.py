import matplotlib.pyplot as plt

planets = ["Mars", "Moon", "Europa", "Titan", "Ganymede", "Callisto", "Venus"]
funding_percentages = [35, 25, 15, 10, 7, 3, 3]
colors = ['#c2c2f0', '#ff6666', '#66b3ff', '#ffcc99', '#ffb366', '#99ff99', '#ff9999']

fig, ax = plt.subplots(figsize=(8, 8), facecolor='#f0f0f0')
wedges, texts, autotexts = ax.pie(
    funding_percentages,
    labels=planets,
    colors=colors,
    autopct='%1.1f%%',
    startangle=180,
    textprops=dict(color="navy"),
    wedgeprops=dict(edgecolor='black', linestyle='--', linewidth=1.5, width=0.4)
)

plt.setp(autotexts, size=12, weight="light")
plt.setp(texts, size=10, color='teal')

ax.set_title(
    'Funding Distribution 2050',
    fontsize=16,
    fontweight='light', 
    color='teal',
    pad=25
)

ax.legend(
    wedges,
    planets,
    loc="best",
    fontsize=9,
    title_fontsize=11,
    frameon=False
)

ax.set_aspect('equal')
plt.tight_layout()
plt.show()