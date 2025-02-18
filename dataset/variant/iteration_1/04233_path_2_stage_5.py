import matplotlib.pyplot as plt
import numpy as np

genres = ['Drama', 'Adventure', 'Technology', 'Magic', 'History', 'Thriller']
borrowings_2011 = [510, 420, 290, 350, 210, 440]
borrowings_2016 = [560, 470, 370, 410, 250, 490]
borrowings_2021 = [630, 530, 440, 610, 310, 580]

# Sort each year's data in descending order (can change to ascending if needed)
sorted_indices_2011 = sorted(range(len(borrowings_2011)), key=lambda i: -borrowings_2011[i])
sorted_indices_2016 = sorted(range(len(borrowings_2016)), key=lambda i: -borrowings_2016[i])
sorted_indices_2021 = sorted(range(len(borrowings_2021)), key=lambda i: -borrowings_2021[i])

sorted_genres_2011 = [genres[i] for i in sorted_indices_2011]
sorted_borrowings_2011 = [borrowings_2011[i] for i in sorted_indices_2011]

sorted_genres_2016 = [genres[i] for i in sorted_indices_2016]
sorted_borrowings_2016 = [borrowings_2016[i] for i in sorted_indices_2016]

sorted_genres_2021 = [genres[i] for i in sorted_indices_2021]
sorted_borrowings_2021 = [borrowings_2021[i] for i in sorted_indices_2021]

fig, ax1 = plt.subplots(figsize=(14, 8))
bar_width = 0.25
y_pos = np.arange(len(genres))

ax1.barh(y_pos - bar_width, sorted_borrowings_2011, bar_width, color='#8e44ad', label='2011')
ax1.barh(y_pos, sorted_borrowings_2016, bar_width, color='#e67e22', label='2016')
ax1.barh(y_pos + bar_width, sorted_borrowings_2021, bar_width, color='#3498db', label='2021')

ax1.set_yticks(y_pos)
ax1.set_yticklabels(sorted_genres_2021, fontsize=12)  # Use 2021 sorting order for labels
ax1.set_xlabel('Count of Borrowings', fontsize=12)
ax1.set_title('Trends of Book Categories in ABC Library (Sorted by 2021 Data)', fontsize=15, fontweight='bold')
ax1.legend()

ax2 = ax1.twinx()
growth_2011_2021 = [(borrowings_2021[i] - borrowings_2011[i]) / borrowings_2011[i] * 100 for i in range(len(genres))]
growth_sorted_2021 = [growth_2011_2021[i] for i in sorted_indices_2021]
ax2.plot(growth_sorted_2021, y_pos, marker='o', linestyle='-', color='darkblue')

for bars, indices in [(sorted_borrowings_2011, sorted_indices_2011), (sorted_borrowings_2016, sorted_indices_2016), (sorted_borrowings_2021, sorted_indices_2021)]:
    for i, width in enumerate(bars):
        label_x_pos = width + 10 if width < max(borrowings_2021) / 1.1 else width - 40
        ax1.text(label_x_pos, y_pos[i] + (indices.index(sorted_indices_2021[i]) - 1) * bar_width, f'{width}', va='center', fontsize=10, color='black')
        
for i, growth in enumerate(growth_sorted_2021):
    ax2.text(growth + 2, y_pos[i], f'{growth:.1f}%', va='center', fontsize=10, color='darkblue')

plt.tight_layout()
plt.show()