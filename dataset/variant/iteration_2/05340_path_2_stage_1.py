import matplotlib.pyplot as plt
import numpy as np

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
apples_sales = np.array([120, 130, 110, 150, 180, 200, 220, 240, 200, 150, 140, 130])
bananas_sales = np.array([90, 100, 110, 120, 130, 140, 150, 160, 150, 140, 130, 110])
oranges_sales = np.array([80, 90, 100, 110, 120, 130, 140, 150, 140, 130, 120, 100])
berries_sales = np.array([70, 80, 90, 100, 110, 120, 130, 140, 130, 120, 110, 90])

fig, ax = plt.subplots(figsize=(14, 6))

bar_width = 0.7
positions = np.arange(len(months))

bar1 = ax.bar(positions, apples_sales, width=bar_width, color='red', label='Apples', edgecolor='black', alpha=0.8)
bar2 = ax.bar(positions, bananas_sales, width=bar_width, bottom=apples_sales, color='yellow', label='Bananas', edgecolor='black', alpha=0.8)
bar3 = ax.bar(positions, oranges_sales, width=bar_width, bottom=apples_sales + bananas_sales, color='orange', label='Oranges', edgecolor='black', alpha=0.8)
bar4 = ax.bar(positions, berries_sales, width=bar_width, bottom=apples_sales + bananas_sales + oranges_sales, color='purple', label='Berries', edgecolor='black', alpha=0.8)

ax.set_title('Comparative Monthly Sales Volume of Different Fruits\n(2023)', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Month', fontsize=12)
ax.set_ylabel('Sales Volume', fontsize=12)
ax.set_xticks(positions)
ax.set_xticklabels(months, rotation=45, ha='right', fontsize=11)
ax.legend(title='Fruits', loc='upper right', fontsize=11, title_fontsize=12)
ax.yaxis.grid(True, linestyle='--', which='major', color='grey', alpha=0.7)

for bar in bar1 + bar2 + bar3 + bar4:
    height = bar.get_height()
    ax.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_y() + height / 2,
        f'{int(height)}',
        ha='center',
        va='center',
        color='white',
        fontsize=10
    )

plt.tight_layout()
plt.show()