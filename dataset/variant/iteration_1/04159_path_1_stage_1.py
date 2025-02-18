import matplotlib.pyplot as plt
import numpy as np

# Artistic Movements and Museum Representation

art_movements = ['Ren', 'Bar', 'Rom', 'Imp', 'Mod', 'Cont']
museum_counts = [150, 100, 80, 120, 90, 60]
colors = ['#FFD700', '#C0C0C0', '#D3A9A9', '#A2D9A2', '#87CEEB', '#800080']

fig, ax = plt.subplots(figsize=(14, 8))
bars = ax.bar(art_movements, museum_counts, color=colors, width=0.5, edgecolor='black')

for bar in bars:
    yval = bar.get_height()
    ax.text(
        bar.get_x() + bar.get_width()/2,
        yval,
        f'{yval}',
        ha='center',
        va='bottom',
        fontsize=10,
        fontweight='bold'
    )

ax.set_title('Art Trends in Museums', fontsize=16, fontweight='bold')
ax.set_ylabel('Museums Count', fontsize=12)
ax.set_xlabel('Movements', fontsize=12)

plt.xticks(rotation=30, ha='right')
ax.legend(bars, art_movements, title='Movements', title_fontsize='13', loc='upper right', fontsize='10')
ax.grid(True, linestyle='--', alpha=0.5, axis='y')

plt.tight_layout()
plt.show()