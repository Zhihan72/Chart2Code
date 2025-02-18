import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)

streaming_services = np.array([3, 6, 9, 14, 24, 36, 44, 56, 68, 71, 79])
podcasts = np.array([2, 1, 4, 6, 10, 9, 16, 20, 23, 24, 29])
ebooks = np.array([1, 3, 2, 5, 4, 8, 9, 11, 11, 14, 16])
online_magazines = np.array([4, 3, 5, 8, 8, 11, 11, 13, 14, 15, 16])

fig, ax = plt.subplots(figsize=(10, 6))

ax.plot(years, streaming_services, marker='s', color='#1f77b4', linestyle='-.', label='Streaming Services')
ax.plot(years, podcasts, marker='D', color='#ff7f0e', linestyle=':', label='Podcasts')
ax.plot(years, ebooks, marker='^', color='#2ca02c', linestyle='-', label='E-books')
ax.plot(years, online_magazines, marker='v', color='#d62728', linestyle='--', label='Online Magazines')

ax.grid(False)

plt.xticks(rotation=45, ha='left')

plt.legend(loc='upper left', frameon=False)

plt.tight_layout()

plt.show()