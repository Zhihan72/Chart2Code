import matplotlib.pyplot as plt
import numpy as np

art_movements = ['Renaissance', 'Baroque', 'Romantic', 'Impression', 'Modern']
museum_counts = [150, 100, 80, 120, 90]

fig, ax = plt.subplots(figsize=(14, 8))

# Randomly altered coloring and edge styles
colors = ['#FFD700', '#C0C0C0', '#800080', '#87CEEB', '#D3A9A9']
edge_colors = ['black', 'darkred', 'navy', 'darkgreen', 'teal']

bars = ax.barh(art_movements, museum_counts, color=colors, edgecolor=edge_colors, linestyle='dotted', linewidth=1.5)

# Altered annotation styles
for bar in bars:
    xval = bar.get_width()
    ax.text(
        xval + 5,  # shifted the text to the right
        bar.get_y() + bar.get_height() / 2,
        f'{xval}',
        va='center',
        ha='left',
        fontsize=12,  # changed font size
        fontweight='normal',  # changed font weight
        color='darkblue'  # changed text color
    )

# Modified title and labels
ax.set_title(
    'Various Art Movements Represented in Museums',
    fontsize=18, fontweight='normal'
)
ax.set_xlabel('Number of Museums', fontsize=14)
ax.set_ylabel('Art Movements', fontsize=14)

plt.yticks(rotation=0)

# Randomly changed legend placement and style
ax.legend(bars, art_movements, title='Art Movements',
          title_fontsize='11', loc='upper left', fontsize='10')

# Randomly altered grid style
ax.grid(True, linestyle='-', alpha=0.8, axis='y')

plt.tight_layout()

plt.show()