import matplotlib.pyplot as plt
import numpy as np

# Altered names for the art movements and altered annotations
art_movements_shuffled = ['Impressionism', 'Contemporary Art', 'Baroque', 'Renaissance', 'Romanticism']
color_usage = [22, 15, 25, 20, 18]

# Adjusted title and legend title
fig, ax = plt.subplots(figsize=(12, 8))
wedges, texts, autotexts = ax.pie(
    color_usage, 
    labels=art_movements_shuffled, 
    autopct='%1.1f%%',
    startangle=140, 
    colors=['#4682B4'] * len(color_usage),  # Same color remains
    shadow=True
)

plt.setp(autotexts, size=9, weight='bold', color='white')
plt.setp(texts, size=11, style='italic')

# Randomly altered title
plt.title("What Colors Reflect:\nArt Declinations and Their Preferences", fontsize=15, fontweight='bold', family='serif')

# Shuffled legend labels
legend_labels_shuffled = [f'{movement}: Uniform Color' for movement in art_movements_shuffled]
ax.legend(
    wedges, legend_labels_shuffled, 
    title="Art Styles",  # Altered legend title
    loc="center left", 
    bbox_to_anchor=(1, 0, 0.5, 1), 
    fontsize=9
)

# Shuffled and slightly altered annotations
annotations_shuffled = [
    "Light hues and fast strokes",
    "Innovative approaches & variety",
    "Lavish details & stunning grandeur",
    "Revivalism & classic echoes",
    "Personal expression and deep emotions"
]
for i, wedge in enumerate(wedges):
    angle = (wedge.theta2 - wedge.theta1) / 2. + wedge.theta1
    x = 1.1 * np.cos(np.radians(angle))
    y = 1.1 * np.sin(np.radians(angle))
    ax.annotate(
        annotations_shuffled[i], xy=(x, y), xytext=(x*1.25, y*1.25),
        arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"), fontsize=9, family='serif'
    )

plt.tight_layout()

plt.show()