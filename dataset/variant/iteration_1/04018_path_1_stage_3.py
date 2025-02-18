import matplotlib.pyplot as plt
import numpy as np

age_groups = ['18-25', '26-35', '36-45', '66+']
avg_books_read = [4, 3, 2, 4.5]
enjoy_reading_percentages = [75, 65, 55, 80]

positions = np.arange(len(age_groups))

fig, ax1 = plt.subplots(figsize=(14, 8))

# Use a single color for all bars
single_color = '#FFA07A'
bars = ax1.bar(positions, avg_books_read, color=single_color, alpha=0.7)
ax1.set_xticks(positions)

ax2 = ax1.twinx()
ax2.plot(positions, enjoy_reading_percentages, color='blue', linestyle='-', marker='o')
ax2.set_ylim(0, 100)
ax2.spines['right'].set_color('blue')

# Adjust layout
plt.tight_layout()

plt.show()