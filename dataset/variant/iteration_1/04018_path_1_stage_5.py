import matplotlib.pyplot as plt
import numpy as np

age_groups = ['36-45', '26-35', '18-25', '66+']
avg_books_read = [2, 3, 4, 4.5]
enjoy_reading_percentages = [55, 65, 75, 80]

# Get the sort order based on average books read
sorted_indices = np.argsort(avg_books_read)

# Sort the data
age_groups_sorted = [age_groups[i] for i in sorted_indices]
avg_books_read_sorted = [avg_books_read[i] for i in sorted_indices]
enjoy_reading_percentages_sorted = [enjoy_reading_percentages[i] for i in sorted_indices]

positions = np.arange(len(age_groups_sorted))

fig, ax1 = plt.subplots(figsize=(14, 8))

single_color = '#FFA07A'
ax1.bar(positions, avg_books_read_sorted, color=single_color, alpha=0.7)
ax1.set_xticks(positions)
ax1.set_xticklabels(age_groups_sorted)

ax2 = ax1.twinx()
ax2.plot(positions, enjoy_reading_percentages_sorted, color='blue', linestyle='-', marker='o')
ax2.set_ylim(0, 100)

# Remove borders, grids, and right spine color setting
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)
ax1.spines['left'].set_visible(False)
ax1.spines['bottom'].set_visible(False)
ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)
ax2.spines['left'].set_visible(False)

plt.tight_layout()
plt.show()