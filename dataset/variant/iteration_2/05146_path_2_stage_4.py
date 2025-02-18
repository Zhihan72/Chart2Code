import matplotlib.pyplot as plt
import numpy as np

# Shortened labels
sectors = ['A', 'B', 'G', 'D', 'E']
elements_discovered = np.array([35, 20, 15, 18, 12])

colors = ['#FF6347', '#4682B4', '#32CD32', '#FFD700', '#8A2BE2']

fig, ax = plt.subplots(figsize=(10, 7))
wedges, texts, autotexts = ax.pie(
    elements_discovered,
    labels=sectors,
    colors=colors,
    autopct='%1.1f%%',
    startangle=90,
    wedgeprops=dict(edgecolor='grey', linestyle='-.'),
    explode=(0.1, 0, 0.2, 0, 0),
    shadow=False
)

plt.setp(autotexts, size=10, weight="normal", color="darkgreen")
plt.setp(texts, size=10, color="darkred")

ax.legend(wedges, sectors, title="Sectors",
          loc="upper right", bbox_to_anchor=(1.1, 1), fontsize=9)

# Shortened title
ax.set_title("Galaxy Elements", fontsize=14, color='darkorange', pad=15)

plt.grid(visible=True, linestyle=':', color='grey', linewidth=0.5)

plt.tight_layout()
plt.show()