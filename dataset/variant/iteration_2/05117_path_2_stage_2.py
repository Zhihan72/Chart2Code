import matplotlib.pyplot as plt
import numpy as np

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
cats = [20, 25, 30, 35, 40, 45]
dogs = [30, 35, 40, 45, 50, 55]
fish = [15, 18, 22, 25, 28, 30]
birds = [10, 12, 15, 20, 25, 28]

fig, ax = plt.subplots(figsize=(12, 7))

x = np.arange(len(months))
bar_width = 0.2

ax.bar(x - 3*bar_width/2, cats, width=bar_width, color='salmon', edgecolor='darkred', linestyle='-', hatch='/')
ax.bar(x - bar_width/2, dogs, width=bar_width, color='skyblue', edgecolor='steelblue', linestyle='--', hatch='\\')
ax.bar(x + bar_width/2, fish, width=bar_width, color='lightgreen', edgecolor='darkgreen', linestyle='-.', hatch='|')
ax.bar(x + 3*bar_width/2, birds, width=bar_width, color='gold', edgecolor='goldenrod', linestyle=':', hatch='+')

ax.set_xticks(x)
ax.yaxis.grid(True, which='major', linestyle='-', linewidth=0.5, color='gray', alpha=0.7)

plt.tight_layout()
plt.show()