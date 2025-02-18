import numpy as np
import matplotlib.pyplot as plt

years = np.array([2010, 2012, 2014, 2016, 2018, 2020])
fiction = np.array([30, 35, 40, 45, 50, 55])
non_fiction = np.array([20, 22, 25, 27, 30, 32])
sci_fi = np.array([10, 12, 14, 16, 18, 20])
fantasy = np.array([8, 10, 13, 16, 20, 25])

single_color = '#a8dadc'

fig, ax = plt.subplots(figsize=(12, 8))

bar_width = 0.2
x_indices = np.arange(len(years))

ax.bar(x_indices, fiction, width=bar_width, color=single_color, alpha=0.9)
ax.bar(x_indices + bar_width, non_fiction, width=bar_width, color=single_color, alpha=0.9)
ax.bar(x_indices + 2 * bar_width, sci_fi, width=bar_width, color=single_color, alpha=0.9)
ax.bar(x_indices + 3 * bar_width, fantasy, width=bar_width, color=single_color, alpha=0.9)

plt.tight_layout()
plt.show()