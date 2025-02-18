import matplotlib.pyplot as plt
import numpy as np

# Data
years = np.array([2015, 2016, 2017, 2018, 2019, 2020])
milk_chocolate_sales = np.array([150, 180, 170, 190, 200, 220])
dark_chocolate_sales = np.array([100, 120, 130, 150, 160, 180])
white_chocolate_sales = np.array([70, 80, 75, 90, 95, 100])
ruby_chocolate_sales = np.array([50, 60, 55, 65, 70, 75])  # New data series
sales_errors = np.array([10, 12, 11, 13, 14, 15])

fig, ax = plt.subplots(figsize=(12, 7))

bar_height = 0.2
bar_positions1 = years - 1.5 * bar_height
bar_positions2 = years - 0.5 * bar_height
bar_positions3 = years + 0.5 * bar_height
bar_positions4 = years + 1.5 * bar_height

# Horizontal bar plots
ax.barh(bar_positions1, milk_chocolate_sales, bar_height, xerr=sales_errors, capsize=3, color='chocolate', alpha=0.7)
ax.barh(bar_positions2, dark_chocolate_sales, bar_height, xerr=sales_errors, capsize=3, color='firebrick', alpha=0.7)
ax.barh(bar_positions3, white_chocolate_sales, bar_height, xerr=sales_errors, capsize=3, color='tan', alpha=0.7)
ax.barh(bar_positions4, ruby_chocolate_sales, bar_height, xerr=sales_errors, capsize=3, color='pink', alpha=0.7)  # New bar plot for ruby chocolate

# Change tick appearance
ax.set_yticks(years)
ax.set_yticklabels(years, fontsize=10)

# Grid settings
ax.grid(True, axis='x', linestyle='-.', linewidth=0.75, alpha=0.4)

# Borders removed
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()
plt.show()