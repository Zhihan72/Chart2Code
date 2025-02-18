import matplotlib.pyplot as plt
import numpy as np

months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
interest_data = {
    'Coding': np.array([6, 7, 8, 8, 9, 9, 7, 6, 7, 8, 8, 9]),
    'Cooking': np.array([5, 6, 6, 8, 9, 9, 8, 7, 6, 6, 7, 8]),
    'Gardening': np.array([4, 5, 6, 7, 8, 9, 9, 7, 6, 5, 4, 4]),
    'Hiking': np.array([7, 6, 7, 9, 10, 9, 8, 7, 7, 7, 6, 7]),
    'Reading': np.array([8, 8, 9, 9, 10, 10, 8, 8, 9, 10, 10, 9])
}

colors = {
    'Coding': 'blue',
    'Cooking': 'orange',
    'Gardening': 'green',
    'Hiking': 'red',
    'Reading': 'purple'
}

fig, ax = plt.subplots(figsize=(14, 7))
for hobby, interest in interest_data.items():
    ax.plot(months, interest, marker='o', color=colors[hobby], linewidth=2)

ax.set_xticks(months)
ax.set_yticks(np.arange(0, 11, 1))

plt.tight_layout()
plt.show()