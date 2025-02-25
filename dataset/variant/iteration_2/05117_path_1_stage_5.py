import matplotlib.pyplot as plt
import numpy as np

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
cats = [20, 25, 30, 35, 40, 45]
dogs = [30, 35, 40, 45, 50, 55]
fish = [15, 18, 22, 25, 28, 30]

fig, ax = plt.subplots(figsize=(12, 7))

y = np.arange(len(months))
bar_height = 0.2

# Randomly chosen stylistic changes
ax.barh(y - bar_height, cats, height=bar_height, color='salmon', linestyle='dashed', label='Cats')
ax.barh(y, dogs, height=bar_height, color='lightgreen', linestyle='solid', label='Dogs')
ax.barh(y + bar_height, fish, height=bar_height, color='skyblue', linestyle='dotted', label='Fish')

ax.set_yticks(y)
ax.grid(axis='x', color='gray', linestyle=':', alpha=0.3)

# Alter legend and border
ax.legend(loc='upper right', frameon=False)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()
plt.show()