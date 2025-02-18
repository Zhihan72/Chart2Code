import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)
solar = [5, 7, 10, 14, 18, 23, 29, 35, 42, 50, 58]
wind = [4, 6, 9, 13, 17, 22, 27, 33, 40, 47, 55]
hydro = [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]

fig, ax1 = plt.subplots(figsize=(16, 9))
ax1.plot(years, solar, marker='o', linestyle='-', color='#FF8C00', linewidth=2)
ax1.plot(years, wind, marker='s', linestyle='--', color='#1E90FF', linewidth=2)
ax1.plot(years, hydro, marker='^', linestyle='-.', color='#32CD32', linewidth=2)

ax1.set_xticks(years)

plt.tight_layout()
plt.show()