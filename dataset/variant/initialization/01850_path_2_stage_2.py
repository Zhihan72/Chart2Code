import numpy as np
import matplotlib.pyplot as plt

centuries = ['15th Century', '18th Century', '20th Century']
methods = ['Stone Masonry', 'Brickwork', 'Wood Framing', 'Steel Framing']

data = np.array([
    [60, 30, 10, 0],
    [20, 50, 30, 0],
    [10, 20, 30, 40]
])

num_centuries = len(centuries)
bar_width = 0.4

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Colors for bars
colors = ['#FF5733', '#33FF57', '#3357FF', '#F0E68C']

# Plot each method data as a separate set of vertical bars
for i in range(num_centuries):
    ax.bar(i + np.arange(len(methods)) * bar_width, data[i], bar_width, color=colors)

# Set xticks to center the labels under each group of bars
ax.set_xticks(np.arange(num_centuries) + bar_width / 2)
ax.set_xticklabels(centuries, fontsize=10)

ax.set_xlabel('Centuries', labelpad=10)
ax.set_ylabel('Prevalence (%)', labelpad=10)
ax.set_title('Evolution of Construction Methods Across Centuries', fontsize=14, pad=15)

ax.legend(methods, title='Methods', fontsize=9)

plt.tight_layout()
plt.show()