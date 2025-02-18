import matplotlib.pyplot as plt

art_movements = ['Renaissance', 'Baroque', 'Romanticism', 'Impressionism', 'Contemporary Art', 'Cubism', 'Surrealism']
color_usage = [20, 25, 18, 22, 15, 12, 8]

colors = ['#4682B4', '#FFD700', '#003366', '#8B0000', '#FFE4B5', '#FF6347', '#8A2BE2']

fig, ax = plt.subplots(figsize=(10, 8))
wedges, texts, autotexts = ax.pie(
    color_usage, 
    labels=art_movements, 
    autopct='%1.1f%%',
    startangle=90, 
    colors=colors, 
    shadow=True, 
    explode=(0.05,) * len(art_movements)
)

plt.setp(autotexts, size=10, weight='normal', color='gray')
plt.setp(texts, size=10, style='normal')

plt.title("Art Movements and Color Usage", fontsize=14, family='monospace')

ax.axis('equal')

legend_labels = [f'{movement}: {color}' for movement, color in zip(art_movements, ['Vibrant', 'Brilliant', 'Sophisticated', 'Classic', 'Warm', 'Avant-garde', 'Dreamlike'])]
ax.legend(
    wedges, legend_labels, 
    title="Movements", 
    loc="upper right", 
    bbox_to_anchor=(1, 1), 
    fontsize=8
)

plt.tight_layout()

plt.show()