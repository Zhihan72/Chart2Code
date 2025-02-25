import matplotlib.pyplot as plt
import numpy as np

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
cats = [20, 25, 30, 35, 40, 45]
dogs = [30, 35, 40, 45, 50, 55]
fish = [15, 18, 22, 25, 28, 30]

fig, ax = plt.subplots(figsize=(12, 7))

x = np.arange(len(months))
bar_width = 0.2

ax.bar(x - bar_width, cats, width=bar_width, color='salmon', edgecolor='darkred', linestyle='-', hatch='/')
ax.bar(x, dogs, width=bar_width, color='skyblue', edgecolor='steelblue', linestyle='--', hatch='\\')
ax.bar(x + bar_width, fish, width=bar_width, color='lightgreen', edgecolor='darkgreen', linestyle='-.', hatch='|')

ax.set_xticks(x)
ax.set_xticklabels(months)
ax.yaxis.grid(True, which='major', linestyle='-', linewidth=0.5, color='gray', alpha=0.7)

plt.tight_layout()
plt.show()