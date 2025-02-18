import matplotlib.pyplot as plt
import numpy as np

art_movements = ['Renaissance', 'Baroque', 'Romanticism', 'Impressionism', 'Contemporary Art']
color_usage = [22, 18, 25, 15, 20]

# Using a single color for all wedges
single_color = ['#4682B4']

fig, ax = plt.subplots(figsize=(10, 7))
wedges, texts, autotexts = ax.pie(color_usage, labels=art_movements, autopct='%1.1f%%',
                                  startangle=140, colors=single_color * len(art_movements), pctdistance=0.85,
                                  wedgeprops=dict(width=0.3), shadow=True, explode=(0.05, 0.05, 0.05, 0.05, 0.05))

plt.setp(autotexts, size=9, weight='bold', color='white')

plt.title("The Palette of Emotions:\nColor Preferences Across Art Movements", fontsize=15, fontweight='bold')

centre_circle = plt.Circle((0, 0), 0.7, fc='white')
fig.gca().add_artist(centre_circle)

ax.axis('equal')

# Legend adjustments to reflect consistent color usage
ax.legend(wedges, [f'{movement}' for movement in art_movements],
          title="Art Movements", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1), fontsize=9)

plt.tight_layout()
plt.show()