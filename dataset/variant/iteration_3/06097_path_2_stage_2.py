import matplotlib.pyplot as plt
import numpy as np

weeks = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
candy_types = ['Bright Chocolate', 'Milky Chocolate', 'Light Chocolate']

bright_chocolate = [15, 18, 20, 22, 19, 18, 20, 24, 23, 22, 20, 21]
milky_chocolate = [25, 28, 30, 27, 26, 30, 34, 33, 31, 30, 29, 30]
light_chocolate = [10, 12, 14, 13, 12, 15, 18, 17, 16, 15, 14, 16]

colors = ['#C70039', '#FFBF00', '#6A0572']

bar_width = 0.25
x = np.arange(len(weeks))

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 8))

ax1.bar(x - bar_width, bright_chocolate, width=bar_width, color=colors[0], edgecolor='grey', label='Bright Chocolate', linestyle='-.')
ax1.bar(x, milky_chocolate, width=bar_width, color=colors[1], edgecolor='grey', label='Milky Chocolate', linestyle=':')
ax1.bar(x + bar_width, light_chocolate, width=bar_width, color=colors[2], edgecolor='grey', label='Light Chocolate', linestyle='--')

ax1.set_xlabel('Weeks', fontsize=14)
ax1.set_ylabel('Output (in thousands of bars)', fontsize=14)
ax1.set_title('Monthly Chocolate Output in the Candy Factory', fontsize=18, fontweight='bold')
ax1.set_xticks(x)
ax1.set_xticklabels(weeks, rotation=45)
ax1.grid(False)

total_output = np.array(bright_chocolate) + np.array(milky_chocolate) + np.array(light_chocolate)

ax2.plot(weeks, total_output, marker='s', linestyle='--', color='purple', linewidth=3, markersize=8, label='Aggregate Output')
ax2.fill_between(weeks, total_output, color='thistle', alpha=0.6)

ax2.set_xlabel('Weeks', fontsize=14)
ax2.set_ylabel('Aggregate Output (in thousands of bars)', fontsize=14)
ax2.set_title('Total Candy Bars Output Across the Year', fontsize=18, fontweight='bold')
ax2.legend(fontsize=12)
ax2.grid(False)

plt.tight_layout()
plt.show()