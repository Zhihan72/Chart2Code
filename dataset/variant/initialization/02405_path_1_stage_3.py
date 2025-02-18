import numpy as np
import matplotlib.pyplot as plt

years = np.arange(2010, 2021)

solar = [74, 8, 35, 80, 22, 5, 60, 68, 40, 52, 30]
wind = [70, 10, 23, 5, 3, 75, 45, 35, 63, 16, 55]
geothermal = [20, 1, 15, 25, 10, 35, 5, 30, 7, 3, 2]

plt.figure(figsize=(12, 8))

plt.plot(years, solar, marker='o', color='skyblue', linestyle='-', linewidth=2)
plt.plot(years, wind, marker='s', color='lightcoral', linestyle='-', linewidth=2)
plt.plot(years, geothermal, marker='^', color='gold', linestyle='-', linewidth=2)

plt.grid(True, alpha=0.3)
plt.tight_layout()

plt.show()