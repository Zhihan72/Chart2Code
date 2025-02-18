import matplotlib.pyplot as plt
import numpy as np

months = ['Feb', 'Jan', 'Apr', 'Mar', 'Jun', 'May', 'Aug', 'Jul', 'Oct', 'Sep', 'Dec', 'Nov']
apples_sales = np.array([120, 130, 110, 150, 180, 200, 220, 240, 200, 150, 140, 130])
bananas_sales = np.array([90, 100, 110, 120, 130, 140, 150, 160, 150, 140, 130, 110])
oranges_sales = np.array([80, 90, 100, 110, 120, 130, 140, 150, 140, 130, 120, 100])

average_apples = np.mean(apples_sales)
average_bananas = np.mean(bananas_sales)
average_oranges = np.mean(oranges_sales)

fig, ax = plt.subplots(figsize=(14, 6))

bar_width = 0.7
positions = np.arange(len(months))

bar1_apples = ax.bar(positions, apples_sales - average_apples, width=bar_width, color='red', edgecolor='black', alpha=0.8)
bar2_bananas = ax.bar(positions, bananas_sales - average_bananas, width=bar_width, bottom=apples_sales - average_apples, color='yellow', edgecolor='black', alpha=0.8)
bar3_oranges = ax.bar(positions, oranges_sales - average_oranges, width=bar_width, bottom=(apples_sales + bananas_sales) - (average_apples + average_bananas), color='orange', edgecolor='black', alpha=0.8)

ax.set_title('2023 Diverging Fruit Sales Volume', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Monthly Duration', fontsize=12)
ax.set_ylabel('Deviation from Average Sales', fontsize=12)
ax.set_xticks(positions)
ax.set_xticklabels(months, rotation=45, ha='right', fontsize=11)
ax.axhline(0, color='black', linewidth=0.8)

# Hiding the spines to eliminate borders
for spine in ax.spines.values():
    spine.set_visible(False)

for bar in bar1_apples + bar2_bananas + bar3_oranges:
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