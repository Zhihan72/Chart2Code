import matplotlib.pyplot as plt
import numpy as np

years_actual = np.arange(2015, 2023)
years_forecast = np.arange(2023, 2027)

product_a_sales = np.array([50, 65, 75, 90, 105, 120, 140, 160])
product_b_sales = np.array([30, 45, 60, 80, 100, 110, 130, 150])
product_c_sales = np.array([20, 25, 35, 50, 65, 75, 90, 110])
product_d_sales = np.array([40, 50, 60, 70, 80, 95, 110, 130])  # New data for Product D

product_a_forecast = np.array([180, 200, 220, 240])
product_b_forecast = np.array([170, 190, 210, 230])
product_c_forecast = np.array([130, 150, 170, 190])
product_d_forecast = np.array([150, 170, 190, 210])  # New forecast for Product D

fig, axes = plt.subplots(2, 1, figsize=(10, 12))

# Plot actual sales data
ax1 = axes[0]
ax1.plot(years_actual, product_a_sales, marker='o', linestyle='-', color='#8b0000', linewidth=2, label='Product A')
ax1.plot(years_actual, product_b_sales, marker='s', linestyle='--', color='#00008b', linewidth=2, label='Product B')
ax1.plot(years_actual, product_c_sales, marker='^', linestyle='-.', color='#006400', linewidth=2, label='Product C')
ax1.plot(years_actual, product_d_sales, marker='x', linestyle=':', color='#800080', linewidth=2, label='Product D')  # Plot Product D
ax1.set_title('Tech Product Sales Data (2015-2022)', fontsize=14, fontweight='bold')
ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Sales (in thousands of units)', fontsize=12)
ax1.set_xticks(years_actual)
ax1.set_xticklabels(years_actual, rotation=45)
ax1.legend(title='Products', loc='upper left', fontsize=10)
ax1.grid(True, linestyle='--', alpha=0.6)

annotations = {
    2018: ("Product A hits 75k units", product_a_sales[3]),
    2020: ("Product B crosses 100k units", product_b_sales[5]),
    2022: ("Product C reaches 110k units", product_c_sales[7]),
}
for year, (text, y_value) in annotations.items():
    ax1.annotate(text, xy=(year, y_value), xytext=(year, y_value + 20),
                arrowprops=dict(facecolor='black', shrink=0.05, width=1, headwidth=5), fontsize=10, color='black', ha='center')

# Plot forecasted sales data
ax2 = axes[1]
ax2.plot(years_forecast, product_a_forecast, marker='o', linestyle='-', color='#8b0000', linewidth=2, label='Product A')
ax2.plot(years_forecast, product_b_forecast, marker='s', linestyle='--', color='#00008b', linewidth=2, label='Product B')
ax2.plot(years_forecast, product_c_forecast, marker='^', linestyle='-.', color='#006400', linewidth=2, label='Product C')
ax2.plot(years_forecast, product_d_forecast, marker='x', linestyle=':', color='#800080', linewidth=2, label='Product D')  # Plot Product D Forecast
ax2.set_title('Tech Product Sales Forecast (2023-2026)', fontsize=14, fontweight='bold')
ax2.set_xlabel('Year', fontsize=12)
ax2.set_ylabel('Forecasted Sales (in thousands of units)', fontsize=12)
ax2.set_xticks(years_forecast)
ax2.set_xticklabels(years_forecast, rotation=45)
ax2.legend(title='Products', loc='upper left', fontsize=10)
ax2.grid(True, linestyle='--', alpha=0.6)

plt.tight_layout()
plt.show()