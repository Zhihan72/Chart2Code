import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2013, 2023)
apple_sales = np.array([50, 55, 60, 70, 80, 85, 90, 100, 110, 120])
orange_sales = np.array([45, 48, 50, 55, 60, 65, 70, 75, 80, 85])
grape_sales = np.array([30, 32, 35, 40, 45, 48, 50, 55, 60, 65])
pineapple_sales = np.array([20, 22, 25, 28, 30, 35, 40, 42, 45, 50])
total_sales = apple_sales + orange_sales + grape_sales + pineapple_sales

fig, ax = plt.subplots(figsize=(14, 8))
ax.plot(years, apple_sales, marker='o', linestyle='-', color='green')
ax.plot(years, orange_sales, marker='v', linestyle='--', color='orange')
ax.plot(years, grape_sales, marker='s', linestyle='-.', color='purple')
ax.plot(years, pineapple_sales, marker='D', linestyle=':', color='gold')
ax.plot(years, total_sales, marker='*', linestyle='-', linewidth=2, color='black', alpha=0.7)

ax.set_xticks(years)
ax.set_xticklabels(years, rotation=45)
ax.grid(True, linestyle='--', alpha=0.6)

plt.tight_layout()
plt.show()