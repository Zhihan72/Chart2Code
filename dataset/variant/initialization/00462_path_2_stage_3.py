import matplotlib.pyplot as plt
import numpy as np

temperature_data = np.array([
    [33, 26, 20, 24, 31, 22, 33, 30, 28, 27],
    [28, 32, 31, 17, 30, 27, 26, 29, 25, 21],
    [19, 22, 25, 32, 18, 24, 31, 30, 26, 29],
    [33, 29, 31, 32, 28, 25, 23, 26, 20, 30],
    [28, 32, 21, 25, 34, 27, 31, 23, 22, 28],
    [29, 30, 22, 34, 31, 24, 19, 26, 33, 21],
    [23, 31, 34, 35, 33, 28, 20, 18, 24, 32],
    [30, 27, 26, 29, 30, 31, 32, 25, 34, 31],
    [31, 24, 25, 23, 22, 30, 27, 32, 33, 32],
    [19, 20, 29, 24, 28, 31, 21, 33, 30, 31],
])

mask = np.tril(np.ones(temperature_data.shape, dtype=bool), -1)
masked_data = np.ma.masked_where(mask, temperature_data)

fig, ax = plt.subplots(figsize=(10, 8))
ax.imshow(masked_data, cmap='hot', interpolation='nearest', aspect='auto')

ax.set_xticks([])
ax.set_yticks([])

plt.show()