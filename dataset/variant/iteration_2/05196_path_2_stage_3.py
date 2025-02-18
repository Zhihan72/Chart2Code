import matplotlib.pyplot as plt

planets = ["Mars", "Moon", "Europa", "Titan", "Ganymede", "Callisto", "Venus"]
funding_percentages = [35, 25, 15, 10, 7, 3, 3]
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0','#ffb366','#ff6666']

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
    'Solar System Colonization Initiatives\nPublic Funding Distribution in 2050',
    fontsize=16,
    fontweight='light', 
    color='teal',
    pad=30
)

ax.legend(
    wedges,
    [f"{planet}: {percentage}%" for planet, percentage in zip(planets, funding_percentages)],
    loc="best",
    fontsize=9,
    title_fontsize=11,
    frameon=False
)

ax.set_aspect('equal')
plt.tight_layout()
plt.show()