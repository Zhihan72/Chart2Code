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
ax1.set_xticklabels(age_groups, fontsize=12, rotation=45, ha='right')
ax1.set_ylabel('Average Books Read per Month', fontsize=14, color='black')
ax1.set_title('Monthly Book Reading Habits by Age Group in 2023', fontsize=16, fontweight='bold', pad=20)

for bar in bars:
    yval = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2, yval + 0.1, f'{yval:.1f}', ha='center', va='bottom', fontweight='bold')

ax2 = ax1.twinx()
ax2.set_ylabel('Percentage Enjoy Reading (%)', fontsize=14, color='blue')
ax2.plot(positions, enjoy_reading_percentages, color='blue', linestyle='-', marker='o')
ax2.set_ylim(0, 100)
ax2.tick_params(axis='y', colors='blue')
ax2.spines['right'].set_color('blue')

for i, (pos, percent) in enumerate(zip(positions, enjoy_reading_percentages)):
    ax2.annotate(f'{percent}%', xy=(pos, percent), xytext=(5, -5), textcoords='offset points', ha='center', va='bottom', color='blue', fontsize=10, fontweight='bold')

# Adjust layout
plt.tight_layout()

plt.show()