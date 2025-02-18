import matplotlib.pyplot as plt

art_movements = ['Renaissance', 'Baroque', 'Romanticism', 'Impressionism', 'Contemporary Art']
color_usage = [22, 18, 25, 15, 20]

fig, ax = plt.subplots(figsize=(10, 7))
wedges, texts, autotexts = ax.pie(color_usage, labels=art_movements, autopct='%1.1f%%',
                                  startangle=140, shadow=True, explode=(0.05, 0.05, 0.05, 0.05, 0.05))

plt.setp(autotexts, size=9, weight='bold', color='white')

plt.title("The Palette of Emotions:\nColor Preferences Across Art Movements", fontsize=15, fontweight='bold')

ax.axis('equal')

ax.legend(wedges, [f'{movement}' for movement in art_movements],
          title="Art Movements", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1), fontsize=9)

plt.tight_layout()
plt.show()