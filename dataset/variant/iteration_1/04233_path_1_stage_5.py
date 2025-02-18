import matplotlib.pyplot as plt
import numpy as np

genres = ['Fiction', 'Non-Fiction', 'Science', 'Fantasy', 'Biography', 'Mystery']
borrowings_2011 = [350, 300, 500, 420, 200, 450]
borrowings_2016 = [480, 260, 550, 500, 430, 360]
borrowings_2021 = [570, 620, 320, 520, 450, 600]

growth_2011_2021 = [(borrowings_2021[i] - borrowings_2011[i]) / borrowings_2011[i] * 100 for i in range(len(genres))]

fig, ax1 = plt.subplots(figsize=(14, 8))
bar_width = 0.25
y_pos = np.arange(len(genres))

# Randomly changing colors for bars
colors_2011 = 'lightcoral'
colors_2016 = 'seagreen'
colors_2021 = 'royalblue'

bars_2011 = ax1.barh(y_pos - bar_width, borrowings_2011, bar_width, color=colors_2011, edgecolor='black')
bars_2016 = ax1.barh(y_pos, borrowings_2016, bar_width, color=colors_2016, edgecolor='black')
bars_2021 = ax1.barh(y_pos + bar_width, borrowings_2021, bar_width, color=colors_2021, edgecolor='black')

ax2 = ax1.twinx()
marker_style = {'marker': 'x', 'linestyle': '--', 'color': 'darkred'}
ax2.plot(growth_2011_2021, y_pos, **marker_style)

legend_labels = ['2011', '2016', '2021', 'Growth 2011-2021']
plt.legend([bars_2011, bars_2016, bars_2021, ax2.lines[0]], legend_labels, loc='lower right')

ax1.grid(True, which='both', axis='both', linestyle=':', linewidth=1.5, alpha=0.5)

for i, growth in enumerate(growth_2011_2021):
    ax2.text(growth + 5, y_pos[i], f'{growth:.1f}%', va='center', fontsize=10, color='darkred')

plt.tight_layout()
plt.show()