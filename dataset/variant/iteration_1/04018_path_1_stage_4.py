import matplotlib.pyplot as plt
import numpy as np

age_groups = ['18-25', '26-35', '36-45', '66+']
avg_books_read = [4, 3, 2, 4.5]
enjoy_reading_percentages = [75, 65, 55, 80]

positions = np.arange(len(age_groups))

fig, ax1 = plt.subplots(figsize=(14, 8))

# Simplified bar plot without stylistic elements
single_color = '#FFA07A'
ax1.bar(positions, avg_books_read, color=single_color, alpha=0.7)
ax1.set_xticks(positions)
ax1.set_xticklabels(age_groups)

ax2 = ax1.twinx()
ax2.plot(positions, enjoy_reading_percentages, color='blue', linestyle='-', marker='o')
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