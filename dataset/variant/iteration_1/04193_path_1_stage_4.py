import matplotlib.pyplot as plt
import numpy as np

apples_consumption = [150, 220, 180, 130]
bananas_consumption = [100, 200, 150, 80]
oranges_consumption = [120, 180, 140, 110]

data = [apples_consumption, bananas_consumption, oranges_consumption]
n_seasons = 4
y = np.arange(n_seasons)
bar_height = 0.25

fig, ax = plt.subplots(figsize=(10, 6))

# Using varied colors for each fruit
colors = ['#e74c3c', '#2ecc71', '#f1c40f']
# Using varied marker styles (hatch patterns)
hatches = ['/', '\\', '|']
# Using varied line styles for grid
line_styles = [':', '-.', '--']

for i in range(3):
    bars = ax.barh(y + i * bar_height, data[i], height=bar_height, color=colors[i], hatch=hatches[i])

# Randomized line style for grid
ax.xaxis.grid(True, linestyle=line_styles[0], alpha=0.9)

# Adding varied border (spanner) widths
ax.spines['top'].set_linewidth(1.5)
ax.spines['right'].set_linewidth(1.5)
ax.spines['left'].set_linewidth(2)
ax.spines['bottom'].set_linewidth(2)

# Different marker in the legend
ax.legend(['Apples', 'Bananas', 'Oranges'], loc='upper right', frameon=True)

plt.tight_layout()
plt.show()