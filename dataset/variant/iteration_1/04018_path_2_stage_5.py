import matplotlib.pyplot as plt
import numpy as np

age_groups = ['18-25', '66+', '46-55', '36-45', '26-35', '56-65']
avg_books_read = [3.5, 4.5, 2, 2.5, 3, 4]
enjoy_reading_percentages = [70, 80, 60, 55, 65, 75]

# Manually reordering the arrays
positions = np.arange(len(age_groups))

fig, ax1 = plt.subplots(figsize=(14, 8))

bar_colors = ['#FF7F50', '#6A5ACD', '#2E8B57', '#FFD700', '#DC143C', '#8A2BE2']
bars = ax1.bar(positions, avg_books_read, color=bar_colors, alpha=0.8, edgecolor='black', linewidth=1.2)

ax1.set_xticks(positions)
ax1.set_xticklabels(age_groups, fontsize=12, rotation=45, ha='right')
ax1.set_ylabel('Avg Books/Month', fontsize=14, color='darkgreen', fontweight='bold')
ax1.yaxis.grid(True, linestyle='--', color='grey', alpha=0.6)

ax2 = ax1.twinx()
ax2.set_ylabel('Enjoy Reading (%)', fontsize=14, color='maroon', fontweight='bold')
ax2.plot(positions, enjoy_reading_percentages, color='maroon', linestyle='--', marker='o', markersize=8, markerfacecolor='orange')
ax2.set_ylim(0, 100)
ax2.tick_params(axis='y', colors='maroon')
ax2.spines['right'].set_color('maroon')

for bar, value in zip(bars, avg_books_read):
    ax1.text(bar.get_x() + bar.get_width() / 2, value + 0.1, f'{value:.1f}', ha='center', va='bottom', fontweight='bold', fontsize=10)

ax2.legend(['Enjoy Reading (%)'], loc='upper left', fontsize=12)

plt.gcf().patch.set_edgecolor('black')
plt.gcf().patch.set_linewidth(2)

plt.tight_layout()
plt.show()