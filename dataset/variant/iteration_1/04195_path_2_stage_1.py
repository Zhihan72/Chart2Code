import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)
streaming_services = np.array([2, 5, 10, 15, 25, 35, 45, 55, 65, 70, 80])
podcasts = np.array([1, 2, 3, 5, 7, 10, 15, 18, 22, 25, 28])
ebooks = np.array([1, 2, 3, 4, 5, 7, 8, 10, 12, 13, 15])
online_magazines = np.array([3, 4, 6, 7, 9, 10, 12, 12, 13, 14, 15])

fig, ax = plt.subplots(figsize=(12, 8))

ax.plot(years, streaming_services, marker='o', color='#1f77b4')
ax.plot(years, podcasts, marker='o', color='#ff7f0e')
ax.plot(years, ebooks, marker='o', color='#2ca02c')
ax.plot(years, online_magazines, marker='o', color='#d62728')

ax.grid(True, linestyle='--', alpha=0.7)

# Note: Legend is still used but without title and labels
ax.legend(loc='upper left', fontsize=10)

plt.xticks(rotation=45, ha='right')

plt.tight_layout()

plt.show()