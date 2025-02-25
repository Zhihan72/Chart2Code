import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)
gdp_growth = np.array([2.3, 2.6, 2.7, 2.9, 3.0, 3.2, 3.1, 2.8, 2.5, 2.0, 1.8])
unemployment_rate = np.array([7.8, 7.5, 7.2, 7.0, 6.8, 6.7, 6.6, 6.5, 6.3, 6.2, 6.1])
inflation_rate = np.array([1.5, 1.7, 1.8, 2.0, 2.2, 2.5, 2.4, 2.3, 2.1, 1.9, 1.8])

fig, ax1 = plt.subplots(figsize=(14, 8))

ax1.plot(years, gdp_growth, color='magenta', marker='x', linestyle='--', linewidth=2, markersize=8)
ax1.plot(years, unemployment_rate, color='cyan', marker='D', linestyle='-.', linewidth=3, markersize=8)
ax1.plot(years, inflation_rate, color='orange', marker='v', linestyle=':', linewidth=1, markersize=10)

ax1.grid(True, linestyle=':', linewidth=0.7, alpha=0.9)

ax1.set_xticks(years)
plt.xticks(rotation=60)
plt.tight_layout()

plt.show()