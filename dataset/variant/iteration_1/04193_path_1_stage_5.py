import matplotlib.pyplot as plt
import numpy as np

apples_consumption = [150, 220, 180, 130]
bananas_consumption = [100, 200, 150, 80]
oranges_consumption = [120, 180, 140, 110]
grapes_consumption = [90, 160, 130, 95]  # New data series for Grapes

data = [apples_consumption, bananas_consumption, oranges_consumption, grapes_consumption]
n_seasons = 4
y = np.arange(n_seasons)
bar_height = 0.2  # Adjusted height for four groups

fig, ax = plt.subplots(figsize=(10, 6))

colors = ['#e74c3c', '#2ecc71', '#f1c40f', '#9b59b6']  # Added color for Grapes
hatches = ['/', '\\', '|', 'x']  # Added hatch pattern for Grapes
line_styles = [':', '-.', '--']

for i in range(4):  # Adjusted range to accommodate four series
    bars = ax.barh(y + i * bar_height, data[i], height=bar_height, color=colors[i], hatch=hatches[i])

ax.xaxis.grid(True, linestyle=line_styles[0], alpha=0.9)

ax.spines['top'].set_linewidth(1.5)
ax.spines['right'].set_linewidth(1.5)
ax.spines['left'].set_linewidth(2)
ax.spines['bottom'].set_linewidth(2)

ax.legend(['Apples', 'Bananas', 'Oranges', 'Grapes'], loc='upper right', frameon=True)

plt.tight_layout()
plt.show()