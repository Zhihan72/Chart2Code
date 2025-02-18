import matplotlib.pyplot as plt
import numpy as np

genres = ['Drama', 'Adventure', 'Technology', 'Magic', 'History', 'Thriller']
borrowings_2011 = [510, 420, 290, 350, 210, 440]
borrowings_2016 = [560, 470, 370, 410, 250, 490]
borrowings_2021 = [630, 530, 440, 610, 310, 580]

growth_2011_2021 = [(borrowings_2021[i] - borrowings_2011[i]) / borrowings_2011[i] * 100 for i in range(len(genres))]

fig, ax1 = plt.subplots(figsize=(14, 8))
bar_width = 0.25
y_pos = np.arange(len(genres))

ax1.barh(y_pos - bar_width, borrowings_2011, bar_width, color='#8e44ad')
ax1.barh(y_pos, borrowings_2016, bar_width, color='#e67e22')
ax1.barh(y_pos + bar_width, borrowings_2021, bar_width, color='#3498db')

ax1.set_yticks(y_pos)
ax1.set_yticklabels(genres, fontsize=12)
ax1.set_xlabel('Count of Borrowings', fontsize=12)
ax1.set_title('Trends of Book Categories in ABC Library', fontsize=15, fontweight='bold')

ax2 = ax1.twinx()
ax2.plot(growth_2011_2021, y_pos, marker='o', linestyle='-', color='darkblue')

for bars in [borrowings_2011, borrowings_2016, borrowings_2021]:
    for i, width in enumerate(bars):
        label_x_pos = width + 10 if width < max(borrowings_2021) / 1.1 else width - 40
        ax1.text(label_x_pos, y_pos[i] + (bars.index(width) - 1) * bar_width, f'{width}', va='center', fontsize=10, color='black')

for i, growth in enumerate(growth_2011_2021):
    ax2.text(growth + 2, y_pos[i], f'{growth:.1f}%', va='center', fontsize=10, color='darkblue')

plt.tight_layout()
plt.show()