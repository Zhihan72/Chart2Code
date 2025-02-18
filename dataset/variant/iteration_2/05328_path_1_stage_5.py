import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2000, 2021)
renewable_energy = [5, 6, 8, 10, 13, 18, 20, 25, 30, 35, 42, 50, 60, 70, 85, 100, 120, 145, 170, 200, 230]

fig, ax = plt.subplots(figsize=(14, 6))

ax.plot(years, renewable_energy, color='red', linewidth=2, marker='s', linestyle='-', markersize=6)

plt.xticks(years, rotation=45)
plt.tight_layout()
plt.show()