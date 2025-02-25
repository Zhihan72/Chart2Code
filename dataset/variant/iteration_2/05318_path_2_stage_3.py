import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)
netflix_subs = np.array([20, 24, 30, 37, 45, 53, 62, 72, 82, 92, 107])
hulu_subs = np.array([7, 8, 10, 13, 16, 20, 25, 29, 31, 33, 36])
prime_subs = np.array([15, 17, 20, 24, 27, 32, 36, 42, 48, 53, 60])
disney_subs = np.array([0, 0, 0, 0, 0, 0, 0, 10, 28, 50, 73])

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