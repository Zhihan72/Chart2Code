import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)
solar_capacity = np.array([50, 60, 75, 95, 110, 130, 150, 180, 210, 240, 280])

plt.figure(figsize=(12, 6))
plt.plot(years, solar_capacity, marker='s', linestyle='--', color='green', linewidth=3)
plt.grid(True, linestyle='-', alpha=0.3)
plt.axvline(x=2015, color='purple', linestyle='-', linewidth=1.5)

plt.tight_layout()
plt.show()