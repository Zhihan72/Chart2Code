import matplotlib.pyplot as plt
import numpy as np

data = np.array([
    [15, 18, 22, 26],  # Adventure
    [20, 22, 24, 30],  # Culture
    [30, 32, 34, 38],  # Food
    [25, 28, 30, 35],  # Nature
])

total_travelers = np.sum(data, axis=1)
sorted_indices = np.argsort(total_travelers)[::-1]

sorted_colors = ['blue', 'green', 'orange', 'red']
sorted_data = data[sorted_indices]

fig, ax = plt.subplots(figsize=(10, 6))

bar_width = 0.5
x = np.arange(len(data))

for i in range(len(sorted_data)):
    ax.bar(x[i], total_travelers[i], color=sorted_colors[i])

ax.set_xticks([])  # Remove x-tick labels
ax.set_yticks([])  # Remove y-tick labels

plt.tight_layout()
plt.show()