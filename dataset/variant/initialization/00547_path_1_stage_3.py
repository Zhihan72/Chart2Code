import matplotlib.pyplot as plt
import numpy as np

# Combined data
all_books = [11, 12, 15, 9, 10, 14, 11, 13, 14, 10, 16, 
             5, 7, 8, 6, 10, 7, 9, 11, 6, 5, 12,
             12, 15, 14, 17, 19, 18, 21, 14, 16, 15, 18,
             9, 10, 11, 8, 12, 7, 11, 13, 12, 14, 10,
             5, 4, 6, 5, 7, 8, 6, 5, 7, 5, 6]

fig, ax = plt.subplots(figsize=(8, 6))

# Create box plot
box = ax.boxplot(all_books, vert=True, patch_artist=True)

# Box color
box_color = plt.cm.viridis(0.5)
box['boxes'][0].set_facecolor(box_color)

# Median annotation
median = np.median(all_books)
ax.annotate(f'{median}', xy=(1, median), xytext=(10, 0), 
            textcoords='offset points', ha='center', va='bottom', color='white',
            bbox=dict(boxstyle='round,pad=0.3', edgecolor='none', facecolor='slategray'))

# Grid
ax.grid(True, linestyle='--', alpha=0.6, axis='y')

# Titles and labels
ax.set_title('Books Read', fontsize=14, fontweight='bold', pad=20)
ax.set_ylabel('Books', fontsize=12)
ax.set_xticks([])

plt.tight_layout()
plt.show()