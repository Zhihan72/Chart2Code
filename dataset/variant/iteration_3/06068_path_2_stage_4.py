import matplotlib.pyplot as plt
import numpy as np

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

prod_development = [15, 20, 10, 18, 28, 16, 22, 30, 17, 27, 35, 24]
prod_marketing = [16, 12, 22, 14, 21, 15, 25, 26, 19, 20, 30, 28]
prod_sales = [18, 22, 19, 25, 30, 20, 27, 33, 29, 26, 34, 29]

fig, ax = plt.subplots(figsize=(12, 8))

ax.plot(months, prod_development, marker='D', linestyle='-.', color='blue', label='Development')
ax.plot(months, prod_marketing, marker='x', linestyle='-', color='green', label='Marketing')
ax.plot(months, prod_sales, marker='|', linestyle='--', color='red', label='Sales')

ax.grid(True, which='major', linestyle='-.', linewidth=1.0, alpha=0.5)
ax.spines['top'].set_visible(False)

ax.legend(loc='upper left', fontsize='small', frameon=True, shadow=True)

plt.tight_layout()
plt.show()