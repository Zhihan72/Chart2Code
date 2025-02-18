import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2031)
solar = np.array([3, 4, 5, 6, 8, 10, 12, 15, 18, 21, 24, 28, 32, 36, 40, 45, 50, 55, 60, 65, 70])
wind = np.array([5, 6, 7, 8, 10, 12, 14, 15, 16, 18, 20, 22, 25, 28, 30, 32, 34, 36, 38, 39, 40])
hydro = np.array([10, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20, 22, 23, 24, 25, 25, 26, 27, 28, 29, 30])
nuclear = np.array([20, 18, 17, 16, 15, 14, 14, 13, 12, 12, 11, 10, 10, 10, 9, 8, 8, 7, 7, 6, 5])
fossil = 100 - (solar + wind + hydro + nuclear)

fig, ax = plt.subplots(figsize=(14, 8))
ax.stackplot(years, solar, wind, hydro, nuclear, fossil, colors=['#1f77b4'], alpha=0.8)
ax.grid(True, linestyle='--', linewidth=0.7, alpha=0.7)
plt.show()