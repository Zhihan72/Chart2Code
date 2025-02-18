import matplotlib.pyplot as plt
import numpy as np

art_movements = ['Ren', 'Bar', 'Rom', 'Imp', 'Mod', 'Cont']
museum_counts = [150, 100, 80, 120, 90, 60]
single_color = '#FFD700'  # Chosen single color for all bars

fig, ax = plt.subplots(figsize=(14, 8))
bars = ax.bar(art_movements, museum_counts, color=single_color, width=0.5, edgecolor='black')

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
ax.grid(True, linestyle='--', alpha=0.5, axis='y')

plt.tight_layout()
plt.show()