import matplotlib.pyplot as plt
import numpy as np

years = np.arange(1990, 2015)
traditional_agriculture = np.array([50, 49, 47, 44, 42, 38, 35, 32, 28, 27, 23, 22, 19, 17, 14, 12, 11, 7, 5, 4, 3, 1, 0, 0, 0])
organic_farming = np.array([2, 3, 5, 5, 7, 7, 10, 12, 14, 15, 19, 20, 24, 26, 27, 31, 33, 33, 35, 37, 40, 42, 43, 45, 46])
hydroponics = np.array([0, 0, 0, 1, 2, 4, 3, 6, 9, 10, 11, 14, 15, 18, 21, 23, 25, 29, 30, 31, 34, 39, 42, 45, 48])
vertical_farming = np.array([0, 0, 0, 0, 1, 1, 2, 3, 4, 5, 6, 8, 10, 12, 14, 16, 18, 20, 21, 25, 26, 28, 29, 33, 34])

total_agriculture = (traditional_agriculture + organic_farming + hydroponics + vertical_farming)

fig, ax = plt.subplots(figsize=(14, 8))

ax.stackplot(years, traditional_agriculture, organic_farming, hydroponics, vertical_farming,
             colors=['#a9dfbf', '#e6b0aa', '#f9e79f', '#d4e6f1'], alpha=0.75)

ax.plot(years, total_agriculture, color='purple', linestyle='-', marker='x')

ax.set_xticks(years[::2])
ax.set_yticks(np.arange(0, 101, 10))

ax.grid(True, which='both', linestyle=':', linewidth=0.7, alpha=0.6)

fig.tight_layout()

plt.show()