import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)
# Randomly altered subscribers data, still preserving its structure
netflix_subs = np.array([24, 20, 45, 37, 30, 53, 82, 62, 92, 107, 72])
hulu_subs = np.array([10, 7, 16, 8, 13, 25, 33, 20, 29, 36, 31])
prime_subs = np.array([32, 15, 27, 17, 20, 48, 36, 60, 24, 53, 42])
disney_subs = np.array([28, 0, 50, 0, 0, 10, 73, 0, 0, 0, 0])

fig, ax1 = plt.subplots(figsize=(14, 8))

ax1.plot(years, netflix_subs, marker='o', color='orange', linewidth=2)
ax1.plot(years, hulu_subs, marker='s', color='blue', linewidth=2)
ax1.plot(years, prime_subs, marker='^', color='pink', linewidth=2)
ax1.plot(years, disney_subs, marker='d', color='teal', linewidth=2)

ax1.set_title('Streaming Growth (2010-2020)', fontsize=18, fontweight='bold', pad=20)
ax1.set_xlabel('Year', fontsize=14)
ax1.set_ylabel('Subs (millions)', fontsize=14)

plt.tight_layout()
plt.show()