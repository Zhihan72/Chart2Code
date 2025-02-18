import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)

platforms = ["A", "B", "C", "D", "Others", "E"]

streamed_hours = np.array([
    [10, 15, 20, 25, 32, 40, 55, 68, 75, 80, 82],  # A
    [5, 10, 15, 20, 28, 35, 45, 50, 55, 60, 65],   # B
    [2, 5, 9, 14, 20, 28, 38, 45, 50, 55, 60],     # C
    [1, 2, 5, 10, 15, 20, 28, 30, 32, 34, 36],     # D
    [5, 6, 8, 11, 15, 20, 25, 30, 32, 35, 37],     # Others
    [0, 1, 2, 3, 5, 10, 15, 20, 23, 26, 28]        # E
])

fig, ax = plt.subplots(figsize=(12, 8))

colors = ['#9467bd', '#d62728', '#2ca02c', '#8c564b', '#ff7f0e', '#1f77b4']

ax.stackplot(years, streamed_hours, labels=platforms, colors=colors, alpha=0.85)

ax.set_title('Streaming Growth 2010-2020', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Billion Hours', fontsize=12)

ax.legend(loc='upper left', fontsize=10, title='Platforms', bbox_to_anchor=(1, 1))

ax.yaxis.grid(True, linestyle='--', alpha=0.7)

ax.set_xticks(years)

plt.xticks(rotation=45)

plt.tight_layout()

plt.show()