import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)

streamed_hours = np.array([
    [10, 15, 20, 25, 32, 40, 55, 68, 75, 80, 82],
    [5, 10, 15, 20, 28, 35, 45, 50, 55, 60, 65],
    [2, 5, 9, 14, 20, 28, 38, 45, 50, 55, 60],
    [1, 2, 5, 10, 15, 20, 28, 30, 32, 34, 36],
    [2, 3, 4, 5, 8, 12, 18, 22, 26, 30, 35],
    [5, 6, 8, 11, 15, 20, 25, 30, 32, 35, 37]
])

fig, ax = plt.subplots(figsize=(12, 8))

# Shuffled color assignments for changing the look of data groups
colors = ['#7f7f7f', '#2ca02c', '#9467bd', '#d62728', '#1f77b4', '#ff7f0e']

ax.stackplot(years, streamed_hours, colors=colors, alpha=0.85)

ax.set_xticks(years)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()