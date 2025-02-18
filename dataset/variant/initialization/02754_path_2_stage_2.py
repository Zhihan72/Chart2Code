import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)
sales = np.array([50, 70, 100, 160, 250, 400, 650, 1000, 1500, 2300, 3500])

fig, ax = plt.subplots(figsize=(12, 6))

# Changed the color of the plot line and markers
ax.plot(years, sales, marker='o', linestyle='-', color='green', linewidth=2, markersize=6)

ax.grid(True, linestyle='--', alpha=0.6)

ax.set_xlim(2010, 2020)
ax.set_ylim(0, 4000)

plt.tight_layout()
plt.show()