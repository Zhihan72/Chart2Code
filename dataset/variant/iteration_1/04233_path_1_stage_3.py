import matplotlib.pyplot as plt
import numpy as np

genres = ['Fiction', 'Non-Fiction', 'Science', 'Fantasy', 'Biography', 'Mystery']
borrowings_2011 = [500, 420, 300, 350, 200, 450]
borrowings_2016 = [550, 480, 360, 430, 260, 500]
borrowings_2021 = [620, 520, 450, 600, 320, 570]

growth_2011_2021 = [(borrowings_2021[i] - borrowings_2011[i]) / borrowings_2011[i] * 100 for i in range(len(genres))]

fig, ax1 = plt.subplots(figsize=(14, 8))
bar_width = 0.25
y_pos = np.arange(len(genres))

common_color = 'steelblue'

bars_2011 = ax1.barh(y_pos - bar_width, borrowings_2011, bar_width, color=common_color)
bars_2016 = ax1.barh(y_pos, borrowings_2016, bar_width, color=common_color)
bars_2021 = ax1.barh(y_pos + bar_width, borrowings_2021, bar_width, color=common_color)

ax2 = ax1.twinx()
ax2.plot(growth_2011_2021, y_pos, marker='o', linestyle='-', color='darkblue')

for bars in [bars_2011, bars_2016, bars_2021]:
    for bar in bars:
        width = bar.get_width()
        label_x_pos = width + 10 if width < max(borrowings_2021) / 1.1 else width - 40

for i, growth in enumerate(growth_2011_2021):
    ax2.text(growth + 2, y_pos[i], f'{growth:.1f}%', va='center', fontsize=10, color='darkblue')

ax1.grid(True, which='major', axis='x', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()