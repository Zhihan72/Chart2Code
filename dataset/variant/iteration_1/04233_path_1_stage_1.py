import matplotlib.pyplot as plt
import numpy as np

# Data for the genres and borrowing statistics for 2011, 2016, and 2021
genres = ['Fiction', 'Non-Fiction', 'Science', 'Fantasy', 'Biography', 'Mystery']
borrowings_2011 = [500, 420, 300, 350, 200, 450]
borrowings_2016 = [550, 480, 360, 430, 260, 500]
borrowings_2021 = [620, 520, 450, 600, 320, 570]

# Calculating growth from 2011 to 2021
growth_2011_2021 = [(borrowings_2021[i] - borrowings_2011[i]) / borrowings_2011[i] * 100 for i in range(len(genres))]

fig, ax1 = plt.subplots(figsize=(14, 8))
bar_width = 0.25
y_pos = np.arange(len(genres))

# Horizontal bar charts for each year
bars_2011 = ax1.barh(y_pos - bar_width, borrowings_2011, bar_width, label='2011', color='#ff9999')
bars_2016 = ax1.barh(y_pos, borrowings_2016, bar_width, label='2016', color='#66b3ff')
bars_2021 = ax1.barh(y_pos + bar_width, borrowings_2021, bar_width, label='2021', color='#99ff99')

# Labels and title
ax1.set_yticks(y_pos)
ax1.set_yticklabels(genres, fontsize=12)
ax1.set_xlabel('Number of Borrowings', fontsize=12)
ax1.set_title('Popularity of Book Genres Over the Last Decade in XYZ Library', fontsize=15, fontweight='bold')

# Add a second y-axis for the growth rate
ax2 = ax1.twinx()
ax2.plot(growth_2011_2021, y_pos, marker='o', linestyle='-', color='darkblue', label='Growth Rate')
ax2.set_ylabel('Growth Rate (%)', fontsize=12, color='darkblue')

# Adding value labels to each bar
for bars in [bars_2011, bars_2016, bars_2021]:
    for bar in bars:
        width = bar.get_width()
        label_x_pos = width + 10 if width < max(borrowings_2021) / 1.1 else width - 40
        ax1.text(label_x_pos, bar.get_y() + bar.get_height() / 2, f'{width}', va='center', fontsize=10, color='black')

# Annotate the growth rate
for i, growth in enumerate(growth_2011_2021):
    ax2.text(growth + 2, y_pos[i], f'{growth:.1f}%', va='center', fontsize=10, color='darkblue')

# Adding legends
ax1.legend(loc='upper left', fontsize=10, bbox_to_anchor=(0, 1))
ax2.legend(loc='upper right', fontsize=10, bbox_to_anchor=(1, 1))

# Enhance layout
ax1.grid(True, which='major', axis='x', linestyle='--', alpha=0.7)
plt.tight_layout()

# Display the plot
plt.show()