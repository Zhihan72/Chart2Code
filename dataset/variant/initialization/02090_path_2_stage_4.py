import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)
solar_capacity = np.array([50, 60, 75, 95, 110, 130, 150, 180, 210, 240, 280])

plt.figure(figsize=(12, 6))

plt.plot(years, solar_capacity, marker='o', linestyle='-', color='green', linewidth=2)

plt.axvline(x=2015, color='gray', linestyle=':', linewidth=1)

plt.tight_layout()
plt.show()