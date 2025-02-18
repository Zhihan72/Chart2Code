import matplotlib.pyplot as plt
import numpy as np

# Data for each age group
children_books = [14, 12, 13, 9, 11, 11, 14, 16, 15, 10, 10]
teens_books = [6, 11, 5, 7, 12, 8, 9, 5, 6, 10, 7]
adults_books = [17, 21, 15, 19, 16, 18, 12, 18, 15, 14, 14]
middle_aged_books = [11, 12, 13, 8, 10, 14, 7, 12, 10, 11, 9]
seniors_books = [7, 5, 5, 6, 8, 6, 5, 6, 5, 7, 4]

data = [children_books, teens_books, adults_books, middle_aged_books, seniors_books]
age_groups = ['Children (6-12)', 'Teens (13-19)', 'Adults (20-35)', 'Middle-aged (36-55)', 'Seniors (56+)']

fig, ax = plt.subplots(figsize=(14, 9))
box = ax.boxplot(data, vert=False, patch_artist=True, labels=age_groups, notch=True, whis=1.5)

# Shuffle the colors assignment manually
colors = plt.cm.viridis(np.linspace(0, 1, len(data)))
shuffled_indices = [3, 0, 4, 2, 1]
shuffled_colors = [colors[i] for i in shuffled_indices]

for patch, color in zip(box['boxes'], shuffled_colors):
    patch.set_facecolor(color)

medians = [np.median(group) for group in data]
for i, median in enumerate(medians):
    ax.annotate(f'{median}', xy=(median, i + 1), xytext=(5, -15), 
                textcoords='offset points', ha='center', va='center', color='white',
                bbox=dict(boxstyle='round,pad=0.3', edgecolor='none', facecolor='dimgray'))

ax.grid(True, linestyle='--', alpha=0.6, axis='x')

ax.set_title('Annual Book Reading Competition 2023\nDistribution of Books Read by Age Group', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Number of Books Read', fontsize=12)
ax.set_ylabel('Age Group', fontsize=12)

plt.gca().set_aspect('auto', adjustable='box')
plt.tight_layout()

ax2 = ax.twinx()
book_trend = [np.mean(group) for group in data]
ax2.plot(book_trend, np.arange(1, len(data)+1), 'o-', color='indianred', linewidth=2, label='Average Trend')
ax2.set_yticks([])

ax2.legend(loc='upper left', fontsize=10)

plt.show()