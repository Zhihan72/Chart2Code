import matplotlib.pyplot as plt
import numpy as np

# Prepare data
art_movements = ['Ren', 'Bar', 'Rom', 'Imp', 'Mod', 'Cont']
museum_counts = [150, 100, 80, 120, 90, 60]
gallery_counts = [130, 110, 70, 100, 85, 65]

# Sort data in descending order based on museum_counts
sorted_indices = np.argsort(museum_counts)[::-1]
art_movements_sorted = [art_movements[i] for i in sorted_indices]
museum_counts_sorted = [museum_counts[i] for i in sorted_indices]
gallery_counts_sorted = [gallery_counts[i] for i in sorted_indices]

# Plot sorted bar chart
fig, ax = plt.subplots(figsize=(14, 8))
bar_width = 0.4
x_indexes = np.arange(len(art_movements))

bars_museum = ax.bar(x_indexes - bar_width/2, museum_counts_sorted, color='#FFD700',
                     width=bar_width, edgecolor='black', label='Museums')
bars_gallery = ax.bar(x_indexes + bar_width/2, gallery_counts_sorted, color='#87CEEB',
                      width=bar_width, edgecolor='black', label='Galleries')

# Annotate bars
for bar in bars_museum + bars_gallery:
    yval = bar.get_height()
    ax.text(
        bar.get_x() + bar.get_width()/2,
        yval,
        f'{int(yval)}',
        ha='center',
        va='bottom',
        fontsize=10,
        fontweight='bold'
    )

ax.set_title('Art Trends in Museums and Galleries', fontsize=16, fontweight='bold')
ax.set_ylabel('Count', fontsize=12)
ax.set_xlabel('Movements', fontsize=12)

plt.xticks(x_indexes, art_movements_sorted, rotation=30, ha='right')
ax.grid(True, linestyle='--', alpha=0.5, axis='y')
ax.legend()

plt.tight_layout()
plt.show()