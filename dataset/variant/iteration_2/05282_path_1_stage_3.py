import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2000, 2020)
# We are removing the data group 'rainfall'
# rainfall = np.array([850, 920, 940, 870, 860, 910, 820, 800, 960, 1000, 
#                      1100, 1050, 1140, 1150, 1005, 1100, 1080, 1200, 1250, 1300])

fig, ax = plt.subplots(figsize=(12, 6))

# The line plot was removed since it used 'rainfall' data
# ax.plot(years, rainfall, color='green', linewidth=2, marker='o')

ax.set_xlim(1999, 2020)
ax.set_ylim(750, 1350)
ax.grid(True, linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()