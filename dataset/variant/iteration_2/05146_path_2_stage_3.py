import matplotlib.pyplot as plt
import numpy as np

sectors = ['Alpha', 'Beta', 'Gamma', 'Delta', 'Epsilon']
elements_discovered = np.array([35, 20, 15, 18, 12])

# Updated colors and marker types
colors = ['#FF6347', '#4682B4', '#32CD32', '#FFD700', '#8A2BE2']

fig, ax = plt.subplots(figsize=(10, 7))
wedges, texts, autotexts = ax.pie(
    elements_discovered,
    labels=sectors,
    colors=colors,
    autopct='%1.1f%%',
    startangle=90,  # Altered angle
    wedgeprops=dict(edgecolor='grey', linestyle='-.'),  # Changed line style and color
    explode=(0.1, 0, 0.2, 0, 0),  # Updated explode settings
    shadow=False  # Removed shadow for a simpler style
)

plt.setp(autotexts, size=10, weight="normal", color="darkgreen")  # Modified text properties
plt.setp(texts, size=10, color="darkred")

# Adjusted legend properties and position
ax.legend(wedges, sectors, title="Galactic Sectors",
          loc="upper right", bbox_to_anchor=(1.1, 1), fontsize=9)

# Simplified title style
ax.set_title("Elements Distribution in the Galaxy", fontsize=14, color='darkorange', pad=15)

plt.grid(visible=True, linestyle=':', color='grey', linewidth=0.5)  # Added a grid

plt.tight_layout()
plt.show()