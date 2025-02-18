import matplotlib.pyplot as plt
import numpy as np

art_movements = ['Renaissance', 'Baroque', 'Romanticism', 'Impressionism', 'Contemporary Art']
color_usage = [20, 25, 18, 22, 15]

# Set a single color for all data groups
single_color = ['#4682B4']  # Steel Blue

fig, ax = plt.subplots(figsize=(12, 8))
wedges, texts, autotexts = ax.pie(
    color_usage, 
    labels=art_movements, 
    autopct='%1.1f%%',
    startangle=140, 
    colors=single_color * len(color_usage),  # Apply the single color to all wedges
    shadow=True
)

plt.setp(autotexts, size=9, weight='bold', color='white')
plt.setp(texts, size=11, style='italic')

plt.title("The Palette of Emotions:\nColor Preferences Across Art Movements", fontsize=15, fontweight='bold', family='serif')

ax.axis('equal')

legend_labels = [f'{movement}: {desc}' for movement, desc in zip(art_movements, ['Uniform Color'] * len(art_movements))]
ax.legend(
    wedges, legend_labels, 
    title="Art Movements", 
    loc="center left", 
    bbox_to_anchor=(1, 0, 0.5, 1), 
    fontsize=9
)

annotations = [
    "Era of rebirth and classical influence",
    "Excessive ornamentation and grandeur",
    "Emphasis on emotion and individualism",
    "Light and color nuances with rapid brushwork",
    "Modern innovations and diverse expressions"
]
for i, wedge in enumerate(wedges):
    angle = (wedge.theta2 - wedge.theta1) / 2. + wedge.theta1
    x = 1.1 * np.cos(np.radians(angle))
    y = 1.1 * np.sin(np.radians(angle))
    ax.annotate(
        annotations[i], xy=(x, y), xytext=(x*1.25, y*1.25),
        arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"), fontsize=9, family='serif'
    )

plt.tight_layout()

plt.show()