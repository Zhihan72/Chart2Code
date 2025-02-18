import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)
sales_product_A = np.array([50, 70, 100, 160, 250, 400, 650, 1000, 1500, 2300, 3500])
sales_product_B = np.array([30, 50, 80, 120, 200, 300, 500, 800, 1200, 1800, 2800])  # Added data for Product B
sales_product_C = np.array([20, 40, 60, 110, 150, 250, 400, 700, 1100, 1700, 2500])  # Added data for Product C

fig, ax = plt.subplots(figsize=(12, 6))

ax.plot(years, sales_product_A, marker='s', linestyle='--', color='purple', linewidth=3, markersize=8)
ax.plot(years, sales_product_B, marker='o', linestyle='-', color='green', linewidth=3, markersize=8)  # Plot for Product B
ax.plot(years, sales_product_C, marker='^', linestyle='-.', color='blue', linewidth=3, markersize=8)  # Plot for Product C

ax.grid(True, linestyle='-.', alpha=0.3)

ax.set_xlim(2009, 2021)
ax.set_ylim(-200, 4000)

ax.legend(['Sales of Product A', 'Sales of Product B', 'Sales of Product C'], loc='upper left')

plt.tight_layout()
plt.show()