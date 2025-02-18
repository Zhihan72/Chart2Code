import matplotlib.pyplot as plt
import numpy as np

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
cats = [20, 25, 30, 35, 40, 45]
dogs = [30, 35, 40, 45, 50, 55]
fish = [15, 18, 22, 25, 28, 30]

fig, ax = plt.subplots(figsize=(12, 7))

y = np.arange(len(months))
bar_height = 0.2

# Create horizontal bars
ax.barh(y - bar_height, cats, height=bar_height, color='lightblue')
ax.barh(y, dogs, height=bar_height, color='lightyellow')
ax.barh(y + bar_height, fish, height=bar_height, color='lightcoral')

ax.set_yticks(y)
ax.grid(axis='x', linestyle='--', alpha=0.6)

plt.tight_layout()
plt.show()