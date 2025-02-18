import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)
ny_commuting = np.array([1.0, 1.2, 1.5, 2.0, 2.5, 3.1, 3.7, 4.3, 4.6, 5.0, 5.2])
cph_commuting = np.array([26.4, 27.5, 28.7, 29.9, 31.0, 32.2, 33.3, 34.5, 35.6, 36.7, 37.8])

fig, ax = plt.subplots(figsize=(12, 7))

ax.plot(years, ny_commuting, marker='o', linestyle='-', linewidth=2, color='blue')
ax.plot(years, cph_commuting, marker='^', linestyle='-', linewidth=2, color='red')

ax.set_xticks(years)
ax.set_ylim(0, 40)

plt.tight_layout()
plt.show()