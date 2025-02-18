import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2020, 2035)

moon_landings = np.array([2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])
mars_landings = np.array([1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])
venus_landings = np.array([1, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
jupiter_landings = np.array([0, 1, 1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
saturn_landings = np.array([0, 0, 0, 1, 2, 3, 3, 4, 5, 6, 7, 8, 9, 10, 11])

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 12))

ax1.stackplot(years, moon_landings, mars_landings, venus_landings, jupiter_landings, saturn_landings,
              colors=['#FFA07A', '#7FFFD4', '#DA70D6', '#FFD700', '#FF4500'], alpha=0.8)
ax1.set_title("Space Landings (2020-2035)", fontsize=16, fontweight='bold', pad=20)
ax1.set_xlabel("Yr", fontsize=14)
ax1.set_ylabel("Landings", fontsize=14)
ax1.set_xticks(years[::1])
ax1.tick_params(axis='x', rotation=45)

moon_growth_rate = np.gradient(moon_landings) / moon_landings * 100
mars_growth_rate = np.gradient(mars_landings) / mars_landings * 100
venus_growth_rate = np.gradient(venus_landings) / venus_landings * 100
jupiter_growth_rate = np.gradient(jupiter_landings) / jupiter_landings * 100
saturn_growth_rate = np.gradient(saturn_landings) / saturn_landings * 100

ax2.plot(years, moon_growth_rate, color='#FFA07A', marker='o')
ax2.plot(years, mars_growth_rate, color='#7FFFD4', marker='o')
ax2.plot(years, venus_growth_rate, color='#DA70D6', marker='o')
ax2.plot(years, jupiter_growth_rate, color='#FFD700', marker='o')
ax2.plot(years, saturn_growth_rate, color='#FF4500', marker='o')
ax2.set_title("Growth Rate (2020-2035)", fontsize=16, fontweight='bold', pad=20)
ax2.set_xlabel("Yr", fontsize=14)
ax2.set_ylabel("Growth (%)", fontsize=14)
ax2.set_xticks(years[::1])
ax2.tick_params(axis='x', rotation=45)

plt.tight_layout()
plt.show()