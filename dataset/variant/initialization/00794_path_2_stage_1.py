import matplotlib.pyplot as plt
import numpy as np

art_movements = ['Renaissance', 'Baroque', 'Romanticism', 'Impressionism', 'Contemporary Art']
color_usage = [20, 25, 18, 22, 15]

colors = ['#4682B4', '#FFD700', '#003366', '#8B0000', '#FFE4B5']
patterns = ['o', '.', '-', '+', '/']

fig, ax = plt.subplots(figsize=(10, 8))
wedges, texts, autotexts = ax.pie(
    color_usage, 
    labels=art_movements, 
    autopct='%1.1f%%',
    startangle=90, 
    colors=colors, 
    pctdistance=0.8,
    wedgeprops=dict(width=0.4, edgecolor='gray', linestyle='-', hatch=patterns, linewidth=2),
    shadow=True, 
    explode=(0.05,) * len(art_movements)
)

plt.setp(autotexts, size=10, weight='normal', color='gray')
plt.setp(texts, size=10, style='normal')

plt.title("Art Movements and Color Usage", fontsize=14, family='monospace')

centre_circle = plt.Circle((0, 0), 0.6, fc='white', edgecolor='gray', lw=2)
fig.gca().add_artist(centre_circle)

ax.axis('equal')

legend_labels = [f'{movement}: {color}' for movement, color in zip(art_movements, ['Vibrant', 'Brilliant', 'Sophisticated', 'Classic', 'Warm'])]
ax.legend(
    wedges, legend_labels, 
    title="Movements", 
    loc="upper right", 
    bbox_to_anchor=(1, 1), 
    fontsize=8
)

plt.tight_layout()

plt.show()