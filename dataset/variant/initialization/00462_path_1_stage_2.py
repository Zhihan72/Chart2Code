import matplotlib.pyplot as plt
import numpy as np

# Modified temperature data with the last two rows removed
temperature_data = np.array([
    [26, 27, 29, 30, 31, 32, 31, 30, 29, 28],
    [25, 26, 28, 30, 32, 33, 32, 31, 29, 27],
    [24, 25, 27, 29, 31, 34, 33, 32, 30, 28],
    [23, 25, 26, 28, 30, 35, 34, 33, 31, 29],
    [22, 23, 25, 27, 29, 33, 35, 34, 32, 30],
    [21, 23, 24, 26, 28, 32, 34, 35, 33, 31],
    [20, 22, 23, 25, 27, 31, 33, 34, 34, 32],
    [19, 21, 22, 24, 26, 30, 32, 33, 33, 33],
])

fig, ax = plt.subplots(figsize=(10, 8))
cax = ax.imshow(temperature_data, cmap='hot', interpolation='nearest', aspect='auto')
fig.colorbar(cax, ax=ax, orientation='vertical')
ax.set_xticks([])
ax.set_yticks([])
ax.grid(False)
plt.tight_layout()
plt.show()