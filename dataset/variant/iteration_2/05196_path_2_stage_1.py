import matplotlib.pyplot as plt
import numpy as np

planets = ["Mars", "Moon", "Europa", "Titan", "Ganymede", "Callisto", "Venus", "Ceres"]
funding_percentages = [35, 25, 15, 10, 7, 3, 3, 2]

colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0','#ffb366','#ff6666','#c2f0c2']

fig, ax = plt.subplots(figsize=(12, 8), facecolor='#f0f0f0')
wedges, texts, autotexts = ax.pie(funding_percentages, labels=planets, colors=colors,
                                  autopct='%1.1f%%', startangle=180, textprops=dict(color="navy"),
                                  wedgeprops=dict(edgecolor='black', linestyle='--', linewidth=1.5))

plt.setp(autotexts, size=12, weight="light")
plt.setp(texts, size=10, color='teal')

ax.set_title('Solar System Colonization Initiatives\nPublic Funding Distribution in 2050',
             fontsize=16, fontweight='light', color='teal', pad=30)

ax.legend(wedges, [f"{planet}: {percentage}%" for planet, percentage in zip(planets, funding_percentages)],
          loc="lower left", bbox_to_anchor=(-0.1, -0.2, 0.5, 1), ncol=2, fontsize=9, title_fontsize=11, frameon=False)

ax.set_aspect('equal')

funding_amounts = [350, 250, 150, 100, 70, 30, 30, 20]
ax_bar = fig.add_subplot(212)
x_pos = np.arange(len(planets))
bars = ax_bar.bar(x_pos, funding_amounts, color=colors, edgecolor='#333333', linestyle=':', linewidth=1.2)

ax_bar.set_title('Comparative Funding Amounts\nFor Solar System Colonization (in Billion USD)', fontsize=14, weight='light')
ax_bar.set_xlabel('Celestial Bodies', fontsize=12, color='maroon')
ax_bar.set_ylabel('Funding Amount (Billion USD)', fontsize=12, color='maroon')
ax_bar.set_xticks(x_pos)
ax_bar.set_xticklabels(planets, rotation=60, ha='right', fontsize=10)
ax_bar.yaxis.grid(True, linestyle='-', linewidth=0.7, color='gray')

for bar in bars:
    height = bar.get_height()
    ax_bar.text(bar.get_x() + bar.get_width() / 2, height + 5, f"${height}B", ha='center', va='bottom', fontsize=9, color='brown')

plt.tight_layout()
plt.show()