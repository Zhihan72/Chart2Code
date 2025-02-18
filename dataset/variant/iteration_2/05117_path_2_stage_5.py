import matplotlib.pyplot as plt
import numpy as np

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
cats = [20, 25, 30, 35, 40, 45]
dogs = [30, 35, 40, 45, 50, 55]
fish = [15, 18, 22, 25, 28, 30]

fig, ax = plt.subplots(figsize=(12, 7))

y = np.arange(len(months))
bar_height = 0.2

# Shuffled the colors assigned to each data group
ax.barh(y - bar_height, cats, height=bar_height, color='skyblue', edgecolor='steelblue', linestyle='-', hatch='/')
ax.barh(y, dogs, height=bar_height, color='lightgreen', edgecolor='darkgreen', linestyle='--', hatch='\\')
ax.barh(y + bar_height, fish, height=bar_height, color='salmon', edgecolor='darkred', linestyle='-.', hatch='|')

ax.set_yticks(y)
ax.set_yticklabels(months)
ax.xaxis.grid(True, which='major', linestyle='-', linewidth=0.5, color='gray', alpha=0.7)

plt.tight_layout()
plt.show()