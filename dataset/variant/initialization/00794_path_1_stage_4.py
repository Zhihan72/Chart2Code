import matplotlib.pyplot as plt
import numpy as np

art_movements_shuffled = ['Romanticism', 'Baroque', 'Contemporary Art', 'Impressionism', 'Renaissance']
color_usage = [22, 15, 25, 20, 18]

fig, ax = plt.subplots(figsize=(10, 6))

wedges, texts, autotexts = ax.pie(
    color_usage, 
    labels=art_movements_shuffled, 
    autopct='%1.1f%%', 
    startangle=90, 
    colors=['#8A2BE2', '#FF6347', '#FFD700', '#3CB371', '#FF69B4'], 
    shadow=False
)

plt.setp(autotexts, size=10, weight='light', color='black')
plt.setp(texts, size=12, family='fantasy')

plt.title("The Spectrum of Art Forms", fontsize=14, style='italic', family='monospace')

legend_labels_shuffled = [f'{movement}: Unique Color' for movement in art_movements_shuffled]
ax.legend(
    wedges, legend_labels_shuffled, 
    title="Art Types", 
    loc="upper right", 
    bbox_to_anchor=(0.9, 1), 
    fontsize=8,
    frameon=False
)

annotations_shuffled = [
    "Emotional depth & personal resonance",
    "Rich ornamentation & elaborate form",
    "Avant-garde trends & unexpected mediums",
    "Lighter colors & delicate brushwork",
    "Echoes of classic art & rebirth"
]

for i, wedge in enumerate(wedges):
    angle = (wedge.theta2 - wedge.theta1) / 2. + wedge.theta1
    x = 1.2 * np.cos(np.radians(angle))
    y = 1.2 * np.sin(np.radians(angle))
    ax.annotate(
        annotations_shuffled[i], xy=(x, y), xytext=(x*1.3, y*1.3),
        arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.15"), fontsize=8, style='italic'
    )

plt.grid(axis='x', linestyle='--', linewidth=0.5)
plt.tight_layout()

plt.show()