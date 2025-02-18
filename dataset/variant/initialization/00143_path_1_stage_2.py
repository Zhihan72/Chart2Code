import numpy as np
import matplotlib.pyplot as plt

years = np.arange(2010, 2021)

fantasy = np.array([20, 25, 30, 45, 65, 80, 95, 110, 130, 145, 160])
mystery = np.array([30, 35, 40, 45, 50, 55, 65, 70, 75, 85, 90])
science_fiction = np.array([15, 20, 28, 35, 45, 55, 70, 85, 100, 115, 130])
romance = np.array([25, 30, 35, 40, 45, 50, 60, 70, 80, 85, 95])
non_fiction = np.array([10, 15, 20, 25, 30, 40, 50, 55, 60, 65, 70])

genre_data = np.vstack([fantasy, mystery, science_fiction, romance, non_fiction])

fig, ax = plt.subplots(figsize=(14, 9))

colors = ['#d73027', '#4575b4', '#f46d43', '#74add1', '#fdae61']

ax.stackplot(years, genre_data, colors=colors, alpha=0.85)

ax.grid(color='gray', linestyle='-', linewidth=0.5, alpha=0.3)

plt.xticks(years, rotation=90)
plt.yticks(np.arange(0, 401, 50))

plt.tight_layout()
plt.show()