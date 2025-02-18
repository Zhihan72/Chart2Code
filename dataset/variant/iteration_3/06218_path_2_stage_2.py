import matplotlib.pyplot as plt
import numpy as np

# Data
years = np.array([2015, 2016, 2017, 2018, 2019, 2020])
milk_chocolate_sales = np.array([150, 180, 170, 190, 200, 220])
dark_chocolate_sales = np.array([100, 120, 130, 150, 160, 180])
white_chocolate_sales = np.array([70, 80, 75, 90, 95, 100])
sales_errors = np.array([10, 12, 11, 13, 14, 15])

fig, ax = plt.subplots(figsize=(12, 7))

bar_width = 0.25
bar_positions1 = years - bar_width
bar_positions2 = years
bar_positions3 = years + bar_width

# Bar plot
ax.bar(bar_positions1, milk_chocolate_sales, bar_width, yerr=sales_errors, capsize=3, color='chocolate', alpha=0.7)
ax.bar(bar_positions2, dark_chocolate_sales, bar_width, yerr=sales_errors, capsize=3, color='firebrick', alpha=0.7)
ax.bar(bar_positions3, white_chocolate_sales, bar_width, yerr=sales_errors, capsize=3, color='tan', alpha=0.7)

# Change tick appearance
ax.set_xticks(years)
ax.set_xticklabels(years, rotation=30, fontsize=10)

# Grid settings
ax.grid(True, linestyle='-.', linewidth=0.75, alpha=0.4)

# Borders removed
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()
plt.show()