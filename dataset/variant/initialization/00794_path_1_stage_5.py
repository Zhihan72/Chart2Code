import matplotlib.pyplot as plt
import numpy as np

# Manually shuffled the art movements and corresponding color usage
art_movements_shuffled = ['Contemporary Art', 'Romanticism', 'Impressionism', 'Renaissance', 'Baroque']
color_usage_shuffled = [25, 22, 20, 18, 15]

fig, ax = plt.subplots(figsize=(10, 6))

# Kept colors and other attributes the same, just rearranged labels and data
wedges, texts, autotexts = ax.pie(
    color_usage_shuffled, 
    labels=art_movements_shuffled, 
    autopct='%1.1f%%', 
    startangle=90, 
    colors=['#FFD700', '#8A2BE2', '#3CB371', '#FF69B4', '#FF6347'], 
    shadow=False
)

plt.setp(autotexts, size=10, weight='light', color='black')
plt.setp(texts, size=12, family='fantasy')

plt.title("The Spectrum of Art Forms", fontsize=14, style='italic', family='monospace')

# Manually shuffled legend labels
legend_labels_shuffled = [
    'Contemporary Art: Unique Color',
    'Romanticism: Unique Color', 
    'Impressionism: Unique Color', 
    'Renaissance: Unique Color', 
    'Baroque: Unique Color'
]
ax.legend(
    wedges, legend_labels_shuffled, 
    title="Art Types", 
    loc="upper right", 
    bbox_to_anchor=(0.9, 1), 
    fontsize=8,
    frameon=False
)

# Manually shuffled annotations
annotations_shuffled = [
    "Avant-garde trends & unexpected mediums",
    "Emotional depth & personal resonance",
    "Lighter colors & delicate brushwork",
    "Echoes of classic art & rebirth",
    "Rich ornamentation & elaborate form"
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