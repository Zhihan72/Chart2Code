import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)
sales = np.array([50, 70, 100, 160, 250, 400, 650, 1000, 1500, 2300, 3500])

fig, ax = plt.subplots(figsize=(12, 6))

# Altered stylistic elements including line color, marker type, and line style
ax.plot(years, sales, marker='s', linestyle='--', color='purple', linewidth=3, markersize=8)

# Customized grid with a different line style and transparency
ax.grid(True, linestyle='-.', alpha=0.3)

# Setting limits which are suitable for the data
ax.set_xlim(2009, 2021)
ax.set_ylim(-200, 4000)

# Adding a legend with a random location
ax.legend(['Sales over years'], loc='upper left')

plt.tight_layout()
plt.show()