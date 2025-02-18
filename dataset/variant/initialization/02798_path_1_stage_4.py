import matplotlib.pyplot as plt
import numpy as np

decades = np.array([1960, 1970, 1980, 1990, 2000, 2010, 2020])
solar_flares = np.array([150, 230, 270, 120, 260, 180, 210])

plt.figure(figsize=(12, 7))
plt.plot(decades, solar_flares, color='blue', marker='o', linestyle='-', linewidth=2, markersize=8)

plt.tight_layout()
plt.show()