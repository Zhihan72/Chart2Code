import matplotlib.pyplot as plt
import numpy as np

months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
interest_data = {
    'Coding': np.array([9, 7, 8, 6, 9, 8, 7, 6, 8, 7, 9, 8]),  # Manually shuffled
    'Cooking': np.array([8, 7, 8, 5, 6, 9, 9, 6, 7, 8, 6, 6]),  # Manually shuffled
    'Gardening': np.array([6, 5, 4, 9, 8, 6, 7, 9, 4, 5, 4, 7]),  # Manually shuffled
    'Hiking': np.array([9, 7, 7, 6, 9, 7, 8, 6, 10, 7, 7, 6]),  # Manually shuffled
    'Reading': np.array([9, 10, 9, 8, 8, 9, 8, 10, 10, 8, 9, 10])  # Manually shuffled
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