import matplotlib.pyplot as plt
import numpy as np

# Data
years = np.array([2015, 2016, 2017, 2018, 2019, 2020])
milk_chocolate_sales = np.array([140, 190, 160, 185, 210, 230])
dark_chocolate_sales = np.array([110, 125, 135, 145, 155, 175])
white_chocolate_sales = np.array([65, 85, 80, 95, 90, 105])
sales_errors = np.array([10, 12, 11, 13, 14, 15])

fig, ax = plt.subplots(figsize=(12, 7))

bar_height = 0.25
bar_positions1 = years - bar_height
bar_positions2 = years
bar_positions3 = years + bar_height

common_color = 'steelblue'

ax.barh(bar_positions1, milk_chocolate_sales, bar_height, xerr=sales_errors, capsize=5, color=common_color, alpha=0.8)
ax.barh(bar_positions2, dark_chocolate_sales, bar_height, xerr=sales_errors, capsize=5, color=common_color, alpha=0.8)
ax.barh(bar_positions3, white_chocolate_sales, bar_height, xerr=sales_errors, capsize=5, color=common_color, alpha=0.8)

ax.set_yticks(years)
ax.set_yticklabels(years)

ax.grid(True, linestyle='--', alpha=0.6)

plt.tight_layout()
plt.show()