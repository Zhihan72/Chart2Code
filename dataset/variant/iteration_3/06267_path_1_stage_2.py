import matplotlib.pyplot as plt
import numpy as np

genres = ['Fiction', 'Non-Fiction', 'Children', 'Science', 'History']
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

monthly_sales = np.array([
    [50, 30, 20, 25, 30],
    [60, 35, 18, 22, 33],
    [70, 40, 22, 27, 35],
    [80, 45, 25, 30, 40],
    [90, 50, 28, 32, 42],
    [105, 55, 30, 35, 45],
    [120, 60, 32, 37, 48],
    [140, 70, 35, 40, 50],
    [160, 80, 38, 42, 52],
    [180, 90, 40, 45, 55],
    [200, 100, 42, 47, 58],
    [220, 110, 45, 50, 60]
])

cumulative_sales = np.cumsum(monthly_sales, axis=0)

bar_colors = ['#FF9999', '#FFD700', '#99FF99', '#FFCC99', '#66B2FF']  # Shuffled
line_styles = [':', '-.', '--', '-', ':']  # Shuffled

fig, ax1 = plt.subplots(figsize=(14, 8))

bar_width = 0.8
prev_sales = np.zeros(len(months))
for i, (genre, color) in enumerate(zip(genres, bar_colors)):
    ax1.bar(months, monthly_sales[:, i], bottom=prev_sales, color=color, edgecolor='black',  # Edge color changed
            width=bar_width, label=f'Monthly {genre}', alpha=0.5)  # Alpha changed
    prev_sales += monthly_sales[:, i]

ax2 = ax1.twinx()
for i, (genre, color, linestyle) in enumerate(zip(genres, bar_colors, line_styles)):
    ax2.plot(months, cumulative_sales[:, i], color=color, linestyle=linestyle, marker='s',  # Marker changed
             label=f'Cumulative {genre}', linewidth=2.5)  # Line width changed

ax1.set_title('Book Haven Monthly and Cumulative Sales by Genre (2023)', fontsize=16, weight='bold', pad=20)
ax1.set_xlabel('Months', fontsize=12, color='darkred')  # Label color changed
ax1.set_ylabel('Monthly Sales (Number of Books)', fontsize=12, color='darkred')  # Label color changed
ax2.set_ylabel('Cumulative Sales (Number of Books)', fontsize=12, color='darkblue')  # Label color changed

ax1.set_xticks(np.arange(len(months)))
ax1.set_xticklabels(months, fontsize=11, rotation=45)  # X-tick rotation added
ax1.set_yticks(np.arange(0, 1300, 100))
ax2.set_yticks(np.arange(0, np.max(cumulative_sales) + 200, 200))

ax1.yaxis.grid(True, linestyle='-.', linewidth=0.5, alpha=0.5)  # Grid style changed

ax1.legend(loc='lower right', fontsize=9, frameon=True, shadow=True, ncol=1)  # Legend position and style changed
ax2.legend(loc='upper left', fontsize=9, frameon=True, shadow=True, ncol=2)  # Legend position and style changed

plt.tight_layout()
plt.show()