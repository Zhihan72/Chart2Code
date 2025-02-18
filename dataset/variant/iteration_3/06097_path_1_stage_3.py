import matplotlib.pyplot as plt
import numpy as np

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
chocolate_types = ['Dark Chocolate', 'Milk Chocolate', 'White Chocolate']

# Manually altering data while preserving the original structure
dark_chocolate = [18, 15, 22, 20, 19, 18, 21, 24, 23, 20, 22, 21]
milk_chocolate = [28, 25, 30, 27, 30, 26, 34, 33, 31, 29, 30, 28]
white_chocolate = [12, 14, 13, 10, 12, 15, 16, 18, 17, 16, 14, 15]

colors = ['#C70039', '#FFBF00', '#6A0572']

bar_width = 0.25
x = np.arange(len(months))

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 8))

ax1.bar(x - bar_width, dark_chocolate, width=bar_width, color=colors[0], edgecolor='black', label='Dark Choco.')
ax1.bar(x, milk_chocolate, width=bar_width, color=colors[1], edgecolor='black', label='Milk Choco.')
ax1.bar(x + bar_width, white_chocolate, width=bar_width, color=colors[2], edgecolor='black', label='White Choco.')

ax1.set_xlabel('Monthly Duration', fontsize=12)
ax1.set_ylabel('Output (K bars)', fontsize=12)
ax1.set_title('Candy Factory: Month-wise Production!', fontsize=16, fontweight='bold')
ax1.set_xticks(x)
ax1.set_xticklabels(months)
ax1.legend(title='Choco Varieties', fontsize=10, title_fontsize=12)
ax1.grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.7)

total_production = np.array(dark_chocolate) + np.array(milk_chocolate) + np.array(white_chocolate)

ax2.plot(months, total_production, marker='o', linestyle='-', color='blue', linewidth=2, markersize=6, label='Total Output')
ax2.fill_between(months, total_production, color='lightblue', alpha=0.3)

ax2.set_xlabel('Month Span', fontsize=12)
ax2.set_ylabel('Total Output (K bars)', fontsize=12)
ax2.set_title('Total Bars Annually: The Curve', fontsize=16, fontweight='bold')
ax2.legend(fontsize=10)
ax2.grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.7)

plt.tight_layout()
plt.show()