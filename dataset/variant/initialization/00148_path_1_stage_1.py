import matplotlib.pyplot as plt
import numpy as np

sectors = ['Residential', 'Agricultural', 'Industrial', 'Recreational', 'Commercial']
water_usage = np.array([120, 80, 50, 30, 70])
colors = ['#66c2a5', '#fc8d62', '#8da0cb', '#e78ac3', '#a6d854']

fig, ax = plt.subplots(figsize=(9, 9))

wedges, texts, autotexts = ax.pie(
    water_usage,
    labels=sectors,
    autopct='%1.1f%%',
    colors=colors,
    startangle=90
)

plt.setp(texts, size=12, weight='bold', va='center')
plt.setp(autotexts, size=12, color='white', weight='bold')

ax.set_title("Water Usage in AquaRidge Eco-City\nOptimizing Resources for Sustainability", 
             fontsize=16, fontweight='bold', loc='center')

ax.axis('equal')

ax.legend(wedges, sectors, title="Sectors", loc="center left", bbox_to_anchor=(1, 0.5), fontsize=10)

plt.tight_layout()
plt.show()