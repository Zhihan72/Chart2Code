import matplotlib.pyplot as plt
import numpy as np

sectors = ['Alpha', 'Beta', 'Gamma', 'Delta', 'Epsilon']
elements_discovered = np.array([35, 20, 15, 18, 12])

# Manually shuffled colors for each sector
colors = ['#FFD700', '#32CD32', '#1E90FF', '#8A2BE2', '#FF69B4']

fig, ax = plt.subplots(figsize=(10, 7))
wedges, texts, autotexts = ax.pie(
    elements_discovered,
    labels=sectors,
    colors=colors,
    autopct='%1.1f%%',
    startangle=140,
    wedgeprops=dict(edgecolor='w'),
    explode=(0.1, 0, 0, 0, 0.2),
    shadow=True
)

plt.setp(autotexts, size=12, weight="bold", color="black")
plt.setp(texts, size=12, color="darkblue")

ax.legend(wedges, sectors, title="Galactic Sectors", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1), fontsize=10)

ax.set_title("Distribution of Elements in the Galaxy (2023)\nDiscoveries by Galactic Explorers", fontsize=16, fontweight='bold', color='royalblue', pad=20)

plt.tight_layout()
plt.show()