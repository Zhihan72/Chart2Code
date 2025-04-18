import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2030, 2040)
data = {
    'A': [20, 22, 27, 35, 40, 43, 45, 50, 56, 65],
    'B': [15, 18, 21, 26, 30, 32, 37, 40, 44, 50],
    'C': [10, 12, 15, 19, 23, 28, 31, 35, 38, 42],
    'D': [8, 10, 12, 15, 20, 24, 27, 30, 33, 38],
    'E': [5, 7, 10, 12, 16, 18, 21, 25, 28, 30],
}

# Randomly shuffling the elements within each data group without using any randomness library
def shuffle_data_set(data_set):
    shuffled_data = []
    for values in data_set.values():
        shuffled = values.copy()
        n = len(shuffled)
        for i in range(n-1, 0, -1):
            j = i // 2
            shuffled[i], shuffled[j] = shuffled[j], shuffled[i]
        shuffled_data.append(shuffled)
    return {key: val for key, val in zip(data_set.keys(), shuffled_data)}

shuffled_data = shuffle_data_set(data)

fig, ax = plt.subplots(figsize=(12, 8))

bar_width = 0.15
x_indexes = np.arange(len(years))
offsets = np.linspace(-0.3, 0.3, len(data))

new_colors = ['#1E90FF', '#32CD32', '#FF4500', '#8A2BE2', '#FFD700']
for i, (planet, tourists) in enumerate(shuffled_data.items()):
    ax.bar(x_indexes + offsets[i], tourists, width=bar_width, color=new_colors[i], alpha=0.8)

ax.set_title('Tourists by Year', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Yr', fontsize=14)
ax.set_ylabel('Tourists (k)', fontsize=14)
ax.set_xticks(x_indexes)
ax.set_xticklabels(years, rotation=45, fontsize=10)

plt.tight_layout()
plt.show()