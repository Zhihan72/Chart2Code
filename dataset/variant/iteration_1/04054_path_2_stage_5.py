import matplotlib.pyplot as plt
import numpy as np

categories = ['Solar Panels', 'Wind Turbines', 'Electric Vehicles', 'Battery Storage']

solar_panels_sales = [35, 40, 42, 45, 50, 60, 65, 55, 70, 75, 80]
wind_turbines_sales = [20, 25, 28, 30, 35, 40, 42, 38, 45, 50, 52]
electric_vehicles_sales = [15, 18, 20, 25, 30, 35, 40, 45, 50, 60, 70]
battery_storage_sales = [10, 12, 15, 18, 22, 25, 30, 35, 40, 42, 45]

sales_data = [solar_panels_sales, wind_turbines_sales, electric_vehicles_sales, battery_storage_sales]

average_sales = np.mean(sales_data, axis=0)
years = list(range(2010, 2020 + 1))

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 8))

new_colors = ['lightyellow', 'lightcyan', 'lightgray', 'lavender']

ax1.boxplot(sales_data, patch_artist=True, notch=True, vert=False,
            boxprops=dict(facecolor='lightyellow', color='darkgreen'),
            whiskerprops=dict(color='darkgreen'),
            capprops=dict(color='darkgreen'),
            medianprops=dict(color='red', linewidth=1.5))

for patch, color in zip(ax1.artists, new_colors):
    patch.set_facecolor(color)

ax1.set_yticklabels(categories)

for spine in ax1.spines.values():
    spine.set_visible(False)

ax2.plot(years, average_sales, marker='o', linestyle='-', color='darkmagenta')

for spine in ax2.spines.values():
    spine.set_visible(False)

plt.tight_layout()
plt.show()