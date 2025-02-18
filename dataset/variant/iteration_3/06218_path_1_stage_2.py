import matplotlib.pyplot as plt
import numpy as np

# Data
years = np.array([2015, 2016, 2017, 2018, 2019, 2020])
milk_chocolate_sales = np.array([140, 190, 160, 185, 210, 230])
dark_chocolate_sales = np.array([110, 125, 135, 145, 155, 175])
white_chocolate_sales = np.array([65, 85, 80, 95, 90, 105])
sales_errors = np.array([10, 12, 11, 13, 14, 15])

fig, ax = plt.subplots(figsize=(12, 7))

bar_width = 0.25
bar_positions1 = years - bar_width
bar_positions2 = years
bar_positions3 = years + bar_width

ax.bar(bar_positions1, milk_chocolate_sales, bar_width, yerr=sales_errors, capsize=5, color='peru', alpha=0.8)
ax.bar(bar_positions2, dark_chocolate_sales, bar_width, yerr=sales_errors, capsize=5, color='brown', alpha=0.8)
ax.bar(bar_positions3, white_chocolate_sales, bar_width, yerr=sales_errors, capsize=5, color='wheat', alpha=0.8)

# Adjust ticks (kept for chart structure, so the bars align with years)
ax.set_xticks(years)
ax.set_xticklabels([])  # Remove x-axis labels

# Grid and background customization
ax.grid(True, linestyle='--', alpha=0.6)

plt.tight_layout()
plt.show()