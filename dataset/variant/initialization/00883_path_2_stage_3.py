import matplotlib.pyplot as plt
import numpy as np

art_movements = ['Impressionism', 'Art Deco', 'Minimalism', 'Surrealism']

influence_matrix = np.array([
    [7, 5, 3, 4, 6],  # Impressionism
    [4, 7, 5, 3, 6],  # Art Deco
    [3, 4, 9, 8, 5],  # Minimalism
    [5, 6, 4, 7, 8],  # Surrealism
])

avg_influence = np.mean(influence_matrix, axis=1)

fig, ax = plt.subplots(figsize=(10, 8))

# New set of colors, one for each bar
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']
bar = ax.barh(art_movements, avg_influence, color=colors)

ax.set_title("Average Influence of Art Movements\non Modern Design Styles", fontsize=16, weight='bold', pad=20)
ax.set_xlabel("Average Influence Level", fontsize=12, labelpad=20)
ax.set_ylabel("Historical Art Movements", fontsize=12, labelpad=20)

for rect in bar:
    width = rect.get_width()
    ax.annotate(f'{width:.1f}',
                xy=(width, rect.get_y() + rect.get_height() / 2),
                xytext=(3, 0),  # 3 points horizontal offset
                textcoords="offset points",
                ha='left', va='center', fontsize=12, color='darkred')

plt.show()