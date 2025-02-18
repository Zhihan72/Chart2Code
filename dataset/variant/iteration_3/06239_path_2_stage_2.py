import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2015, 2026)

# Sales data (in millions) for each type of electric vehicle
sedans_sales = np.array([0.2, 0.4, 0.6, 0.85, 1.2, 1.5, 2.0, 2.4, 2.8, 3.3, 3.8])
suvs_sales = np.array([0.1, 0.3, 0.5, 0.7, 0.9, 1.3, 1.7, 2.1, 2.5, 3.0, 3.5])
hatchbacks_sales = np.array([0.05, 0.1, 0.25, 0.35, 0.45, 0.65, 0.8, 0.9, 1.1, 1.3, 1.4])
trucks_sales = np.array([0.01, 0.05, 0.1, 0.25, 0.45, 0.7, 1.0, 1.4, 1.8, 2.2, 2.6])
vans_sales = np.array([0.02, 0.04, 0.08, 0.15, 0.3, 0.5, 0.7, 0.9, 1.2, 1.5, 1.9])

sales_data = np.vstack([sedans_sales, suvs_sales, hatchbacks_sales, trucks_sales, vans_sales])
colors = ['#ffadad', '#ffdae4', '#ffd6a5', '#fdffb6', '#caffbf']

fig, ax = plt.subplots(figsize=(14, 8))

ax.stackplot(years, sales_data, labels=['Sedans', 'SUVs', 'Hatchbacks', 'Trucks', 'Vans'], colors=colors, alpha=0.85)

# Customize the chart
ax.set_title('EV Sales 2015-2025', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Sales (millions)', fontsize=12)

# Add grid and legend
ax.grid(linestyle='--', alpha=0.7)
ax.legend(loc='upper left', fontsize=12, title='Types')

ax.set_xticks(years)
ax.set_yticks(np.arange(0, 6.1, 0.5))
ax.set_xlim(2015, 2025)
ax.set_ylim(0, 6)

plt.xticks(rotation=45)

ax.annotate('SUV Surge', xy=(2022, suvs_sales[7]), xytext=(2018, 2), 
            arrowprops=dict(facecolor='black', arrowstyle='->'),
            fontsize=10, color='blue')

plt.tight_layout()

plt.show()