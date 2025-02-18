import matplotlib.pyplot as plt
import numpy as np

weeks = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
candies = ['Bright Chocolate', 'Milky Chocolate']

bright_chocolate = [15, 18, 20, 22, 19, 18, 20, 24, 23, 22, 20, 21]
milky_chocolate = [25, 28, 30, 27, 26, 30, 34, 33, 31, 30, 29, 30]

colors = ['#C70039', '#FFBF00']

x = np.arange(len(weeks))

fig, (ax2, ax1) = plt.subplots(1, 2, figsize=(18, 8))  # Switch the order of ax1 and ax2

# Plot total output first
total_output = np.array(bright_chocolate) + np.array(milky_chocolate)
ax2.plot(weeks, total_output, marker='s', linestyle='--', color='purple', linewidth=3, markersize=8, label='Aggregate Output')
ax2.fill_between(weeks, total_output, color='thistle', alpha=0.6)

ax2.set_xlabel('Weeks', fontsize=14)
ax2.set_ylabel('Aggregate Output (in thousands of bars)', fontsize=14)
ax2.set_title('Total Candy Bars Output Across the Year', fontsize=18, fontweight='bold')
ax2.legend(fontsize=12)
ax2.grid(False)

# Now plot the stacked bar chart
ax1.bar(x, bright_chocolate, color=colors[0], edgecolor='grey', label='Bright Chocolate', linestyle='-.')
ax1.bar(x, milky_chocolate, bottom=bright_chocolate, color=colors[1], edgecolor='grey', label='Milky Chocolate', linestyle=':')

ax1.set_xlabel('Weeks', fontsize=14)
ax1.set_ylabel('Output (in thousands of bars)', fontsize=14)
ax1.set_title('Monthly Chocolate Output in the Candy Factory', fontsize=18, fontweight='bold')
ax1.set_xticks(x)
ax1.set_xticklabels(weeks, rotation=45)
ax1.legend(fontsize=12)
ax1.grid(False)

plt.tight_layout()
plt.show()