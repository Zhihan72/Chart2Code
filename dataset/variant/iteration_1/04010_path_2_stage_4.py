import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2000, 2021)

residential = [2, 2.5, 3, 3.8, 4.5, 5.5, 6.5, 7.8, 9, 10.5, 12, 14, 16, 18.5, 21, 24.2, 27.5, 31, 35, 39.5, 44]
commercial = [1, 1.2, 1.5, 2, 2.6, 3.2, 3.9, 4.7, 5.6, 6.6, 7.8, 9, 10.4, 12, 13.7, 15.5, 17.5, 19.7, 22, 24.5, 27]

fig, ax = plt.subplots(figsize=(14, 8))

# Use a consistent color for both data groups.
ax.stackplot(years, residential, commercial, colors=['#66c2a5', '#66c2a5'], alpha=0.8)

ax.set_title("Renewable Energy: 2000-2020", fontsize=16, pad=20)
ax.set_xlabel("Year", fontsize=14)
ax.set_ylabel("Renewable %", fontsize=14)

ax.set_xticks(years[::2])
ax.set_yticks(np.arange(0, 51, 5))
ax.set_xticklabels(years[::2], rotation=45, ha='right')

plt.tight_layout()

plt.show()