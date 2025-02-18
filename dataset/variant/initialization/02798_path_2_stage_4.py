import matplotlib.pyplot as plt
import numpy as np

decades = np.array([1970, 1960, 1990, 2000, 2010, 1980, 2020])
solar_flares = np.array([150, 120, 210, 260, 230, 180, 270])

plt.figure(figsize=(12, 7))
plt.plot(decades, solar_flares, color='coral', marker='x', linestyle='--', linewidth=2.5, markersize=10)

plt.grid(True, linestyle='-', alpha=0.3)
plt.gca().spines['top'].set_visible(False)
plt.tight_layout()
plt.show()