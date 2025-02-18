import matplotlib.pyplot as plt
import numpy as np

years_actual = np.arange(2015, 2023)
years_forecast = np.arange(2023, 2027)

product_a_sales = np.array([50, 65, 75, 90, 105, 120, 140, 160])
product_b_sales = np.array([30, 45, 60, 80, 100, 110, 130, 150])
product_c_sales = np.array([20, 25, 35, 50, 65, 75, 90, 110])

product_a_forecast = np.array([180, 200, 220, 240])
product_b_forecast = np.array([170, 190, 210, 230])
product_c_forecast = np.array([130, 150, 170, 190])

fig, axes = plt.subplots(1, 2, figsize=(18, 8))

ax1 = axes[0]
ax1.plot(years_actual, product_a_sales, marker='o', linestyle='-', color='#4682b4', linewidth=2)
ax1.plot(years_actual, product_b_sales, marker='s', linestyle='--', color='#2e8b57', linewidth=2)
ax1.plot(years_actual, product_c_sales, marker='^', linestyle='-.', color='#ff6347', linewidth=2)

ax1.set_xticks(years_actual)
ax1.set_xticklabels([])

ax2 = axes[1]
ax2.plot(years_forecast, product_a_forecast, marker='o', linestyle='-', color='#4682b4', linewidth=2)
ax2.plot(years_forecast, product_b_forecast, marker='s', linestyle='--', color='#2e8b57', linewidth=2)
ax2.plot(years_forecast, product_c_forecast, marker='^', linestyle='-.', color='#ff6347', linewidth=2)

ax2.set_xticks(years_forecast)
ax2.set_xticklabels([])

plt.tight_layout()

plt.show()