import matplotlib.pyplot as plt
import numpy as np

art_movements = ['Renaissance', 'Baroque', 'Romantic', 'Impression', 'Modern', 'Contemporary']
museum_counts = [150, 100, 80, 120, 90, 60]

fig, ax = plt.subplots(figsize=(14, 8))

# Shuffled colors manually
colors = ['#C0C0C0', '#87CEEB', '#FFD700', '#D3A9A9', '#800080', '#A2D9A2']

bars = ax.barh(art_movements, museum_counts, color=colors, edgecolor='black')

for bar in bars:
    xval = bar.get_width()
    ax.text(
        xval,
        bar.get_y() + bar.get_height() / 2,
        f'{xval}',
        va='center',
        ha='left',
        fontsize=10,
        fontweight='bold'
    )

ax.set_title(
    'Art Movements in Museums',
    fontsize=16, fontweight='bold'
)
ax.set_xlabel('No. of Museums', fontsize=12)
ax.set_ylabel('Movements', fontsize=12)

plt.yticks(rotation=0)

ax.legend(bars, art_movements, title='Movements', title_fontsize='13', loc='lower right', fontsize='10')

ax.grid(True, linestyle='--', alpha=0.5, axis='x')

plt.tight_layout()

plt.show()