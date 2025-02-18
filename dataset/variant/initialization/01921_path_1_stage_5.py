import matplotlib.pyplot as plt
import numpy as np

renewable_data = np.array([
    [40, 25, 30, 3, 2],
    [20, 35, 25, 10, 10],
    [15, 20, 50, 5, 10],
    [45, 30, 10, 10, 5]
])

# Adjusted colors, marker types, and line styles
new_colors = ['#FF5733', '#33FF57', '#3357FF', '#F5A623', '#8E44AD']

fig, ax = plt.subplots(figsize=(14, 8))

x = np.arange(4)  # Directly use the length of continents
bar_width = 0.15

# Altered marker types visually through linestyle variations and edge modification
for i, color in enumerate(new_colors):
    ax.bar(x + i * bar_width, renewable_data[:, i], bar_width, 
           color=color, edgecolor='none', linestyle=(0, (5, 1)),
           hatch='/' if i % 2 == 0 else '\\')

# Randomly adjust the legend display by shuffling visibility or style
labels = ['Type A', 'Type B', 'Type C', 'Type D', 'Type E']
legend = ax.legend(labels, loc='upper left', frameon=False)

# Change the grid style randomly
ax.yaxis.grid(True, linestyle='-', color='gray', linewidth=0.5)

# Border visibility alteration
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Adjusted x-ticks for better alignment
ax.set_xticks(x + bar_width * (len(new_colors) / 2 - 0.5))
ax.set_xticklabels(['Cont1', 'Cont2', 'Cont3', 'Cont4'])

plt.tight_layout()
plt.show()