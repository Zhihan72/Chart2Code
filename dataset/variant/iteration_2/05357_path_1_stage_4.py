import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2012, 2023)

sparrows = np.array([15, 16, 14, 13, 12, 19, 21, 17, 14, 15, 23])
robins = np.array([10, 10, 11, 14, 17, 12, 19, 12, 16, 15, 10])
blue_jays = np.array([5, 8, 7, 10, 12, 8, 12, 6, 9, 14, 10])
eagles = np.array([2, 3, 3, 4, 6, 2, 7, 5, 4, 5, 3])

data = np.vstack([sparrows, robins, blue_jays, eagles])

fig, ax = plt.subplots(figsize=(12, 7))
ax.stackplot(years, data,
             colors=['#9370DB', '#87CEEB', '#98FB98', '#FF4500'], alpha=0.85)

ax.legend(['Eagles', 'Blue Jays', 'Robins', 'Sparrows'], loc='lower right', fontsize=14, frameon=False)
ax.grid(False)

plt.tight_layout()
plt.show()