import matplotlib.pyplot as plt
import numpy as np

# Preserved the original structure but altered the sales and forecast data within certain groups
years_actual = np.arange(2015, 2023)
years_forecast = np.arange(2023, 2027)

# Randomly altered sales data for products
product_a_sales = np.array([75, 50, 90, 65, 120, 140, 105, 160])
product_b_sales = np.array([45, 30, 80, 60, 110, 150, 100, 130])
product_c_sales = np.array([35, 20, 50, 25, 75, 110, 65, 90])

# Randomly altered forecast data for products
product_a_forecast = np.array([220, 180, 240, 200])
product_b_forecast = np.array([190, 170, 230, 210])
product_c_forecast = np.array([150, 130, 190, 170])

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