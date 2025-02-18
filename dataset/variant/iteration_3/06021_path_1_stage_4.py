import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2040, 2051)

wheat_a = np.array([22, 21, 28, 22, 25, 24, 24, 20, 23, 27, 26])
corn_a = np.array([16, 23, 17, 22, 18, 20, 19, 16, 18, 21, 15])
rice_a = np.array([17, 11, 12, 13, 10, 12, 18, 14, 15, 15, 16])
wheat_b = np.array([23, 19, 20, 26, 18, 24, 25, 21, 23, 22, 20])
corn_b = np.array([21, 20, 19, 14, 18, 15, 17, 14, 17, 16, 15])
rice_b = np.array([14, 13, 12, 11, 11, 9, 10, 15, 11, 9, 13])

fig, ax = plt.subplots(figsize=(12, 8))

consistent_color = 'dodgerblue'
ax.plot(years, wheat_a, color=consistent_color, linestyle='-')
ax.plot(years, corn_a, color=consistent_color, linestyle='-')
ax.plot(years, rice_a, color=consistent_color, linestyle='-')
ax.plot(years, wheat_b, color=consistent_color, linestyle='--')
ax.plot(years, corn_b, color=consistent_color, linestyle='--')
ax.plot(years, rice_b, color=consistent_color, linestyle='--')

ax.set_title("Fluctuating Crop Yields in Colonized Martian Farms (2040-2050)", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Annum', fontsize=12)
ax.set_ylabel('Yield Change (%)', fontsize=12)

ax.annotate('Fertilizer Advancement', xy=(2045, 28), xytext=(2042, 30),
            arrowprops=dict(facecolor='black', shrink=0.05),
            fontsize=10, fontweight='bold')

plt.tight_layout()
plt.show()