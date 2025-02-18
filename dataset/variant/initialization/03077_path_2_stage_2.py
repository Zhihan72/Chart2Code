import matplotlib.pyplot as plt
import numpy as np

centuries = np.arange(14, 22)

classical = [60, 55, 45, 30, 20, 10, 5, 0]
renaissance = [20, 30, 40, 35, 25, 10, 5, 0]
baroque = [10, 10, 10, 20, 30, 40, 30, 0]
modernism = [5, 5, 10, 15, 20, 30, 40, 60]
abstract = [5, 0, 0, 0, 5, 10, 20, 40]
cubism = [0, 0, 5, 10, 15, 25, 30, 20]  # New art style added
popart = [0, 0, 0, 5, 10, 20, 30, 50]   # New art style added

famous_artworks = [150, 170, 220, 250, 300, 350, 400, 450]

# Updated data array with new art styles
data = np.array([classical, renaissance, baroque, modernism, abstract, cubism, popart])
styles = ['Classical', 'Renaissance', 'Baroque', 'Modernism', 'Abstract', 'Cubism', 'Pop Art']

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))

ax1.stackplot(centuries, data, labels=styles, alpha=0.8)
ax1.set_title("Time Travelers' Artistic Evolution\nExploration of Art Styles Across Centuries", fontsize=14, fontweight='bold', pad=20)
ax1.set_xlabel('Century', fontsize=12)
ax1.set_ylabel('Popularity (%)', fontsize=12)
ax1.legend(title='Artistic Styles', loc='upper left', bbox_to_anchor=(1, 1), fontsize=10)
ax1.text(14.5, 60, 'Classical Dominance', fontsize=10, color='darkred')
ax1.text(16.5, 75, 'Renaissance Bloom', fontsize=10, color='goldenrod')
ax1.text(18.5, 50, 'Modernism Rise', fontsize=10, color='navy')
ax1.grid(axis='x', color='gray', linestyle='--', linewidth=0.5)

ax2.plot(centuries, famous_artworks, marker='o', linestyle='-', color='darkcyan', label='Famous Artworks')
ax2.set_title('Trend of Famous Artworks Over Centuries', fontsize=14, fontweight='bold', pad=20)
ax2.set_xlabel('Century', fontsize=12)
ax2.set_ylabel('Number of Artworks', fontsize=12)
ax2.legend(loc='upper left', fontsize=10)
ax2.grid(axis='y', color='gray', linestyle='--', linewidth=0.5)

plt.tight_layout()
plt.show()